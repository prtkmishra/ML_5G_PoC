from load_audio_file import AudioProcessing

if __name__ == "__main__":
    """ Path to sample audio file passed as an argument"""
    audio_path = './audio.wav'

    AudioProcObj = AudioProcessing(audio_path)
    AudioProcObj.waveplot()

#load_audio_file.waveplot()
