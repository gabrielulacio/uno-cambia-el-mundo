# Frontend: Interfaz de la Campaña "Uno cambia el mundo"

Este proyecto de frontend, construido con Vue.js, es la interfaz de usuario que permite a los visitantes interactuar con la campaña de donaciones.

## Requisitos Previos

Asegúrate de tener instalado **Node.js** en tu sistema. Puedes descargarlo desde [nodejs.org](https://nodejs.org/). **npm** (el gestor de paquetes de Node) se instala junto con Node.js.

## Configuración y Ejecución

Sigue estos pasos para poner en marcha el frontend.

### 1. Navega al Directorio del Frontend

Abre una terminal **diferente** a la que estás usando para el backend.
```bash
cd uno-cambia-el-mundo/frontend
```

### 2. Instalar las Dependencias
Instala todas las librerías necesarias listadas en el archivo package.json.
```bash
npm install
```

### 3. Configurar Variables de Entorno
Crea un archivo llamado .env.local en la raíz de esta carpeta para definir la URL de tu backend.

```bash
# Ejemplo de archivo .env.local
VUE_APP_API_URL=http://localhost:8000
```
Esto es importante porque le dice a tu frontend dónde encontrar la API.

### 4. Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo de Vue.
```bash
npm run dev
```

