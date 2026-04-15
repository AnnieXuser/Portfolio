# Project 3: Cosmic Problem (Music, Numpy)

In this project I want to explore random generation of music and music editing with mix.

## Innovations in randomized generation methods

I applied what I learned at bilibili.com to generate audio using Numpy, but it didn't work.
（https://www.bilibili.com/list/watchlater?oid=207150965&bvid=BV16h411q7nC&spm_id_from=333.337.top_right_bar_window_view_later.content.click）

So I used `endpoint=False` to avoid overlap, replaced the obsolete `random_integers` with `np.random.randint`, and drawing audio waveforms by using the following code.

```python
plt.plot(np.linspace(0, len(tone) / RATE, len(tone)), tone)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Generated Tone Waveform")
plt.show()
```

<img width="1274" height="955" alt="efa0db8f-ce58-4df1-90c7-818a2485a849" src="https://github.com/user-attachments/assets/f21aef76-9dc9-40ab-8764-943553e5e9f9" />

## Creative Ideas & Audio Editing

I realized that each randomly generated (`tone.wav`) was different, and that such disorganized electronic sounds reminded me of the universe and aliens, so I looked for a soundtrack with a cosmic vibe, (`universe.wav`), and a humorous whisper, (`whocreatedunivers.wav`), hoping to harmoniously combine the three audios together.

Since (`universe.wav`) is five minutes long, I used the classroom example to cut it to 20 seconds and paste it twice to increase the volume. And (`whocreatedunivers.wav`) is only 0.3 seconds, so I generated it into a new 20-second audio by calculating, looping, and combining in (`speakingexpand.py`).

```python
# Calculate how many times to repeat the audio to reach 20 seconds
repetitions = int(np.ceil(20 / audio_length)) 
# Repeat the audio until it reaches 20 seconds
repeated_audio = np.tile(audio, repetitions)
```

The new audio file is saved as (`universe_repeated.wav`).


## Questions and Reflections

The most common error that occurs during the adjustment of the parameters is `ValueError`, and the control of duration is especially critical when generating random notes. Because the remaining two local music files in the project have been pre-processed to the same length, they are not prone to errors, while the dynamics of randomly generated notes increase the uncertainty.

eg. `ValueError: could not broadcast input array from shape (141120,) into shape (490612,)`

Through many attempts at different combinations of numbers, I came to realize that tone lengths in the generate function during audio generation that did not correlate with duration could lead to generation errors. For example, the error message in the code indicated that when the generate function generated an audio clip whose length did not satisfy the condition (89 * y >= x), an exception was thrown because the array could not be broadcast to the specified shape:

```python
create_tone(output_path='project_3/tone.wav', duration=x)
newtone = generate(freqs[i], amp=amps[i], duration=y, phi=phi[i])  
```

This process made me realize more deeply that audio processing is highly matchy-matchy, especially when splicing or mixing multiple audio clips, and that maintaining consistency in audio length is the key to avoiding errors. In addition, this attempt also made me reflect on the need for certain rules or restrictions to ensure overall harmony in randomized creations. Whether it is code logic or artistic creation, the balance between randomness and rules is essential.


## Conclusion

Finally, to make the mix sound better, I lowered the volume of the `speaking` to blend smoothly with the random notes. I then added background sounds to give the piece more depth and space, completing the work.



https://github.com/user-attachments/assets/12785bc9-48ea-4c50-83d2-f59f27e0b229



In this process, I deeply understood the unique charm inspired by the collision of randomness and certainty - the freedom and disorder of random notes, intertwined with the designed structure and rhythm, not only enriched the listening experience, but also injected a dynamic vitality into the work.
