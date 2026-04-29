document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const imgVergil = document.querySelector('.img-vergil');
    const imgDante = document.querySelector('.img-dante');

    const permisoVergil = (typeof HAS_VERGIL !== 'undefined') ? HAS_VERGIL : false;

    if (imgVergil) {
        imgVergil.addEventListener('click', () => {
            if (!permisoVergil) {
                alert("You need more power! Cómpralo en la tienda.");
                return;
            }
            body.classList.add('mode-vergil');
            localStorage.setItem('theme', 'vergil');
            console.log("Motivation active");
        });
    }

    if (imgDante) {
        imgDante.addEventListener('click', () => {
            body.classList.remove('mode-vergil');
            localStorage.setItem('theme', 'dante');
            console.log("Back to red");
        });
    }
});