import cv2
import PoseEstimation

if __name__ == '__main__':
    capture = cv2.VideoCapture('Videos/Beispiel_02.mp4')
    #capture = cv2.VideoCapture(0) # Cam
    pose_detector = PoseEstimation.PoseDetector(capture)
    flip = False

    while True:
        pose_detector.detect_pose()
        pose_detector.draw_landmarks()
        output = pose_detector.image

        # Show Image
        if output is not None:
            if flip:
                output = cv2.flip(output, 1)  # Horizontalflip
            cv2.imshow('PoseDetector', output)
        if cv2.waitKey(1) == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            break
