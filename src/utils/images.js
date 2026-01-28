/**
 * Utilidad para gestionar las rutas de imágenes en el proyecto.
 * @param {string} name - Nombre de la imagen o URL completa.
 * @returns {string} - Ruta procesada para usar en el atributo src.
 */
export const getImageUrl = (name) => {
  if (!name) return '/images/projects/hero-bg.png'; // Imagen por defecto
  
  // Si ya es una URL completa (http...) la devolvemos tal cual
  if (name.startsWith('http')) return name;
  
  // Si empieza con /, asumimos que ya es una ruta absoluta desde public
  if (name.startsWith('/')) return name;
  
  // Por defecto, buscamos en la carpeta de proyectos de public
  // Esto es lo mejor para imágenes dinámicas que vienen de un API/Excel
  return `/images/projects/${name}`;
};
