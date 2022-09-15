import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, cos, sin


with open("water_data.txt") as f:
        lines = f.readlines()
        E = []
        A = []
        for line in lines:
            vals = line.split("\t")
            E.append(float(vals[0]))
            A.append(float(vals[1]))

Energy, mean_path = np.array(E), np.array(A)

#task 1
def plot_1():
    plt.title('Mean path as a function of Energy in water')
    plt.xlabel('log Energy (Mev)')
    plt.ylabel('Mean path μ/ρ(Cm^2/g)')
    plt.plot(np.log(Energy), mean_path)
    plt.show()



#task 2
def scatter(incomming_angle_deg, incomming_energy):
    hv = incomming_energy                             #energy in Mev
    mc2 = 0.511                                       #electron volt mass (Mev)
    phi = np.deg2rad(incomming_angle_deg)             #radians of incomming angle
    c = 3e8                                           #m/s

    new_hv = hv/(1+(hv/mc2)*(1-cos(phi)))
    return new_hv


Energy_range = np.linspace(1, 100, 1000)
new_energy_30deg = scatter(30, Energy_range)
new_energy_60deg = scatter(35, Energy_range)
new_energy_80deg = scatter(40, Energy_range)

def plot_2():
    plt.plot(Energy_range, new_energy_30deg)
    plt.plot(Energy_range, new_energy_60deg)
    plt.plot(Energy_range, new_energy_80deg)
    plt.legend(['30 degrees', '35 degrees', '40 degrees'])
    plt.xlabel('Incomming energy (Mev)')
    plt.ylabel('scattered energy (Mev)')
    plt.show()


#task 3
def cross_sec(hv, angle_deg, radius):
    phi = np.deg2rad(angle_deg)
    #cross_p = pi*radius**2 * (v_marked/v)**2 * (v_marked/v + v/v_marked - sin(phi)**2)*sin(phi) #with respect to phi
    hv_m = scatter(angle_deg, hv)
    f1 = (hv_m/hv)**2
    f2 = ((hv_m/hv) + (hv/hv_m) - (sin(phi))**2)
    crosso = (radius**2/2) * f1 * f2                    #with respect to omega
    return crosso

r0 = 2.82*1e-13                                         #electron radius in cm
cross_sec = cross_sec(Energy_range, 30, r0)
plt.plot(Energy_range, cross_sec)
plt.show()


