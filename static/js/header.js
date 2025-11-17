// Espera a que todo el contenido del HTML esté cargado
document.addEventListener('DOMContentLoaded', () => {
    
    // Selecciona el botón de hamburguesa
    const toggleButton = document.getElementById('menu-toggle');
    // Selecciona el menú de navegación
    const navMenu = document.getElementById('nav-menu');

    // Comprueba que ambos elementos existan
    if (toggleButton && navMenu) {
        
        // Añade un "escuchador" para el evento 'click' en el botón
        toggleButton.addEventListener('click', () => {
            
            // 1. Alterna la clase 'open' en el menú.
            //    El CSS (.menu.open) se encarga de mostrarlo u ocultarlo.
            navMenu.classList.toggle('open');

            // 2. Cambia el ícono del botón (de barras a X y viceversa)
            const icon = toggleButton.querySelector('i');
            
            if (navMenu.classList.contains('open')) {
                // Si el menú AHORA está abierto, muestra la 'X'
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                // Si el menú AHORA está cerrado, muestra las 'barras'
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }
});