import matplotlib.pyplot as plt
from matplotlib.backend_tools import Cursors

fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Hover over an Axes to see alternate Cursors')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name, horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])


def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        print("Skipping setting cursor")
        return

    if event.inaxes:
        fig.canvas.set_cursor(event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)
        print("setting cursor", event.inaxes.cursor_to_use)


fig.canvas.mpl_connect('motion_notify_event', hover)

plt.show()
