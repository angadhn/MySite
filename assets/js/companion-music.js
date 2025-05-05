document.addEventListener('DOMContentLoaded', function() {
  const companionMusicLink = document.getElementById('companion-music-link');
  
  if (companionMusicLink) {
    const url = companionMusicLink.getAttribute('data-url');
    
    if (url) {
      try {
        const urlObj = new URL(url);
        
        // Create audio player container
        const playerContainer = document.createElement('div');
        playerContainer.className = 'audio-player';
        playerContainer.id = 'audio-player';
        playerContainer.setAttribute('aria-hidden', 'true'); // Hide from screen readers when not visible
        
        // Check the current theme
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'dark') {
          playerContainer.classList.add('dark-theme');
        }
        
        // Listen for theme changes
        const observer = new MutationObserver(function(mutations) {
          mutations.forEach(function(mutation) {
            if (mutation.attributeName === 'data-theme') {
              const newTheme = document.documentElement.getAttribute('data-theme');
              if (newTheme === 'dark') {
                playerContainer.classList.add('dark-theme');
              } else {
                playerContainer.classList.remove('dark-theme');
              }
            }
          });
        });
        
        observer.observe(document.documentElement, { attributes: true });

        // Initialize variables
        let artistName = '';
        let trackName = '';
        let isValid = false;
        let embedUrl = '';
        let autoplayEmbedUrl = '';
        let platform = '';
        
        // Handle SoundCloud links
        if (urlObj.hostname.includes('soundcloud.com')) {
          const urlParts = urlObj.pathname.split('/').filter(part => part);
          
          if (urlParts.length >= 2) {
            artistName = urlParts[0].replace(/-/g, ' ');
            trackName = urlParts[1].replace(/-/g, ' ');
            
            // Check for dark mode to customize SoundCloud colors
            const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
            const colorParam = isDarkMode ? '%23ff5500' : '%23ff5500'; // Use orange (%23ff5500) for both themes
            
            // Use visual=false for a more minimal player, auto_play will be set on reveal
            embedUrl = `https://w.soundcloud.com/player/?url=${encodeURIComponent(url)}&color=${colorParam}&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false&visual=false&single_active=false`;
            autoplayEmbedUrl = `https://w.soundcloud.com/player/?url=${encodeURIComponent(url)}&color=${colorParam}&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false&visual=false&single_active=false`;
            isValid = true;
            
            // Store the platform for special handling in the player creation
            platform = 'soundcloud';
          }
        }
        // Handle Spotify links
        else if (urlObj.hostname.includes('spotify.com')) {
          // Extract Spotify track ID
          const match = urlObj.pathname.match(/\/track\/([a-zA-Z0-9]+)/);
          if (match && match[1]) {
            const trackId = match[1];
            embedUrl = `https://open.spotify.com/embed/track/${trackId}`;
            autoplayEmbedUrl = `https://open.spotify.com/embed/track/${trackId}?autoplay=1`;
            isValid = true;
            
            // For Spotify, we'll just use a generic message
            artistName = "this artist";
            trackName = "this track";
          }
        }
        // Handle YouTube links
        else if (urlObj.hostname.includes('youtube.com') || urlObj.hostname.includes('youtu.be')) {
          let videoId = '';
          
          if (urlObj.hostname.includes('youtube.com')) {
            videoId = new URLSearchParams(urlObj.search).get('v');
          } else if (urlObj.hostname.includes('youtu.be')) {
            videoId = urlObj.pathname.substring(1);
          }
          
          if (videoId) {
            // Use privacy-enhanced mode with no cookies
            embedUrl = `https://www.youtube-nocookie.com/embed/${videoId}`;
            autoplayEmbedUrl = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1`;
            isValid = true;
            
            // For YouTube, we'll use a generic message
            artistName = "this creator";
            trackName = "this track";
          }
        }
        
        if (isValid) {
          // Convert to title case if we have specific artist/track
          if (artistName && artistName !== "this artist" && artistName !== "this creator") {
            artistName = artistName.split(' ')
              .map(word => word.charAt(0).toUpperCase() + word.slice(1))
              .join(' ');
          }
          
          if (trackName && trackName !== "this track") {
            trackName = trackName.split(' ')
              .map(word => word.charAt(0).toUpperCase() + word.slice(1))
              .join(' ');
          }
          
          // Store player data but don't create it yet
          playerContainer.dataset.artistName = artistName;
          playerContainer.dataset.trackName = trackName;
          playerContainer.dataset.originalUrl = url;
          playerContainer.dataset.embedUrl = embedUrl;
          playerContainer.dataset.autoplayEmbedUrl = autoplayEmbedUrl;
          
          // Display the link text with hyperlink styling
          companionMusicLink.innerHTML = `I feel that <span class="companion-music-title" tabindex="0" role="button">${artistName}'s "${trackName}"</span> pairs nicely with this essay.`;
          companionMusicLink.style.display = 'block';
          companionMusicLink.style.cursor = 'default';
          
          // Remove role and tabindex from the parent
          companionMusicLink.removeAttribute('role');
          companionMusicLink.removeAttribute('tabindex');
          companionMusicLink.setAttribute('aria-expanded', 'false');
          companionMusicLink.setAttribute('aria-controls', 'audio-player');
          
          // Insert the player after the link
          companionMusicLink.parentNode.insertBefore(playerContainer, companionMusicLink.nextSibling);
          
          // Add click event to the SPAN instead of the parent link
          const musicTitleSpan = companionMusicLink.querySelector('.companion-music-title');
          if (musicTitleSpan) {
            musicTitleSpan.addEventListener('click', function(e) {
              e.preventDefault();
              e.stopPropagation(); // Prevent event from bubbling to parent
              togglePlayer(playerContainer, companionMusicLink);
            });
            
            // Add keyboard support to the SPAN
            musicTitleSpan.addEventListener('keydown', function(e) {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                togglePlayer(playerContainer, companionMusicLink);
              }
            });
          }
        } else {
          // Generic fallback for other music services
          companionMusicLink.innerHTML = `I think this piece is best paired with <a href="${url}" target="_blank" class="music-link">this music</a>`;
          companionMusicLink.style.display = 'block';
        }
      } catch (e) {
        console.error('Error parsing companion music URL:', e);
        companionMusicLink.innerHTML = `I think this piece is best paired with <a href="${url}" target="_blank" class="music-link">this music</a>`;
        companionMusicLink.style.display = 'block';
      }
    }
  }
  
  // Add styling for music links and player
  loadStyles();

  // Add scroll event listener to handle player opacity
  handlePlayerScrollOpacity();
});

