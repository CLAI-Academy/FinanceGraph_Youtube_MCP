# youtube-mcp

Este proyecto implementa un MCP (Multi-Component Platform) que permite buscar videos en YouTube a partir de una consulta (query) y transcribir automáticamente el contenido de los videos encontrados.

## ¿Qué hace el MCP?

- **Busca videos en YouTube** según una consulta proporcionada.
- **Transcribe los videos** obteniendo el texto de los subtítulos automáticos o manuales disponibles.

## Tools disponibles

- `search_youtube_videos(query: str, max_results: int=5) -> List[str]`  
  Busca videos en YouTube que coincidan con la consulta dada y devuelve una lista de IDs de video.

- `get_transcript_from_video_ids(video_ids: List[str]) -> Dict[str, str]`  
  Recupera la transcripción (texto) de los videos a partir de una lista de IDs de video de YouTube.

## Configuración

Antes de ejecutar el proyecto, debes crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
YOUTUBE_API_SERVICE_NAME=youtube
YOUTUBE_API_VERSION=v3
YOUTUBE_API_KEY=TU_API_KEY_DE_GOOGLE
```

Reemplaza `TU_API_KEY_DE_GOOGLE` por tu propia API Key de Google para YouTube Data API v3.

## Ejecución

### 1. Instalar `uv` si no lo tienes

```bash
pip install uv
```

### 2. Crear y activar el entorno virtual con `uv`

```bash
uv venv
```

- En **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- En **Unix/MacOS**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar dependencias

```bash
uv pip install -r requirements.txt
```

### 4. Iniciar el servidor MCP

```bash
python youtube-mcp.py
```

## Instalación como MCP global

Para usar este MCP de forma global, añade la siguiente configuración en tu archivo de configuración MCP:

```json
"youtube-mcp": {
    "command": "uv",
    "args": [
        "--directory",
        "Path\\A\\Tu\\Directorio\\",
        "run",
        "youtube-mcp.py"
    ]
}
```

Reemplaza `"Path\\A\\Tu\\Directorio\\"` por la ruta donde está este proyecto.

---
