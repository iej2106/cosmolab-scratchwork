

from classy import Class
%matplotlib notebook
import matplotlib.pyplot as plt
from math import pi
import numpy as np

## ---BEST FIT MATTER POWER SPECTRUM P(k)---
# create instance of the class "Class" 
LambdaCDM = Class()
# pass input parameters
LambdaCDM.set({'omega_b':0.022032,'omega_cdm':0.12038,'h':0.67556,'A_s':2.215e-9,'n_s':0.9619,'tau_reio':0.0925})
LambdaCDM.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0})
# run class
LambdaCDM.compute()
# get P(k) at redhsift z=0
kk = np.logspace(-4,np.log10(3),1000)
Pk = []
for k in kk:
    Pk.append(LambdaCDM.pk(k,0.)) # function .pk(k,z)

#Upper limit on h
LambdaCDM2 = Class()
LambdaCDM2.set({'omega_b':0.022032,'omega_cdm':0.12038,'h':2.70224,'A_s':2.215e-9,'n_s':0.9619,'tau_reio':0.0925})
LambdaCDM2.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0})
LambdaCDM2.compute()
kk2 = np.logspace(-4,np.log10(3),1000)
Pk2 = []
for k in kk2:
    Pk2.append(LambdaCDM2.pk(k,0.)) # function .pk(k,z)
    
#Lower limit on h
LambdaCDM3 = Class()
LambdaCDM3.set({'omega_b':0.022032,'omega_cdm':0.12038,'h':0.16889,'A_s':2.215e-9,'n_s':0.9619,'tau_reio':0.0925})
LambdaCDM3.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0})
LambdaCDM3.compute()
kk3 = np.logspace(-4,np.log10(3),1000)
Pk3 = []
for k in kk3:
    Pk3.append(LambdaCDM3.pk(k,0.)) # function .pk(k,z)
    
#Upper limit on omega_cdm    omega_b h^2 =0.0224±0.0001
LambdaCDM4 = Class()
LambdaCDM4.set({'omega_b':0.022032,'omega_cdm':0.22038,'h':0.67556,'A_s':2.215e-9,'n_s':0.9619,'tau_reio':0.0925})
LambdaCDM4.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0})
LambdaCDM4.compute()
kk4 = np.logspace(-4,np.log10(3),1000)
Pk4 = []
for k in kk3:
    Pk4.append(LambdaCDM4.pk(k,0.)) # function .pk(k,z)
    
#Lower limit on omega_cdm
LambdaCDM5 = Class()
LambdaCDM5.set({'omega_b':0.022032,'omega_cdm':0.02038,'h':0.67556,'A_s':2.215e-9,'n_s':0.9619,'tau_reio':0.0925})
LambdaCDM5.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0})
LambdaCDM5.compute()
kk5 = np.logspace(-4,np.log10(3),1000)
Pk5 = []
for k in kk5:
    Pk5.append(LambdaCDM5.pk(k,0.)) # function .pk(k,z)

# plot P(k)
plt.figure(1)
plt.xscale('log');plt.yscale('log');plt.xlim(kk[0],kk[-1])
plt.xlabel(r'$k \,\,\,\, [h/\mathrm{Mpc}]$')
plt.ylabel(r'$P(k) \,\,\,\, [\mathrm{Mpc}/h]^3$')
bestfit, = plt.plot(kk,Pk,'r-')
upperlimh, = plt.plot(kk,Pk2,'b--')
lowerlimh, = plt.plot(kk,Pk3,'y--')
upperlimomega, = plt.plot(kk,Pk4,'orange')
lowerlimomega, = plt.plot(kk,Pk5,'g--')
plt.legend([bestfit, upperlimh, lowerlimh, upperlimomega-cdm, lowerlimomega_cdm], ['Best Fit', 'Upper limit on h', 'Lower limit on h','Upper limit on omega_b','Lower limit on omega_b'])
plt.grid()


