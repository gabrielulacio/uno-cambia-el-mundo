<template>
  <footer class="footer-section">
    <div class="footer-container">
      <div class="footer-bottom">
        <div class="footer-logos">
          <div class="logo-group">
            <img src="/images/logo-rotary.png" alt="Rotary Logo" class="footer-logo" />
          </div>
          
          <div class="unidos-logo">
            <img src="/images/unocambiaelmundo-logo.png" alt="Uno Cambia el Mundo" class="footer-logo-main" />
          </div>
        </div>

        <!-- Redes sociales -->
        <div class="social-media">
          <a href="https://www.instagram.com/cmrdrpablopuky/" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Instagram">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" fill="currentColor"/>
            </svg>
            <span class="social-handle">cmrdrpablopuky</span>
          </a>
          
          <a href="https://www.instagram.com/rotary_sc/" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Instagram">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" fill="currentColor"/>
            </svg>
            <span class="social-handle">rotary_sc</span>
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
// No props needed for static footer
</script>

<style scoped lang="scss">
@use '@/assets/styles/_main' as *;

.footer-section {
  background: linear-gradient(135deg, var(--rotary-blue) 0%, var(--azure) 100%);
  padding: 32px 0 32px;
  color: var(--white);
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}


.footer-main-text {
  @include heading-2;
  color: var(--white);
  margin-bottom: 12px;
  font-style: italic;
}


.footer-cta {
  display: flex;
  justify-content: center;
}


.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 30px;
}

.footer-logos {
  display: flex;
  align-items: center;
  gap: 40px;
  flex-wrap: wrap;
}

.logo-group {
  display: flex;
  align-items: center;
  gap: 15px;
}

.footer-logo {
  height: 50px;
  width: auto;
}

.footer-logo-main {
  height: 40px;
  width: auto;
}

.district-text {
  @include paragraph-small;
  color: var(--white);
  line-height: 1.3;
  opacity: 0.9;
}

.social-media {
  display: flex;
  align-items: center;
  gap: 25px;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--white);
  text-decoration: none;
  opacity: 0.8;
  transition: opacity 0.3s ease;
}

.social-link:hover {
  opacity: 1;
}

.social-link svg {
  width: 20px;
  height: 20px;
}

.social-handle {
  @include paragraph-small;
  color: var(--white);
}

/* Responsive design */
@media (max-width: 768px) {
  .footer-section {
    padding: 50px 0 30px;
  }
  
  .footer-content {
    margin-bottom: 40px;
  }
  
  .footer-main-text {
    font-size: 1.8rem;
  }
  
  .footer-sub-text {
    font-size: 1.1rem;
  }
  
  .footer-bottom {
    flex-direction: column;
    text-align: center;
    gap: 25px;
  }
  
  .footer-logos {
    justify-content: center;
    gap: 30px;
  }
  
  .social-media {
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
  }
}

@media (max-width: 480px) {
  .footer-section {
    padding: 40px 0 25px;
  }
  
  .footer-message {
    margin-bottom: 30px;
  }
  
  .footer-main-text {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .footer-sub-text {
    font-size: 1rem;
  }
  
  .donate-button {
    padding: 14px 28px;
    font-size: 1rem;
  }
  
  .footer-logos {
    flex-direction: column;
    gap: 20px;
  }
  
  .logo-group {
    flex-direction: column;
    text-align: center;
    gap: 10px;
  }
  
  .social-media {
    gap: 15px;
  }
}
</style>