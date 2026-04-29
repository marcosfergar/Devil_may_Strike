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

    const btnTienda = document.getElementById("Tienda");

    if (btnTienda) {
        btnTienda.addEventListener("click", () => {
            window.location.href = btnTienda.getAttribute("data-url");
        });
    }

    const btnForo = document.getElementById("Foro");

    if (btnForo) {
        btnForo.addEventListener("click", () => {
            window.location.href = btnForo.getAttribute("data-url");
        });
    }

    // Lógica global para mensajes Flash
    document.addEventListener('DOMContentLoaded', () => {
        const messages = document.querySelectorAll('.flash-message');
        
        messages.forEach(msg => {
            setTimeout(() => {
                msg.style.animation = "fadeOut 0.5s forwards";
                setTimeout(() => msg.remove(), 500);
            }, 5000);
        });
    });

    setInterval(() => {
        fetch('/home/recompensa-tiempo', { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Solo dejamos un log para que tú sepas que funciona al probar
                console.log(`Sistema: +${data.puntos} orbes sumados con éxito.`);
            }
        })
        .catch(err => console.error("Error en sistema de recompensa:", err));
    }, 10000); // 5 minutos
});