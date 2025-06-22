// Intelligent table scroll detection
document.addEventListener('DOMContentLoaded', function() {
  function checkTableOverflow() {
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