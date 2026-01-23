<template>
  <section class="brand-intro">
    <div class="container">
      
      <div class="intro-grid">
        <div class="intro-text">
          <span class="eyebrow">{{ $t('brand.eyebrow') }}</span>
          <h2 class="section-title">{{ $t('brand.title') }}</h2>
          <p class="description" v-html="$t('brand.description')"></p>
          
          <div class="location-box">
            <div class="icon-map">📍</div>
            <div class="location-details">
              <strong>{{ $t('brand.location_label') }}</strong>
              <p>{{ $t('brand.location_city') }}</p>
              <small>{{ $t('brand.location_info') }}</small>
            </div>
          </div>

          <a href="https://www.instagram.com/rotary_sc/" target="_blank" class="instagram-cta">
            <div class="icon-ig">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
            </div>
            <div class="cta-text">
              <strong>{{ $t('brand.follow_us_ig') }}</strong>
              <p>@rotary_sc</p>
            </div>
          </a>
        </div>

        <div class="intro-visual">
          <div class="stat-card">
            <span class="stat-number">100%</span>
            <span class="stat-label">{{ $t('brand.transparency') }}</span>
          </div>
          <div class="stat-card">
            <span class="stat-number">+50</span>
            <span class="stat-label">{{ $t('brand.years_service') }}</span>
          </div>
        </div>
      </div>

      <div class="divider"></div>

      <div class="team-section">
        <h3 class="team-title">{{ $t('brand.team_title') }}</h3>
        <p class="team-subtitle">{{ $t('brand.team_subtitle') }}</p>
        
        <div class="team-grid">
          <a v-for="(member, index) in $tm('brand.team_members')" 
             :key="index" 
             :href="member.instagram" 
             target="_blank" 
             rel="noopener noreferrer"
             class="team-card">
            <div class="avatar-container">
              <img 
                v-if="member.image" 
                :src="member.image" 
                :alt="member.name" 
                class="member-photo"
                @error="(e) => (e.target.style.display = 'none')"
              />
              <div class="avatar-placeholder">{{ member.initials }}</div>
            </div>
            <div class="member-info">
              <h4>{{ member.name }}</h4>
              <span class="role">{{ member.role }}</span>
            </div>
          </a>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped lang="scss">
.brand-intro {
  background-color: var(--white);
  padding: 80px 20px;
  color: var(--rotary-blue);
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

/* Intro Grid */
.intro-grid {
  display: grid;
  grid-template-columns: 1fr 0.8fr; /* Texto más ancho que visuales */
  gap: 60px;
  align-items: center;
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

.eyebrow {
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 1px;
  color: var(--rotary-gold);
  font-weight: 700;
  margin-bottom: 12px;
  display: block;
}

.section-title {
  font-size: 2.5rem;
  line-height: 1.2;
  margin-bottom: 24px;
  font-weight: 800;
  color: var(--rotary-blue);
}

.description {
  font-size: 1.1rem;
  line-height: 1.7;
  color: #555;
  margin-bottom: 32px;

  .text-rotary {
    color: var(--rotary-blue);
    font-weight: 700;
  }
}

/* Location Box */
.location-box {
  display: flex;
  gap: 16px;
  background: #f8f9fa;
  padding: 20px;
  border-radius: 12px;
  border-left: 4px solid var(--rotary-gold);

  .icon-map {
    font-size: 2rem;
  }
  
  .location-details p {
    margin: 4px 0;
    color: #333;
  }
  
  small {
    color: #777;
    font-size: 0.85rem;
  }
}

.instagram-cta {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 24px;
  text-decoration: none;
  color: var(--rotary-blue);
  padding: 16px 20px;
  border-radius: 12px;
  border: 1px solid #eee;
  transition: all 0.3s ease;

  &:hover {
    border-color: #e4405f;
    background: #fff5f7;
    transform: translateX(5px);
    
    .icon-ig {
      color: #e4405f;
    }
  }

  .icon-ig {
    display: flex;
    align-items: center;
    color: #555;
    transition: color 0.3s ease;
  }

  .cta-text {
    strong {
      display: block;
      font-size: 1rem;
    }
    p {
      margin: 0;
      font-size: 0.9rem;
      color: #777;
    }
  }
}

/* Visual Stats */
.intro-visual {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.stat-card {
  background: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  display: flex;
  align-items: center;
  gap: 20px;
  transition: transform 0.3s ease;
  border: 1px solid rgba(0,0,0,0.05);

  &:hover {
    transform: translateY(-5px);
  }

  .stat-number {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--rotary-gold);
  }
  
  .stat-label {
    font-size: 1rem;
    font-weight: 600;
    color: var(--rotary-blue);
    line-height: 1.2;
  }
}

/* Divider */
.divider {
  height: 1px;
  background: rgba(0,0,0,0.1);
  margin: 60px 0;
}

/* Team Section */
.team-section {
  text-align: center;
}

.team-title {
  font-size: 2rem;
  margin-bottom: 8px;
  color: var(--rotary-blue);
}

.team-subtitle {
  color: #666;
  margin-bottom: 40px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
}

.team-card {
  background: white;
  padding: 24px;
  border-radius: 12px;
  border: 1px solid #eee;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  transition: all 0.3s ease;
  text-decoration: none;

  &:hover {
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    border-color: var(--rotary-gold);
    transform: translateY(-5px);
  }
}

.avatar-container {
  width: 80px;
  height: 80px;
  flex-shrink: 0;
  position: relative;
}

.member-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid var(--rotary-blue);
  position: relative;
  z-index: 2;
  background-color: white;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  background-color: var(--rotary-blue);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  text-transform: uppercase;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.member-info h4 {
  margin: 0;
  font-size: 1.1rem;
  color: #333;
}

.member-info .role {
  font-size: 0.9rem;
  color: var(--rotary-gold);
  font-weight: 600;
}
</style>