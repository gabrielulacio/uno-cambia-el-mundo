# Uno Cambia el Mundo (UCEM) 💛

**Uno Cambia el Mundo** es la plataforma oficial de recaudación y gestión de proyectos sociales de **Rotary San Cristóbal (Dtto 4380)**. Diseñada para conectar la generosidad de la comunidad con las necesidades más urgentes del Estado Táchira, Venezuela, en áreas de salud, alimentación y educación.

## 🚀 Características principales

- **Gestión de Proyectos:** Visualización detallada de iniciativas enfocadas en el impacto social.
- **Reporte de Donaciones:** Sistema transparente para el reporte y seguimiento de aportes.
- **Multilingüe:** Soporte completo para español e inglés. (i18n ready).
- **Backend Serverless:** API robusta integrada con Google Sheets para gestión de datos en tiempo real.

## 🛠️ Stack Tecnológico

### Frontend
- **Framework:** [Vue 3](https://vuejs.org/) (Composition API)
- **Herramienta de Build:** [Vite](https://vitejs.dev/)
- **Gestión de Estado:** Componibles reactivos (Custom Stores)
- **Internacionalización:** [Vue I18n](https://vue-i18n.intlify.dev/)
- **Estilos:** Sass / SCSS (Arquitectura modular)
- **Animaciones:** Canvas Confetti

### Backend
- **Lenguaje:** Python 3.11+
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Persistencia:** Google Sheets API (vía `gspread`)
- **Seguridad:** Rate Limiting con [SlowAPI](https://slowapi.readthedocs.io/)
- **Despliegue:** [Vercel Functions](https://vercel.com/docs/functions)

## 📁 Estructura del Proyecto

```text
.
├── api/                # Backend (FastAPI para Vercel Serverless)
│   └── index.py        # Endpoints y lógica de negocio
├── public/             # Archivos estáticos públicos
├── src/                # Código fuente del Frontend
│   ├── assets/         # Estilos globales, imágenes e iconos
│   ├── components/     # Componentes de interfaz (UI)
│   ├── constants/      # Datos constantes (proyectos, configuraciones)
│   ├── locales/        # Diccionarios de traducción (i18n)
│   ├── router/         # Rutas de la aplicación (Vue Router)
│   ├── services/       # Clientes HTTP (Axios)
│   ├── store/          # Lógica de estado y lógica de negocio reactiva
│   └── views/          # Vistas (páginas) principales
├── vercel.json         # Configuración de infraestructura (Builds & Routes)
└── requirements.txt    # Dependencias de Python
```

## 💻 Instalación y Desarrollo Local

### Requisitos
- **Node.js:** Versión 20.19.0 o superior.
- **Python:** Versión 3.11 o superior.
- **Git:** Para clonar el repositorio.

### Paso 1: Clonar y configurar dependencias
```bash
git clone https://github.com/gabrielulacio/uno-cambia-el-mundo.git
cd uno-cambia-el-mundo

# Instalar dependencias del frontend
npm install
```

### Paso 2: Ejecutar el Frontend
El servidor de desarrollo de Vite se iniciará en `http://localhost:5173`.
```bash
npm run dev
```

### Paso 3: Configurar el Backend (Opcional)
Si necesitas probar la API localmente con una base de datos real:
1. Crea un entorno virtual: `python -m venv venv`.
2. Actívalo: `source venv/bin/activate` (o `venv\Scripts\activate` en Windows).
3. Instala dependencias: `pip install -r requirements.txt`.
4. Define las variables de entorno en un archivo `.env` (credenciales de Google Cloud).

### Paso 4: Ejecutar el Backend
Con el entorno virtual activado, ejecuta:
```bash
python -m uvicorn api.index:app --reload --port 8000
```
La API estará disponible en `http://localhost:8000`. El frontend está configurado para comunicarse con la API en este puerto durante el desarrollo.

## 🚀 Despliegue
Este repositorio está optimizado para **Vercel**. Cualquier cambio en la rama `main` disparará un despliegue automático que gestiona tanto el frontend estático como las funciones serverless de la API.

---

## 🤝 Contribuciones
Este es un proyecto impulsado por el voluntariado de **Rotary San Cristóbal**. Si deseas contribuir al código, por favor abre un *Issue* o envía un *Pull Request*.

## 📄 Licencia
Este proyecto está bajo la [Licencia MIT](LICENSE).

---
*Desarrollado con ❤️ para la comunidad del Táchira.*
