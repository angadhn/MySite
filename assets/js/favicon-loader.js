document.addEventListener('DOMContentLoaded', function() {
  // Select all external links that don't have specific icons
  const links = document.querySelectorAll('a[href^="http"]:not(.internal-link):not([href*="google.com"]):not([href*="github.com"]):not([href*="youtube.com"]):not([href*="wikipedia.org"]):not([href*="ourworldindata.org"]):not([href$=".pdf"])');
  
  links.forEach(link => {
    if (link.href) {
      try {
        const url = new URL(link.href);
        const domain = url.hostname;
        const faviconUrl = `https://www.google.com/s2/favicons?domain=${domain}&size=32`;
        link.style.setProperty('--favicon-url', `url('${faviconUrl}')`);
      } catch (e) {
        console.warn('Invalid URL:', link.href);
      }
    }
  });
}); 