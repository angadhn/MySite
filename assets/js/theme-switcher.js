const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');

// Handle image switching for theme changes
function updateImages(isDark) {
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

// Apply theme changes
function applyTheme(themeName) {
    document.documentElement.setAttribute('data-theme', themeName);
    toggleSwitch.checked = themeName === 'dark';
    updateImages(themeName === 'dark');
}

// Handle manual theme switching
function switchTheme(e) {
    const isDark = e.target.checked;
    const themeName = isDark ? 'dark' : 'light';
    localStorage.setItem('theme', themeName);
    applyTheme(themeName);
}

// Listen for toggle switch changes
toggleSwitch.addEventListener('change', switchTheme, false);

// Check system theme preference
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

// Initialize theme
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme');
    
    if (savedTheme) {
        applyTheme(savedTheme);
    } else {
        const systemTheme = prefersDarkScheme.matches ? 'dark' : 'light';
        applyTheme(systemTheme);
    }
}

// Listen for system theme changes
prefersDarkScheme.addListener((e) => {
    // Only apply system theme changes if user hasn't set a preference
    if (!localStorage.getItem('theme')) {
        applyTheme(e.matches ? 'dark' : 'light');
    }
});

// Initialize theme when page loads
document.addEventListener('DOMContentLoaded', () => {
    initializeTheme();
}); 