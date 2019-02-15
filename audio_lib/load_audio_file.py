import librosa
import Ipython.display as ipd
import matplotlib.pyplot as plt 
import librosa.display

audio_path = '../audio.wav'

""" x = returns an audio time series as a numpy array 
    sr = default sampling rate 
"""

x , sr = librosa.load(audio_path)

""" print numpy array and default sampling rate"""
print("x", "sr")

"""below line to execute in jupyter notebook for playing audio """
#ipd.Audio(audio_path)


"""to display the audio file plot """
plt.figure(figsize=(14,5))
librosa.display.waveplot(x, sr=sr)
