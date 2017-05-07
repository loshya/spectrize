from PIL import Image
import math
import soundfile as sf
import numpy as np
def getData(volume, freq, sampleRate, index):
    return int(volume * math.sin(freq * math.pi * 2 * index /sampleRate))

im = Image.open('/home/hasebou/Pictures/seven-mile-beach-grand.jpg')
width, height = im.size

audio_duration = 3
sample_rate = 20000

total_samples = audio_duration * sample_rate
samplesPerPixel = total_samples // width

color = 10000 / height
slist = []
for x in range(total_samples):
    xpixel = x//samplesPerPixel
    if xpixel >= width:
        xpixel = width - 1
    resultingfreq = 0

    for y in range(height):
        pcolor = sum(im.getpixel((xpixel,y)))
        volume = pcolor * 100 / 765

        freq = color * (height - y + 1)
        resultingfreq += getData(volume,freq,sample_rate,x)
    slist.append(resultingfreq)

slist = np.asarray(slist,dtype='int16')
# max_amp = np.max(slist)
# slist *= (2**15 - 1)/max_amp

#slist = slist.astype('int16')

sf.write('new_file3.wav',slist,sample_rate)