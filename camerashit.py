import cv2
from logger import log_action

IMAGE_PATH = "static/image.jpg"

def capture():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port) 

    # Check if the camera opened successfully
    if not cam.isOpened():
        print("Error: Could not access the camera")
        return

    # Capture a frame
    result, image = cam.read() 

    if result:
        cv2.imwrite(IMAGE_PATH, image) 
        log_action("Saved plant photo.")
    else:
        print("No image detected. Please try again.")
        log_action("Error saving plant photo.")
    # Release the camera
    cam.release()

# Run the function
#capture()
