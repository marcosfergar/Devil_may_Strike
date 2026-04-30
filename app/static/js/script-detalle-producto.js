document.addEventListener('DOMContentLoaded', () => {

    // COMPRA DINÁMICA 
    const btnComprar = document.getElementById('btn-comprar');

    if (btnComprar) {
        btnComprar.addEventListener('click', () => {
            const productoId = btnComprar.getAttribute('data-producto-id');

            btnComprar.disabled = true;
            btnComprar.textContent = '...';

            fetch(`/tienda/comprar/${productoId}`, { method: 'POST' })
                .then(res => res.json())
                .then(data => {
                    if (data.success) {
                        crearFlashDinamico(data.message, 'success');

                        // Actualizar orbes en pantalla
                        const orbCount = document.getElementById('orb-count');
                        if (orbCount && data.nuevos_orbes !== undefined) {
                            orbCount.textContent = data.nuevos_orbes;
                        }

                        // Cambiar botón a "desbloqueado"
                        btnComprar.textContent = 'DESBLOQUEADO';
                        btnComprar.classList.add('owned');
                        // Se queda disabled
                    } else {
                        crearFlashDinamico(data.message, 'error');
                        btnComprar.disabled = false;
                        btnComprar.textContent = 'ADQUIRIR';
                    }
                })
                .catch(() => {
                    crearFlashDinamico('Error de conexión.', 'error');
                    btnComprar.disabled = false;
                    btnComprar.textContent = 'ADQUIRIR';
                });
        });
    }

    // COMENTARIO DINÁMICO
    const formComentario = document.getElementById('form-comentario');

    if (formComentario) {
        formComentario.addEventListener('submit', (e) => {
            e.preventDefault();

            const productoId = formComentario.getAttribute('data-producto-id');
            const input = document.getElementById('input-comentario');
            const texto = input.value.trim();

            if (!texto) {
                crearFlashDinamico('El comentario no puede estar vacío.', 'error');
                return;
            }

            fetch(`/tienda/producto/${productoId}/comentar`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ contenido: texto })
            })
                .then(res => res.json())
                .then(data => {
                    if (data.success) {
                        crearFlashDinamico(data.message, 'success');

                        const lista = document.querySelector('.lista-comentarios-compacta');
                        const sinRegistros = lista.querySelector('.no-com');
                        if (sinRegistros) sinRegistros.remove();

                        const hoy = new Date();
                        const fecha = `${String(hoy.getDate()).padStart(2,'0')}/${String(hoy.getMonth()+1).padStart(2,'0')}`;

                        const nuevoComentario = document.createElement('div');
                        nuevoComentario.className = 'comentario-item';
                        nuevoComentario.innerHTML = `
                            <div class="com-meta">
                                <span class="autor">${data.autor}</span>
                                <span class="fecha">${fecha}</span>
                            </div>
                            <p class="com-contenido">${data.contenido}</p>
                        `;
                        lista.appendChild(nuevoComentario);
                        nuevoComentario.scrollIntoView({ behavior: 'smooth' });

                        input.value = '';
                    } else {
                        crearFlashDinamico(data.message, 'error');
                    }
                })
                .catch(() => crearFlashDinamico('Error de conexión.', 'error'));
        });
    }
});