// Add active class to the current navigation menu item
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll('nav ul li a');

navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
    }
});
//This code adds an "active" class to the current navigation menu item based on the current URL path.