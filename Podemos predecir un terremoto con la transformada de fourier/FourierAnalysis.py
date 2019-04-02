#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
#data visualization
import matplotlib.pyplot as plt
import matplotlib.colors as colors
plt.rcParams["figure.figsize"] = (15,10)


import numpy as np
from scipy.fftpack import fft, rfft
import scipy.signal as signal
import os
import gc

pd.options.display.precision = 15


# In[3]:


seq_0 = pd.read_csv('seq_0.csv', dtype={'acoustic_data': np.int16, 'time_to_failure': np.float64})


# In[4]:


def fast_fourier_transform(df, interval):
    '''It takes a dataframe and a intervale number for split the dataframe
    df: pd.DataFrame()
    interval: int
    
    saves the figures generated
    '''
    images = []
    cont_name = 1
    for x in range(0, len(df), interval):
        print('\nInterval {} to {}'.format(x, x+interval))
        y = rfft(df['acoustic_data'][x:x+interval])
        fig, ax = plt.subplots()
        ax.set_ylabel('Frequency [Hz]')
        ax.plot(y)#(y[1:])
        ax.set_xlim([-1,40_000])
        ax.set_ylim([-500_000, 500_000])
        plt.title(str(x+interval) + ' de ' + str(len(df)))
        plt.savefig(f'img/rfft/seq0_fft_{cont_name}.jpg')
        plt.close(fig)
        cont_name+=1


# In[5]:


def st_fourier_transform(inputSignal, samplingFreq, nperseg=256, ylim_max=None):
    '''Calculates the STFT for a time series:
        inputSignal: numpy array for the signal (it also works for Pandas.Series)
        samplingFreq: the sampling frequency
        nperseg : int, optional
            Length of each segment. Defaults to 256.
        ylim_max: the max frequency to be shown. By default it's the half sampling frequency.'''
    
    f, t, Zxx = signal.stft(inputSignal, samplingFreq, nperseg=nperseg)

    fig = plt.figure()

    spec = plt.pcolormesh(t, f, np.abs(Zxx), 
                          norm=colors.PowerNorm(gamma=1./8.),
                          cmap=plt.get_cmap('magma'))
    
    cbar = plt.colorbar(spec)
    plt.title('STFT Spectrogram')
    ax = fig.axes[0]
    ax.grid(True)
    ax.set_title('STFT Magnitude')
    if ylim_max:
        ax.set_ylim(0,ylim_max)
    ax.set_ylabel('Frequency [Hz]')
    ax.set_xlabel('Time [sec]')
    fig.show
    return


# In[7]:


st_fourier_transform(seq_0['acoustic_data'], 4e6, nperseg=1048576, ylim_max=300000)


# In[8]:


fast_fourier_transform(seq_0, 150_000)


# In[ ]:




