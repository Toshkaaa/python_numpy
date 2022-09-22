import numpy as np
import matplotlib.pyplot as plt
 
def break_into_knots(lower_limit,high_limit, step):
    amount = int((high_limit - lower_limit) / step)
    amount += 1
    x = np.linspace(lower_limit, high_limit, num=amount)
    return x, amount

def runge_kutta(x,y0,h,n):
    y = np.zeros(n)
    y[0] = y0
    for i in range(n-1):
        k1 = h*f(x[i],y[i])
        k2 = h*f(x[i] + 1/2 *h, y[i] +1/2 *k1)
        k3 = h*f(x[i] + 1/2 *h, y[i] +1/2 *k2)
        k4 = h*f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    print("Runge kutta result: \n", x, "\n", y)
    return y

def adams_bashforth(x,y0,h,n):
    y = np.zeros(n)
    y[0:4] = runge_kutta(x,y0,h,4)
    for i in range(3, n-1):
        y[i+1] = y[i] + h/24 * (55* f(x[i],y[i]) - 59 * f(x[i-1],y[i-1]) + 37 * f(x[i-2],y[i-2])-9 * f(x[i-3],y[i-3]))
    print("Adams bushfort result: \n", x, "\n", y)
    return y

def exact_value(x,n):
    fx = lambda x: np.e**x + x**2
    y = np.zeros(n)
    for i in range(n):
        y[i] = fx(x[i])
    print("Exact result result: \n", x, "\n", y)
    return y

def create_plot(rows,cols):
    axs = plt.subplots(rows, cols, figsize=(13, 6))[1]
    for i in range(rows):
        for j in range(cols):
            axs[i,j].grid(True)

    axs[0, 0].plot(x, exact_result,'go--')
    axs[0, 0].set_title("Exact result")
    axs[0, 1].plot(x, runge_result,'bo--')
    axs[0, 1].set_title("Runge result")
    axs[0, 2].plot(x, runge_error_value,'ro--')
    axs[0, 2].set_title("Runge error")

    axs[1, 0].plot(x, exact_result,'go--')
    axs[1, 0].set_title("Exact result")
    axs[1, 1].plot(x, adams_result,'bo--')
    axs[1, 1].set_title("Adams result")
    axs[1, 2].plot(x,adams_error_value,'ro--')
    axs[1, 2].set_title("Adams error")
    plt.show()

if __name__ == '__main__':
    a = 0
    b = 1
    h = 0.1
    x0 = 0; y0 = 1
    f = lambda x,y : 2*x +(x**2)*(np.e**x) +(x**4) - x**2 + y*(1-x**2)
    x , n = (break_into_knots(a,b,h))
    runge_result = runge_kutta(x,y0,h,n)
    adams_result = adams_bashforth(x,y0,h,n)
    exact_result = exact_value(x,n)
    runge_error_value = np.abs(exact_result - runge_result)
    print("Runge error = \n",runge_error_value)
    adams_error_value = np.abs(exact_result - adams_result)
    print("Adams error = \n ", adams_error_value)
    create_plot(2,3)