#!/usr/bin/env python3
import json
import os
import re
from pathlib import Path


CUSTOM_DESCRIPTIONS = {
    "dddsample-core": "DDD cargo/booking aggregates demo.",
    "spring-petclinic": "Spring Boot MVC + data demo.",
    "jpetstore": "MyBatis/Spring PetStore-style demo.",
    "springblog": "Minimal Spring blog (MVC + JPA).",
    "airsonic-advanced-106": "Self-hosted audio streaming fork.",
    "jhipster-sample-application": "JHipster-generated full-stack reference.",
    "shopizer-2x": "Open-source e-commerce platform.",
    "broadleaf-commerce": "Enterprise e-commerce framework.",
    "realworld-spring": "RealWorld spec backend in Spring.",
    "thingsboard": "IoT: devices, telemetry, rules.",
    "JeecgBoot": "Spring low-code with scaffolding.",
    "RuoYi-Vue": "Spring + Vue admin starter.",
    "mall": "Modular mall/e-commerce sample.",
    "zipkin": "Distributed tracing system.",
    "spring-boot-admin": "Spring Boot apps monitoring dashboard.",
}


# ----- Config -----
EXCLUDE_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vscode", ".gradle",
    "node_modules", "target", "build", "dist", "out", ".venv", "venv"
}
JAVA_DECL_RE = re.compile(
    r"(?m)^\s*(?:public|protected|private)?\s*(?:abstract|final|sealed|non-sealed)?\s*"
    r"(class|interface|enum|record)\s+\w+"
)

# ----- FS walk -----
def traverse_files(folder_path: str):
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            yield os.path.join(root, file)

# ----- Counting -----
def count_java_loc_in_file(p: Path) -> int:
    if p.suffix.lower() != ".java":
        return 0
    try:
        with p.open("r", encoding="utf-8", errors="ignore") as fh:
            return sum(1 for line in fh if line.strip())
    except Exception:
        return 0

def count_java_classes_in_file(p: Path) -> int:
    if p.suffix.lower() != ".java":
        return 0
    try:
        with p.open("r", encoding="utf-8", errors="ignore") as fh:
            src = fh.read()
        return len(JAVA_DECL_RE.findall(src))
    except Exception:
        return 0

# ----- LaTeX helpers -----
def latex_escape(s: str) -> str:
    return (s.replace("\\", r"\textbackslash{}")
             .replace("&", r"\&").replace("%", r"\%").replace("$", r"\$")
             .replace("#", r"\#").replace("_", r"\_").replace("{", r"\{")
             .replace("}", r"\}").replace("~", r"\textasciitilde{}")
             .replace("^", r"\^{}"))

def fmt_int(n: int) -> str:
    return f"{n:,}"

def tnote_label(idx: int) -> str:
    # a, b, ..., z, aa, ab, ...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    k = idx
    while True:
        s = alphabet[k % 26] + s
        k = k // 26 - 1
        if k < 0:
            break
    return s

def make_threepart_table_desc_column(rows, title=None, label=None):
    """
    Emits a compact threeparttable with Description as a wrapping X column.
    Only the URL is footnoted via \tnote{...}. Descriptions live in a column.
    Columns: Project | Java LOC | Java classes | Description
    """
    lines = []
    lines.append(r"\begin{threeparttable}")
    if title:
        lines.append(rf"\caption{{{latex_escape(title)}}}")
    if label:
        lines.append(rf"\label{{{label}}}")

    # Tight local formatting
    lines.append(r"{\scriptsize")
    lines.append(r"\setlength{\tabcolsep}{4pt}")
    lines.append(r"\renewcommand{\arraystretch}{1.05}")

    # Use tabularx with X for Description
    lines.append(r"\begin{tabularx}{\linewidth}{lrrX}")
    lines.append(r"\toprule")
    lines.append(r"Project & Java LOC & Java classes & Description \\")
    lines.append(r"\midrule")

    notes = []  # (label, url)
    for i, r in enumerate(rows):
        proj = latex_escape(r["name"])
        url = r.get("github") or "N/A"
        desc = r["description"]  # keep full, rely on wrapping
        label_ch = tnote_label(i)

        # Project name carries the footnote marker
        proj_cell = f"{proj}\\tnote{{{label_ch}}}"
        lines.append(f"{proj_cell} & {fmt_int(r['java_loc'])} & {fmt_int(r['java_classes'])} & {latex_escape(desc)} \\\\")

        notes.append((label_ch, r"\url{" + latex_escape(url) + r"}"))

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabularx}")
    lines.append(r"}")  # end local formatting scope

    # Notes: only URLs, compact paragraph
    lines.append(r"\begin{tablenotes}[para]")
    lines.append(r"\scriptsize")
    lines.append(" ".join([rf"[{lbl}] {u}." for (lbl, u) in notes]))
    lines.append(r"\end{tablenotes}")
    lines.append(r"\end{threeparttable}")

    return "\n".join(lines)

# ----- Main -----
def main():
    with open("../projects/projects-with-validations.json", "r", encoding="utf-8") as f:
        projects = json.load(f)

    results = []
    for project in projects:
        base = project["source_basedir"]
        name = project.get("name") or Path(base).name
        github = project.get("github")

        java_loc = 0
        java_classes = 0
        for fp in traverse_files(base):
            p = Path(fp)
            java_loc += count_java_loc_in_file(p)
            java_classes += count_java_classes_in_file(p)

        description = CUSTOM_DESCRIPTIONS.get(name, "Open-source Java project")

        results.append({
            "name": name,
            "github": github,
            "source_basedir": base,
            "java_loc": java_loc,
            "java_classes": java_classes,
            "description": description,
        })

    # LaTeX (desc column + URL footnotes)
    latex = make_threepart_table_desc_column(
        results,
        title="Subject Systems Summary",
        label="tab:subject-systems"
    )
    print(latex)

if __name__ == "__main__":
    main()
