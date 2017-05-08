from PIL import Image
import math
import soundfile as sf
import numpy as np

def getData(volume, freq, sampleRate, index):
    return int(volume * math.cos(freq * 6.28 * index /sampleRate))

def image_to_audio(filepath,sample_rate=44100,audio_duration=3):
    im = Image.open(filepath)
    width, height = im.size

    total_samples = audio_duration * sample_rate 
    samplesPerPixel = total_samples // width # how many samples should each pixel occupy

    freq_increments = (sample_rate//2) / height # difference in frequency between each pixel
    slist = np.empty((total_samples,),dtype='float64')
    max_freq = 0
    for x in range(total_samples):
        xpixel = x//samplesPerPixel # used to map several samples to same pixel
        if xpixel >= width:
            xpixel = width - 1
        
        resultingfreq = 0
        for y in range(height):
            pixel_color = sum(im.getpixel((xpixel,y)))
            volume = (pixel_color * 100 / 765)**2

            freq = freq_increments * (height - y + 1)
            resultingfreq += getData(volume,freq,sample_rate,x)
            max_freq = max(abs(resultingfreq),max_freq)
        slist[x] = resultingfreq

    slist *= (32767/max_freq)
    slist = slist.astype(dtype='int16')

    return slist

sample_rate=44100
audio_duration=3

slist = image_to_audio('/home/hasebou/Pictures/car.jpg')
sf.write('new_file15.wav',slist,sample_rate)