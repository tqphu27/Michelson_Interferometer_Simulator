from __future__ import unicode_literals
import random
import numpy as np
import matplotlib.pyplot as plt
from colour_system import cs_hdtv
from simulation import spec_wavelengths


'''
    This function calculates RGB map from simulation pattern
'''
def RGBConverter(pattern):
    wavelength_arr = np.array([entry[1] for entry in pattern]).reshape(100,100,-1)[0,0,:]
    intensity_arr = np.array([entry[2] for entry in pattern]).reshape(100,100,-1)
    
    spec_map = np.zeros((100,100,np.size(spec_wavelengths)))
    
    for i in range(np.size(wavelength_arr)):
        idx = int((wavelength_arr[i]-380)/5)
        if 0<=idx<np.size(spec_wavelengths):
            spec_map[:,:,idx] += intensity_arr[:,:,i]
       
    return np.apply_along_axis(cs_hdtv.spec_to_rgb, axis=2, arr=spec_map)

def showPattern(ax, simulation, is_colored=False):

    pattern = simulation.Interference()
    
    if is_colored:
        ax.imshow(RGBConverter(pattern), interpolation='none')
    else:
        ax.imshow(np.array([entry[2] for entry in pattern]).reshape(100,100,-1).sum(axis=2))

