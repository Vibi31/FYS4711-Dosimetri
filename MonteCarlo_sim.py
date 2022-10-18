import numpy as np 
from numpy import pi, log, exp
import matplotlib.pyplot as plt

min, max = 50, 2000      #min and max photon energy in kev
nv = 3.43e23             #number of electrons in water per cubic centimeter 


# task 1

def atten_coef(hv):        #takes in photon energy hv as input,calculates K-N cross section per electron (ATTIX 7.15)

    #using constants and calculating alpha from given energy
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

    #calculating attenuation coefficient
    mu = sigma * nv

    return mu #returns attenuation coefficient

pub_200, pub2 = 0.137, 0.049  #published values
low_en, high_en = atten_coef(0.2), atten_coef(2)
low_per, high_per = 100*((atten_coef(0.2)-pub_200)/atten_coef(0.2)), 100*((atten_coef(2)-pub2)/atten_coef(2))

#printing specified values and comparing with published values
print(f"The attenuation coefficient for 200KeV is:          {low_en:.3f} cm-1")
print(f'percent difference from published value for 200KeV: {low_per:.1f}%')

print(f'The attenuation coefficient for 2MeV is:            {high_en:.3f} cm-1')
print(f'percent difference from published value for 2MeV:   {high_per:.1f}%')

def plot_task1():
    energy = np.linspace(min/1000, max/1000, 100)

    plt.title('atttenuation coefficient as a function of energy')
    plt.ylabel('attenuation coeeficent [cm^-1]')
    plt.xlabel('energy [Mev]')

    plt.plot(energy, atten_coef(energy))
    plt.show()

#plot_task1()


# task 2
x = np.linspace(0, 50, 100)

def PD(hv, x):               #Probability Distrubution, takes in energy as argument
    mu = atten_coef(hv)      #uses function from task1
    pd = mu * exp(mu*(-x))   #probability distubutuion formula
    return pd


def CD(hv, x):               #Cumalative Distrubution, takes in energy as argument
    mu = atten_coef(hv)      #uses function from task1
    cd = 1 - exp(mu*(-x))    #cumalative distrubution formula
    return cd

def plot_task2():
    plt.title('probability distrubution')
    plt.plot(x, PD(0.2, x), 'b--')
    plt.plot(x, PD(2, x),'r--') 
    #plt.legend(['PD 200 KeV', 'PD 2 MeV'])
    #plt.show()

    #plt.title('cumalative distrubution')
    plt.plot(x, CD(0.2, x),'b-')
    plt.plot(x, CD(2, x), 'r-')
    #plt.legend(['CD 200 KeV', ' CD 2 MeV'])

    plt.legend(['PD 200 KeV', 'PD 2 MeV', 'CD 200 KeV', ' CD 2 MeV'])
    
    plt.show()

#plot_task2()


# task 3

def paths(hv):                                      #runs path siumulation for 1000 photons for given photon energy
    mu = atten_coef(hv)                             #either 2MeV or 200KeV
    tot_phot = 1000
    path_list = np.zeros(tot_phot)
    for i in range(tot_phot):
        path_list[i] = -log(1-np.random.randint(0, 100)/100)/mu  #using formula x = -log(1-u)

    mean = np.mean(path_list)                           #mean value of sampled events

    #the randit method fins a number between 0 and 100, it is then converted into a decimal between 0 and 1
    print(f'the mean path value for {hv}KeV is {mean:.1f}')

    return path_list
   
def plot_task3(hv):  #function to plot histogram 
    x = paths(hv)

    plt.title(f'histogram for path length of {hv} KeV and probability distrubution')
    plt.hist(x, bins = 100)
    plt.show()


plot_task3(0.2)
plot_task3(2)


    





