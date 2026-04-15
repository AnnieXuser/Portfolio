from dorothy import Dorothy
from cv2 import fillPoly, circle, rectangle
import numpy as np

dot = Dorothy(width=600, height=1000)

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.num_flakes = 100
        x = np.linspace(0, dot.width, self.num_flakes).astype(int)
        # random ys stop grouping
        y = np.random.randint(0, dot.height, self.num_flakes)
        self.speed = np.random.randint(1, 5, self.num_flakes)
        self.fish = []
        # iterate through both and combine into the variable pt
        for pt in zip(x,y):
            self.fish.append(list(pt))
        
        ## Random fish color
        self.colors_bg = [[np.random.randint(0, 256) for _ in range(4)] for _ in range(self.num_flakes)]
        self.color_step_bg = [[np.random.randint(1, 4) for _ in range(4)] for _ in range(self.num_flakes)]
        # self.colors_bg = [[np.random.randint(0, 256) for _ in range(3)] for _ in range(self.num_flakes)]
        # self.color_step_bg = [[np.random.randint(1, 3) for _ in range(3)] for _ in range(self.num_flakes)]
        
        # Background color 
        # #interpolate between these colours
        self.color = [0, 0, 0]  
        self.a = dot.lightblue
        self.b = dot.black

        self.pos = [dot.width // 2, dot.height // 2]

    def draw(self):
        # Veritical color change
        #Get y position as fraction of screen 
        t = dot.mouse_y / dot.height
        #Use to interpolate r g and b values
        for i in range(3):
            self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)
        dot.background(self.color)

        # Fish in random colors
        ptr = 0
        for pt in self.fish:
            # Different from circle
            x, y = pt
            speed = self.speed[ptr]

            # Small triangle(fish fin)
            small_triangle_size = speed * 2
            small_triangle_points = np.array([
                [x - small_triangle_size, y + small_triangle_size],
                [x, y],
                [x - small_triangle_size, y]
            ], np.int32)

            # Big triangle(fish body)
            big_triangle_size = speed * 4
            big_triangle_points = np.array([
                [x, y],
                [x, y + big_triangle_size * 2],
                [x + big_triangle_size * 2, y + big_triangle_size]
            ], np.int32)

            fillPoly(dot.canvas, [small_triangle_points], color=tuple(self.colors_bg[ptr]))
            fillPoly(dot.canvas, [big_triangle_points], color=tuple(self.colors_bg[ptr]))

             # Color update
            for i in range(4):
                self.colors_bg[ptr][i] = (self.colors_bg[ptr][i] + self.color_step_bg[ptr][i]) % 256

            ## 0 & 1 means x & y
            self.fish[ptr][0] = (self.fish[ptr][0] + speed) % dot.width
            #self.fish[ptr][1] = (self.fish[ptr][1] + speed) % dot.width
            ptr += 1
            
        # Mouse position
        self.pos[0] = int(self.pos[0] + (dot.mouse_x - self.pos[0]) * 0.05)
        self.pos[1] = int(self.pos[1] + (dot.mouse_y - self.pos[1]) * 0.05)

        # Bubble drawing: depending on relative position
        circle(dot.canvas, self.pos, 75, dot.darkblue, 5)
        circle(dot.canvas, self.pos, 70, dot.steelblue, 10)
        circle(dot.canvas, self.pos, 60, dot.lightblue, 17)
        rectangle(dot.canvas, (self.pos[0] - 50, self.pos[1] - 30), (self.pos[0] -40, self.pos[1] - 20), dot.white, -1)
        rectangle(dot.canvas, (self.pos[0] - 60, self.pos[1] - 20), (self.pos[0] -50, self.pos[1] - 10), dot.white, -1)
        rectangle(dot.canvas, (self.pos[0] - 60, self.pos[1] - 10), (self.pos[0] -50, self.pos[1] - 0), dot.white, -1)
        rectangle(dot.canvas, (self.pos[0] - 50, self.pos[1] - 0), (self.pos[0] -40, self.pos[1] + 10), dot.white, -1)
        rectangle(dot.canvas, (self.pos[0] + 50, self.pos[1] + 20), (self.pos[0] +40, self.pos[1] +10), dot.white, -1)

MySketch()
