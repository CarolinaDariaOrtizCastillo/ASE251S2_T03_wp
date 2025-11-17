document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".formulario");
    
    const celularEstInput = document.getElementById("celular_est");
    const celularApodInput = document.getElementById("celular_apod");
    
    const errorCelularEst = document.getElementById("error_celular_est");
    const errorCelularApod = document.getElementById("error_celular_apod");

    form.addEventListener("submit", (e) => {
        let isValid = true;

        const celularEst = celularEstInput.value.trim();
        if (celularEst.length !== 9 || isNaN(celularEst)) {
            isValid = false;
            errorCelularEst.style.display = "block";
        } else {
            errorCelularEst.style.display = "none";
        }

        const celularApod = celularApodInput.value.trim();
        if (celularApod.length !== 9 || isNaN(celularApod)) {
            isValid = false;
            errorCelularApod.style.display = "block";
        } else {
            errorCelularApod.style.display = "none";
        }

        if (!isValid) {
            e.preventDefault();
        }
    });

    celularEstInput.addEventListener("input", () => {
        errorCelularEst.style.display = "none";
    });

    celularApodInput.addEventListener("input", () => {
        errorCelularApod.style.display = "none";
    });
});
