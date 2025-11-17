document.addEventListener('DOMContentLoaded', () => {

    // 1. Selecciona los íconos de redes sociales
    // (Usaremos una clase 'social-icon-js' que añadiremos en el HTML)
    const socialIcons = document.querySelectorAll('.social-icon-js');

    if (socialIcons.length === 0) return;

    let currentIcon = 0;

    // 2. Función para animar un ícono
    function animateIcon() {
        // Quita la clase de todos por si acaso
        socialIcons.forEach(icon => icon.classList.remove('jiggle'));

        // Selecciona el ícono actual
        const icon = socialIcons[currentIcon];
        
        // Añade la clase 'jiggle' para activar la animación CSS
        icon.classList.add('jiggle');

        // Prepara el siguiente ícono
        currentIcon = (currentIcon + 1) % socialIcons.length;

        // Quita la clase después de que termine la animación (400ms)
        // para que pueda volver a animarse en el futuro.
        setTimeout(() => {
            icon.classList.remove('jiggle');
        }, 400);
    }

    // 3. Llama a la función cada 2 segundos (2000 milisegundos)
    setInterval(animateIcon, 2000);
});