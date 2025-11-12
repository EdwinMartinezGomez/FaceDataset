# FaceDataset

Aplicación para la creación de un dataset de caras/rostros. Permite capturar múltiples fotos de una persona con etiquetas apropiadas para crear un conjunto de datos de entrenamiento.

## Características

- ✅ Solicita el nombre de la persona al inicio
- ✅ Captura 12 fotos en total:
  - 1 foto frontal (mirando directamente a la cámara)
  - 11 fotos adicionales (diferentes ángulos y expresiones)
- ✅ Guarda las fotos con etiquetas descriptivas
- ✅ Organiza automáticamente el dataset en directorios
- ✅ Genera archivo de metadatos con información del dataset

## Requisitos

- Python 3.6 o superior
- Cámara web conectada
- OpenCV (se instala automáticamente)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/EdwinMartinezGomez/FaceDataset.git
cd FaceDataset
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutar la aplicación:
```bash
python create_dataset.py
```

2. Seguir las instrucciones en pantalla:
   - Ingresar el nombre de la persona
   - Presionar ENTER para iniciar la captura
   - Presionar ESPACIO para capturar cada foto
   - Presionar ESC para cancelar (si es necesario)

3. Las fotos se guardarán automáticamente en:
```
dataset/
└── [nombre_persona]/
    ├── [nombre]_front_[timestamp].jpg      # Foto frontal
    ├── [nombre]_photo_02_[timestamp].jpg   # Foto 2
    ├── [nombre]_photo_03_[timestamp].jpg   # Foto 3
    └── ...
    └── dataset_info.txt                    # Información del dataset
```

## Estructura del Proyecto

```
FaceDataset/
├── create_dataset.py      # Aplicación principal
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación
└── dataset/              # Directorio donde se guardan las fotos (se crea automáticamente)
```

## Controles durante la captura

- **ESPACIO**: Capturar foto actual
- **ESC**: Cancelar y salir de la aplicación

## Consejos para mejores resultados

1. **Iluminación**: Asegúrate de tener buena iluminación frontal
2. **Fondo**: Usa un fondo neutro si es posible
3. **Variedad**: Para las 11 fotos adicionales, varía:
   - Ángulos (izquierda, derecha, arriba, abajo)
   - Expresiones (sonrisa, serio, etc.)
   - Distancias (más cerca, más lejos)
4. **Estabilidad**: Mantén la cámara estable al capturar

## Formato de las fotos

- **Resolución**: 640x480 pixels
- **Formato**: JPEG
- **Nomenclatura**: `[nombre]_[etiqueta]_[timestamp].jpg`

## Información técnica

El dataset generado está organizado de manera que puede ser utilizado para:
- Entrenamiento de modelos de reconocimiento facial
- Sistemas de detección de rostros
- Aplicaciones de verificación de identidad
- Proyectos de machine learning con visión por computadora

## Licencia

Este proyecto está bajo la licencia MIT.

## Autor

Edwin Martinez Gomez