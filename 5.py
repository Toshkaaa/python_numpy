import numpy as np
import matplotlib.pyplot as plt

def break_into_knots(lower_limit,high_limit, amount):
    x = np.linspace(lower_limit, high_limit, num=amount)
    return x

def divided_difference(x_values):
    divided_difference_result = 0
    for j in x_values:
        temp_result = 1
        for i in x_values:
            if j!=i:
                temp_result *= (j - i)
        divided_difference_result += fx(j) / temp_result
    return divided_difference_result
              
def newton_polynom(x, point):
    result =  divided_difference([x[0]])
    for k in range(1, x.size - 1):
        temp_result = 1
        for i in range(k):
            temp_result *= (point - x[i])
        result += divided_difference(x[:k+1]) * temp_result
    return result
    
def spline_interpolation(x,y,x_points):
    global h 
    h = x[1] - x[0]
    n = x.size - 1
    a_coefficients = np.zeros(n)
    d = np.array([3*((y[i]-y[i-1])/h-(y[i-1]-y[i-2])/h) for i in range(2,n)])
    for i in range(n):
        a_coefficients[i] = y[i]
    A = np.zeros( (n-2,n-2) )
    np.fill_diagonal(A,4*h)
    np.fill_diagonal(A[0:,1:],h)
    np.fill_diagonal(A[1:,0:],h)
    c_coefficients = np.linalg.solve(A,d)
    c_coefficients = np.concatenate([[0],c_coefficients,[0]])

    d_coefficients = np.zeros(n)
    for i in range(n-1):
        d_coefficients[i] = (c_coefficients[i+1] - c_coefficients[i]) / 3*h
    d_coefficients[n-1] = -1*(c_coefficients[n-1]/3*h)

    b_coefficients = np.zeros(n)
    for i in range(n-1):
        b_coefficients[i] = (y[i] - y[i-1]) / h  - h/3 * (c_coefficients[i+1] + 2*c_coefficients[i])
    b_coefficients[n-1] = (y[n-1] - y[n-2]) /h - 2*h*c_coefficients[n-1] / 3

    value_list = []
    for i in x_points:
        for j in range(n):
            if (i >=x [j] and i <= x[j+1]):
                value_list.append(a_coefficients[j] + b_coefficients[j]*(i - x[j]) + c_coefficients[j]*(i - x[j])**2 + d_coefficients[j] * (i - x[j])**3)
                break    
    return x_points,value_list

def create_plot(cols):
    axs = plt.subplots(1, cols, figsize=(13, 6))[1]
    for j in range(cols):
        axs[j].grid(True)
    axs[0].plot(x,y,'bo--',x, newton_points, 'r--') 
    axs[0].legend(['Initial function', 'interpolation method'])
    axs[0].set_title("Newthon method") 
    axs[1].plot(x,(y-newton_points),'bo--') 
    axs[1].legend(['Error'])
    axs[1].set_title("Newton method error")
    axs[2].plot(spline_points_x,spline_points_y, 'ro--',x,y,'bo--',) 
    axs[2].legend(['Spline interpolation', 'Initial function'])
    axs[2].set_title("Spline interpolation")
    plt.show()

if __name__ == '__main__':
    fx = lambda x: 2* (np.sin(x/2))**2
    x = break_into_knots(-np.pi, np.pi, 10)
    y = np.array([fx(x[i]) for i in range(x.size)])
    print("List of node: \nx:", x, "\ny:",y)
    newton_points = np.array([newton_polynom(x,x[i]) for i in range(x.size)])
    points = break_into_knots(-np.pi+0.5, np.pi-0.2, 10)
    spline_points_x, spline_points_y = spline_interpolation(x,y,points)
    print("Error during newton method:", max(np.abs(newton_points-y)))
    print("Error during spline interpolation method:", max(np.abs(spline_points_y-y)))
    M3 = max(np.abs(np.power(spline_points_y,3)))
    print("M3 = ",M3 )
    print("R(x) <= ",(5*M3*(h**3)/2))
    create_plot(3)