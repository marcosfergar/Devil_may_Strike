document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const usuario = form.querySelector('[name="usuario"]').value;
        const passwd = form.querySelector('[name="passwd"]').value;
        const passwd2 = form.querySelector('[name="passwd2"]').value;

        fetch('/register-ajax', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ usuario, passwd, passwd2 })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect;
            } else {
                crearFlashDinamico(data.message, 'error');
            }
        })
        .catch(() => crearFlashDinamico('Error de conexión.', 'error'));
    });
});