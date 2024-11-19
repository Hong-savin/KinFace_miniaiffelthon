import cv2
import numpy as np

def preprocess_images(uploaded_files):
    processed_images = {}
    for role, file in uploaded_files.items():
        if file:
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
            processed_images[role] = preprocess_image(image)
    return processed_images

def preprocess_image(image, target_size=(224, 224), margin=0.1):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        raise ValueError("No face detected in the image.")

    x, y, w, h = faces[0]
    margin_w, margin_h = int(w * margin), int(h * margin)
    x_start, y_start = max(0, x - margin_w), max(0, y - margin_h)
    x_end, y_end = min(image.shape[1], x + w + margin_w), min(image.shape[0], y + h + margin_h)
    cropped = image[y_start:y_end, x_start:x_end]
    resized = cv2.resize(cropped, target_size)
    return cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
