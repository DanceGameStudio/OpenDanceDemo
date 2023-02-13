import cv2
import time
def start_camera_capture():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print("Failed to open camera")
        exit()

    while True:
        success, image = capture.read()
        if not success:
            print("Image Stream not available")

        image = cv2.flip(image, 1)  # Horizontalflip
        cv2.imshow('Camera', image)
        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


def play_video(filepath):
    capture = cv2.VideoCapture(filepath)
    previos_time = 0

    while capture.isOpened():
        success, image = capture.read()
        if not success:
            print("Image Stream not available")
            break

        current_time = time.time()
        fps = 1 / (current_time - previos_time)
        previos_time = current_time
        cv2.putText / image, str(int(fps), (70, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow('Video', image)
        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
