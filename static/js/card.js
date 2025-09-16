
document.addEventListener("DOMContentLoaded", () => {
  const botones = document.querySelectorAll(".ver-mas-btn");
  botones.forEach((btn) => {
    btn.addEventListener("click", () => {
      const info = btn.closest("div").nextElementSibling;
      info.classList.toggle("hidden");
      btn.textContent = info.classList.contains("hidden") ? "Ver más" : "Ocultar";
    });
  });
});
