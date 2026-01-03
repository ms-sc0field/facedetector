# Programming:

import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
video_capture = cv2.VideoCapture(r'peoples2.mp4')

prev_frame_time = time.time()
new_frame_time = 0

while video_capture.isOpened():
        ret, frame = video_capture.read()
        
        if not ret:
                print('Finished processing or cann et read the video')
                break

        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 10) 
        for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
                cv2.putText(frame, 'Face', (x + 75, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9 ,(255, 255, 255), 2)

        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)

        prev_frame_time = new_frame_time

        fps = int(fps)
        fps_text = f'FPS: {fps}'

        cv2.putText(frame, fps_text, (frame.shape[1] - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow('Wind0w', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

video_capture.release()
