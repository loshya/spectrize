import soundfile as sf
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt

def getData(volume, freq, sampleRate, index):
    return int(volume * math.cos(freq * 6.28 * index /sampleRate))

def image_to_audio(filepath,sample_rate=44100,audio_duration=3):
    image  = imread(filepath,mode='RGB')
    height,width,depth = image.shape

    total_samples = audio_duration * sample_rate 
    samplesPerPixel = total_samples // width # how many samples should each pixel occupy
    freq_increments = (sample_rate//2) // height # difference in frequency between each pixel
    
    image  = image.sum(axis=2)
    
    volume = (100/765 * image) **2
    volume = volume.repeat(samplesPerPixel,axis=1)
    

    height  = np.arange((1+height)*freq_increments,freq_increments,-freq_increments).reshape(-1,1)
    nsample = np.arange(0,volume.shape[1]).reshape(-1,1)

    print('image  ',image.shape)
    print('volume ',volume.shape)
    print('nsample',nsample.shape)
    print('height ',height.shape)

    frequencies = volume * np.cos(height.dot(nsample.T) * 6.28 / sample_rate)
    print('frequencyy ',frequencies.shape)
    max_freq = np.abs(frequencies).sum(axis=0).max()
    print('max ',max_freq.shape)

    frequencies = frequencies.sum(axis=0) * (2**15-1) / max_freq

    print('frequencies',frequencies.shape)

    return frequencies.astype('int16')

sample_rate=44100
audio_duration=3

import time

t = time.time()
slist = image_to_audio('/home/hasebou/Pictures/bus.jpg')
print(time.time()-t)
sf.write('faster_numpy.wav',slist,sample_rate)