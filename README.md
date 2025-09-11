# uno-cambia-el-mundo
Web para la campaña de recaudación de fondos de Rotary San Cristóbal para la Fundación Centro Médico Rotario Dr. Pablo Puky

```bash
/backend (FASTAPI)
│
├── /src
│   │
│   ├── /routers         # Endpoints de la API
│   │
│   ├── /services        # Lógica de la aplicación y casos de uso
│   │
│   ├── /models          # Modelos y reglas de negocio
│   │
│   └── /utils           # Utilidades generales (opcional)
│
├── **.env**             # Archivo de variables de entorno (NO se sube a Git)
│
├── **.gitignore**       # Reglas para Git
│
├── **main.py**          # Punto de entrada de la aplicación FastAPI
│
└── **requirements.txt** # Dependencias de Python
```

```bash
/frontend (VUE.JS)
│
├── /public              # Archivos estáticos públicos (favicon, index.html, etc.)
│
├── /src
│   │
│   ├── /assets          # Recursos estáticos como imágenes, estilos, etc.
│   │
│   ├── /components      # Componentes reutilizables de la UI
│   │
│   ├── /views           # Vistas principales de la aplicación
│   │
│   ├── /router          # Configuración de rutas de la aplicación
│   │
│   ├── /store           # Gestión del estado global (Vuex o Pinia)
│   │
│   └── /utils           # Servicios y utilidades generales (ej. `api.js`)
│
├── **.env**             # Variables de entorno para el frontend (NO se sube a Git)
│
├── **.gitignore**       # Reglas para Git
│
├── **package.json**     # Dependencias y scripts del proyecto
│
└── **vite.config.js**   # Configuración de Vite (o Webpack si aplica)
```
