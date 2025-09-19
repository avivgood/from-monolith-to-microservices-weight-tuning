
 This work is based on the paper:
 
 > From monolithic to microservice architecture: an automated approach based on graph clustering and combinatorial optimization	
 > 
	Published at **2023 IEEE 20th International Conference on Software Architecture (ICSA)**
	Paper available at https://doi.org/10.1109/ICSA56044.2023.00013

And the [https://github.com/sosygroup/from-monolith-to-microservices](replication package) provided by sosygroup for this paper. From now on the "original solution" will refer to this paper and the repository associated with it.

The paper is about decomposing a monolithic system to microservices. 

The original solution implemented in the paper builds a graph representation based on static code analysis, representing entities and methods as nodes, with edges representing the relationships between those elements.

>    After having allocated classes in the layers, the tool inspects
	the classes to find the declared methods and, going recursively
	deep in the code’s syntax tree, collects the method calls and the
	references to the entities. Then, a node of the graph is created
	for: (i) each method from classes of the logic and repository
	layer, (ii) each entity class. Relationships between methods
	and entities are put in the graph as directed arcs

and then assigns weights to the edges of the graphs based on the nature of the relationship

>After the analysis, default weights  
	are assigned according to the type of the relationship. The  
	default weight of the Persists relationship is 1, while  
	those of the Calls, Uses, References, and Extends  
	relationships are 0.8, 0.6, 0.2, and 0, respectively.

While the reasons why some weights were assigned heavier values then other are mentioned in the paper:

> In this way,
	we set the Persists relationship as the most important,
	and the method call relationship next to it. The reference
	and extends relationship weights are lower to favor domain
	entities to be distributed into different microservices

nowhere in the paper is there any mention as to why the those specific default weights been chosen and not others, and there is no mention of trying different weights in order to see which weights perform best.

Weights *can* be manually tuned in the original solution.

>weights can be manually refined to comply
	with specific application domains and requirement

But as the paper mentions, this is more for domain-specific constraints rather than for universal, "default" optimisation, which is what this work tries to achieve.  

The weights are important, as are used later in the work in the *System Decomposition* and *Optimization* to detriment how to best decompose a given system. It is highly suggested to read the original work for more context.

The purpose of this work is to create an algorithm that repeatedly runs the original solution from the paper on the 3 tested and included sample repositories, treating it as a "black box", and tries to find the weights  for each type of relationships that will perform "best", where "best" evaluated on part of the metrics that are automatically calculated and are defined in the paper. 
## Repository structure
```
Root
│   readme.md                           # This file
│   projects.json                       # Json file containing the list of the selectable monolithic systems
|   1-System_analysis.ipynb             # Jupyter Notebook implementing the static analysis step
|   2-Decomposition_optimization.ipynb  # Jupyter Notebook implementing the decomposition and optimization step
|─── javalang                           # Javalang library for java file parsing
└─── applications                       # Folder containing the considered usecases
     └─── *                             # Use case folders
          |── results                  # Folder containing the output files for the use case (results analysis included)
          └── source                   # Java source files of the use case monolithic application
```

## Included sources
This repository includes the Java source files of the following evaluated systems for auto-containment purposes (last update November 2022):
- Spring Petclinic (https://github.com/spring-projects/spring-petclinic)
- JPetstore (https://github.com/mybatis/jpetstore-6)
- Spring Blog (https://github.com/Raysmond/SpringBlog)
