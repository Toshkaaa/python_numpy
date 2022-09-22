import numpy as np


def solve_matrix(a, b):
    print("Matrix A = ", a)
    print("Matrix B = ", b)
    a = np.column_stack((a, b))
    print("Union matrix = ", a)
    for k in range(a.shape[0] - 1):
        c = a[k:a.shape[0], k:a.shape[1]]
        max_element = np.unravel_index(np.absolute(c[:, 0:c.shape[0]]).argmax(), c[:, 0:c.shape[0]].shape)
        for i in range(c.shape[0]):
            if i != max_element[0]:
                m = - (c[i][max_element[1]]) / (c[max_element[0]][max_element[1]])
                c[i] = c[i] + c[max_element[0]] * m
        if max_element[1] != 0:
            c[:, [max_element[1], 0]] = c[:, [0, max_element[1]]]
        if max_element[0] != 0:
            c[[max_element[0], 0], :] = c[[0, max_element[0]], :]
        a[k:a.shape[0], k:a.shape[1]] = c
        print("Temporary value of matrix = \n", a)
    m = a.shape[0]
    x = np.zeros(m)
    x[m-1] = a[m-1][m] / (a[m-1, m-1])
    for i in reversed(range(m-1)):
        a[:, i+1] = a[:, i+1] * x[i+1]
        x[i] = (a[i][m] - np.sum(a[i, i+1:m]))/a[i][i]
    print("Your answer = ", x)
    r = np.abs(b - A @ x)
    print("r =", r)


if __name__ == '__main__':
    A = np.array([[3.81, 0.25, 1.28, 1.75],
                 [2.25, 1.32, 5.58, 0.49],
                 [5.31, 7.28, 0.98, 1.04],
                 [10.39, 2.45, 3.35, 2.28]])
    B = np.array([4.21, 8.97, 2.38, 12.98])
    np.set_printoptions(suppress=True)
    solve_matrix(A, B)
