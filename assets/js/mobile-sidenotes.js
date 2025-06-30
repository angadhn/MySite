class MobileSidenotes {
  constructor() {
    this.backdrop = null;
    this.init();
  }

  init() {
    // Only initialize on mobile devices
    if (!this.isMobileDevice()) {
      return;
    }
    
    this.createBackdrop();
    this.attachEventListeners();
  }

  isMobileDevice() {
    return window.innerWidth <= 768;
  }

  createBackdrop() {
    this.backdrop = document.createElement('div');
    this.backdrop.className = 'mobile-sidenote-backdrop';
    document.body.appendChild(this.backdrop);
  }

  attachEventListeners() {
    // Monitor checkbox changes to show/hide backdrop
    document.addEventListener('change', (e) => {
      if (e.target.classList.contains('margin-toggle')) {
        this.updateBackdropVisibility();
      }
    });

    // Handle backdrop clicks
    this.backdrop.addEventListener('click', (e) => {
      this.dismissAllSidenotes();
    });

    // Handle window resize
    window.addEventListener('resize', () => {
      if (!this.isMobileDevice()) {
        // Close all open sidenotes when switching to desktop
        this.dismissAllSidenotes();
      }
    });

    // Close sidenotes on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.dismissAllSidenotes();
      }
    });
  }

  updateBackdropVisibility() {
    // Only check for actual sidenotes, not marginnotes (which are for image captions)
    const openSidenotes = document.querySelectorAll('.margin-toggle:checked + .sidenote');
    
    if (openSidenotes.length > 0) {
      this.backdrop.style.display = 'block';
    } else {
      this.backdrop.style.display = 'none';
    }
  }

  dismissSidenote(sidenote) {
    // Find the associated checkbox/toggle
    const toggle = sidenote.previousElementSibling;
    if (toggle && toggle.classList.contains('margin-toggle')) {
      toggle.checked = false;
      // Trigger change event manually to ensure normal flow
      toggle.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }

  dismissAllSidenotes() {
    const openToggles = document.querySelectorAll('.margin-toggle:checked');
    openToggles.forEach(toggle => {
      toggle.checked = false;
      // Trigger change event manually to ensure normal flow  
      toggle.dispatchEvent(new Event('change', { bubbles: true }));
    });
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new MobileSidenotes();
});

// Also initialize if script loads after DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new MobileSidenotes();
  });
} else {
  new MobileSidenotes();
} 