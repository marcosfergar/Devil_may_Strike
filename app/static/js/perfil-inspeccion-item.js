function inspeccionarItem(nombre, descripcion, imagenSrc) {
    const contenedor = document.querySelector('.perfil-container');
    const imgElement = document.getElementById('inspeccion-img');
    const nombreElement = document.getElementById('inspeccion-nombre');
    const descElement = document.getElementById('inspeccion-desc');

    imgElement.src = imagenSrc;
    nombreElement.innerText = nombre.toUpperCase();
    
    descElement.innerText = descripcion !== "None" ? descripcion : "Un objeto misterioso obtenido en combate.";

    contenedor.classList.add('show-details');
}

function cerrarInspeccion() {
    const contenedor = document.querySelector('.perfil-container');
    contenedor.classList.remove('show-details');
}