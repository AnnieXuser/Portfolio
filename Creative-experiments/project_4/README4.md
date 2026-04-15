# Project 4: Naughty Eyes (Face Filter, Hand Moving)

For my final project I wanted to explore face recognition and gesture recognition. During the exploration of these experiments, I associated `wearable virtual devices` that may be relevant to this aspect of the technology. In the future, I hope to combine modeling and face recognition technologies. But for this project, I decided to focus on the interesting combination of face filtering, gesture tracking and mouse tracking.

## Give me Five 🖐️

I wanted to create a finger spreading gesture that would be used to control subsequent patterns.

My first step was to understand what MediaPipe Hands' hand keypoints are and what parts of the hand they represent. I learned that there are 21 MediaPipe Hands keypoints, numbered from 0 to 20, and they are numbered logically as follows:

```python
"Wrist": [0],
"Thumb": [1, 2, 3, 4],
"Index Finger": [5, 6, 7, 8],
"Middle Finger": [9, 10, 11, 12],
"Ring Finger": [13, 14, 15, 16],
"Pinky Finger": [17, 18, 19, 20]
```

And to implement a machine to recognize the gesture of an open palm, I chose to compare the coordinates of the tip and the base of the hand: if the y-coordinate of the tip is smaller than the y-coordinate of the base (smaller y-coordinate means more leaning up), it means that the fingers are straight.

```python
is_open_hand = all(
    hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_bases[i]].y
    for i in range(1, 5)
)  # Exclude thumb
```

The reason I ignore thumb movements here is because the movements and structure of the thumb are different from the other four fingers. In particular, the position and direction of movement of the thumb is significantly different from the other fingers. This is evidenced by the fact that `number 1` is the metacarpophalangeal joint (CMC Joint) of the thumb, which connects the thumb to the palm of the hand, and by the fact that the thumb, when straightened, is usually oriented laterally, which cannot be determined by simple vertical comparisons.

There is ALMOST no difference between (1, 5) and (0, 5).

## Troubleshooting and Fix it

It was a challenge to keep the pupil from going beyond the white part of the eye, and at the beginning, I only applied the following code, which made a ridiculous `error`:

```python
def pupil_position(mouse_x, mouse_y, eye_center, eye_width, eye_height):
    dx = mouse_x - eye_center[0]
    dy = mouse_y - eye_center[1]
    return (int(eye_center[0] + dx), int(eye_center[1] + dy))
```

I realized that the range of movement of the pupil needed to be corrected. After checking google and asking Chatgpt, I found that using the math of `elliptic equations` could be a good way to improve this.

<img width="416" height="136" alt="c74157b6-933f-4acb-b6d9-c5ed3d0ad155" src="https://github.com/user-attachments/assets/a179229f-df48-41f5-892f-83f6c7548f3a" />

a is the horizontal radius of the `ellipse (eye_width)`,b is the vertical radius of the `ellipse (eye_height)`. When this `value > 1`, the mouse position is outside the ellipse. Otherwise, the pupil position is inside the ellipse.

The angle of the mouse relative to the center of the eye is calculated with `np.arctan2(dy, dx)`, which represents the direction from the center of the eye to the mouse position.

The coordinates of the points on the ellipse boundary at this angle are:

<img width="338" height="148" alt="9abfb2af-bb08-474c-befb-234a905c801a" src="https://github.com/user-attachments/assets/8a040733-906f-4829-8d5a-2245d559c8ef" />

This restricts the pupil to the boundaries of the ellipse, ensuring that the pupil position is constrained to the ellipse of the eye.


## Experimentation and Abandonment

I also experimented with how `camera_feed = cv2.flip(camera_feed, 1)` would affect the video.

This code controls the video mirroring effect. However, because I added mouse tracking, the pupil and the mouse are moving in completely opposite paths after the video is mirrored. To fix this, I tried reversing the pupil tracking by switching the x and y readings `dx = mouse_x - eye_center[1]` and `dy = mouse_y - eye_center[0]`, but this didn't work and the pupil became untrackable, so I eventually abandoned the code.

The final example of the video looks like this:




https://github.com/user-attachments/assets/9ebe39b4-c134-4c65-9f87-12f5b622836c




## Conclusion

Through this project, I gained a deeper understanding of the complexity of integrating different tracking technologies (such as facial filtering, gesture recognition, and mouse tracking) into a seamless user experience, and I was pleasantly surprised by the mathematical principles of combining code and images to enhance the accuracy and realism of virtual effects.

This experiment made me realize that when designing image processing and interaction, the interaction between various functional modules should be more fully considered, and more precise control and coordination is needed to avoid a simple operation leading to the failure of the whole function.

