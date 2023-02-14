import cv2
import PoseEstimation

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    pose_detector = PoseEstimation.PoseDetector(capture)

    while True:
        pose_detector.detect_pose()
        pose_detector.draw_landmarks()

        # Show Image
        if pose_detector.image is not None:
            cv2.imshow('PoseDetector', pose_detector.image)
        if cv2.waitKey(1) == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            break

