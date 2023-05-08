// Smooth scrolling on all links with the '#' symbol
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Text animation on scroll
const animatedElements = document.querySelectorAll('.animate-on-scroll');

window.addEventListener('scroll', () => {
  animatedElements.forEach(element => {
    if (isInViewport(element)) {
      element.classList.add('animate');
    }
  });
});

function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  const windowHeight = (window.innerHeight || document.documentElement.clientHeight);
  const windowWidth = (window.innerWidth || document.documentElement.clientWidth);

  const vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0);
  const horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0);

  return (vertInView && horInView);
}

window.onload = function() {
    var animation = document.getElementById('animation');
    animation.addEventListener('load', function() {
        var svgDoc = animation.contentDocument;
        var yourAnimation = svgDoc.getElementById('your-animation');
        yourAnimation.beginElement();
    });
};

