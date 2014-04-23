import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_func(curve, name):
    sens = np.arange(0, 10, 3.0)
    x = mpl.mlab.frange(0, 1, 0.01)
    plt.figure(name)
    plt.title("%s curve" % (name))
    for s in sens:
        plt.plot(x, curve(x, s), label=("%i" % s))
    plt.legend(loc="best")
    plt.savefig("%s.png" % name)
    np.frange(0, 1)
    print("Saved figure %s.png" % (name))
    return


def herra_tight(x, s):
    out = x**(s/9.0) * ((1.0-np.cos(x*np.pi))/2.0)**((9-s)/9.0)
    return out


def herra_wide(x, s):
    out = x**(s/9.0) * ((1.0-np.cos(x*np.pi))/2.0)**((9-s)/4.5)
    return out


def exponential(x, s):
    out = (np.exp(x)-1)/(np.exp(1)-1)
    return out


def sigm(x, s):
    a = s+1
    out = 1.0/(1+np.exp(a*(-x+0.5)))
    return out


def logistic(x, s):
    s_x = sigm(x, s)
    s_one = sigm(1, s)
    s_zero = sigm(0, s)
    out = (s_x - s_zero)/(s_one - s_zero)
    return out


if __name__ == "__main__":
    plot_func(herra_tight, "Herra_9)")
    plot_func(herra_wide, "Herra_4.5")
    plot_func(exponential, "exp")
    plot_func(logistic, "sigmoid")
    print("All done!")
    sys.exit(0)
