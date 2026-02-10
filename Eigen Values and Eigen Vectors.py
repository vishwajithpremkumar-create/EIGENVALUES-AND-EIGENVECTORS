#Program to find the eigen values and eigen vectors.
#Developed by: Vishwajith P
#RegisterNumber:212225220122
import numpy as np

A = np.array([[2,-3,0],[2,-5,0],[0,0,3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values are", eigenvalues,"and Eigen Vectors are", eigenvectors)
