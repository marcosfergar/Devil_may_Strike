document.addEventListener("DOMContentLoaded", () => {
    const btnInvitado = document.getElementById("jugarInvitado");

    if (btnInvitado) {
        btnInvitado.addEventListener("click", () => {
            const urlDestino = btnInvitado.getAttribute("data-url");
            
            if (urlDestino) {
                window.location.href = urlDestino;
            } else {
                console.error("Error: No se encontró la ruta de invitado.");
            }
        });
    }
    const btnPerfil = document.getElementById("Perfil");

    if (btnPerfil) {
        btnPerfil.addEventListener("click", () => {
            window.location.href = btnPerfil.getAttribute("data-url");
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
            window.location.href = btnLogin.getAttribute("data-url");
        });
    }

    const btnLogout = document.getElementById("Logout");
    
    if (btnLogout) {
        btnLogout.addEventListener("click", () => {
            window.location.href = btnLogout.getAttribute("data-url");
        });
    }
    
    const btnBibliotecaDmc = document.getElementById("biblioteca-dmc");

    if (btnBibliotecaDmc) {
        btnBibliotecaDmc.addEventListener("click", () => {
            window.location.href = btnBibliotecaDmc.getAttribute("data-url");
        });
    }
});