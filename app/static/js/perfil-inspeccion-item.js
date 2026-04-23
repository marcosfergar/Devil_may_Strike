function inspeccionarItem(nombre, descripcion, imagenSrc) {
    const wrapper = document.querySelector('.perfil-container');
    const img = document.getElementById('inspeccion-img');
    const title = document.getElementById('inspeccion-nombre');
    const desc = document.getElementById('inspeccion-desc');

    // Cambiar contenido
    img.src = imagenSrc;
    title.innerText = nombre.toUpperCase();
    desc.innerText = descripcion;

    // Mostrar columna
    wrapper.classList.add('show-details');
    
    // Sonido opcional
    // playSound('click_metalico.mp3');
}

function cerrarInspeccion() {
    document.querySelector('.re4-perfil-wrapper').classList.remove('show-details');
}