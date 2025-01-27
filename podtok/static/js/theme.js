function getPreferredTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        return savedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

// Apply theme to document
function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    // Update button icon
    const themeIcon = document.getElementById('theme-icon');
    if (themeIcon) {
        if (theme === 'dark') {
            themeIcon.className = 'fas fa-sun'; // Sun icon for dark theme
        } else {
            themeIcon.className = 'fas fa-moon'; // Moon icon for light theme
        }
    }
}

// Toggle theme
function toggleTheme() {
    const currentTheme = localStorage.getItem('theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    applyTheme(newTheme);
}

// Initialize theme
document.addEventListener('DOMContentLoaded', () => {
    // Apply initial theme
    applyTheme(getPreferredTheme());
    
    // Add click handler to theme toggle button
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
});