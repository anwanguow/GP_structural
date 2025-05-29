Graph-based Descriptors for Condensed Matter
==============

This repository contains the code and data from the article "Graph-based Descriptors for Condensed Matter".

The related article has been accepted in Physical Review E (PRE), see https://journals.aps.org/pre/accepted/cc072Ra1I1e19520f386411797c9bfb2a2d6501bc.

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
3. Type C descriptor: Use Networkx directly
4. Type D descriptor: type\_d.py

Batch Processing Script
-----------------
In the article, the procedures for generating distance matrices, constructing networks from point cloud data (frames in trajectories), calculating descriptors, assigning sample labels, and integrating feature matrices all involve batch computations and storage by traversing multiple sets of parameters. This part of the script is stored in the "Script" directory.

1. 
2.


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

Early Preprint Edition (Informal)
-----------------
The preprint edition is available at https://drive.google.com/file/d/1SP3bxhoXYQ117zxxdf5iud5gAEc-1Zj4/view?usp=sharing.

Contact
-----------------
An Wang: amturing@outlook.com 
