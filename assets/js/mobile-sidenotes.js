class MobileSidenotes {
  constructor() {
    this.backdrop = null;
    this.init();
  }

  init() {
    // Always attach toggle symbol listeners for all devices
    this.attachToggleSymbolListeners();
    
    // Only initialize mobile-specific features on mobile devices
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

  attachToggleSymbolListeners() {
    // Initialize all toggle symbols on page load
    document.querySelectorAll('.margin-toggle').forEach(toggle => {
      this.updateToggleSymbol(toggle);
    });

    // Monitor checkbox changes to update toggle symbols (works on all devices)
    document.addEventListener('change', (e) => {
      if (e.target.classList.contains('margin-toggle')) {
        this.updateToggleSymbol(e.target);
      }
    });
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

  updateToggleSymbol(toggle) {
    // Find the associated label (previous sibling for marginnotes)
    const label = toggle.previousElementSibling;
    if (label && label.classList.contains('margin-toggle') && !label.classList.contains('sidenote-number')) {
      // Update the symbol based on toggle state
      label.textContent = toggle.checked ? ' ⊖' : ' ⊕';
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
      // Update the symbol when dismissing
      this.updateToggleSymbol(toggle);
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