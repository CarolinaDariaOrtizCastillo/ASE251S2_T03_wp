// Espera a que todo el contenido del HTML esté cargado
document.addEventListener('DOMContentLoaded', () => {
    
    // --- Lógica para la Animación al Hacer Scroll ---

    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    if (animatedElements.length > 0) {
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                
                // ESTA ES LA LÓGICA NUEVA:
                if (entry.isIntersecting) {
                    // 1. Si el elemento está en la pantalla, añade la clase
                    entry.target.classList.add('is-visible');
                } else {
                    // 2. Si el elemento sale de la pantalla, quita la clase
                    //    para que la animación pueda repetirse.
                    entry.target.classList.remove('is-visible');
                }
                
                // YA NO USAMOS 'observer.unobserve()'
            });
        }, {
            threshold: 0.1 // Se activa cuando el 10% del elemento es visible
        });

        animatedElements.forEach(el => {
            observer.observe(el);
        });
    }

    // --- (Aquí puedes agregar más JS que solo sea para la página de inicio) ---
});