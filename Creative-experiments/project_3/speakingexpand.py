from dorothy import Dorothy 
import librosa
import numpy as np
import scipy.io.wavfile

dot = Dorothy(600, 150)

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        audio, sr = librosa.load("project_3/whocreatedunivers.wav")
        audio_length = len(audio) / sr
        print(f"Original audio length: {audio_length} seconds")
        
        # Calculate how many times to repeat the audio to reach 20 seconds
        repetitions = int(np.ceil(20 / audio_length)) 
        
        # Repeat the audio until it reaches 20 seconds
        repeated_audio = np.tile(audio, repetitions)
        print(f"Repeated audio length: {len(repeated_audio) / sr} seconds")
     
        dot.music.start_sample_stream(repeated_audio, sr=sr)
        
        output_path = "project_3/universe_repeated.wav"
        scipy.io.wavfile.write(output_path, sr, (repeated_audio * 32767).astype(np.int16))

    def draw(self):
        dot.background((255, 255, 255))
        dot.draw_waveform(dot.canvas, col=dot.black, with_playhead=True)

MySketch()
