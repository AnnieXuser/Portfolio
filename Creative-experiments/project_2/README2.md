# Project 2: Bubble (Mouse, Transformation, Color, Scale)

In this project I wanted to further explore dynamic graphics with random colors. I liked the visuals presented in the WEEK 3 classroom `week3-final-snow.py` and based on that I started my project.


## Random Color

In the original example, the color of the snowflake was a fixed white. I turned to Chatgpt and learned how to generate random colors and color change steps.

```python
self.colors_bg = [[np.random.randint(0, 256) for _ in range(4)] for _ in range(self.num_flakes)]
```

I was interested in the numbers in `randint()`, and after trying some random numbers I realized that This interval controls the brightness of the color. If the range is too small, the color is not vibrant enough.

Also, after finishing all the codes I found some new thing about this same code. The second number in `range()` can only be 4 at the maximum - correlates with the color change of the triangles behind:

Correlates with the color change of the triangles behind:

```python
fillPoly(dot.canvas, [small_triangle_points], color=tuple(self.colors_bg[ptr]))
fillPoly(dot.canvas, [big_triangle_points], color=tuple(self.colors_bg[ptr]))
```

That's because most of the plotting functions in OpenCV require that the color parameter be a tuple or list of lengths 3 or 4, depending on the type of image channel being used:

Length 3: represents RGB or BGR colors (no transparency).
Length 4: RGBA or BGRA colors (with transparency).

When passing in a color parameter longer than 4, such as [R, G, B, A, ExtraValue]. This will cause the function to not recognize it.

In my project, it is not obvious whether the number is 3 or 4.



## Change Shapes

I've replaced the shape of the snowflake with a triangle whose size can be adjusted based on speed. Specifically, `speed = self.speed[ptr]` gets the current speed value of the small triangle, which is used to control the movement of the triangle. And `small_triangle_size = speed * 2` calculates the size of the fins based on the speed value, which is proportional to the speed, thus reflecting the effect of speed on the appearance of the fish. As you can see, the value of `small_triangle_size` depends on `speed`, which comes from the `self.speed` list.

```python
small_triangle_size = speed * 2
big_triangle_size = speed * 4
```

I learned how to draw `triangle` with the `draw()` function from Chatgpt. To better control the composition of the triangles, I created a Numpy array and forced its data type to int32, making sure that the coordinates of each point (i.e. [x, y]) are 32-bit integers. This approach allowed me to write triangles of two different sizes.

<img width="124" alt="fish2parts" src="https://git.arts.ac.uk/24009429/STEM2425-AiningXu-Portfolio/assets/1178/103fea95-4d16-4b12-8962-5457d49b82ec">

## Troubleshooting

After completing everything above, I got the following canvas:

https://git.arts.ac.uk/24009429/STEM2425-AiningXu-Portfolio/assets/1178/317660c0-9a48-4991-8b9f-1c707a51abd4

During my review, I realized an important detail: the relative position of the fish should change with movement. This issue prompted me to revisit the code and eventually found a potential error.

Upon troubleshooting, I realized that I had incorrectly confused the fish's vertical position (y) with its horizontal position (x). Specifically, the wrong code was:

```python
self.fish[ptr][1] = (self.fish[ptr][1] + speed) % dot.width
```

The right thing to do is:

```python
self.fish[ptr][0] = (self.fish[ptr][0] + speed) % dot.width
```

Here, the fish move laterally and only the x-axis changes, the y-axis stays the same, with 0 representing the reading position x, while 1 represents the reading position y.


## Add More Colors

Inspired by relative position, the fish would twinkle if the colors also changed relative to each other, regenerating new colors with each movement. So I added the following code. In this way `elf.color_step_bg` and `self.colors_bg` combine to determine the dynamics of the color over time.

```python
self.color_step_bg = [[np.random.randint(1, 4) for _ in range(4)] for _ in range(self.num_flakes)]
for i in range(4):
    self.colors_bg[ptr][i] = (self.colors_bg[ptr][i] + self.color_step_bg[ptr][i]) % 256
```

Finally, I combined the mouse pattern with the color change in the background to complete the final piece. Since I had a good grasp of the relationship between color and relative position at the beginning of the project, I had no problems with these two features.

https://git.arts.ac.uk/24009429/STEM2425-AiningXu-Portfolio/assets/1178/3044a81b-568f-4d37-9d90-f62c0e3ce71a

## Conclusion

This project deepened my understanding of random generation and relative position of [RGB] colors. There are many ways to transform just by changing the direction of the change, such as directly modifying x or y, or changing 0 or 1 to change the way the position is read.

It's like the butterfly effect, sometimes just changing a single parameter can lead to a cascade of unexpected results. This has made me pay more attention to how the details affect the overall system. This phenomenon is not only visible in programming, but similar examples can be found in many fields, whether it's creating art or making decisions in life, where every small change can have a profound effect.
