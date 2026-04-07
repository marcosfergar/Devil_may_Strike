document.addEventListener("DOMContentLoaded", () => {
    // 1. Referenciamos el botón
    const btnInvitado = document.getElementById("jugarInvitado");

    // 2. Añadimos el "escuchador" de eventos
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
    
    // Puedes hacer lo mismo para el botón de Iniciar Sesión
    const btnLogin = document.getElementById("iniciarSesion");
    if (btnLogin) {
        btnLogin.addEventListener("click", () => {
            console.log("Abriendo menú de login...");
            // Aquí tu lógica para el login
        });
    }
});