import mediapipe as mp
import numpy as np
import cv2

class PoseDetector:
    def __init__(self, capture):
        self.capture = capture
        self.media_pose = mp.solutions.pose
        self.media_draw = mp.solutions.drawing_utils
        self.image = np.zeros((1280, 720, 3), np.uint8)
        self.pose = self.media_pose.Pose()
        self.results = self.pose.process(self.image)

    def detect_pose(self):
        success, self.image = self.capture.read()
        if not success:
            print("Image Stream not available")
            return
        self.image = cv2.flip(self.image, 1)  # Horizontalflip
        self.results = self.pose.process(self.image)

    def draw_landmarks(self):
        if self.results.pose_landmarks:
            self.media_draw.draw_landmarks(self.image, self.results.pose_landmarks, self.media_pose.POSE_CONNECTIONS)