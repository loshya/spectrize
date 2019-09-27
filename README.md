![Spectrize](logo.png)

A simple python script that transforms an image into audio form and vice versa.
The "encrypted" message can then be viewed on a spectrogram (audacity for example).
inspired by a cool easter egg in season one of Mr.Robot

# Usage
To spectrize an image(turn into audio form):
```bash
    ./spectrize <image-here>
```

To restore an image from a spectrize waveform (recommended to add the resolution for a cleaner output):
```bash
    ./despectrize <waveform-here> (optional: <width> <height>) #Default width/height 800x600
```

# Dependencies
recommended to have Anaconda 3. You also need the soundfile library:

```bash
    pip install soundfile
```

# License
MIT. Check 'LICENSE'
