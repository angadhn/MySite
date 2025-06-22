// Intelligent table scroll detection
document.addEventListener('DOMContentLoaded', function() {
  function checkTableOverflow() {
    // Handle tables in table-wrapper divs
    const tableWrappers = document.querySelectorAll('.table-wrapper');
    
    tableWrappers.forEach(wrapper => {
      const table = wrapper.querySelector('table');
      if (!table) return;
      
      // Check if table is wider than its container
      if (table.scrollWidth > wrapper.clientWidth) {
        wrapper.classList.add('show-scroll-hint');
      } else {
        wrapper.classList.remove('show-scroll-hint');
      }
    });
    
    // Handle standalone markdown tables (not in table-wrapper)
    const standaloneTables = document.querySelectorAll('table:not(.table-wrapper table)');
    
    standaloneTables.forEach(table => {
      // Check if table content is wider than viewport on mobile
      if (window.innerWidth <= 480 && table.scrollWidth > table.clientWidth) {
        table.classList.add('show-scroll-hint');
        
        // Add scroll hint if it doesn't exist
        if (!table.hasAttribute('data-scroll-hint-added')) {
          const hint = document.createElement('div');
          hint.className = 'table-scroll-hint';
          hint.textContent = '← Scroll to view full table →';
          hint.style.cssText = `
            text-align: center;
            font-size: 0.8em;
            color: #666;
            padding: 0.5em;
            background: rgba(0,0,0,0.02);
            margin-bottom: 0;
            display: block;
          `;
          table.parentNode.insertBefore(hint, table);
          table.setAttribute('data-scroll-hint-added', 'true');
          
          // Remove hint after user scrolls
          table.addEventListener('scroll', function() {
            hint.remove();
          }, { once: true });
        }
      } else {
        table.classList.remove('show-scroll-hint');
        // Remove existing hint if table fits
        const existingHint = table.previousElementSibling;
        if (existingHint && existingHint.classList.contains('table-scroll-hint')) {
          existingHint.remove();
          table.removeAttribute('data-scroll-hint-added');
        }
      }
    });
  }
  
  // Check on load
  checkTableOverflow();
  
  // Check on window resize
  window.addEventListener('resize', checkTableOverflow);
  
  // Remove scroll hint after user scrolls
  document.querySelectorAll('.table-wrapper').forEach(wrapper => {
    wrapper.addEventListener('scroll', function() {
      this.classList.remove('show-scroll-hint');
    }, { once: true });
  });
}); 