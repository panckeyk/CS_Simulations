# initializes the global random number generator with a specific starting value,  ensuring that subsequent calls to NumPy's random functions produce the same sequence of numbers every time the code is run.

# example code : 
# This will always produce the same output: [0.37454012 0.95071431 0.73199394]
# Legacy method (sets global states)
import numpy as np 
np.random.seed(42)
print("Legacy method output: ", np.random.rand(3))  

# This will always produce the same output: [0.37454012 0.95071431 0.73199394]
# Modern method (isolated generator)
rng = np.random.default_rng(42)
print("Modern method output: ", rng.random(3))