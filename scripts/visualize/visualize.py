#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:31:36 2025

@author: alraune
"""
import numpy as np
import matplotlib.pyplot as plt

def pure_advection(t_50,t_dur,dt = 0.1):

    time_cinitial = np.arange(0,t_50 + 1.5*t_dur +dt,dt)
    ct_initial = np.zeros_like(time_cinitial)
    ct_initial[int(t_50//dt):int((t_50+t_dur)//dt)] = 1

    plt.plot(time_cinitial,ct_initial,ls = '--',lw = 3,label = 'BTC without dispersion')

    plt.grid(True)
    plt.xlabel("Time $t$ [min]")
    plt.ylabel("Concentration")
    plt.legend(loc= 'best')
    
def btc(tracer, time, t_50 = False):
    
    plt.plot(time,tracer,'o:',lw = 2,label = 'data')

    if t_50 is not False:
        plt.scatter(t_50,0.5,c = 'red',s = 50,zorder = 5)

    plt.grid(True)
    plt.xlabel("Time $t$ [min]")
    plt.ylabel("Concentration ")
    plt.legend(loc= 'best')
    