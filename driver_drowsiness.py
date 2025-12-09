import cv2
import dlib
import numpy as np
import winsound  # For alarm sound on Windows
from scipy.spatial import distance as dist
import time

# Initialize dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/Grancy/Desktop/shape_predictor_68_face_landmarks.dat/shape_predictor_68_face_landmarks.dat")

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    alarm_on = False
    closed_eye_frames = 0  # To count how many frames eyes are closed
    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Get frame rate of the camera
    required_frames = int(frame_rate * 2)  

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = detector(gray)

        for face in faces:
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

            # Get facial landmarks
            landmarks = predictor(gray, face)

            # Extract left and right eye landmarks
            left_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)])
            right_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)])

            # Compute EAR
            left_EAR = eye_aspect_ratio(left_eye)
            right_EAR = eye_aspect_ratio(right_eye)
            avg_EAR = (left_EAR + right_EAR) / 2.0

            # Drowsiness detection threshold
            status = "Awake"
            color = (0, 255, 0)  # Green (awake)

            if avg_EAR < 0.25:
                closed_eye_frames += 1
                if closed_eye_frames >= required_frames:
                    status = "Drowsy"
                    color = (0, 0, 255)  # Red (drowsy)
                    if not alarm_on:
                        winsound.Beep(1000, 2000)  # Sound alarm for 2 seconds
                        alarm_on = True
            else:
                closed_eye_frames = 0  # Reset counter if eyes are open
                alarm_on = False  # Reset alarm state

            # Display status
            cv2.putText(frame, f"Status: {status}", (face.left(), face.top() - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Display the frame
        cv2.imshow("Drowsiness Detection", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