function togglePlayer(playerContainer, linkElement) {
  const isVisible = playerContainer.style.display === 'block';
  
  if (isVisible) {
    hidePlayer(playerContainer, linkElement);
  } else {
    showPlayer(playerContainer, linkElement);
  }
}

function showPlayer(playerContainer, linkElement) {
  // Extract data from the container
  const artistName = playerContainer.dataset.artistName;
  const trackName = playerContainer.dataset.trackName;
  const originalUrl = playerContainer.dataset.originalUrl;
  const embedUrl = playerContainer.dataset.embedUrl;
  const autoplayEmbedUrl = playerContainer.dataset.autoplayEmbedUrl;
  
  // Create player with autoplay enabled when revealing
  createCustomAudioPlayer(
    playerContainer, 
    artistName, 
    trackName, 
    originalUrl, 
    autoplayEmbedUrl || (embedUrl + (embedUrl.includes('?') ? '&' : '?') + 'autoplay=1')
  );
  
  playerContainer.style.display = 'block';
  playerContainer.setAttribute('aria-hidden', 'false');
  linkElement.setAttribute('aria-expanded', 'true');
  
  // Add padding to the body to accommodate the fixed player
  document.body.classList.add('has-audio-player');
}

function hidePlayer(playerContainer, linkElement) {
  playerContainer.style.display = 'none';
  playerContainer.setAttribute('aria-hidden', 'true');
  linkElement.setAttribute('aria-expanded', 'false');
  
  // Remove body padding when player is hidden
  document.body.classList.remove('has-audio-player');
}

