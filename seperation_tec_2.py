import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0,1, 1001)

#Dew curve
y_dew_curve = -4.5063*(x_values**2) + 20.238*x_values + 339.53

#Bubble point
y_bubble_point = 6.0734*(x_values**2) + 9.5984*x_values + 339.52


#plotting dew curve and bubble point
plt.plot(x_values, y_dew_curve, label = 'Dew Cruve')
plt.plot(x_values, y_bubble_point, label = 'Bubble Point')

#plotting lines
plt.axvline(0.95)
plt.axhline(354.15)

#creating graph atrabutes
plt.legend()
plt.title('Binary Vapor Liquid Equilibrium', weight = 'bold')
plt.ylabel('Temperature [K]')
plt.xlabel('Xa, Xb mole fractions')

plt.minorticks_on()
plt.grid(which = 'major', linewidth  = 1)
plt.grid(which  = 'minor', linewidth = 0.1)

plt.xlim(0,1)
plt.ylim(339.5,356)
plt.show()
