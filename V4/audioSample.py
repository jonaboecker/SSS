# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:13:25 2023

@author: jo741boe
"""

import pyaudio
import numpy
import matplotlib.pyplot as plt
import time
import os
import re

def find_last_numbered_file(directory):
    pattern = r'^audioaufname_(\d+)'  # Muster, um nach Dateien mit dem Namen 'audio_#' zu suchen

    existing_files = [file for file in os.listdir(directory) if re.match(pattern, file)]
    numbers = []

    for file_name in existing_files:
        match = re.match(pattern, file_name)
        if match:
            numbers.append(int(match.group(1)))

    if numbers:
        return max(numbers)
    else:
        return 0  # Wenn keine Dateien gefunden werden, starte bei 0

directory = r'TestdatenJona'  # Hier den Pfad zu deinem Verzeichnis eintragen

last_number = find_last_numbered_file(directory)
next_number = last_number + 1

next_filename = f'TestdatenJona\\audioaufname_{next_number}'
print(f'Der nächste Dateiname sollte {next_filename} sein.')


FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
print('running')
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,
input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.frombuffer(data, dtype=int);
stream.stop_stream()
stream.close()
p.terminate()
print('done')
plt.plot(decoded)
plt.ylabel('Frequenz')
plt.xlabel('Zeit')
plt.show()
filename = 'audioaufname' + str(time.time())
numpy.save(next_filename, decoded)