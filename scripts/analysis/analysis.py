#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:00:19 2025

@author: alraune
"""

import numpy as np
import pandas as pd
from scipy.special import erfc, erfcinv

def import_data(file_path, display_data = True):
    tracer_data = pd.read_csv(file_path)
    
    if display_data:
        display(tracer_data)
        
    tracer_data.drop(index = 0,inplace = True)  # delete first row after headings which contains units
    time = pd.to_numeric(tracer_data['time'])
    tracer = pd.to_numeric(tracer_data['EC'])

    return time, tracer

def normalize_data(tracer,C_back = 0):

    """
    Normalizing tracer concentration by deducing background concentration

    Input
    -----
    tracer  - concentration (as function of time)
    C_back  - background concentration
    
    """
    
    tracer_norm = np.where(tracer<C_back,0,(tracer - C_back))

    return tracer_norm

def input_concentration(tracer, time, t_dur):

    """
    Determining average input concentration for finite duration of input
    
    Input
    -----
    tracer  - concentration (as function of time)
    time    - time 
    t_dur   - duration of injection
    
    """
    mass_total = np.trapz(tracer, x=time)
    c_av = mass_total/t_dur
    
    return c_av

def max_concentration(tracer):
    c_max = np.max(tracer)

    return c_max

def concentration_dimensionless(tracer, time, t_dur):   
    
    c_max = max_concentration(tracer)
    c_av = input_concentration(tracer, time, t_dur)
    if c_av<c_max:
        print("Average input concentration lower than maximal observed value")
        print("Fix mass for normalization to maximal observed input concentration")
        c_norm = c_max   
    else:
        print("Average input concentration higher than maximal observed value")
        print("Fix mass for normalization to average input concentration")
        c_norm = c_av
    
    tracer_dimless = tracer/c_norm
    return tracer_dimless

def advection_front(tracer,time):
    
    i_peak = np.argmax(tracer)
    t_50 = np.interp(0.5,tracer[0:i_peak],time[0:i_peak])

    return t_50
