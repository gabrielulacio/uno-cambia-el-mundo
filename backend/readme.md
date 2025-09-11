# Backend: API de la Campaña "Uno cambia el mundo"

Este proyecto de backend, construido con FastAPI, gestiona toda la lógica de la API para la campaña de donaciones.

## Requisitos Previos

Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

## Configuración y Ejecución

Sigue estos pasos para poner en marcha el backend en tu máquina local.

### 1. Clona el Repositorio

Si aún no lo has hecho, clona el repositorio principal del proyecto.
```bash
git clone https://github.com/gabrielulacio/uno-cambia-el-mundo.git
```

### 2. Navega al Directorio del Backend

Abre una terminal y navega hasta la carpeta del backend.
```bash
cd uno-cambia-el-mundo/backend
```
### 3. Crear un Entorno Virtual (Opcional, pero recomendado)

Es una buena práctica crear un entorno virtual para aislar las dependencias de este proyecto de otros que puedas tener.


```Bash
python -m venv venv
```

Luego, activa el entorno virtual:

En Windows:

```Bash
venv\Scripts\activate
```

En macOS y Linux:

```Bash
source venv/bin/activate
```

### 4. Instalar las Dependencias
Instala todas las librerías necesarias listadas en el archivo requirements.txt.

```Bash
pip install -r requirements.txt
```

### 5. Configurar Variables de Entorno
Crea un archivo llamado .env en la raíz de esta carpeta. Este archivo contiene información sensible y nunca se sube a Git.

```Bash
# Ejemplo de archivo .env
DATABASE_URL="sqlite:///./test.db"
# Otras claves de API irían aquí
```

### 6. Ejecutar el Servidor
Inicia el servidor de FastAPI. El flag --reload es muy útil porque reinicia automáticamente el servidor cuando detectas cambios en tu código.

```Bash
uvicorn main:app --reload
```


Puedes acceder a la documentación interactiva de la API en http://localhost:8000/docs.


