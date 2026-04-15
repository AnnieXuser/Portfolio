from dorothy import Dorothy
from cv2 import rectangle, ellipse
import math

dot = Dorothy(width=600, height=900)

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")
        dot.music.start_file_stream("project_1/soul.wav")
        dot.music.pause()

    def draw(self):
        dot.background(dot.powderblue)
        amplitude = dot.music.amplitude()

        # Animation of golden fish
        if dot.music.amplitude() > 0.01:
            # Top
            rectangle(dot.canvas, (90, 160), (120, 180), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (110, 150), (140, 170), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (120, 130), (130, 150), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (100, 150), (110, 180), dot.orange, -1)
            rectangle(dot.canvas, (110, 140), (120, 150), dot.orange, -1)
            rectangle(dot.canvas, (120, 150), (130, 170), dot.orange, -1)
            rectangle(dot.canvas, (130, 130), (140, 150), dot.orange, -1)
            rectangle(dot.canvas, (140, 150), (150, 170), dot.orange, -1)
            
            # Bottom
            rectangle(dot.canvas, (120, 240), (140, 270), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (140, 240), (150, 260), dot.orange, -1)
            rectangle(dot.canvas, (130, 260), (140, 270), dot.orange, -1)
            rectangle(dot.canvas, (120, 270), (130, 280), dot.orange, -1)

        # Seperate the canvas into 9 parts, and show which area
        col = math.floor((dot.mouse_x / dot.width)*3)
        row = math.floor((dot.mouse_y / dot.height)*3)
        print({col}, {row})

        # Animation of Ripple_1
        if col == 0 and row == 1:
            if amplitude > 0.01 and amplitude <= 0.02:
                ellipse(dot.canvas, (150, 520), (50, 10), 0, 0, 360, dot.darkblue, -1)
            elif amplitude > 0.02 and amplitude <= 0.03:
                ellipse(dot.canvas, (150, 520), (70, 16), 0, 0, 360, dot.blue, -1)
            elif amplitude > 0.03 and amplitude <= 0.04:
                ellipse(dot.canvas, (150, 520), (90, 23), 0, 0, 360, dot.steelblue, -1)
            elif amplitude > 0.04 and amplitude <= 0.05:
                ellipse(dot.canvas, (150, 520), (135, 30), 0, 0, 360, dot.royalblue, -1)
        else:
            self.remain_visible = True
            
        # Animation of Ripple_2
        if col == 2 and row == 0:
            if amplitude > 0.01 and amplitude <= 0.02:
                ellipse(dot.canvas, (450, 150), (40, 5), 0, 0, 360, dot.blue, -1)
            elif amplitude > 0.02 and amplitude <= 0.03:
                ellipse(dot.canvas, (450, 150), (60, 10), 0, 0, 360, dot.royalblue, -1)
            elif amplitude > 0.03 and amplitude <= 0.04:
                ellipse(dot.canvas, (450, 150), (80, 15), 0, 0, 360, dot.steelblue, -1)
            elif amplitude > 0.04:
                ellipse(dot.canvas, (450, 150), (100, 20), 0, 0, 360, dot.darkblue, -1)
        else:
            self.remain_visible = True

        # Animation of Ripple_3
        if col == 1 and row == 2:
            if amplitude > 0.01 and amplitude <= 0.02:
                ellipse(dot.canvas, (380, 750), (50, 15), 0, 0, 360, dot.royalblue, -1)
            elif amplitude > 0.02 and amplitude <= 0.03:
                ellipse(dot.canvas, (380, 750), (100, 30), 0, 0, 360, dot.blue, -1)
            elif amplitude > 0.03 and amplitude <= 0.04:
                ellipse(dot.canvas, (380, 750), (150, 40), 0, 0, 360, dot.steelblue, -1)
            elif amplitude > 0.04:
                ellipse(dot.canvas, (380, 750), (180, 50), 0, 0, 360, dot.darkblue, -1)
        else:
            self.remain_visible = True

        if self.remain_visible:
            # Drawings which are visible all the time
            # Ripple_1
            ellipse(dot.canvas, (150, 520), (50, 10), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (150, 520), (70, 16), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (150, 520), (90, 23), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (150, 520), (135, 30), 0, 0, 360, dot.royalblue, 2)
            # Ripple_2
            ellipse(dot.canvas, (450, 150), (40, 5), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (450, 150), (60, 10), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (450, 150), (80, 15), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (450, 150), (100, 20), 0, 0, 360, dot.royalblue, 2)
            # Ripple_3
            ellipse(dot.canvas, (380, 750), (50, 15), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (380, 750), (100, 30), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (380, 750), (140, 40), 0, 0, 360, dot.royalblue, 2)
            ellipse(dot.canvas, (380, 750), (180, 50), 0, 0, 360, dot.royalblue, 2)
            # Lotus leaf
            ellipse(dot.canvas, (450, 440), (100, 50), 0, 10, 355, dot.darkgreen, -1)
            ellipse(dot.canvas, (450, 440), (5, 2), 0, 0, 360, dot.black, 2)
            ellipse(dot.canvas, (380, 350), (150, 75), 0, 10, 355, dot.green, -1)
            ellipse(dot.canvas, (380, 350), (5, 2), 0, 0, 360, dot.black, 2)

            # Golden fish
            # Body
            rectangle(dot.canvas, (180, 200), (190, 210), dot.black, -1)
            rectangle(dot.canvas, (120, 170), (160, 210), dot.orange, -1)
            rectangle(dot.canvas, (160, 180), (180, 210), dot.orange, -1)
            rectangle(dot.canvas, (100, 180), (120, 210), dot.orange, -1)
            rectangle(dot.canvas, (190, 200), (210, 220), dot.orange, -1)
            rectangle(dot.canvas, (160, 190), (200, 200), dot.orange, -1)
            rectangle(dot.canvas, (120, 210), (150, 220), dot.orange, -1)
            rectangle(dot.canvas, (160, 210), (190, 220), dot.orange, -1)
            rectangle(dot.canvas, (70, 200), (100, 210), dot.orange, -1)
            rectangle(dot.canvas, (60, 190), (100, 200), dot.orange, -1)
            rectangle(dot.canvas, (60, 180), (80, 190), dot.orange, -1)
            rectangle(dot.canvas, (40, 170), (70, 180), dot.orange, -1)
            rectangle(dot.canvas, (30, 160), (60, 170), dot.orange, -1)
            rectangle(dot.canvas, (90, 240), (100, 250), dot.orange, -1)
            rectangle(dot.canvas, (100, 230), (110, 240), dot.orange, -1)
            rectangle(dot.canvas, (170, 220), (200, 230), dot.orange, -1)
            rectangle(dot.canvas, (40, 180), (60, 190), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (50, 190), (60, 200), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (50, 200), (70, 210), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (60, 210), (80, 230), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (80, 210), (90, 220), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (90, 210), (100, 240), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (100, 210), (120, 230), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (120, 220), (170, 230), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (130, 230), (180, 240), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (150, 210), (160, 220), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (60, 230), (70, 240), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (40, 220), (60, 240), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (30, 230), (50, 250), dot.palegoldenrod, -1)
            rectangle(dot.canvas, (20, 250), (30, 260), dot.palegoldenrod, -1)

        # Lotus leaf animation
        new_canvas = dot.get_layer()
        period = 200
        factor = (dot.frame % period) / period
        # max_factor = 2
        # factor = min(factor + 0.5, max_factor) - 0.5

        if (col == 1 and row == 1) or (col == 2 and row == 1):
            ellipse(new_canvas, (450, 440), 
                    (int(200 * factor), int(100 * factor)), 0, 10, 355, dot.darkgreen, -1)
            ellipse(new_canvas, (450, 440), 
                    (5, 2), 0, 0, 360, dot.black, 2)
            
            ellipse(new_canvas, (380, 350), 
                    (int(200 * factor), int(100 * factor)), 0, 10, 355, dot.green, -1)
            ellipse(new_canvas, (380, 350), 
                    (5, 2), 0, 0, 360, dot.black, 2)
            
            dot.draw_layer(new_canvas)
        else:
            dot.music.pause()

        # Play music when mouse in different area
        if col == 2 and row == 0:
            dot.music.resume()
        elif col == 0 and row == 1:
            dot.music.resume() 
        elif col == 1 and row == 2:
            dot.music.resume()
        elif (col == 1 and row == 1) or (col == 2 and row == 1):
            dot.music.resume()
        else:
            dot.music.pause()

MySketch()
