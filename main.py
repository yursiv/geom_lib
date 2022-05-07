# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import matplotlib as plt
    from matplotlib.pyplot import plot
    import numpy as np

    xvalues = np.array([0, 1, 2, 3, 4]);
    yvalues = np.array([0, 1, 2, 3, 4]);

    xx, yy = np.meshgrid(xvalues, yvalues)


    plot(xx, yy, marker='.', color='k', linestyle='none')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