function createCustomAudioPlayer(container, artistName, trackName, originalUrl, embedUrl) {
  // Default player styling
  let playerStyle = `width: 100%; border: none; transition: opacity 0.2s ease; opacity: 0.95;`;
  let embedHtml = '';
  
  // Special handling for SoundCloud to better match the site theme
  if (originalUrl.includes('soundcloud.com')) {
    const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
    
    // Add class to container for additional styling
    if (isDarkMode) {
      container.classList.add('soundcloud-dark');
    }
    
    // Use a more compact SoundCloud embed (visual=false, smaller height)
    embedHtml = `
      <iframe 
        src="${embedUrl}"
        frameborder="0" 
        allow="autoplay; encrypted-media" 
        allowfullscreen
        style="${playerStyle}; height: 80px;"
        title="Music player for ${artistName}'s ${trackName}"
        onload="this.style.opacity='1'"
        class="soundcloud-embed"
      ></iframe>
    `;
  } else {
    // Default embed for other platforms
    embedHtml = `
      <iframe 
        src="${embedUrl}" 
        frameborder="0" 
        allow="autoplay; encrypted-media" 
        allowfullscreen
        style="${playerStyle}; height: 80px;"
        title="Music player for ${artistName}'s ${trackName}"
        onload="this.style.opacity='1'"
      ></iframe>
    `;
  }
  
  // Add close button to the player
  const playerHtml = `
    <div class="close-player" aria-label="Close player" role="button" tabindex="0">&times;</div>
    <div class="player-container">
      ${embedHtml}
    </div>
  `;
  
  container.innerHTML = playerHtml;
  
  // Add click event to close button
  const closeButton = container.querySelector('.close-player');
  if (closeButton) {
    closeButton.addEventListener('click', function() {
      const companionMusicLink = document.getElementById('companion-music-link');
      hidePlayer(container, companionMusicLink);
    });
    
    // Add keyboard support for the close button
    closeButton.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const companionMusicLink = document.getElementById('companion-music-link');
        hidePlayer(container, companionMusicLink);
      }
    });
  }
  
  // Add event listener to update dark mode for SoundCloud iframes
  if (originalUrl.includes('soundcloud.com')) {
    const observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        if (mutation.attributeName === 'data-theme') {
          updateSoundCloudTheme(container);
        }
      });
    });
    
    observer.observe(document.documentElement, { attributes: true });
  }
  
  // Add keyboard event for Escape key to close the player
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && container.style.display === 'block') {
      const companionMusicLink = document.getElementById('companion-music-link');
      hidePlayer(container, companionMusicLink);
    }
  });
}

function updateSoundCloudTheme(container) {
  const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
  const iframe = container.querySelector('iframe.soundcloud-embed');
  
  if (iframe) {
    let src = iframe.src;
    
    // Always use orange color
    src = src.replace(/color=%23[a-fA-F0-9]{6}/, 'color=%23ff5500');
    
    if (isDarkMode) {
      container.classList.add('soundcloud-dark');
    } else {
      container.classList.remove('soundcloud-dark');
    }
    
    iframe.src = src;
  }
}

