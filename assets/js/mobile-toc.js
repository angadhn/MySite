class MobileTOC {
  constructor() {
    this.headings = [];
    this.tocContainer = null;
    this.tocButton = null;
    this.init();
  }

  init() {
    if (window.innerWidth > 768) {
      return; // Only for mobile
    }

    const content = document.querySelector('content');
    if (!content) return;

    this.gatherHeadings();
    if (this.headings.length < 2) return;

    this.createTOC();
    this.attachEventListeners();
  }

  gatherHeadings() {
    const content = document.querySelector('content');
    const headingElements = content.querySelectorAll('h1, h2, h3, h4, h5, h6');
    
    headingElements.forEach((heading, index) => {
      const headingText = heading.textContent.trim().toLowerCase();
      if (headingText.includes('notes mentioning') || 
          heading.closest('side') ||
          heading.closest('.newsletter-container')) {
        return;
      }
      
      if (!heading.id) {
        heading.id = this.createSlug(heading.textContent) + '-' + index;
      }
      
      this.headings.push({
        element: heading,
        id: heading.id,
        text: heading.textContent.trim(),
        level: parseInt(heading.tagName.charAt(1)),
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

  createTOC() {
    // Create the TOC button
    this.tocButton = document.createElement('button');
    this.tocButton.className = 'mobile-toc-button';
    this.tocButton.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-up">
        <polyline points="18 15 12 9 6 15"></polyline>
      </svg>
    `;
    document.body.appendChild(this.tocButton);

    // Create the TOC container
    this.tocContainer = document.createElement('div');
    this.tocContainer.className = 'mobile-toc-container';
    this.tocContainer.innerHTML = `
      <div class="mobile-toc-header">Table of Contents</div>
      <div class="mobile-toc-sections">
        ${this.headings.map(heading => this.createTocItem(heading)).join('')}
      </div>
    `;
    document.body.appendChild(this.tocContainer);
  }

  createTocItem(heading) {
    return `
      <div class="mobile-toc-item" data-target="${heading.id}" data-level="${heading.level}">
        <div class="mobile-toc-title" data-level="${heading.level}">${heading.text}</div>
      </div>
    `;
  }

  attachEventListeners() {
    this.tocButton.addEventListener('click', () => {
      this.tocContainer.classList.toggle('show');
      this.tocButton.classList.toggle('open');
    });

    this.tocContainer.addEventListener('click', (e) => {
      const tocItem = e.target.closest('.mobile-toc-item');
      if (tocItem && tocItem.dataset.target) {
        e.preventDefault();
        const targetElement = document.getElementById(tocItem.dataset.target);
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
          this.tocContainer.classList.remove('show');
          this.tocButton.classList.remove('open');
        }
      }
    });
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new MobileTOC());
} else {
  new MobileTOC();
} 