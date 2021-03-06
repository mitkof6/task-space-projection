from opensim_importer import readMotionFile, indices_containing_substring
import matplotlib.pyplot as plt
import numpy as np
import os

###############################################################################

# parameters
working_dir = os.getcwd() + '/../data/results/'
# sto_file = 'ExampleAbsoluteCoordinates_BodyKinematics_pos_global.sto'
sto_file = 'ExampleCycling_TaskBasedTorqueController.sto'
# sto_file = 'ExampleArm26_states.sto'
substring_filter = 'gear'
# y_label = 'forces $(N | Nm)$'
# y_label = 'coordinates $(deg | rad)$'
y_label = ''
export_name = ''
max_cols = 3

###############################################################################

# load data
header, labels, data = readMotionFile(working_dir + sto_file)
indices = indices_containing_substring(labels, substring_filter)
assert(indices != [])
data = np.array(data)

# construct plots
rows = int(np.ceil(len(indices) / float(max_cols)))
fig, ax = plt.subplots(nrows=rows, ncols=max_cols, sharex='none',
                       sharey='none', figsize=(3 * max_cols, 2.5 * rows))
ax = ax.flatten()
for p, i in enumerate(indices):
    ax[p].plot(data[0:, 0], data[0:, i])
    ax[p].set_title(labels[i])
    ax[p].set_xlabel('time $(s)$')
    ax[p].set_ylabel(y_label)

# export figure
fig.tight_layout()
fig.show()
if export_name != '':
    fig.savefig(working_dir + export_name, dpi=300)
