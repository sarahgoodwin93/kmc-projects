gsap.registerPlugin(ScrollTrigger);

window.addEventListener('DOMContentLoaded', () => {
  const tl = gsap.timeline();

  tl.to(".hero-title", {
    opacity: 1,
    y: 0,
    duration: 1,
    ease: "power3.out"
  }).to(".hero-subtitle", {
    opacity: 1,
    y: 0,
    duration: 1,
    ease: "power3.out"
  }, "-=0.5").to(".hero-button", {
    opacity: 1,
    y: 0,
    duration: 1,
    ease: "power3.out"
  }, "-=0.5");
});
