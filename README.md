# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
Step 1:

Import the NumPy library to perform numerical operations.

Step 2:

Define the matrix 
𝐴
A for which eigenvalues and eigenvectors are to be calculated.

Step 3:

Use the function np.linalg.eig(A) to compute:

Eigenvalues (stored in a variable)

Corresponding Eigenvectors (stored in another variable)

Step 4:

Display the eigenvalues and eigenvectors as output.
## Program:
```
#Program to find the eigen values and eigen vectors.
#Developed by: Vishwajith P
#RegisterNumber:212225220122
import numpy as np

A = np.array([[2,-3,0],[2,-5,0],[0,0,3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values are", eigenvalues,"and Eigen Vectors are", eigenvectors)
```
## Output:
<img width="1346" height="516" alt="image" src="https://github.com/user-attachments/assets/944ee337-a705-48e7-ade5-1f61aa1054d7" />

## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
