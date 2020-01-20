"""
    filename : custom_ai_utils.py
    description : Custom implementation of various AI things so that I don't
        have to rewrite them everytime I make something. Yes, I could just use
        an existing library and use their functions in the exact same way I'll
        be using these, but that's no fun! Better to write them myself and
        demonstrate my understanding. 
    author : Dylan P. Jackson
"""

import numpy as np

# Perform sigmoid function on input z, whether it be a scalar, vector, or matrix
def sigmoid(z):
    # Convert into numpy array
    z = np.array(z)
    return (1/(1 + np.exp(-z)) 
