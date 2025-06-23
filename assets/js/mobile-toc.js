class MobileTOC {
  constructor() {
    this.headings = [];
    this.tocButton = null;
    this.tocPopup = null;
    this.isOpen = false;
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
    return window.innerWidth <= 768 || 
           /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
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
        <span class="chevron-up">▲</span>
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
    });

    // Update active section on scroll
    let ticking = false;
    const updateOnScroll = () => {
      if (!ticking) {
        requestAnimationFrame(() => {
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
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  }

  closeTOC() {
    this.isOpen = false;
    this.tocPopup.classList.remove('show');
    this.tocButton.classList.remove('open');
    document.body.style.overflow = ''; // Restore scrolling
  }

  updateActiveSection() {
    if (!this.isOpen) return;

    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Find current active section
    let activeIndex = 0;
    for (let i = 0; i < this.headings.length; i++) {
      if (scrollTop >= this.headings[i].offsetTop - 100) {
        activeIndex = i;
      }
    }

    // Update active state in mobile TOC
    const tocItems = this.tocPopup.querySelectorAll('.mobile-toc-item');
    tocItems.forEach((item, index) => {
      item.classList.toggle('active', index === activeIndex);
    });
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