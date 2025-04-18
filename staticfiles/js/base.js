// Register GSAP plugins
gsap.registerPlugin(ScrollTrigger);

// Log when base.js is loaded
console.log("🚀 base.js loaded");

// Select all text elements inside the parallax section
const texts = gsap.utils.toArray('.parallax-text');

// Animate each text element
texts.forEach((text, i) => {
  gsap.fromTo(
    text,
    {
      opacity: 0,
      y: 50
    },
    {
      opacity: 1,
      y: 0,
      scrollTrigger: {
        trigger: text,
        start: "top 70%",
        end: "top 40%",
        scrub: true,
      }
    }
  );
});
