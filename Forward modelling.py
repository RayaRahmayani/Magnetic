import numpy as np
import matplotlib.pyplot as plt
#Diketahui
rho = -250
r = 50
z = 100
L = 1000
dL = 10
S = 500
# G = 6.673*(10**-11)
v = 4/3*np.pi*(r**3)

G = 6.673 * 1e-11 # Gravitational Constant
dx = np.arange(0, L, dL) # Matrix of station location
x = dx - S # Horizontal distance of station to sphere
m = x**2 + z**2
n = m ** 1.5
g = G * rho * v *z / n * 1e5 # m/s^2 -> mGal
print(g)
print(n)

plt.plot(dx,g)
plt.title ('gravity anomaly of buried sphere model')
plt.ylabel('gravity anomaly (mGal)')
plt.xlabel('Disantance(m')
plt.show()

p = np.arange(0, 360, 1)  # angle in degree
q = np.array(p * np.pi / 180)  # angle in radian

fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True)
ax1.plot(dx, g, "-")
ax1.grid()
ax1.set_ylabel("Gravity Anomaly (mGal)")
ax1.set_title("Gravity Anomaly of Burried Sphere Model")

ax2.fill(r * np.cos(q) + S, r * np.sin(q) + z, "-")
ax2.axis('equal')
ax2.invert_yaxis()
ax2.grid()
ax2.set_xlabel("Distance (m)")
ax2.set_ylabel("Depth (m)")
plt.show()

