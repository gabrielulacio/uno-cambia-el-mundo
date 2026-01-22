import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import path from 'path'

// https://vite.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [
    vue(),
    // Load Vue DevTools only in development to prevent prod build issues on Vercel
    mode === 'development' && vueDevTools(),
  ].filter(Boolean),
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // Apunta a tu backend Python
        changeOrigin: true,
        secure: false,
        // IMPORTANTE: Esto elimina '/api' de la ruta antes de enviarla a Python.
        // Frontend pide: /api/hello -> Backend recibe: /hello
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use '@/assets/styles/_main.scss' as *;`,
      },
    },
  },
}))