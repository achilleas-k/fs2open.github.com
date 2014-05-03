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
    filename = ("%s.png" % name).lower().replace(" ", "_")
    plt.savefig(filename)
    print("Saved figure %s" % (filename))
    return


def retail(x, s):
    out = x*(s/9)+(x**5)*(9-s)/9
    return out


def windows(x, s):
    out = x**(3-(s/4.5))
    return out


def herra_tight(x, s):
    out = x**(s/9.0) * ((1.0-np.cos(x*np.pi))/2.0)**((9-s)/9.0)
    return out


def herra_wide(x, s):
    out = x**(s/9.0) * ((1.0-np.cos(x*np.pi))/2.0)**((9-s)/4.5)
    return out


def exponential(x, s):
    out = (np.exp(x)-1)/(np.exp(1)-1)
    return out


def mixed(x, s):
    out = x**(1+((5-s)/9))
    return out


def power(x, s):
    out = x**(1+(9-s)/9)
    return out


if __name__ == "__main__":
    plot_func(retail, "Retail")
    plot_func(windows, "Windows")
    plot_func(herra_tight, "Herra 9")
    plot_func(herra_wide, "Herra 4.5")
    plot_func(exponential, "Exponential")
    plot_func(mixed, "Mixed")
    plot_func(power, "Power")
    print("All done!")
    sys.exit(0)
