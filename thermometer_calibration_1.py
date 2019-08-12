#!/usr/bin/env python
# coding: utf-8

# In[191]:


import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import interpolate as spi

x1, y1 = np.loadtxt('X103389.txt', delimiter=',', unpack=True)
x2, y2 = np.loadtxt('X103395.txt', delimiter=',', unpack=True)
x3, y3 = np.loadtxt('X103397.txt', delimiter=',', unpack=True)
x4, y4 = np.loadtxt('X103399.txt', delimiter=',', unpack=True)

T, t1, t2, t3, t4 = np.loadtxt('cooldown_20190809.csv', delimiter=',', unpack=True) 

x_new1 = np.arange(293.0, 4.0)
func1 = spi.interp1d(x1,y1,fill_value="extrapolate")
y_new1 = func1(x_new1)
y_newer1 = func1(t1)

x_new2 = np.arange(293.0, 4.0)
func2 = spi.interp1d(x2,y2,fill_value="extrapolate")
y_new2 = func2(x_new2)
y_newer2 = func2(t2)

x_new3 = np.arange(293.0, 4.0)
func3 = spi.interp1d(x3,y3,fill_value="extrapolate")
y_new3 = func3(x_new3)
y_newer3 = func3(t3)

x_new4 = np.arange(293.0, 4.0)
func4 = spi.interp1d(x4,y4,fill_value="extrapolate")
y_new4 = func4(x_new4)
y_newer4 = func4(t4)

#plt.plot(x,y,'r', label='Thermometer 1')
plt.plot(T, y_newer1, 'c-', label='Thermometer 1')
plt.plot(T, y_newer2, 'y-', label='Thermometer 2')
plt.plot(T, y_newer3, 'b:', label='Thermometer 3')
plt.plot(T, y_newer4, 'r:', label='Thermometer 4')
#plt.plot(x_new,y_new, 'b--', label = 'extrapolate')

#plt.xlabel('Resistance (Ω)')
#plt.ylabel('Temperature (K)')
#plt.title('Calibration Curve')
plt.xlabel('Time (ms)')
plt.ylabel('Temperature (K)')
plt.title('Temperature')

plt.legend()
plt.show()


# In[149]:


x2, y2 = np.loadtxt('X103395.txt', delimiter=',', unpack=True)
y_new = np.arange(293.0, 4.0)
func = spi.interp1d(y2,x2,fill_value="extrapolate")
x_new = func(y_new)

plt.plot(x2,y2,'r', label='Thermometer 1')
plt.plot(x_new,y_new, 'b--', label = 'extrapolate')

plt.xlabel('Resistance')
plt.ylabel('Temperature (K)')
plt.title('Calibration Curves')
plt.legend()
plt.show()
print(func(4.0))


# In[184]:


y_newer1, y_newer2, y_newer3, y_newer4


# In[147]:


x3, y3 = np.loadtxt('X103397.txt', delimiter=',', unpack=True)
y_new = np.arange(293.0, 4.0)
func = spi.interp1d(y3,x3,fill_value="extrapolate")
x_new = func(y_new)

plt.plot(x3,y3,'r', label='Thermometer 1')
plt.plot(x_new,y_new, 'b--', label = 'extrapolate')

plt.xlabel('Resistance')
plt.ylabel('Temperature (K)')
plt.title('Calibration Curves')
plt.legend()
plt.show()
print(func(4.1))


# In[148]:


x4, y4 = np.loadtxt('X103399.txt', delimiter=',', unpack=True)
y_new = np.arange(293.0, 4.0)
func = spi.interp1d(y3,x3,fill_value="extrapolate")
x_new = func(y_new)

plt.plot(x,y,'r', label='Thermometer 1')
plt.plot(x_new,y_new, 'b--', label = 'extrapolate')

plt.xlabel('Resistance')
plt.ylabel('Temperature (K)')
plt.title('Calibration Curves')
plt.legend()
plt.show()
print(func(4.1))


# In[153]:


#T = time

#Thermometer 1 = Top of cavity
#Thermometer 2 = Bottom of cavity
#Thermometer 3 = Bottom of shield
#Thermometer 4 = Top of shield

T, t1, t2, t3, t4 = np.loadtxt('cooldown_20190809.csv', delimiter=',', unpack=True) 
plt.plot(T,t1,'r', label='Thermometer 1')
plt.plot(T,t2,'y', label='Thermometer 2')
plt.plot(T,t3,'g', label='Thermometer 3')
plt.plot(T,t4,'b--', label='Thermometer 4')


plt.xlabel('Time')
plt.ylabel('Resistance')
plt.title('Calibration Curves')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




