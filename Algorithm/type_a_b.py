#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# Type A (G function) and Type B (Psi Function) descriptors with and without cut-off

def Feature_G(idx, env, r, delta):
    N = len(env)
    sum = 0
    vec_i = env[idx]
    for j in range(N):
        if idx != j:
            vec_j = env[j]
            vec_ij = vec_i - vec_j
            R_ij = np.sqrt(np.power(vec_ij[0],2) + np.power(vec_ij[1],2) + np.power(vec_ij[2],2))
            P = -1/(2*np.power(delta,2)) * np.power((r-R_ij),2)
            sum = sum + np.exp(P)
    G = sum
    return G


def Feature_Psi(idx, env, xi, zeta, lambda_):
    N = len(env)
    sum = 0
    vec_i = env[idx]
    for j in range(N):
        vec_j = env[j]
        for k in range(N):
            vec_k = env[k]
            vec_ij = vec_j - vec_i
            vec_jk = vec_k - vec_j
            vec_ik = vec_k - vec_i
            R_ij = np.sqrt(np.power(vec_ij[0],2) + np.power(vec_ij[1],2) + np.power(vec_ij[2],2))
            R_jk = np.sqrt(np.power(vec_jk[0],2) + np.power(vec_jk[1],2) + np.power(vec_jk[2],2))
            R_ik = np.sqrt(np.power(vec_ik[0],2) + np.power(vec_ik[1],2) + np.power(vec_ik[2],2))   
            dot_ij_ik = vec_ij[0]*vec_ik[0] + vec_ij[1]*vec_ik[1] + vec_ij[2]*vec_ik[2]
            cos_theta = dot_ij_ik / (R_ij * R_ik)
            B = np.power((1+lambda_*cos_theta), zeta)
            A = np.exp(-(np.power(R_ij,2)+np.power(R_jk,2)+np.power(R_ik,2))/(np.power(xi,2)))
            sum = sum + A * B
    Psi = sum
    return Psi

def F_G(idx, table, r, delta):
    N = len(table)
    sum = 0
    i = idx
    for j in range(N):      
        R_ij = table[i,j]
        P = -1/(2*np.power(delta,2)) * np.power((r-R_ij),2)
        sum = sum + np.exp(P)
    G = sum
    return G

def F_Psi(idx, env, xi, zeta, lambda_, table):
    N = len(env)
    sum = 0
    i = idx
    vec_i = env[idx]
    for j in range(N):
        if i != j:
            vec_j = env[j]
            for k in range(N):
                if (i != j) and (j != k) and (i != k):
                    vec_k = env[k]
                    vec_ij = vec_j - vec_i
                    vec_ik = vec_k - vec_i
                    R_ij = table[i,j]
                    R_jk = table[j,k]
                    R_ik = table[i,k]  
                    dot_ij_ik = vec_ij[0]*vec_ik[0] + vec_ij[1]*vec_ik[1] + vec_ij[2]*vec_ik[2]
                    try:
                        cos_theta = dot_ij_ik / (R_ij * R_ik)
                    except RuntimeWarning:
                        cos_theta = 0
                    B = np.power((1+lambda_*cos_theta), zeta)
                    A = np.exp(-(np.power(R_ij,2)+np.power(R_jk,2)+np.power(R_ik,2))/(np.power(xi,2)))
                    sum = sum + A * B
    Psi = sum
    return Psi

def F_G_with_cut(idx, table, r, delta, r_cut):
    N = len(table)
    sum = 0
    i = idx
    for j in range(N):
        if i!= j:
            R_ij = table[i,j]
            if R_ij <= r_cut:
                P = -1/(2*np.power(delta,2)) * np.power((r-R_ij),2)
                sum = sum + np.exp(P)
    G = sum
    return G

def F_Psi_with_cut(idx, env, xi, zeta, lambda_, table, r_cut):
    N = len(env)
    sum = 0
    i = idx
    vec_i = env[idx]
    for j in range(N):
        if i != j:
            if table[i,j] <= r_cut:
                vec_j = env[j]
                R_ij = table[i,j]
                vec_ij = vec_j - vec_i
                for k in range(N):
                    if (i != j) and (j != k) and (i != k):
                        if table[i,k] <= r_cut:
                            vec_k = env[k]   
                            vec_ik = vec_k - vec_i          
                            R_jk = table[j,k]
                            R_ik = table[i,k]  
                            dot_ij_ik = vec_ij[0]*vec_ik[0] + vec_ij[1]*vec_ik[1] + vec_ij[2]*vec_ik[2]
                            cos_theta = dot_ij_ik / (R_ij * R_ik)
                            B = np.power((1+lambda_*cos_theta), zeta)
                            A = np.exp(-(np.power(R_ij,2) + np.power(R_jk,2) + np.power(R_ik,2)) / np.power(xi,2))
                            sum = sum + A * B   
                          
    Psi = sum
    return Psi

