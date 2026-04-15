from dorothy import Dorothy
import cv2
from cv2 import ellipse, circle
import mediapipe as mp
import numpy as np

dot = Dorothy(600, 400)

class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier("project_4/data/haarcascade_frontalface_default.xml")

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            results = self.hands.process(camera_feed)
            # No gesture means no eyes picture
            show_eyes = False

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Check if it is a five
                    finger_tips = [4, 8, 12, 16, 20]  # Thumb, index, middle, ring, little
                    finger_bases = [2, 5, 9, 13, 17]  # Base of each finger
                    is_open_hand = all(
                        hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_bases[i]].y
                        for i in range(1, 5)
                    )  # Exclude thumb
                    if is_open_hand:
                        show_eyes = True
                        break

            # Face detection
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)

            if show_eyes:
                for face_x, face_y, face_w, face_h in faces:
                    # Draw left eye
                    left_eye_center = (face_x + face_w // 4, face_y + face_h // 3)
                    eye_width = face_w // 6
                    eye_height = face_h // 10
                    ellipse(camera_feed, left_eye_center, (eye_width, eye_height), 0, 0, 360, (255, 255, 255), -1)

                    # Draw right eye
                    right_eye_center = (face_x + 3 * face_w // 4, face_y + face_h // 3)
                    ellipse(camera_feed, right_eye_center, (eye_width, eye_height), 0, 0, 360, (255, 255, 255), -1)

                    # Control pupils with mouse
                    def pupil_position(mouse_x, mouse_y, eye_center, eye_width, eye_height):
                        dx = mouse_x - eye_center[0]
                        dy = mouse_y - eye_center[1]
                        # Amendment * Fix it
                        if (dx / eye_width) ** 2 + (dy / eye_height) ** 2 > 1:
                            angle = np.arctan2(dy, dx)
                            dx = eye_width * np.cos(angle)
                            dy = eye_height * np.sin(angle)
                        return (int(eye_center[0] + dx), int(eye_center[1] + dy))

                    # Draw left pupil
                    left_pupil = pupil_position(dot.mouse_x, dot.mouse_y, left_eye_center, eye_width // 2, eye_height // 2)
                    circle(camera_feed, left_pupil, eye_width // 2, (0, 0, 0), -1)

                    # Draw right pupil
                    right_pupil = pupil_position(dot.mouse_x, dot.mouse_y, right_eye_center, eye_width // 2, eye_height // 2)
                    circle(camera_feed, right_pupil, eye_width // 2, (0, 0, 0), -1)

            #camera_feed = cv2.flip(camera_feed, 1)
            dot.canvas = camera_feed

MySketch()
