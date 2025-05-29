#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
from sklearn.preprocessing import normalize

def get_neighbors(g: nx.Graph, node: int, depth: int) -> dict:
    output = {}
    layers = dict(nx.bfs_successors(g, source=node, depth_limit=depth))
    current = [node]
    for l in range(1, depth + 1):
        nxt = []
        for u in current:
            nxt.extend(layers.get(u, []))
        output[l] = nxt
        current = nxt
    return output

def type_d(
    coords: np.ndarray,
    graph: nx.Graph,
    dist_matrix: np.ndarray,
    max_depth: int
) -> np.ndarray:
    N = coords.shape[0]
    features = np.zeros((N, max_depth), dtype=np.float64)
    for l in range(1, max_depth + 1):
        decay = np.exp(-l)
        for i in range(N):
            nbrs = get_neighbors(graph, i, depth=l).get(l, [])
            s = 0.0
            r_i = coords[i]
            for idx_j, j in enumerate(nbrs):
                r_j = coords[j]
                v_ij = r_j - r_i
                R_ij = dist_matrix[i, j]
                for k in nbrs[idx_j+1:]:
                    if k == j:
                        continue
                    r_k = coords[k]
                    v_ik = r_k - r_i
                    R_ik = dist_matrix[i, k]
                    cos_theta = np.dot(v_ij, v_ik) / (R_ij * R_ik)
                    s += (1 + cos_theta) * decay * 2
            features[i, l-1] = s
    features = normalize(features, axis=0, norm='max')
    return features
