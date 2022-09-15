import matplotlib.pyplot as plt
import numpy as np


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

    new_hv = hv/(1+(hv/mc2)*(1-np.cos(phi)))
    return new_hv


Energy_range = np.linspace(1, 10, 1000)
new_energy_30deg = scatter(30, Energy_range)
new_energy_60deg = scatter(35, Energy_range)
new_energy_80deg = scatter(40, Energy_range)

plt.plot(Energy_range, new_energy_30deg)
plt.plot(Energy_range, new_energy_60deg)
plt.plot(Energy_range, new_energy_80deg)
plt.legend(['30 degrees', '35 degrees', '40 degrees'])
plt.xlabel('Incomming energy (Mev)')
plt.ylabel('scattered energy (Mev)')
plt.show()



