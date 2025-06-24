// Intelligent table scroll detection
document.addEventListener('DOMContentLoaded', function() {
  function checkTableOverflow() {
    const tableWrappers = document.querySelectorAll('.table-wrapper');
    console.log('Found table wrappers:', tableWrappers.length);
    
    tableWrappers.forEach((wrapper, index) => {
      const table = wrapper.querySelector('table');
      if (!table) {
        console.log(`No table found in wrapper ${index}`);
        return;
      }
      
      // Check if table is wider than its container
      const needsScroll = table.scrollWidth > wrapper.clientWidth;
      console.log(`Table ${index}: scrollWidth=${table.scrollWidth}, clientWidth=${wrapper.clientWidth}, needsScroll=${needsScroll}`);
      
      if (needsScroll) {
        wrapper.classList.add('show-scroll-hint');
        console.log(`Added scroll hint to table ${index}`);
      } else {
        wrapper.classList.remove('show-scroll-hint');
        console.log(`Removed scroll hint from table ${index}`);
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