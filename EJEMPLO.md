# Ejemplo de Uso - Face Dataset Application

Este archivo muestra ejemplos de cómo usar la aplicación de dataset de rostros.

## Ejecución Básica

```bash
# Ejecutar la aplicación
python face_dataset_app.py
```

## Flujo de Trabajo Esperado

### 1. Inicio de la Aplicación
```
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
```

### 2. Captura de Fotos

La aplicación abrirá una ventana con la cámara web que mostrará:

- **Contador de fotos**: "Fotos: X/12" en la esquina superior
- **Detección de rostro**: Rectángulo verde alrededor del rostro detectado
- **Mensajes guía**:
  - Si no se ha capturado la foto frontal: "Busque una posicion frontal" (en rojo)
  - Si se detecta un rostro frontal: "ROSTRO FRONTAL DETECTADO - Presione ESPACIO" (en verde)
  - Después de la foto frontal: "Puede tomar fotos desde cualquier angulo" (en amarillo)

### 3. Captura de la Primera Foto (Frontal)

1. Posiciónese de frente a la cámara
2. Espere a que aparezca el mensaje "ROSTRO FRONTAL DETECTADO"
3. Presione **ESPACIO** para capturar
4. Verá el mensaje: `✓ Foto frontal capturada: Juan_Perez_frontal_1_[timestamp].jpg`

### 4. Captura de las Fotos Restantes (11 fotos)

Después de la foto frontal, puede tomar fotos desde diferentes ángulos:
- Perfil derecho
- Perfil izquierdo
- Ligeramente arriba
- Ligeramente abajo
- Con diferentes expresiones
- Con diferentes iluminaciones

Para cada foto:
1. Posiciónese como desee
2. Presione **ESPACIO**
3. Verá: `✓ Foto X capturada: Juan_Perez_pose_X_[timestamp].jpg`

### 5. Finalización

Después de capturar las 12 fotos:
```
¡Completado! Se capturaron 12 fotos para Juan_Perez
Dataset guardado en: dataset/Juan_Perez

¡Dataset creado exitosamente!
```

## Estructura de Archivos Resultante

```
dataset/
└── Juan_Perez/
    ├── Juan_Perez_frontal_1_20231112_143025_123456.jpg
    ├── Juan_Perez_pose_2_20231112_143030_234567.jpg
    ├── Juan_Perez_pose_3_20231112_143035_345678.jpg
    ├── Juan_Perez_pose_4_20231112_143040_456789.jpg
    ├── Juan_Perez_pose_5_20231112_143045_567890.jpg
    ├── Juan_Perez_pose_6_20231112_143050_678901.jpg
    ├── Juan_Perez_pose_7_20231112_143055_789012.jpg
    ├── Juan_Perez_pose_8_20231112_143100_890123.jpg
    ├── Juan_Perez_pose_9_20231112_143105_901234.jpg
    ├── Juan_Perez_pose_10_20231112_143110_012345.jpg
    ├── Juan_Perez_pose_11_20231112_143115_123456.jpg
    └── Juan_Perez_pose_12_20231112_143120_234567.jpg
```

## Consejos para Mejores Resultados

### Para la Foto Frontal:
- Mire directamente a la cámara
- Mantenga una expresión neutral
- Asegúrese de tener buena iluminación frontal
- Evite sombras en el rostro
- Mantenga la cabeza erguida

### Para las Fotos Adicionales:
- Varíe los ángulos (perfil derecho, izquierdo, 3/4)
- Pruebe diferentes alturas (ligeramente arriba, abajo)
- Incluya diferentes expresiones faciales
- Varíe la iluminación si es posible
- Mantenga siempre el rostro visible

## Cancelación

Si necesita cancelar la captura en cualquier momento:
- Presione **ESC**
- Las fotos ya capturadas se mantendrán en el directorio
- Puede reiniciar la aplicación para completar las fotos faltantes con un nombre diferente

## Uso con Múltiples Personas

Para crear datasets de varias personas:

```bash
# Primera persona
python face_dataset_app.py
# Ingrese: Maria_Lopez

# Segunda persona
python face_dataset_app.py
# Ingrese: Carlos_Rodriguez

# Tercera persona
python face_dataset_app.py
# Ingrese: Ana_Martinez
```

Resultado:
```
dataset/
├── Maria_Lopez/
│   └── [12 fotos]
├── Carlos_Rodriguez/
│   └── [12 fotos]
└── Ana_Martinez/
    └── [12 fotos]
```

## Solución de Problemas

### "Error: No se pudo abrir la cámara"
- Verifique que su cámara web esté conectada
- Cierre otras aplicaciones que puedan estar usando la cámara
- En Linux, verifique permisos de acceso a `/dev/video0`

### "Busque una posicion frontal" no cambia a verde
- Acérquese más a la cámara
- Mejore la iluminación de su rostro
- Mire directamente a la cámara
- Retire obstáculos del rostro (gafas oscuras, gorros, etc.)

### La ventana no aparece
- Verifique que OpenCV esté instalado correctamente: `pip install -r requirements.txt`
- En servidores remotos sin GUI, esta aplicación no funcionará (requiere interfaz gráfica)
