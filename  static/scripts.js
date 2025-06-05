// Load particles.js
particlesJS.load('particles-js', 'https://cdn.jsdelivr.net/gh/VincentGarreau/particles.js/particles.json', function() {
  console.log('Particles.js loaded.');
});

// Load a quote
function loadQuote() {
  fetch('/quote')
    .then(response => response.json())
    .then(data => {
      document.getElementById('quote').textContent = data.quote;
    });
}

// Optional: load one quote on page load
document.addEventListener('DOMContentLoaded', loadQuote);
