document.addEventListener("DOMContentLoaded", () => {
    const btnInvitado = document.getElementById("jugarInvitado");

    if (btnInvitado) {
        btnInvitado.addEventListener("click", () => {
            // Leemos la URL que Flask inyectó en el HTML
            const urlDestino = btnInvitado.getAttribute("data-url");
            
            if (urlDestino) {
                window.location.href = urlDestino;
            } else {
                console.error("Error: No se encontró la ruta de invitado.");
            }
        });
    }

    const btnRegistro = document.getElementById("btnRegistro");

    if (btnRegistro) {
        btnRegistro.addEventListener("click", () => {
            window.location.href = btnRegistro.getAttribute("data-url");
        });
    }

    const btnLogin = document.getElementById("iniciarSesion");
    
    if (btnLogin) {
        btnLogin.addEventListener("click", () => {
            console.log("Abriendo menú de login...");
        });
    }
});