document.addEventListener('DOMContentLoaded', () => {
    const imgDante = document.querySelector('.img-dante');
    const imgVergil = document.querySelector('.img-vergil');
    const body = document.body;

    // Cargar preferencia guardada
    if (localStorage.getItem('theme') === 'vergil') {
        body.classList.add('mode-vergil');
    }

    // Si clickas en Vergil -> Activa su modo
    imgVergil.addEventListener('click', () => {
        if (!body.classList.contains('mode-vergil')) {
            body.classList.add('mode-vergil');
            localStorage.setItem('theme', 'vergil');
            console.log("Power... I need more power!");
        }
    });

    // Si clickas en Dante -> Vuelve al modo normal
    imgDante.addEventListener('click', () => {
        if (body.classList.contains('mode-vergil')) {
            body.classList.remove('mode-vergil');
            localStorage.setItem('theme', 'dante');
            console.log("Let's rock, baby!");
        }
    });
});