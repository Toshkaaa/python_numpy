import numpy as np
e = 10e-5

def jacobi_method(a):
    print("Primary matrix a = \n",a)
    v = np.eye(4)
    k = 0
    m,n = np.shape(a)
    condition = True
    while condition:
        temp_a = np.copy(a)
        np.fill_diagonal(temp_a,0)
        temp_a[np.tril_indices(m,-1)] = 0
        i,j = np.unravel_index(np.argmax(np.abs(temp_a)), temp_a.shape)
        x = np.eye(4)
        d = ((a[i][i] - a[j][j])**2 + 4*((a[i][j])**(2)))**(0.5)
        c = (1/2 * (1 + abs(a[i][i] - a[j][j])/d))**(0.5)
        s = np.sign(a[i][j] * (a[i][i] - a[j][j])) * (1/2 * (1 - abs(a[i][i] - a[j][j])/d))**(0.5)
        x[i][i] = x[j][j] = c
        x[j][i] = s
        x[i][j] = -s
        v = np.dot(v,x)  
        a = np.dot(np.dot(np.transpose(x),a),x)
        print("T = \n", x, "\nT' = \n", np.transpose(x))
        temp = np.copy(a)
        np.fill_diagonal(temp,0)
        sa = 0; snd = 0; sd = 0
        sum_of_nondiagonal_elements = np.sum(temp)
        for i in range(m):
            for j in range(n):
                snd += temp[i][j] **2
                sa += a[i][j] **2
            sd += a[i][i] **2
        print("Sa=", sa, "Snd=", snd, "Sd = ", sd)
        if abs(sum_of_nondiagonal_elements) <= e:
            print("Sum of nondiagonal elements = ",sum_of_nondiagonal_elements)
            print("Final matrix a = \n",a)
            condition = False
        k +=1

def test_with_eig_func(a):
    evalue = np.linalg.eig(A)[0]
    print("\n--- Test with eig() --- \n Eigenvalues of the said matrix: ",evalue)

if __name__ == '__main__':
    A = np.array([[7.41, 1.13, 0.93, 1.22],
                 [1.13, 8.31, 1.30, 0.16],
                 [0.93, 1.30, 5.42, 2.10],
                 [1.22, 0.16, 2.10, 11.10]])
    jacobi_method(A)
    test_with_eig_func(A)
