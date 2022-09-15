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

plt.title('Mean path as a function of Energy in water')
plt.xlabel('log Energy (Mev)')
plt.ylabel('Mean path μ/ρ(Cm^2/g)')
plt.plot(np.log(Energy), mean_path)
plt.show()