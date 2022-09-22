import numpy as np
e = 1e-4

def seidel_method(a, b):
    print("Original matrices: \n","a=",a,"\n","b=", b)
    a, b = np.transpose(a)@a, np.transpose(a)@b 
    print("Symmetric positive definite matrices: \n","a=", a, "\n", "b=", b)
    n = a.shape[0]
    b = b / np.diagonal(a)
    a = -a / np.diagonal(a)[:,None]
    np.fill_diagonal(a,0)
    x0 = np.copy(b)
    x1 = np.copy(b)
    condition = True
    iteration = 0
    while condition:
        iteration += 1
        for i in range(n):
            x1[i] = b[i] +  a[i]@x1 
        r = np.abs(b - a@x1)
        print("Iteration №", iteration ,", approximate value = ", x1, "r =", r)
        if (max(np.abs((x1-x0))) < e):
            print("Your solution is:", x1)
            condition = False 
        x0 = np.copy(x1)

if __name__ == '__main__':
    A = np.array([[3.81, 0.25, 1.28, 1.75],
                 [2.25, 1.32, 5.58, 0.49],
                 [5.31, 7.28, 0.98, 1.04],
                 [10.39, 2.45, 3.35, 2.28]])
    B = np.array([4.21, 8.97, 2.38, 12.98])
    seidel_method(A, B)