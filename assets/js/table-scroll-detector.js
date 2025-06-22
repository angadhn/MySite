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
    
    // Handle standalone markdown tables by wrapping them like booktabs tables
    const standaloneTables = document.querySelectorAll('table:not(.table-wrapper table)');
    
    standaloneTables.forEach(table => {
      // Check if we're on mobile and table needs scrolling
      const isMobile = window.innerWidth <= 414;
      const needsScrolling = table.scrollWidth > (isMobile ? window.innerWidth : table.clientWidth);
      
      if (isMobile && needsScrolling) {
        // Wrap table in table-wrapper if not already wrapped
        if (!table.parentElement.classList.contains('table-wrapper')) {
          const wrapper = document.createElement('div');
          wrapper.className = 'table-wrapper';
          table.parentNode.insertBefore(wrapper, table);
          wrapper.appendChild(table);
          
          // Now check if the wrapped table overflows
          if (table.scrollWidth > wrapper.clientWidth) {
            wrapper.classList.add('show-scroll-hint');
          }
          
          // Remove hint after user scrolls
          wrapper.addEventListener('scroll', function() {
            wrapper.classList.remove('show-scroll-hint');
          }, { once: true });
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