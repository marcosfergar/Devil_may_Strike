document.addEventListener('DOMContentLoaded', () => {
    const btnVergil = document.getElementById('btn-vergil');
      
        if (localStorage.getItem('theme') === 'vergil') {
            document.body.classList.add('mode-vergil');
        }

        btnVergil.addEventListener('click', () => {
            document.body.classList.toggle('mode-vergil');
            
            if (document.body.classList.contains('mode-vergil')) {
                localStorage.setItem('theme', 'vergil');
            } else {
                localStorage.setItem('theme', 'dante');
            }
        });
});