Graph-based Descriptors for Condensed Matter
==============

This repository contains the code and data from the article "Graph-based Descriptors for Condensed Matter".

The related article has been published in Physical Review E (PRE), where it is accessible at https://journals.aps.org/pre/abstract/10.1103/PhysRevE.111.064302.

Data
-----------------
The raw data involved in the paper, namely the MD simulation trajectories and the LAMMPS scripts used to generate them, can be found in the “data/Traj” directory.

Figures
-----------------
The code for reproducing each figure in the article can be found in the "Figures" directory.

Algorithms
-----------------
The code for key algorithms in the article can be found in the "Algorithm" directory.

1. Modified Voronoi method: voronoi.py
2. $p_{hop}$: p\_hop.py
3. Type A and B descriptors: type\_a\_b.py
4. Type C descriptor: Use Networkx directly
5. Type D descriptor: type\_d.py

Batch Processing Script
-----------------
In the article, the procedures for generating distance matrices, constructing networks (using the modified Voronoi method) from point cloud data (frames in trajectories), calculating various descriptors, assigning sample labels, and integrating feature matrices all involve batch computations and storage by traversing multiple sets of parameters. This part of the script is stored in the "Script" directory. Before running, please configure the relevant directories and paths according to your local environment, and set the corresponding parameters in scripts as needed (see comments for variables from the code).

1. Distance matrix: get\_distance\_table.py
2. Graph Generation (modified Voronoi method): generate\_graph.py
3. Sample Labelling (labelled as soft or hard according to $p_{hop}$): y\_label.py
4. The value of $p_{hop}$: p\_hop\_value.py
5. Type A descriptor: Type\_A.py
6. Type B descriptor: Type\_B.py
7. Type C descriptor: Type\_C.py
8. Type D descriptor: Type\_D.py
9. Feature matrix and dataset for ML: dataset.py


Traditional Machine Learning Approach
-----------------
This part is related to the results of traditional machine learning part.

The saved sessions of MATLAB Classification Learner:
https://drive.google.com/file/d/1-0hi_-P2unh_muGqAeghlDOeup4i5-NR/view?usp=sharing

Deep Learning Approach
-----------------
See https://github.com/anwanguow/graph_descriptor_deep_learning.

PCA on Feature Matrix
-----------------
See directory "PCA".

Reference
-----------------
```bibtex
Information from Google Scholar
Awaiting...
```

Early Preprint Edition (Informal)
-----------------
The preprint edition is available at https://drive.google.com/file/d/1SP3bxhoXYQ117zxxdf5iud5gAEc-1Zj4/view?usp=sharing.

Contact
-----------------
An Wang: amturing@outlook.com 
