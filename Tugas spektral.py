import numpy as np
from scipy.stats import linregress
#Diketahui
rho1 =300
r1 = 50
z1 = 200
v1 = 4/3*np.pi*(r1**3)

rho2 = 500
r2 = 200
z2 = 1000
v2 = 4/3*np.pi*(r2**3)

L = 5000
dL = 20
s1 = 1500
s2 = 2500

G = 6.673 * 10e-11 # Gravitational Constant
dx = np.arange(0, L, dL) # Matrix of station location

x1 = dx - s1 # Horizontal distance of station to sphere #1
m1 = x1**2 + z1**2
n1 = m1 ** 1.5
g1 = G * rho1 * v1 *z1 / n1* 1e5

x2 = dx - s2 # Horizontal distance of station to sphere #2
m2 = x2**2 + z2**2
n2 = m2 ** 1.5
g2 = G * rho2 * v2 *z2 / n2 * 1e5

g = g1 + g2
import matplotlib.pyplot as plt
p = np.arange(0, 360, 1)  # angle in degree
q = np.array(p * np.pi / 180)  # angle in radian

fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True)
ax1.plot(dx, g, "-")
ax1.grid()
ax1.set_ylabel("Gravity Anomaly (mGal)")
ax1.set_title("Gravity Anomaly of Burried Sphere Model")

ax2.fill(r1 * np.cos(q) + s1, r1 * np.sin(q) + z1, "-")
ax2.fill(r2 * np.cos(q) + s2, r2 * np.sin(q) + z2, "-")
ax2.axis('equal')
ax2.invert_yaxis()
ax2.grid()
ax2.set_xlabel("Distance (m)")
ax2.set_ylabel("Depth (m)")
plt.show()
# Regional and residual
A = np.fft.fft(g) #using fft function, obtained the amplitude
A = np.abs(A) #sbsolute the imaginary part
A = A[0:int(np.floor(len(A)/2))] #cut off the mirrored amplitude
k = np.linspace(0, 1, len(A))/(2*dL) #generating the wavenumber (k)
plt.plot(k, np.log(A),'.')
plt.xlabel('k (rad/m)')
plt.ylabel('ln A')
plt.show()
print(np.log(A))
print(k)

#slope
Ap = np.log(A)
slope, intercept, rvalue, pvalue,stderr = linregress(k, Ap)
print(slope, intercept, rvalue, pvalue,stderr)
plt.plot(k, Ap, '.', label= 'original data')
plt.plot(k, intercept+slope*k, 'r', label = 'fifted line')
plt.legend()
plt.show()
