from PIL import Image
import math
import soundfile as sf
import numpy as np

def getData(volume, freq, sampleRate, index):
    return int(volume * math.sin(freq * math.pi * 2 * index /sampleRate))

def image_to_audio(filepath):
    im = Image.open(filepath)
    width, height = im.size

    audio_duration = 3 # how many seconds should the audio be
    sample_rate = 20000 #samples per second

    total_samples = audio_duration * sample_rate 
    samplesPerPixel = total_samples // width # how many samples should each pixel occupy

    freq_increments = 8000 / height # difference in frequency between each pixel
    slist = []
    for x in range(total_samples):
        xpixel = x//samplesPerPixel # used to map several samples to same pixel
        if xpixel >= width:
            xpixel = width - 1
        
        resultingfreq = 0
        for y in range(height):
            pixel_color = sum(im.getpixel((xpixel,y)))
            volume = pixel_color * 100 / 765

            freq = freq_increments * (height - y)
            resultingfreq += getData(volume,freq,sample_rate,x)
        slist.append(resultingfreq)

    slist = np.asarray(slist,dtype='int16')
    return slist

slist = image_to_audio('/home/hasebou/Desktop/dsp/HelloWorld.png')
sf.write('new_file12.wav',slist,20000)