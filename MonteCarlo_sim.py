import numpy as np 
from numpy import pi, log
import matplotlib.pyplot as plt

min, max = 50, 2000      #min and max photon energy in kev
nv = 3.43e23             #number of electrons in water per cubic centimeter 


# task 1

def atten_coef(hv):        #takes in photon energy hv as input,calculates K-N cross section per electron (ATTIX 7.15)
    radius = 2.818e-13
    m0c = 0.511 #MeV
    alpha = hv/m0c 
    
    #electronic cross section for Compton scattering
    sigma  = 2*pi*(
        radius**2 * ( ((1+alpha)/(alpha**2)) * (2*(1+alpha)/(1+2*alpha) 
        - log(1+2*alpha)/alpha)
        + log(1+2*alpha)/(alpha*2) 
        - (1+3*alpha)/((1+2*alpha)**2))
        )

    mu = sigma * nv

    return mu #returns attenuation coefficient

pub_200, pub2 = 0.137, 0.049  #published values
low_en, high_en = atten_coef(0.2), atten_coef(2)
low_per, high_per = 100*((atten_coef(0.2)-pub_200)/atten_coef(0.2)), 100*((atten_coef(2)-pub2)/atten_coef(2))

print(f"The attenuation coefficient for 200KeV is:          {low_en:.3f}")
print(f'percent difference from published value for 200KeV: {low_per:.1f}%')

print(f'The attenuation coefficient for 2MeV is:            {high_en:.3f}')
print(f'percent difference from published value for 2MeV:   {high_per:.1f}%')

# task 2

def prob_dis(): 
    return 0

# task 3

