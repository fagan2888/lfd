from tpsopt.constants import *
import numpy as np

NUM_PROCS = 5
GRIPPER_OPEN_CLOSE_THRESH = 0.06 # .06 for fig8 (thick rope), 0.04 for thin rope (overhand)
COLLISION_DIST_THRESHOLD = 0.0
MAX_ACTIONS_TO_TRY = 10  # Number of actions to try (ranked by cost), if TrajOpt trajectory is infeasible
TRAJOPT_MAX_ACTIONS = 5  # Number of actions to compute full feature (TPS + TrajOpt) on
WEIGHTS = np.array([-1]) 
##################
#  ROPE DEFAULTS
##################
ROPE_RADIUS        = .005
ROPE_ANG_STIFFNESS = .1
ROPE_ANG_DAMPING   = 1
ROPE_LIN_DAMPING   = .75
ROPE_ANG_LIMIT     = .4
ROPE_LIN_STOP_ERP  = .2
ROPE_MASS          = 1.0
ROPE_RADIUS_THICK  = .008

##################
# Planning Params
##################
JOINT_LENGTH_PER_STEP = .1
FINGER_CLOSE_RATE     = .1
