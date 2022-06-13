import matplotlib as mpl
import matplotlib.pyplot as plt


def rule(x):    # the iterative function
    return x ** 2 - 1


def makeplot(min, max, step, iterations, axis):
    # min is the minimum seed value wanting to plot
    # max is the maximum seed value wanting to plot
    # step is number of seeds to test from the min to max seed
    # iterations is the number of iterations wanting to go for
    # axis of the form [minX, maxX, minY, maxY]
    cmap = mpl.cm.hsv   # change this if you want to change the color map, maps can be found in mpl documentation
    y = []
    for i in range(iterations+1):   # creates an array of 0 to iterations
        y.append(i)
    plt.axis(axis)
    for x in range(step+1):   # loops thought the steps
        seed = x * ((max-min) / step) + min     # calculates the seed seed based on step
        path = [seed]
        for i in range(len(y)-1):   # creates array of the iterations of the function
            path.append(rule(path[i]))
        plt.plot(y, path, color=cmap(x/step), linewidth=.2)     # add the resulting line to graph
    plt.show()


if __name__ == "__main__":
    makeplot(-2, 2, 500, 10, [0,11,-2,4])