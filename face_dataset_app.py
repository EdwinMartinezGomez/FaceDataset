"""
Face Dataset Application
Captures 12 photos of a person's face with labels to create a dataset.
One front-facing photo is mandatory.
"""

import cv2
import os
import sys
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk


class FaceDatasetApp:
    def __init__(self):
        self.name = None
        self.dataset_path = "dataset"
        self.total_photos = 12
        self.photos_taken = 0
        self.front_face_captured = False
        
        # Load face cascade classifier for front face detection
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
    def get_name(self):
        """Get the person's name from user input"""
        while True:
            name = input("Ingrese el nombre de la persona: ").strip()
            if name:
                self.name = name
                print(f"\nNombre registrado: {self.name}")
                print(f"Se tomarán {self.total_photos} fotos, incluyendo 1 foto frontal obligatoria.")
                return True
            else:
                print("Por favor ingrese un nombre válido.")
    
    def create_person_directory(self):
        """Create directory for storing person's photos"""
        person_path = os.path.join(self.dataset_path, self.name)
        os.makedirs(person_path, exist_ok=True)
        return person_path
    
    def detect_front_face(self, frame):
        """Detect if there's a front-facing face in the frame"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(100, 100)
        )
        return len(faces) > 0, faces
    
    def capture_photos(self):
        """Main photo capture loop"""
        # Initialize camera
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: No se pudo abrir la cámara.")
            return False
        
        person_path = self.create_person_directory()
        print(f"\nDirectorio creado: {person_path}")
        print("\nInstrucciones:")
        print("- Presione ESPACIO para tomar una foto")
        print("- Presione ESC para cancelar")
        print("- Se requiere al menos una foto frontal clara")
        
        while self.photos_taken < self.total_photos:
            ret, frame = cap.read()
            if not ret:
                print("Error al capturar el frame.")
                break
            
            # Detect front face
            has_front_face, faces = self.detect_front_face(frame)
            
            # Draw rectangles around detected faces
            display_frame = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Display status information
            status_text = f"Fotos: {self.photos_taken}/{self.total_photos}"
            cv2.putText(display_frame, status_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            if not self.front_face_captured:
                if has_front_face:
                    cv2.putText(display_frame, "ROSTRO FRONTAL DETECTADO - Presione ESPACIO", 
                              (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    cv2.putText(display_frame, "Busque una posicion frontal", 
                              (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                cv2.putText(display_frame, "Puede tomar fotos desde cualquier angulo", 
                          (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # Try to use OpenCV window; if it fails (no GUI support), fall back to Tkinter
            try:
                cv2.imshow('Face Dataset - Captura de Fotos', display_frame)
                key = cv2.waitKey(1) & 0xFF
            except cv2.error:
                # release OpenCV windows and delegate to tkinter-based UI
                cv2.destroyAllWindows()
                cap.release()
                return self._run_tkinter_capture(person_path)
            
            # ESC to cancel
            if key == 27:
                print("\nCaptura cancelada por el usuario.")
                cap.release()
                cv2.destroyAllWindows()
                return False
            
            # SPACE to capture
            elif key == 32:
                # Check if front face is required
                if not self.front_face_captured and not has_front_face:
                    print("¡Atención! Debe capturar primero una foto frontal clara.")
                    continue
                
                # Save photo
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                photo_type = "frontal" if (not self.front_face_captured and has_front_face) else "pose"
                filename = f"{self.name}_{photo_type}_{self.photos_taken + 1}_{timestamp}.jpg"
                filepath = os.path.join(person_path, filename)
                
                cv2.imwrite(filepath, frame)
                self.photos_taken += 1
                
                if not self.front_face_captured and has_front_face:
                    self.front_face_captured = True
                    print(f"✓ Foto frontal capturada: {filename}")
                else:
                    print(f"✓ Foto {self.photos_taken} capturada: {filename}")
        
        cap.release()
        cv2.destroyAllWindows()
        
        print(f"\n¡Completado! Se capturaron {self.photos_taken} fotos para {self.name}")
        print(f"Dataset guardado en: {person_path}")
        return True

    def _run_tkinter_capture(self, person_path):
        """Fallback GUI using Tkinter + Pillow to show frames and capture photos.
        This is used when OpenCV has no GUI support (common on headless builds).
        """
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: No se pudo abrir la cámara (Tkinter fallback).")
            return False

        root = tk.Tk()
        root.title("Face Dataset - Captura de Fotos")

        # State shared between callbacks
        state = {
            'frame': None,
            'has_front': False,
            'running': True,
        }

        # UI elements
        img_label = tk.Label(root)
        img_label.pack()

        status_var = tk.StringVar()
        status_label = tk.Label(root, textvariable=status_var, font=("Arial", 12))
        status_label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=8)

        def save_photo(event=None):
            # Use most recent frame
            frame = state['frame']
            if frame is None:
                return
            if not state['has_front'] and not self.front_face_captured:
                print("¡Atención! Debe capturar primero una foto frontal clara.")
                return

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            photo_type = "frontal" if (not self.front_face_captured and state['has_front']) else "pose"
            filename = f"{self.name}_{photo_type}_{self.photos_taken + 1}_{timestamp}.jpg"
            filepath = os.path.join(person_path, filename)
            cv2.imwrite(filepath, frame)
            self.photos_taken += 1
            if not self.front_face_captured and state['has_front']:
                self.front_face_captured = True
                print(f"✓ Foto frontal capturada: {filename}")
            else:
                print(f"✓ Foto {self.photos_taken} capturada: {filename}")

            if self.photos_taken >= self.total_photos:
                stop_capture()

        def cancel(event=None):
            print("\nCaptura cancelada por el usuario.")
            stop_capture()

        def stop_capture():
            state['running'] = False
            try:
                cap.release()
            except Exception:
                pass
            try:
                root.quit()
            except Exception:
                pass

        capture_btn = tk.Button(btn_frame, text="Capturar (Espacio)", command=save_photo)
        capture_btn.pack(side=tk.LEFT, padx=6)
        cancel_btn = tk.Button(btn_frame, text="Cancelar (Esc)", command=cancel)
        cancel_btn.pack(side=tk.LEFT, padx=6)

        # Bind keys
        root.bind('<space>', save_photo)
        root.bind('<Escape>', cancel)

        def update_frame():
            if not state['running']:
                return
            ret, frame = cap.read()
            if not ret:
                status_var.set("Error al capturar el frame.")
                root.after(100, update_frame)
                return

            # Detect front face
            has_front_face, faces = self.detect_front_face(frame)
            state['has_front'] = has_front_face
            state['frame'] = frame.copy()

            display_frame = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            status_text = f"Fotos: {self.photos_taken}/{self.total_photos}"
            cv2.putText(display_frame, status_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if not self.front_face_captured:
                if has_front_face:
                    cv2.putText(display_frame, "ROSTRO FRONTAL DETECTADO - Presione ESPACIO", 
                              (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    cv2.putText(display_frame, "Busque una posicion frontal", 
                              (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                cv2.putText(display_frame, "Puede tomar fotos desde cualquier angulo", 
                          (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # Convert BGR to RGB then to PIL Image
            rgb = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            img_label.imgtk = imgtk
            img_label.configure(image=imgtk)

            # Update status label
            if not self.front_face_captured and has_front_face:
                status_var.set("ROSTRO FRONTAL DETECTADO - Presione ESPACIO")
            elif not self.front_face_captured:
                status_var.set("Busque una posicion frontal")
            else:
                status_var.set("Puede tomar fotos desde cualquier angulo")

            # Schedule next frame
            root.after(15, update_frame)

        # Start updating frames
        root.after(0, update_frame)
        root.mainloop()

        # When GUI closed, ensure resources released
        try:
            cap.release()
        except Exception:
            pass

        if self.photos_taken >= self.total_photos:
            print(f"\n¡Completado! Se capturaron {self.photos_taken} fotos para {self.name}")
            print(f"Dataset guardado en: {person_path}")
            return True
        else:
            return False
    
    def run(self):
        """Main application entry point"""
        print("=" * 60)
        print("APLICACIÓN DE DATASET DE ROSTROS")
        print("=" * 60)
        
        if not self.get_name():
            return
        
        if self.capture_photos():
            print("\n¡Dataset creado exitosamente!")
        else:
            print("\nLa creación del dataset fue cancelada o falló.")


def main():
    app = FaceDatasetApp()
    app.run()


if __name__ == "__main__":
    main()
