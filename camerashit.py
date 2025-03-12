import cv2

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
    else:
        print("No image detected. Please try again.")

    # Release the camera
    cam.release()

# Run the function
#capture()
