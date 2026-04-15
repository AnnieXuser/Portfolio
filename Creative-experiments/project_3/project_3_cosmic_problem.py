from dorothy import Dorothy
import librosa
import scipy.io.wavfile
import numpy as np

dot = Dorothy()

RATE = 44100
DTYPE = np.int16

def generate(freq, amp, duration, phi):
    t = np.linspace(0, duration, int(duration * RATE), endpoint=False) 
    data = np.sin(2 * np.pi * freq * t + phi) * amp
    return data.astype(DTYPE)

def create_tone(output_path = 'project_3/tone.wav', duration = 20):
    NTONES = 89
    amps = 2000.0 * np.random.random((NTONES,)) + 200
    keys = np.random.randint(1, 89, NTONES)
    freqs = 440.0 * 2 ** ((keys - 49.0) / 12.0)
    phi = 2 * np.pi * np.random.random((NTONES,))

    tone = np.array([], dtype = DTYPE)
    for i in range(NTONES):
        # Each note lasts 0.5 second
        newtone = generate(freqs[i], amp = amps[i], duration = 0.5, phi = phi[i])  
        tone = np.concatenate((tone, newtone))

    total_samples = int(duration * RATE)
    tone = tone[: total_samples] 

    scipy.io.wavfile.write(output_path, RATE, tone)
    return output_path

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        # Create new audio
        tone_path = create_tone()
        audio, sr = librosa.load(tone_path)

        # Load local audio files
        universe, sr = librosa.load("project_3/universe_modified.wav")
        speaking, sr = librosa.load("project_3/universe_repeated.wav")
        # Quieter
        speaking = speaking / 3

        # Mix
        samples_in_bar = len(speaking) // 4
        samples_in_beat = samples_in_bar // 2
        cut = speaking[:samples_in_beat * 2]
        audio[samples_in_beat:samples_in_beat * 3] = cut

        combined_audio = audio + universe[:len(audio)]
        
        dot.music.start_sample_stream(combined_audio, sr = sr)

        self.show_beat = 0

    def draw(self):
        col = dot.black
        if dot.music.is_beat():
            self.show_beat = 10

        if self.show_beat > 0:
            col = dot.yellow

        dot.background(col)
        self.show_beat -= 1
    
MySketch()
