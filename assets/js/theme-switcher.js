const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');

function switchTheme(e) {
    const isDark = e.target.checked;
    document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    
    // Handle theme-specific images
    document.querySelectorAll('img').forEach(img => {
        const currentSrc = img.getAttribute('src');
        if (currentSrc) {
            if (isDark && currentSrc.includes('_for_dark_theme')) {
                img.src = currentSrc.replace('_for_dark_theme', '_for_light_theme');
            } else if (!isDark && currentSrc.includes('_for_light_theme')) {
                img.src = currentSrc.replace('_for_light_theme', '_for_dark_theme');
            }
        }
    });
}

toggleSwitch.addEventListener('change', switchTheme, false);

// Check for saved theme preference and set initial images
const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
        // Set initial dark theme images
        document.querySelectorAll('img').forEach(img => {
            const currentSrc = img.getAttribute('src');
            if (currentSrc && currentSrc.includes('_for_dark_theme')) {
                img.src = currentSrc.replace('_for_dark_theme', '_for_light_theme');
            }
        });
    }
} 