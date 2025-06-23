class ScrollProgress {
  constructor() {
    this.headings = [];
    this.progressContainer = null;
    this.currentSection = null;
    this.init();
  }

  init() {
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

    this.createProgressIndicator();
    this.attachScrollListener();
    this.updateProgress();
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

  createProgressIndicator() {
    // Create the progress container
    this.progressContainer = document.createElement('div');
    this.progressContainer.className = 'scroll-progress';
    this.progressContainer.innerHTML = `
      <div class="scroll-progress-content">
        <div class="mobile-chevron" aria-label="Toggle table of contents">
          <svg viewBox="0 0 24 24" width="16" height="16">
            <path d="M7 10l5 5 5-5z" fill="currentColor"/>
          </svg>
        </div>
        <div class="progress-sections">
          ${this.headings.map(heading => this.createProgressSection(heading)).join('')}
        </div>
        <div class="scroll-progress-toc">
          <div class="toc-header">Table of Contents</div>
          <div class="toc-sections">
            ${this.headings.map(heading => this.createTocItem(heading)).join('')}
          </div>
        </div>
      </div>
    `;

    // Insert into the page
    document.body.appendChild(this.progressContainer);

    // Add table of contents functionality for desktop/laptop devices
    this.addTableOfContents();

    // Add mobile chevron functionality
    this.addMobileChevronHandler();

    // Add click handlers
    this.progressContainer.addEventListener('click', (e) => {
      const sectionLink = e.target.closest('.progress-section');
      if (sectionLink && sectionLink.dataset.target) {
        e.preventDefault();
        const targetElement = document.getElementById(sectionLink.dataset.target);
        if (targetElement) {
          // Update URL hash with the section ID
          const sectionId = sectionLink.dataset.target;
          history.pushState(null, null, `#${sectionId}`);
          
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  }

  addTableOfContents() {
    // Only add table of contents on devices that support precise pointing (mouse)
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      return;
    }

    const tocItems = this.progressContainer.querySelectorAll('.toc-item');

    // Add click handlers to table of contents items
    tocItems.forEach((item, index) => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const targetElement = document.getElementById(item.dataset.target);
        if (targetElement) {
          // Update URL hash with the section ID
          const sectionId = item.dataset.target;
          history.pushState(null, null, `#${sectionId}`);
          
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  addMobileChevronHandler() {
    // Only add mobile chevron functionality on touch devices
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      return;
    }

    const chevron = this.progressContainer.querySelector('.mobile-chevron');
    const tocContainer = this.progressContainer.querySelector('.scroll-progress-toc');
    
    if (!chevron || !tocContainer) return;

    // Add click handlers to table of contents items for mobile
    const tocItems = this.progressContainer.querySelectorAll('.toc-item');
    tocItems.forEach((item, index) => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const targetElement = document.getElementById(item.dataset.target);
        if (targetElement) {
          // Close the ToC first
          this.progressContainer.classList.remove('toc-open');
          
          // Update URL hash with the section ID
          const sectionId = item.dataset.target;
          history.pushState(null, null, `#${sectionId}`);
          
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });

    // Handle chevron tap
    chevron.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      this.progressContainer.classList.toggle('toc-open');
    });

    // Close ToC when clicking outside
    document.addEventListener('click', (e) => {
      if (!this.progressContainer.contains(e.target)) {
        this.progressContainer.classList.remove('toc-open');
      }
    });
  }

  createTocItem(heading) {
    return `
      <div class="toc-item" data-target="${heading.id}" data-level="${heading.level}">
        <div class="toc-indicator"></div>
        <div class="toc-title" data-level="${heading.level}">${heading.text}</div>
      </div>
    `;
  }

  createProgressSection(heading) {
    return `
      <div class="progress-section" data-target="${heading.id}" data-level="${heading.level}">
        <div class="progress-line"></div>
        <span class="progress-text">${heading.text}</span>
      </div>
    `;
  }

  attachScrollListener() {
    let ticking = false;
    
    const updateOnScroll = () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          this.updateProgress();
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener('scroll', updateOnScroll);
    window.addEventListener('resize', () => {
      // Recalculate heading positions on resize
      this.headings.forEach(heading => {
        heading.offsetTop = heading.element.offsetTop;
      });
      updateOnScroll();
    });
  }

  updateProgress() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    
    // Find current active section
    let activeIndex = 0;
    for (let i = 0; i < this.headings.length; i++) {
      if (scrollTop >= this.headings[i].offsetTop - 100) {
        activeIndex = i;
      }
    }

    // Update progress indicators
    const progressSections = this.progressContainer.querySelectorAll('.progress-section');
    const tocItems = this.progressContainer.querySelectorAll('.toc-item');
    
    progressSections.forEach((section, index) => {
      const isActive = index === activeIndex;
      const isPassed = index < activeIndex;
      
      section.classList.toggle('active', isActive);
      section.classList.toggle('passed', isPassed);
      
      // Calculate progress for current section
      if (isActive) {
        const currentHeading = this.headings[index];
        const nextHeading = this.headings[index + 1];
        
        let progress = 0;
        if (nextHeading) {
          const sectionHeight = nextHeading.offsetTop - currentHeading.offsetTop;
          const scrollInSection = scrollTop - currentHeading.offsetTop + 100;
          progress = Math.min(Math.max(scrollInSection / sectionHeight, 0), 1);
        } else {
          // Last section - calculate based on remaining document
          const remainingHeight = documentHeight - currentHeading.offsetTop;
          const scrollInSection = scrollTop - currentHeading.offsetTop + 100;
          progress = Math.min(Math.max(scrollInSection / remainingHeight, 0), 1);
        }
        
        section.style.setProperty('--progress', progress);
      } else {
        section.style.setProperty('--progress', isPassed ? 1 : 0);
      }
    });

    // Update table of contents items to match progress bars
    tocItems.forEach((item, index) => {
      const isActive = index === activeIndex;
      const isPassed = index < activeIndex;
      
      item.classList.toggle('active', isActive);
      item.classList.toggle('passed', isPassed);
      
      // Sync progress with the corresponding progress bar
      const correspondingSection = progressSections[index];
      if (correspondingSection) {
        const progress = correspondingSection.style.getPropertyValue('--progress') || (isPassed ? 1 : 0);
        item.style.setProperty('--progress', progress);
      }
    });
  }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new ScrollProgress());
} else {
  new ScrollProgress();
} 