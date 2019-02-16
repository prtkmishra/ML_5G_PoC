import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
#import librosa.display.specshow

class AudioProcessing:
    """ load a sample audio and process the wave plots"""
    def __init__(self, audio_path):
        self.audio_path = audio_path


    def waveplot(self):

        """ x = returns an audio time series as a numpy array
            sr = default sampling rate
        """
        x , sr = librosa.load(self.audio_path)

        """ print numpy array and default sampling rate"""
        print(x, sr)
        """below line to execute in jupyter notebook for playing audio """
        #ipd.Audio(audio_path)
        """to display the audio file plot """
        plt.figure(figsize=(14,5))
        plt.plot(x)
        plt.show()
        librosa.display.waveplot(x, sr=sr)
