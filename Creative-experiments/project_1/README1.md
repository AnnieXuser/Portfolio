# Project 1: Little Pond (Music, Drawings, Animation)

In WEEK 1, I was inspired to create the INFINITE MIRROR through the randomization tool provided in class, and I began by creating a preliminary version of the image using layers of nested rectangles and lines connected to diagonal lines.

<img width="635" alt="infinite_mirror" src="https://git.arts.ac.uk/24009429/STEM2425-AiningXu-Portfolio/assets/1178/3a88abd9-3cca-4aaf-8d95-296e0ff07443">

Over the next few weeks of study, I realized that music could be combined with images for more interesting interactions and visual effects, so I created Little Pond.


## Error & Solution: Amplitude Gap

I started my research by looking at how images expand from the inside out, which means when splash changes, the number of the rectangles changes at the same time.

```python
if self.splash = 10：
    rectangle(dot.canvas, (240,240), (260,260), dot.yellow, 2)
elif self.splash = 8:
    rectangle(dot.canvas, (240,240), (260,260), dot.yellow, 2)
    rectangle(dot.canvas, (220,220), (280,280), dot.yellow, 2)
elif self.splash = 6:
    rectangle(dot.canvas, (240,240), (260,260), dot.yellow, 2)
    rectangle(dot.canvas, (220,220), (280,280), dot.yellow, 2)
    rectangle(dot.canvas, (200,200), (300,300), dot.yellow, 2)
    ...
```
This didn't work, so I thought about amplitude. Amplitude determines the energy transfer of a sound wave and thus affects the perception of the loudness of a sound. I'm trying to figure out how to pronounce musical accents and control images.
I observed that the `rectangle` wasn't smooth enough when changing because the edges were sharper, so I replaced the `rectangle` with an `ellipse`.

```python
if amplitude > 0.01 and amplitude <= 0.02:
    ellipse(dot.canvas, (150, 520), (50, 10), 0, 0, 360, dot.darkblue, -1)
elif amplitude > 0.02 and amplitude <= 0.03:
    ellipse(dot.canvas, (150, 520), (70, 16), 0, 0, 360, dot.blue, -1)
    ...
```
        
I used the amplitude, or volume gap, to make the ellipses show at different volumes, giving them a ripple effect. This worked well! This allowed me to explore the difference between a complete graphic that appears with the accents of the music, a method that allows for accents to exist alongside lighter notes, expanding the visibility of the music beyond a simple `bass`.

## Drawing!

I used the following code to find all the available colors in Dorothy and experimented with them in my project to achieve the visual effect I was looking for.

```python
colors = [attr for attr in dir(dot) if not callable(getattr(dot, attr)) and not attr.startswith("__")]
for color in colors:
    print(color)
```
Some of the colors didn't show up on my python, and I eventually discovered that in addition to the `blue, green, orange`, there were also `palegoldenrod, steelblue, powderblue`, which combined to produce the visual effect I expected.
I used `-1` to fill effect in the drawing, but I wanted to keep a constant shape to guide the viewer in their exploration. After some repetitive drawing, I got the complete pattern.

<img width="298" alt="play" src="https://git.arts.ac.uk/24009429/STEM2425-AiningXu-Portfolio/assets/1178/3580f478-e1c3-43ca-b968-7e6ef6ba0af1">

## Transformations

Inspired by `week8-transformations.py`, I added a transformation effect to the lotus leaves. Since I didn't want the lotus leaf to zoom across the entire canvas, I turned to Chatgpt for help in finding a more friendly transformation for ellipse.

I change the code `scale = np.array([[factor, 0.0], [0.0, factor]])` , which was used to scale the matrix and change the proportions of all elements on the canvas as a whole, to applying `(int(200 * factor), int(100 * factor))` to dynamically adjust the width and height of the ellipse. However, compared to the original way, the new method has more decentralized logic, and I will be modifying this method in the future.

In the meantime, I wanted to control the maximum variation of the ruffles to keep their scaling within cavans, and at the very beginning, I added the following code in an attempt to accomplish this. But then I realized that this code is actually redundant, probably because `factor = (dot.frame % period) / period` has a range of 0 to 1, and `(int(200 * factor), int(100 * factor))` is already able to control the size without the need to put limits on the maximum and minimum values.

```python
max_factor = 2
factor = min(factor + 0.5, max_factor) - 0.5
```

https://git.arts.ac.uk/24009429/STEM2425-AiningXu-Portfolio/assets/1178/6bb579b3-2cd7-4b63-9cb5-f06fc32be53c

Through this exploration, I realized the importance of qualifying values for project completeness, but unnecessary constraints can make code redundant.

## Col and Row

I've also changed the way `seg` is zoned to make the music more tightly influenced by the image via `col, row`.

```python
col = math.floor((dot.mouse_x / dot.width)*3)
row = math.floor((dot.mouse_y / dot.height)*3)
print({col}, {row})
```


https://github.com/user-attachments/assets/e153bf7d-9df2-444b-bd93-f702aabc50c8


I intended to have different music playing in each different area, but tried multiple methods that didn't work, so I continued the interaction with only one music file.

## Conclusions

In addition to the above results, I tried to use `self.remain_visible = False` to control some of the graphics to be invisible after the music starts and reappear after the music ends, but I removed it because the response tends to a little bit lag and affects the interactive experience.

Finally, according to music, the music I found on https://freesound.org had little effect on the ripple state, so I reused the music provided in the classroom to highlight the animation effect.

This project greatly improved my understanding of graphics and amplitude, and I implemented three dynamic changes on a sheet of cavans: graphics moving with amplitude >0.01, graphics moving with different groupings of amplitude, and images moving smoothly under the control of `factor`. After trial and error and removing redundant code, I was deeply aware of the importance of code logic and interaction fluency.





