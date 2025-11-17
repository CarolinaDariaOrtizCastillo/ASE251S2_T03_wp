document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (!form) return;

    // Obtenemos los campos y los mensajes de error
    const telefonoInput = document.getElementById("telefono_contacto");
    const errorTelefono = document.getElementById("error_telefono");

    form.addEventListener("submit", (e) => {
        let isValid = true; 
        
        // 1. Validar Celular del Representante
        if (telefonoInput && errorTelefono) {
            const telefono = telefonoInput.value.trim();
            if (telefono.length !== 9 || isNaN(telefono)) {
                isValid = false;
                errorTelefono.style.display = "block"; // Muestra el error
            } else {
                errorTelefono.style.display = "none"; // Oculta el error si es correcto
            }
        }

        // 3. Si algo es inválido, previene el envío
        if (!isValid) {
            e.preventDefault();
        }
    });

    // Ocultar error mientras el usuario escribe
    if (telefonoInput && errorTelefono) {
        telefonoInput.addEventListener("input", () => {
            if (errorTelefono.style.display === "block") {
                errorTelefono.style.display = "none";
            }
        });
    }
});