function loadStyles() {
  // Check if our styles are already loaded
  if (!document.getElementById('audio-player-styles')) {
    // First try to load the CSS file
    const link = document.createElement('link');
    link.id = 'audio-player-styles';
    link.rel = 'stylesheet';
    
    // Use the location origin to determine the base path
    const baseUrl = document.querySelector('meta[name="baseurl"]')?.getAttribute('content') || '';
    link.href = baseUrl + '/assets/js/audio-player.css';
    
    document.head.appendChild(link);
    
    // Fallback inline styles in case the CSS file fails to load
    link.onerror = function() {
      const style = document.createElement('style');
      style.id = 'audio-player-styles';
      style.textContent = `
        .audio-player {
          display: none;
          position: fixed;
          bottom: 0;
          left: 0;
          right: 0;
          width: 100%;
          background: rgba(245, 245, 245, 0.95);
          backdrop-filter: blur(10px);
          border-top: 1px solid rgba(0, 0, 0, 0.1);
          padding: 5px 5%;
          z-index: 1000;
          box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
          transition: transform 0.3s ease, opacity 0.3s ease;
          box-sizing: border-box;
          opacity: 1;
        }
        
        .audio-player.dark-theme {
          background: rgba(30, 30, 30, 0.95);
          border-top: 1px solid rgba(255, 255, 255, 0.1);
          box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.2);
        }
        
        /* When scrolling down, make player more transparent */
        .audio-player.scrolled-down {
          opacity: 0.6;
        }
        
        .companion-music-title {
          color: inherit !important;
          cursor: pointer;
          font-weight: inherit;
          transition: all 0.2s ease;
          text-decoration: underline !important;
          text-decoration-style: dotted !important;
          text-decoration-thickness: 1px !important;
          text-underline-offset: 2px !important;
          background: transparent !important;
          display: inline-block;
          padding: 0 !important;
          border: none !important;
          outline: none !important;
          -webkit-tap-highlight-color: transparent !important;
        }
        
        .companion-music-title:hover,
        .companion-music-title:active,
        .companion-music-title:focus,
        .companion-music-title:visited {
          opacity: 0.85;
          background: transparent !important;
          color: inherit !important;
          text-decoration: underline !important;
          text-decoration-style: solid !important;
          border: none !important;
          outline: none !important;
          box-shadow: none !important;
        }
        
        .dark-theme .companion-music-title,
        .dark-theme .companion-music-title:hover,
        .dark-theme .companion-music-title:active,
        .dark-theme .companion-music-title:focus,
        .dark-theme .companion-music-title:visited {
          background: transparent !important;
          color: inherit !important;
          text-decoration: underline !important;
          border: none !important;
          outline: none !important;
          box-shadow: none !important;
        }
        
        .dark-theme .companion-music-title {
          text-decoration-style: dotted !important;
        }
        
        .dark-theme .companion-music-title:hover {
          text-decoration-style: solid !important;
        }
        
        .player-container {
          display: flex;
          align-items: center;
          justify-content: center;
          position: relative;
          overflow: hidden;
          margin: 0 auto;
          max-width: 100%;
          width: 100%;
        }
        
        .close-player {
          position: absolute;
          top: 5px;
          right: 15px;
          cursor: pointer;
          font-size: 18px;
          line-height: 1;
          color: rgba(0, 0, 0, 0.5);
          transition: color 0.2s ease;
          z-index: 1001;
        }
        
        .close-player:hover {
          color: rgba(0, 0, 0, 0.8);
        }
        
        .dark-theme .close-player {
          color: rgba(255, 255, 255, 0.5);
        }
        
        .dark-theme .close-player:hover {
          color: rgba(255, 255, 255, 0.8);
        }
        
        body.has-audio-player {
          padding-bottom: 100px;
        }
        
        .music-link {
          color: inherit;
          text-decoration: none;
          border-bottom: 1px dotted;
          padding-bottom: 1px;
        }
        .music-link:hover {
          border-bottom: 1px solid;
        }
      `;
      document.head.appendChild(style);
    };
  }
}

function handlePlayerScrollOpacity() {
  let lastScrollTop = 0;
  const audioPlayer = document.getElementById('audio-player');
  
  // Skip if no audio player is present
  if (!audioPlayer) return;
  
  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Determine scroll direction
    if (scrollTop > lastScrollTop) {
      // Scrolling down - make more transparent
      audioPlayer.classList.add('scrolled-down');
    } else {
      // Scrolling up - reset opacity
      audioPlayer.classList.remove('scrolled-down');
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For Mobile or negative scrolling
  }, { passive: true }); // Use passive listener for better scroll performance
} 