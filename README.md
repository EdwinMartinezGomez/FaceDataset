# FaceDataset

Aplicación para crear un dataset de rostros con etiquetas mediante captura de fotos con cámara web.

## Descripción

Esta aplicación permite capturar 12 fotos de rostros con etiquetas personalizadas. Al inicio se solicita el nombre de la persona y luego se capturan las fotos, incluyendo una foto frontal obligatoria. Las imágenes se organizan automáticamente en carpetas con el nombre de la persona.

## Características

- ✅ Solicita nombre al inicio para etiquetar las fotos
- ✅ Captura 12 fotos por persona
- ✅ Foto frontal obligatoria (detectada automáticamente)
- ✅ Detección de rostros en tiempo real
- ✅ Organización automática en carpetas por persona
- ✅ Nombres de archivo descriptivos con timestamp

## Requisitos

- Python 3.7 o superior
- Cámara web
- OpenCV

## Instalación

1. Clone el repositorio:
```bash
git clone https://github.com/EdwinMartinezGomez/FaceDataset.git
cd FaceDataset
```

2. Instale las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecute la aplicación:
```bash
python face_dataset_app.py
```

2. Ingrese el nombre de la persona cuando se le solicite

3. Use las siguientes teclas durante la captura:
   - **ESPACIO**: Tomar una foto
   - **ESC**: Cancelar y salir

4. Instrucciones durante la captura:
   - La primera foto debe ser frontal (el sistema detectará cuando su rostro esté de frente)
   - Después de la foto frontal, puede tomar fotos desde diferentes ángulos
   - El contador mostrará el progreso (ej: "Fotos: 5/12")

## Estructura del Dataset

Las fotos se guardan en la carpeta `dataset/` con la siguiente estructura:

```
dataset/
└── [Nombre_Persona]/
    ├── [Nombre]_frontal_1_[timestamp].jpg
    ├── [Nombre]_pose_2_[timestamp].jpg
    ├── [Nombre]_pose_3_[timestamp].jpg
    └── ...
```

## Ejemplo de Uso

```
$ python face_dataset_app.py

============================================================
APLICACIÓN DE DATASET DE ROSTROS
============================================================
Ingrese el nombre de la persona: Juan_Perez

Nombre registrado: Juan_Perez
Se tomarán 12 fotos, incluyendo 1 foto frontal obligatoria.

Directorio creado: dataset/Juan_Perez

Instrucciones:
- Presione ESPACIO para tomar una foto
- Presione ESC para cancelar
- Se requiere al menos una foto frontal clara

✓ Foto frontal capturada: Juan_Perez_frontal_1_20231112_143025_123456.jpg
✓ Foto 2 capturada: Juan_Perez_pose_2_20231112_143030_234567.jpg
...
✓ Foto 12 capturada: Juan_Perez_pose_12_20231112_143145_345678.jpg

¡Completado! Se capturaron 12 fotos para Juan_Perez
Dataset guardado en: dataset/Juan_Perez

¡Dataset creado exitosamente!
```

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación
- **OpenCV**: Procesamiento de imágenes y captura de video
- **NumPy**: Operaciones numéricas

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.