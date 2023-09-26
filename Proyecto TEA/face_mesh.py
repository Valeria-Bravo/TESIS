import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Error al abrir la cámara")
            break

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_TESSELATION,
                    mp_drawing.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1)
                )
                
                # Medidas proporcionadas
                eye_distance = face_landmarks.landmark[2].x - face_landmarks.landmark[5].x
                mouth_width = face_landmarks.landmark[30].x - face_landmarks.landmark[54].x
                cheek_lift = face_landmarks.landmark[17].y - face_landmarks.landmark[21].y
                eyebrow_lift = face_landmarks.landmark[22].y - face_landmarks.landmark[26].y
                eye_width = face_landmarks.landmark[36].x - face_landmarks.landmark[41].x
                jaw_lift = face_landmarks.landmark[8].y - face_landmarks.landmark[12].y

                # Detectar expresiones
                if eye_distance > 0.03 and mouth_width > 0.03:
                    expression = "Feliz"
                elif mouth_width < 0.03:
                    expression = "Triste"
                elif cheek_lift > 0.03 and eyebrow_lift > 0.03:
                    expression = "Asustado"
                else:
                    expression = "Molesto"

                # Mostrar expresión detectada
                cv2.putText(image, expression, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Face Mesh', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

