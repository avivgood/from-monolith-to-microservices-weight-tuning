#!/usr/bin/env python3
"""
make_trails_table.py

Walks a 'trails/' directory tree, reads per-project baseline.json and improvement json,
and prints a one-page LaTeX table comparing Baseline vs Improvement across key metrics.

Usage:
  python make_trails_table.py --root trails --out trails_summary_table.tex

If --out is omitted, LaTeX is printed to stdout.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Dict, Optional, Tuple, List

# ---- Configuration ----

PROJECT_HIGHLIGHT_NAMES = {
    "spring-boot-admin",   # exact dir name shown in your tree
    "springboot-admin",    # user-typed alias; we’ll treat both as highlight triggers
}

IMPROVEMENT_CANDIDATES = [
    "improved.json"
]

# metric_key -> (Pretty Header, decimals_for_values)
METRICS = {
    "n_micros":   (r"\# Services", 0),
    "avg_cop":    (r"Avg Coupling $\downarrow$", 2),
    "cohesion":   (r"Cohesion $\uparrow$", 3),
    "ifn":        (r"IFN", 2),
    "n_calls":    (r"Calls", 0),
    "n_refs":     (r"Refs", 0),
}

# For some keys, allow fallback to "*_fixed" variant if primary missing
FALLBACK_KEYS = {
    "avg_cop": "avg_cop_fixed",
    "cohesion": "cohesion_fixed",
}

# ---- Helpers ----

def latex_escape(s: str) -> str:
    """Escape LaTeX special chars in project names."""
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    out = []
    for ch in s:
        out.append(repl.get(ch, ch))
    return "".join(out)

def find_improvement_file(d: Path) -> Optional[Path]:
    for name in IMPROVEMENT_CANDIDATES:
        p = d / name
        if p.exists():
            return p
    return None

def robust_get(d: Dict, key: str):
    if key in d:
        return d[key]
    fb = FALLBACK_KEYS.get(key)
    if fb and fb in d:
        return d[fb]
    return None

def as_float(x) -> Optional[float]:
    if x is None:
        return None
    try:
        return float(x)
    except Exception:
        raise

def format_num(x: Optional[float], decimals: int) -> str:
    if x is None:
        return r"--"
    if decimals == 0:
        return f"{int(round(x))}"
    return f"{x:.{decimals}f}"

def format_cell(b: Optional[float], i: Optional[float], decimals: int) -> str:
    """Return 'B→I (Δ%)' compact cell; if missing I, show just baseline; if both missing, '--'."""
    b_str = format_num(b, decimals)
    i_str = format_num(i, decimals)
    if b is not None and i is not None:
        if abs(b) <= 0.001:
            dp = None
        else:
            dp = (i - b) / b * 100.0
        dp_str = f"{dp:+.1f}\\%" if dp is not None else r"--"
        # Use math arrow for safety with pdflatex
        return r"\mbox{" + rf"${b_str}"+r"\!{\to}\!" + rf"{i_str}$" + r"}" + f" ({dp_str})"
    elif b is not None:
        return b_str
    elif i is not None:
        # Rare, but if baseline missing and improvement present
        return i_str
    else:
        return r"--"

def mean(nums: List[float]) -> Optional[float]:
    nums = [x for x in nums if x is not None]
    return sum(nums) / len(nums) if nums else None

def collect_projects(root: Path) -> List[Tuple[str, Dict, Optional[Dict]]]:
    rows = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        baseline = child / "baseline.json"
        if not baseline.exists():
            continue
        try:
            b = json.loads(baseline.read_text(encoding="utf-8"))
        except Exception:
            continue
        imp_path = find_improvement_file(child)
        i = None
        if imp_path:
            try:
                i = json.loads(imp_path.read_text(encoding="utf-8"))
            except Exception:
                i = None
        rows.append((child.name[:3], b, i))
    return rows

# ---- LaTeX Builder ----

def build_table(projects: List[Tuple[str, Dict, Optional[Dict]]]) -> str:
    # Prepare per-project rows and collect aggregates
    metric_keys = list(METRICS.keys())

    # For means:
    baseline_values: Dict[str, List[Optional[float]]] = {k: [] for k in metric_keys}
    improvement_values: Dict[str, List[Optional[float]]] = {k: [] for k in metric_keys}
    paired_delta_pct: Dict[str, List[Optional[float]]] = {k: [] for k in metric_keys}

    # Build body rows
    body_lines = []
    for name, bdict, idict in projects:
        cells = []
        for k in metric_keys:
            bval = as_float(robust_get(bdict, k))
            ival = as_float(robust_get(idict or {}, k)) if idict else None
            decimals = METRICS[k][1]
            cells.append(format_cell(bval, ival, decimals))

            # aggregates
            baseline_values[k].append(bval)
            improvement_values[k].append(ival)
            if bval is not None and ival is not None:
                paired_delta_pct[k].append((ival - bval) / (bval if bval != 0 else 1.0) * 100.0)
            else:
                paired_delta_pct[k].append(None)

        proj_label = latex_escape(name)
        highlight_trigger = name in PROJECT_HIGHLIGHT_NAMES
        row_prefix = r"\rowcolor{yellow!12} " if highlight_trigger else ""
        proj_disp = r"\textbf{" + proj_label + r"} (validation)" if "spring-boot-admin" in name or "springboot-admin" in name else proj_label
        if "spring-boot-admin" in name or "springboot-admin" in name:
            proj_disp = r"\textbf{" + proj_label + r"} (validation)"

        body_lines.append(
            f"{row_prefix}{proj_disp} & " + " & ".join(cells) + r" \\"
        )

    # Overall mean row (mean of baselines, mean of improvements, Δ% over paired)
    overall_cells = []
    for k in metric_keys:
        decimals = METRICS[k][1]
        bmean = mean(baseline_values[k])
        imean = mean(improvement_values[k])
        dpmean = mean([x for x in paired_delta_pct[k] if x is not None])
        if bmean is not None and imean is not None:
            cell = rf"${format_num(bmean, decimals)}\to {format_num(imean, decimals)}$ ({(dpmean if dpmean is not None else 0):+.1f}\%)"
        elif bmean is not None:
            cell = format_num(bmean, decimals)
        elif imean is not None:
            cell = format_num(imean, decimals)
        else:
            cell = r"--"
        overall_cells.append(cell)

    # Column headers
    headers = ["Project"] + [METRICS[k][0] for k in metric_keys]

    # LaTeX table (compact, one page friendly)
    colspec = "l" + "X" * len(metric_keys)
    lines = []
    lines.append(r"% Requires: \usepackage{booktabs,tabularx,graphicx}")
    lines.append(r"% Optional (for row highlight): \usepackage[table]{xcolor}")
    lines.append(r"\begin{table}[t]")
    lines.append(r"\footnotesize")
    lines.append(r"\setlength{\tabcolsep}{4pt}")
    lines.append(r"\renewcommand{\arraystretch}{1.1}")
    lines.append(r"\centering")
    lines.append(r"\caption{Baseline vs.~Improvement across systems. Cells show $B\to I$ and $\Delta\%$ relative to Baseline. Validation system highlighted.}")
    lines.append(r"\begin{tabularx}{\textwidth}{" + colspec + "}")
    lines.append(r"\toprule")
    lines.append(" & ".join(headers) + r" \\")
    lines.append(r"\midrule")
    lines.extend(body_lines)
    lines.append(r"\midrule")
    lines.append(r"\textbf{mean} & " + " & ".join(overall_cells) + r" \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabularx}")
    lines.append(r"\end{table}")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("../trails"), help="Root directory containing project subdirectories")
    ap.add_argument("--out", type=Path, default=None, help="Write LaTeX to this file; defaults to stdout")
    args = ap.parse_args()

    projects = collect_projects(args.root)
    if not projects:
        raise SystemExit(f"No projects with baseline.json found under {args.root}")

    # Sort by name, but put spring-boot-admin first to make the highlight easy to spot (optional)
    projects.sort(key=lambda t: (0 if ("spring-boot-admin" in t[0] or "springboot-admin" in t[0]) else 1, t[0].lower()))

    tex = build_table(projects)
    if args.out:
        args.out.write_text(tex, encoding="utf-8")
    else:
        print(tex)

if __name__ == "__main__":
    main()
