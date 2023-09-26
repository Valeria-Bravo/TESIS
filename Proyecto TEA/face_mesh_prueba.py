import face_mesh
import cv2
face_mesh = face_mesh.FaceMesh(device="cpu")
frame = cv2.imread('C:/Users/ValeriaBravo/Pictures/Camera Roll/rostro.jpg')
face_landmarks = face_mesh.process(frame)
# Distancia entre los ojos
eye_distance = face_landmarks.landmarks[1].x - face_landmarks.landmarks[5].x

# Distancia entre las comisuras de la boca
mouth_width = face_landmarks.landmarks[48].x - face_landmarks.landmarks[54].x

# Elevación de las mejillas
cheek_lift = face_landmarks.landmarks[17].y - face_landmarks.landmarks[21].y

# Elevación de las cejas
eyebrow_lift = face_landmarks.landmarks[22].y - face_landmarks.landmarks[26].y

# Ancho de los ojos
eye_width = face_landmarks.landmarks[36].x - face_landmarks.landmarks[41].x

# Elevación de la mandíbula
jaw_lift = face_landmarks.landmarks[8].y - face_landmarks.landmarks[12].y
if eye_distance > 0.05 and mouth_width > 0.05 and cheek_lift > 0.05:
    expression = "feliz"
elif eye_distance < 0.05 and mouth_width < 0.05 and cheek_lift < 0.05:
    expression = "triste"
elif eyebrow_lift > 0.05 and eye_width > 0.05 and jaw_lift > 0.05:
    expression = "asustado"
elif eyebrow_lift > 0.05 and mouth_width < 0.05 and jaw_lift > 0.05:
    expression = "enojado"
