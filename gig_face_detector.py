import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 7)

    cv2.imshow("Face Detection", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == ord('s'):
        cv2.imwrite("detected_face.jpg", frame)
        print("Frame saved as 'detected_face.jpg'")
    elif key == 29:
        print("Exiting...")
        break

video_capture.release()
cv2.destroyAllWindows()
