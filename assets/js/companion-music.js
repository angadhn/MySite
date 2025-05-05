document.addEventListener('DOMContentLoaded', function() {
  const companionMusicLink = document.getElementById('companion-music-link');
  
  if (companionMusicLink) {
    const url = companionMusicLink.getAttribute('data-url');
    
    if (url) {
      try {
        const urlObj = new URL(url);
        
        // Initialize variables
        let artistName = '';
        let trackName = '';
        let isValid = false;
        
        // Handle SoundCloud links
        if (urlObj.hostname.includes('soundcloud.com')) {
          const urlParts = urlObj.pathname.split('/').filter(part => part);
          
          if (urlParts.length >= 2) {
            artistName = urlParts[0].replace(/-/g, ' ');
            trackName = urlParts[1].replace(/-/g, ' ');
            isValid = true;
          }
        }
        // Handle Spotify links
        else if (urlObj.hostname.includes('spotify.com')) {
          // Example: https://open.spotify.com/track/1234567890
          if (urlObj.pathname.includes('/track/')) {
            // For Spotify, we can't easily get artist and track from URL
            // Instead, use a generic message
            companionMusicLink.innerHTML = `I think this piece is best paired with <a href="${url}" target="_blank" class="music-link">this track on Spotify</a>`;
            companionMusicLink.style.display = 'block';
            return;
          }
        }
        // Handle YouTube links
        else if (urlObj.hostname.includes('youtube.com') || urlObj.hostname.includes('youtu.be')) {
          // For YouTube, we can't easily get artist and track from URL
          companionMusicLink.innerHTML = `I think this piece is best paired with <a href="${url}" target="_blank" class="music-link">this track on YouTube</a>`;
          companionMusicLink.style.display = 'block';
          return;
        }
        
        if (isValid) {
          // Convert to title case
          const formattedArtist = artistName.split(' ')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
            
          const formattedTrack = trackName.split(' ')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
          
          // Display the message
          companionMusicLink.innerHTML = `I think this piece is best paired with <a href="${url}" target="_blank" class="music-link">${formattedArtist}'s "${formattedTrack}"</a>`;
          companionMusicLink.style.display = 'block';
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
  
  // Add styling for music links
  const style = document.createElement('style');
  style.textContent = `
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
}); 