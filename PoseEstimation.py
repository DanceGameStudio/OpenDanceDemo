import mediapipe as mp
import cv2

def start_camera_detection():
    media_pose = mp.solutions.pose
    media_draw = mp.solutions.drawing_utils
    pose = media_pose.Pose()
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        print("Failed to open camera")
        exit()

    while True:
        success, image = capture.read()
        if not success:
            print("Image Stream not available")

        image = cv2.flip(image, 1)  # Horizontalflip
        results = pose.process(image)

        if results.pose_landmarks:
            media_draw.draw_landmarks(image, results.pose_landmarks, media_pose.POSE_CONNECTIONS)

        cv2.imshow('Camera', image)
        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()