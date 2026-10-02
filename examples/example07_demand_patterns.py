"""
This example demonstrates how VisWaterNet can be used to illustrate the different nodal demand patterns present in a water distribution network.
"""

# Import libraries
import viswaternet as vis
import matplotlib.pyplot as plt

# Initialize VisWaterNet model
model = vis.VisWNModel('Networks/CTown.inp')
style = vis.NetworkStyle(cmap='tab10',
                         discrete_legend_loc='lower left',
                         discrete_legend_title_font_size=13,
                         discrete_legend_label_font_size=15,
                         node_size=200,
                         dpi=400)
model.plot_unique_data(parameter="demand_patterns",
                       #discrete_legend_title='Demand Patterns',
                       label_list=['Training Area', 'Administrative Facilities', 'Barracks',
                                   'Lodging', 'Support Facilities', 'Utility Structures'],
                       savefig=True, save_name='figures/example07',
                       style=style)
plt.show()

# In[]
import wntr
import numpy as np
# Create a water network model
inp_file = 'Networks/CTown.inp'
wn = wntr.network.WaterNetworkModel(inp_file)

# Simulate hydraulics
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim()

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 5))),
     ('densely dotted',        (0, (1, 1))),

     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

def plot_linestyles(ax, linestyles, title):
    X, Y = np.linspace(0, 100, 10), np.zeros(10)
    yticklabels = []

    for i, (name, linestyle) in enumerate(linestyles):
        ax.plot(X, Y+i, linestyle=linestyle, linewidth=1.5, color='black')
        yticklabels.append(name)

    ax.set_title(title)
    ax.set(ylim=(-0.5, len(linestyles)-0.5),
           yticks=np.arange(len(linestyles)),
           yticklabels=yticklabels)
    ax.tick_params(left=False, bottom=False, labelbottom=False)
    ax.spines[:].set_visible(False)

    # For each line style, add a text annotation with a small offset from
    # the reference point (0 in Axes coords, y tick value in Data coords).
    for i, (name, linestyle) in enumerate(linestyles):
        ax.annotate(repr(linestyle),
                    xy=(0.0, i), xycoords=ax.get_yaxis_transform(),
                    xytext=(-6, -12), textcoords='offset points',
                    color="blue", fontsize=8, ha="right", family="monospace")

ff = [0.8, 1.5, 1.6, 2.0, 2.1, 2, 2.2, 2.5, 2.5, 2.5, 2.6, 2.5, 2.4, 2.4, 2.4, 2.3, 2.2, 1.5, 1.32, 0.8, 0.5, 0.6, 0.5, 0.4]
fig = plt.subplots(figsize = (12,6))
plt.plot(x[:24],pat[:24], color = 'k', lw = 2, label = 'Baseline')
plt.plot(x[:24],2*pat[:24], color = 'k', ls = '--',lw = 2, label = 'Personnel surge')
plt.plot(x[:24],ff, color = 'k', ls = ':',lw = 2, label = 'Wildfire suppression')
plt.plot(x[:24],0.3*pat[:24], color = 'k', ls = (0, (3, 10, 1, 10, 1, 10)),lw = 2, label ='Drought conditions')
plt.legend(fontsize = 14, frameon = False)
plt.xlabel('Time [hour]', fontsize = 14)
plt.ylabel('Demand [m3/hr]', fontsize = 14)
# plt.plot(x,pat2)
# plt.plot(x,pat3)
# plt.plot(x,pat4)
# plt.plot(x,pat5)