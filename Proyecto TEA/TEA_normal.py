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

        # Convierte la imagen a blanco y negro para mejorar el rendimiento
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Procesa la imagen y obtén los resultados
        results = face_mesh.process(image_rgb)

        # Dibuja los puntos faciales en la imagen
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_TESSELATION,
                    mp_drawing.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1)
                )

                mouth_landmarks = face_landmarks.landmark[12:20]
                mouth_open = mouth_landmarks[6].y < mouth_landmarks[0].y

                if mouth_open:
                    cv2.putText(image, "Feliz", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(image, "Triste", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Face Mesh', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
