# Guía: Cómo Agregar Canciones

Sigue estos pasos para agregar correctamente una nueva canción al repertorio.

## 1. Crear la Carpeta
Ve a la carpeta `source/canciones/` y crea una **nueva carpeta** con el nombre de la canción.
*   Usa minúsculas y guiones en lugar de espacios.
*   *Ejemplo:* `source/canciones/mi-nueva-cancion`

## 2. Crear el archivo de Letra
Dentro de tu nueva carpeta, crea un archivo llamado **`letra.txt`**.
Este archivo **debe** comenzar con la información de la canción (metadatos) encerrada en llaves `{}`.

### Estructura Obligatoria
Copia y pega esto al inicio de tu archivo `letra.txt`:

```text
{
  title: Título de la Canción
  artist: Nombre del Artista
  key: C (La tonalidad)
}

[VERSO 1]
Aquí va la letra del verso.
<soprano>Esta parte la cantan solo sopranos</soprano>
<todos>¡Aquí cantan todos!</todos>

[CORO]
Letra del coro...
```

### Reglas Importantes
1.  **Metadatos**: `title`, `artist` y `key` son **obligatorios**. Si falta alguno, el sistema dará error.
2.  **Secciones**: Usa corchetes `[...]` para marcar partes (ej: `[INTRO]`, `[VERSO]`, `[CORO]`).
3.  **Voces**: Usa las etiquetas para colorear voces específicas:
    *   `<soprano> ... </soprano>`
    *   `<alto> ... </alto>`
    *   `<tenor> ... </tenor>`
    *   `<solista> ... </solista>`
    *   `<todos> ... </todos>`

## 3. Agregar Audios (Opcional)
Si tienes audios de referencia, ponlos en la **misma carpeta** que `letra.txt`.
Deben llamarse **exactamente** como la voz (en minúsculas) y ser formato `.mp3`:

*   `soprano.mp3`
*   `alto.mp3`
*   `tenor.mp3`
*   `solista.mp3`
*   `todos.mp3` (o `mezcla.mp3`)

## 4. Actualizar la Página web
Una vez creada la carpeta y el archivo:

1.  Ve a la carpeta principal del proyecto.
2.  Haz doble clic en el archivo **`actualizar_canciones.command`**.
3.  Se abrirá una ventana negra que te dirá si todo salió bien o si hay algún error.
4.  Si dice **"Build successful!"**, actualiza tu página web (abre `docs/index.html`) y la canción aparecerá.

---

## Solución de Errores Comunes

*   **Error: Missing 'letra.txt'**: Olvidaste crear el archivo de texto o lo llamaste de otra forma.
*   **Error: Missing metadata**: Borraste las llaves `{ ... }` del principio o te faltó el `title` o `artist`.
