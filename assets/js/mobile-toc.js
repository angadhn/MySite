class MobileTOC {
  constructor() {
    this.headings = [];
    this.tocButton = null;
    this.tocPopup = null;
    this.isOpen = false;
    this.lastScrollY = 0;
    this.scrollDirection = 'up';
    this.currentActiveIndex = 0;
    this.init();
  }

  init() {
    // Only initialize on mobile devices
    if (!this.isMobileDevice()) return;
    
    // Don't show on home/index page
    const isHomePage = window.location.pathname === '/' || 
                       window.location.pathname === '/index.html' ||
                       window.location.pathname.endsWith('/');
    if (isHomePage) return;
    
    // Only initialize if we're on a page with substantial content
    const content = document.querySelector('content');
    if (!content) return;

    this.gatherHeadings();
    if (this.headings.length < 2) return; // Don't show for short content

    this.createTOCButton();
    this.createTOCPopup();
    this.attachEventListeners();
  }

  isMobileDevice() {
    // Check if it's a touch device first
    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    
    // For tablets in landscape (up to iPad Pro 12.9" landscape: 1366px)
    const isTabletSize = window.innerWidth <= 1366 && isTouchDevice;
    
    // For phones and smaller tablets
    const isMobileSize = window.innerWidth <= 1024;
    
    // Device detection fallback
    const isMobileUA = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    return isMobileSize || isTabletSize || isMobileUA;
  }

  isLandscapeMode() {
    return window.innerHeight <= 600 && window.innerWidth > window.innerHeight;
  }

  gatherHeadings() {
    const content = document.querySelector('content');
    const headingElements = content.querySelectorAll('h1, h2, h3, h4, h5, h6');
    
    headingElements.forEach((heading, index) => {
      // Skip "Notes mentioning this note" section and other backlink-related content
      const headingText = heading.textContent.trim().toLowerCase();
      if (headingText.includes('notes mentioning') || 
          heading.closest('side') ||
          heading.closest('.newsletter-container')) {
        return;
      }
      
      // Create unique ID if it doesn't exist
      if (!heading.id) {
        heading.id = this.createSlug(heading.textContent) + '-' + index;
      }
      
      this.headings.push({
        element: heading,
        id: heading.id,
        text: heading.textContent.trim(),
        level: parseInt(heading.tagName.charAt(1)),
        offsetTop: heading.offsetTop
      });
    });
  }

  createSlug(text) {
    return text
      .toLowerCase()
      .replace(/[^\w\s-]/g, '')
      .replace(/[\s_-]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  createTOCButton() {
    this.tocButton = document.createElement('div');
    this.tocButton.className = 'floating-mobile-toc-button';
    this.tocButton.innerHTML = `
      <button class="mobile-toc-toggle" aria-label="Toggle table of contents">
        <span class="chevron">⌄</span>
      </button>
    `;
    
    document.body.appendChild(this.tocButton);
  }

  createTOCPopup() {
    this.tocPopup = document.createElement('div');
    this.tocPopup.className = 'mobile-toc-popup';
    this.tocPopup.innerHTML = `
      <div class="mobile-toc-header">
        <span>Table of Contents</span>
        <button class="mobile-toc-close" aria-label="Close table of contents">×</button>
      </div>
      <div class="mobile-toc-content">
        ${this.headings.map(heading => this.createMobileTocItem(heading)).join('')}
      </div>
    `;
    
    document.body.appendChild(this.tocPopup);
  }

  createMobileTocItem(heading) {
    return `
      <div class="mobile-toc-item" data-target="${heading.id}" data-level="${heading.level}">
        <div class="mobile-toc-title" data-level="${heading.level}">${heading.text}</div>
      </div>
    `;
  }

  attachEventListeners() {
    // Toggle button click
    const toggleButton = this.tocButton.querySelector('.mobile-toc-toggle');
    toggleButton.addEventListener('click', (e) => {
      e.stopPropagation();
      this.toggleTOC();
    });

    // Close button click
    const closeButton = this.tocPopup.querySelector('.mobile-toc-close');
    closeButton.addEventListener('click', (e) => {
      e.stopPropagation();
      this.closeTOC();
    });

    // TOC item clicks
    const tocItems = this.tocPopup.querySelectorAll('.mobile-toc-item');
    tocItems.forEach((item) => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = item.dataset.target;
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
          // Update URL hash
          history.pushState(null, null, `#${targetId}`);
          
          // Smooth scroll to target
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
          
          // Close TOC after navigation
          this.closeTOC();
        }
      });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (this.isOpen && 
          !this.tocPopup.contains(e.target) && 
          !this.tocButton.contains(e.target)) {
        this.closeTOC();
      }
    });

    // Handle orientation changes and window resize
    window.addEventListener('resize', () => {
      if (!this.isMobileDevice() && this.tocButton) {
        this.destroy();
      } else if (this.isMobileDevice() && !this.tocButton) {
        this.init();
      }
      
      // If TOC is open during orientation change, close and reopen for proper positioning
      if (this.isOpen) {
        setTimeout(() => {
          this.closeTOC();
          setTimeout(() => {
            this.openTOC();
          }, 100);
        }, 100);
      }
    });

    // Update active section and handle scroll direction
    let ticking = false;
    const updateOnScroll = () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          this.handleScroll();
          this.updateActiveSection();
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener('scroll', updateOnScroll);
  }

  toggleTOC() {
    if (this.isOpen) {
      this.closeTOC();
    } else {
      this.openTOC();
    }
  }

  openTOC() {
    this.isOpen = true;
    this.tocPopup.classList.add('show');
    this.tocButton.classList.add('open');
    this.showTOCButton(); // Ensure button is visible when opening
    
    // In landscape mode with limited height, don't prevent background scrolling
    // to allow better interaction with the page
    if (!this.isLandscapeMode()) {
      document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
    
    // Update active section when opening to show current position
    this.updateActiveSection();
  }

  closeTOC() {
    this.isOpen = false;
    this.tocPopup.classList.remove('show');
    this.tocButton.classList.remove('open');
    document.body.style.overflow = ''; // Restore scrolling
    
    // Resume normal scroll-based hiding behavior
    if (this.scrollDirection === 'down' && this.lastScrollY > 100) {
      this.hideTOCButton();
    }
  }

  handleScroll() {
    const currentScrollY = window.pageYOffset || document.documentElement.scrollTop;
    
    // Determine scroll direction
    if (currentScrollY > this.lastScrollY && currentScrollY > 100) {
      // Scrolling down and past initial scroll threshold
      this.scrollDirection = 'down';
      this.hideTOCButton();
    } else if (currentScrollY < this.lastScrollY) {
      // Scrolling up
      this.scrollDirection = 'up';
      this.showTOCButton();
    }
    
    this.lastScrollY = currentScrollY;
  }

  hideTOCButton() {
    if (!this.isOpen) { // Only hide if TOC popup is not open
      this.tocButton.classList.add('hidden');
    }
  }

  showTOCButton() {
    this.tocButton.classList.remove('hidden');
  }

  updateActiveSection() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Find current active section
    let activeIndex = 0;
    for (let i = 0; i < this.headings.length; i++) {
      if (scrollTop >= this.headings[i].offsetTop - 100) {
        activeIndex = i;
      }
    }

    // Store the current active index
    this.currentActiveIndex = activeIndex;

    // Update active state in mobile TOC if it exists and is open
    if (this.tocPopup) {
      const tocItems = this.tocPopup.querySelectorAll('.mobile-toc-item');
      tocItems.forEach((item, index) => {
        item.classList.toggle('active', index === activeIndex);
      });
    }
  }

  destroy() {
    if (this.tocButton) {
      this.tocButton.remove();
      this.tocButton = null;
    }
    if (this.tocPopup) {
      this.tocPopup.remove();
      this.tocPopup = null;
    }
    this.isOpen = false;
    document.body.style.overflow = '';
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new MobileTOC();
}); 