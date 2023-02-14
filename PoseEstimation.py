import mediapipe as mp
import numpy as np
import cv2


class PoseDetector:
    def __init__(self, capture):
        self.capture = capture
        self.media_pose = mp.solutions.pose
        self.media_draw = mp.solutions.drawing_utils
        self.image = np.zeros((1280, 720, 3), np.uint8)
        self.pose = self.media_pose.Pose(static_image_mode=False,
                                         model_complexity=1,
                                         smooth_landmarks=True,
                                         enable_segmentation=True,
                                         min_tracking_confidence=0.5,
                                         min_detection_confidence=0.5)
        self.results = None
        self.segmentation_mask = None

    def detect_pose(self):
        success, self.image = self.capture.read()
        if not success:
            print("Image Stream not available")
            return
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(image)
        self.segmentation_mask = self.results.segmentation_mask

    def draw_landmarks(self):
        if self.results.pose_landmarks and self.image is not None:
            self.media_draw.draw_landmarks(self.image,
                                           self.results.pose_landmarks,
                                           self.media_pose.POSE_CONNECTIONS)
