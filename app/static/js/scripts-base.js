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

    // Mensaje flash
    function crearFlashDinamico(mensaje, categoria = 'success') {
        const container = document.getElementById('flash-container');
        
        if (!container) {
            const nuevoContenedor = document.createElement('div');
            nuevoContenedor.id = 'flash-container';
            nuevoContenedor.className = 'flash-global-wrapper';
            document.body.appendChild(nuevoContenedor);
        }

        const flashDiv = document.createElement('div');
        flashDiv.className = `flash-message alert-${categoria}`;
        
        flashDiv.innerHTML = `
            <div class="flash-icon">
                <i class="fas ${categoria === 'success' ? 'fa-check-circle' : 'fa-exclamation-triangle'}"></i>
            </div>
            <div class="flash-text">${mensaje}</div>
            <button class="flash-close" onclick="this.parentElement.remove()">×</button>
        `;

        document.getElementById('flash-container').appendChild(flashDiv);

        // Auto-eliminación
        setTimeout(() => {
            flashDiv.style.animation = "fadeOut 0.5s forwards";
            setTimeout(() => flashDiv.remove(), 500);
        }, 5000);
    }

    setInterval(() => {
        fetch('/home/recompensa-tiempo', { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                crearFlashDinamico(data.message, 'success');
                console.log(`Sistema: +${data.puntos} orbes sumados.`);
            }
        })
        .catch(err => console.error("Error en sistema de recompensa:", err));
    }, 300000); // 5 minutos
});