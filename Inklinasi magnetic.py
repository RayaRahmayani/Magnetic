import numpy as np
import matplotlib.pyplot as plt

bm =50000
i = 23
i = np.pi*((90-i)/180)
print(i)
bez = -bm * np.cos(i)
bex = -bm * np.sin(i)


k = 1e-2
r = -46
z = 100
o = 500
v = 4/3 * np.pi *r **3
mu0 = 4*np.pi*1e-7

M = v*k*bm/mu0

s= 1000
ds = 10
x = np.arange(0,s,ds)
dx = x-o

R = np.array((z*z+dx*dx)**0.5)
theta= np.arctan(np.array(dx/z))

br = np.array(-(mu0*2*M*np.cos(i-theta))/(R**3))
bt = np.array(-(mu0*M*np.sin(i-theta))/(R**3))

baz = np.array((br*np.cos(theta))+(bt*np.sin(theta)))
bax = np.array((br*np.sin(theta))-(bt*np.cos(theta)))

bx = bex+bax
bz = bez + baz
boobs = (bx*bx+bz*bz)**0.5

p = np.arange(0,360,1)#angle in degree
q = np.array(p*np.pi/180)
b = r*np.cos(q)+o
c = r*np.sin(q)+z
fig, (ax1,ax2) = plt.subplots(2, 1, sharex = True)
ax1.plot(x,boobs,'-')
ax1.grid()
ax1.set_ylabel('Magnetic Anomaly (mGal)')
ax1.set_xlabel('Magnetic Anomaly of Burried Sphere Model')
ax2.fill(b,c, '-')
ax2.axis('equal')
ax2.invert_yaxis()
ax2.grid()
ax2.set_xlabel('Distance(m)')
ax2.set_ylabel('Depth(m)')
plt.show()
