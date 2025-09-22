# Uno Cambia el Mundo

Sitio web y API para la campaña de recaudación de fondos de Rotary San Cristóbal para la Fundación Centro Médico Rotario Dr. Pablo Puky.

Este monorepo contiene:

- Frontend: Vue 3 + Vite (`frontend/`)
- API (Producción en Vercel): FastAPI (`api/index.py`)
- Infra de despliegue: `vercel.json`

## Arquitectura y estructura

```
.
├─ api/
│  └─ index.py           # FastAPI para Vercel Serverless Functions
├─ frontend/
│  ├─ src/
│  ├─ index.html
│  ├─ package.json
│  └─ vite.config.js
├─ backend/              # Proyecto FastAPI separado (no usado en Vercel)
├─ vercel.json           # Builds + rutas para Vercel (SPA + API)
└─ requirements.txt      # Dependencias Python para la API
```

## Endpoints (Producción)

- `GET /api/hello` → salud de la API
- `GET /api/donation-status` → { goal: number, current: number }
- `GET /api/payment-methods` → Lista de métodos de pago (puede depender de Google Sheets)

Notas:
- Si no configuras las credenciales de Google, la API devuelve valores de fallback para evitar fallos.

## Desarrollo local

Requisitos:
- Node.js 20.x (o superior compatible)
- Python 3.11+ (recomendado)

### 1) API local (FastAPI)

Instalar dependencias Python (desde la raíz del repo):

```powershell
pip install -r .\requirements.txt
```

Opcional: exporta credenciales de Google para obtener datos reales (si no, devuelve mocks):

```powershell
$env:GOOGLE_CREDENTIALS_JSON = Get-Content -Raw -Path "C:\ruta\a\service-account.json"
```

Levantar la API (recomendado con root-path para emular producción):

```powershell
uvicorn api.index:app --reload --host 127.0.0.1 --port 8000 --root-path /api
```

Pruebas rápidas:

- http://127.0.0.1:8000/api/hello
- http://127.0.0.1:8000/api/donation-status

Alternativa sin `--root-path` (rutas en `/`):

```powershell
uvicorn api.index:app --reload --host 127.0.0.1 --port 8000
```

En ese caso, usa `VITE_API_URL=http://127.0.0.1:8000` en el frontend (sin `/api`).

### 2) Frontend local (Vite + Vue 3)

Instalar dependencias y ejecutar:

```powershell
cd frontend
npm install
# Si corriste la API con --root-path /api
$env:VITE_API_URL = "http://127.0.0.1:8000/api"
# Si corriste la API sin --root-path, usa en cambio:
# $env:VITE_API_URL = "http://127.0.0.1:8000"
npm run dev
```

Abrir: http://localhost:5173

## Despliegue en Vercel

El archivo `vercel.json` define dos builds y el enrutamiento:

- Frontend (static build):
	- `@vercel/static-build` con `src: frontend/package.json`
	- `config.distDir: "dist"` (Vite genera `dist`)
	- Rutas: `{ "handle": "filesystem" }` y fallback SPA → `/(.*) -> /index.html`
- API (serverless Python):
	- `@vercel/python` sobre `api/index.py`
	- Rutas: `/api$` y `/api/(.*)` → `api/index.py`

Variables de entorno en Vercel (Settings → Environment Variables):

- `GOOGLE_CREDENTIALS_JSON` (Production y Preview) con el contenido JSON de tu service account.

Notas:
- El frontend en producción usa por defecto `baseURL: '/api'` (`VITE_API_URL` es opcional). No definas `VITE_API_URL` en producción si llamas a la API del mismo dominio.
- El proyecto especifica engines de Node en `frontend/package.json`. Vercel suele respetarlo automáticamente.

## Solución de problemas

- 404 en `/` (raíz):
	- Revisa que el deploy haya tomado el `vercel.json` y que el fallback `/(.*) -> /index.html` exista.
	- En el Deployment, verifica que `index.html` aparece en "Static Files".
	- Forza un redeploy del último commit y limpia caché del navegador.

- 404 en `/api`:
	- Verifica las rutas `/api$` y `/api/(.*)` en `vercel.json`.
	- Asegura que la app usa `FastAPI(root_path="/api")` (ya configurado en `api/index.py`).

- Datos de Google Sheets:
	- Si falta `GOOGLE_CREDENTIALS_JSON`, la API devuelve valores mock. Añádelo en Vercel o como variable local si quieres datos reales.

## Licencia

MIT © 2025 Gabriel Ulacio
