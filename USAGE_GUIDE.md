# Guía de Uso - Face Dataset Creator

## Descripción General

Esta aplicación te permite crear un dataset de fotos faciales de manera sencilla y organizada. Es ideal para proyectos de:
- Reconocimiento facial
- Detección de rostros
- Machine Learning
- Visión por computadora

## ¿Qué hace la aplicación?

1. **Solicita tu nombre**: Al iniciar, te pedirá que ingreses tu nombre
2. **Captura 12 fotos**:
   - Primera foto: Foto frontal (mirando directamente a la cámara)
   - Fotos 2-12: Fotos adicionales desde diferentes ángulos
3. **Guarda automáticamente**: Todas las fotos se guardan con nombres descriptivos
4. **Organiza el dataset**: Crea una estructura de directorios ordenada
5. **Genera metadatos**: Crea un archivo con información del dataset

## Instalación Rápida

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar la aplicación
python create_dataset.py
```

## Flujo de Uso

### 1. Inicio de la Aplicación
```
==================================================
FACE DATASET CREATOR
==================================================
Enter the person's name: Juan Perez
✓ Name set to: Juan_Perez
```

### 2. Preparación
La aplicación creará automáticamente:
- Directorio `dataset/` (si no existe)
- Subdirectorio `dataset/Juan_Perez/`

### 3. Captura de Fotos
Se abrirá una ventana con la vista de tu cámara:

**Primera foto (Frontal)**:
- Mira directamente a la cámara
- Mantén una expresión neutral
- Presiona ESPACIO para capturar

**Fotos 2-12 (Adicionales)**:
- Varía el ángulo de tu rostro
- Prueba diferentes expresiones
- Presiona ESPACIO para cada captura

### 4. Finalización
```
==================================================
DATASET CREATION COMPLETE!
==================================================
Person: Juan_Perez
Photos saved: 12
Location: dataset/Juan_Perez
==================================================
```

## Estructura del Dataset Generado

```
dataset/
└── Juan_Perez/
    ├── Juan_Perez_front_20231112_143022.jpg      # Foto frontal
    ├── Juan_Perez_photo_02_20231112_143035.jpg   # Foto 2
    ├── Juan_Perez_photo_03_20231112_143048.jpg   # Foto 3
    ├── ... (continúa hasta photo_12)
    └── dataset_info.txt                           # Metadatos
```

## Formato de Nombres de Archivo

**Patrón**: `[nombre]_[etiqueta]_[timestamp].jpg`

- **nombre**: Tu nombre con espacios reemplazados por guiones bajos
- **etiqueta**: 
  - `front` para la primera foto
  - `photo_02` a `photo_12` para las demás
- **timestamp**: Fecha y hora en formato `YYYYMMDD_HHMMSS`

## Consejos para Mejores Resultados

### Iluminación
- ✅ Usa luz natural o luz frontal suave
- ✅ Evita sombras fuertes en el rostro
- ❌ No uses luz muy brillante detrás de ti

### Fondo
- ✅ Usa un fondo neutro (pared blanca, gris, etc.)
- ✅ Evita fondos con muchos elementos
- ❌ No uses fondos con patrones complejos

### Variedad en las Fotos
Para las 11 fotos adicionales, prueba:

**Ángulos**:
- Rostro girado a la izquierda (leve y pronunciado)
- Rostro girado a la derecha (leve y pronunciado)
- Cabeza inclinada hacia arriba
- Cabeza inclinada hacia abajo

**Expresiones**:
- Sonriendo
- Serio
- Con anteojos (si usas)
- Sin anteojos

**Distancias**:
- Más cerca de la cámara
- Más lejos de la cámara

## Controles Durante la Captura

| Tecla | Acción |
|-------|--------|
| ESPACIO | Capturar la foto actual |
| ESC | Cancelar y salir de la aplicación |

## Información Técnica

### Especificaciones de las Fotos
- **Resolución**: 640x480 píxeles
- **Formato**: JPEG
- **Calidad**: Estándar OpenCV

### Requisitos del Sistema
- **Sistema Operativo**: Windows, macOS, Linux
- **Python**: 3.6 o superior
- **Cámara**: Webcam integrada o externa
- **Permisos**: Acceso a la cámara debe estar habilitado

### Dependencias
- `opencv-python`: Para captura de video y procesamiento de imágenes

## Archivo de Metadatos

El archivo `dataset_info.txt` contiene:
```
Face Dataset Information
==================================================
Person Name: Juan_Perez
Total Photos: 12
Creation Date: 2023-11-12 14:30:45
Directory: dataset/Juan_Perez

Photo Breakdown:
  - 1 front photo (direct face)
  - 11 additional photos (various angles)
```

## Solución de Problemas

### Error: "Could not open camera"
**Soluciones**:
1. Verifica que tu cámara esté conectada
2. Cierra otras aplicaciones que usen la cámara (Zoom, Skype, etc.)
3. Reinicia tu computadora
4. Verifica los permisos de la cámara en tu sistema operativo

### La aplicación no inicia
**Soluciones**:
1. Verifica que Python esté instalado: `python --version`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Verifica que el archivo `create_dataset.py` exista

### Las fotos se ven oscuras
**Soluciones**:
1. Mejora la iluminación del ambiente
2. Ajusta la posición respecto a fuentes de luz
3. Limpia el lente de tu cámara

### El directorio ya existe
La aplicación te preguntará si deseas continuar. Si aceptas, las nuevas fotos se agregarán al directorio existente.

## Usos del Dataset

Una vez creado tu dataset, puedes usarlo para:

1. **Entrenar modelos de reconocimiento facial**
   - Sistemas de seguridad
   - Control de acceso
   - Identificación automática

2. **Proyectos de Machine Learning**
   - Clasificación de rostros
   - Detección de emociones
   - Verificación de identidad

3. **Investigación y Educación**
   - Proyectos universitarios
   - Pruebas de algoritmos
   - Aprendizaje de visión por computadora

## Privacidad y Seguridad

⚠️ **Importante**: 
- Las fotos se guardan localmente en tu computadora
- No se suben a ningún servidor externo
- Es tu responsabilidad proteger las imágenes capturadas
- El directorio `dataset/` está incluido en `.gitignore` para evitar commits accidentales

## Próximos Pasos

Después de crear tu dataset:

1. **Revisar las fotos**: Abre la carpeta y verifica que todas las fotos sean nítidas
2. **Crear más datasets**: Ejecuta la aplicación múltiples veces para diferentes personas
3. **Usar en tu proyecto**: Integra el dataset en tu aplicación de ML
4. **Ampliar el dataset**: Puedes ejecutar la aplicación nuevamente para agregar más fotos

## Contacto y Soporte

Para preguntas o problemas:
- Crear un issue en el repositorio de GitHub
- Consultar la documentación en README.md

---

**¡Disfruta creando tu dataset de caras!** 📸
