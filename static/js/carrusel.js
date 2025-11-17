
const carousel = document.querySelector(".carousel-inner");
const totalSlides = document.querySelectorAll(".carousel-item").length;
let index = 0;

function updateCarousel() {
    carousel.style.transform = `translateX(-${index * 100}%)`;
}

function nextSlide() {
    index = (index + 1) % totalSlides;
    updateCarousel();
}

function prevSlide() {
    index = (index - 1 + totalSlides) % totalSlides;
    updateCarousel();
}

document.getElementById("next").addEventListener("click", nextSlide);
document.getElementById("prev").addEventListener("click", prevSlide);

// Cambio automático cada 3 segundos
setInterval(nextSlide, 3000);

