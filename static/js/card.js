
// Seleccionar todas las cards
const cards = document.querySelectorAll(".card");
let currentCard = 0;

// Mostrar solo una card a la vez (si quieres que roten como slider)
function showCard(index) {
  cards.forEach((card, i) => {
    card.style.display = i === index ? "block" : "none";
  });
}

// Rotación automática cada 4 segundos
function autoRotateCards() {
  currentCard = (currentCard + 1) % cards.length;
  showCard(currentCard);
}

// Iniciar
if (cards.length > 0) {
  showCard(currentCard);
  setInterval(autoRotateCards, 4000);
}

// Efecto hover con escala y sombra
cards.forEach(card => {
  card.addEventListener("mouseenter", () => {
    card.style.transform = "scale(1.05)";
    card.style.boxShadow = "0 8px 20px rgba(0,0,0,0.2)";
    card.style.transition = "all 0.3s ease";
  });
  card.addEventListener("mouseleave", () => {
    card.style.transform = "scale(1)";
    card.style.boxShadow = "0 4px 10px rgba(0,0,0,0.1)";
  });
});
