let cropper;
let fotoOriginal = "";

// Elementos Globales
const modal = document.getElementById("modalPerfil");
const imageToCrop = document.getElementById('image-to-crop');
const inputFoto = document.getElementById('input-foto');
const croppedDataInput = document.getElementById('cropped_data');
const avatarPrincipal = document.querySelector('.avatar');
const wrapperEditor = document.getElementById('wrapper-editor');
const mensajeExito = document.getElementById('mensaje-exito');
const inventarioSelector = document.getElementById('inventario-avatares-selector');
const btnConfirmarInv = document.getElementById('btn-confirmar-inventario');
const labelArchivo = document.getElementById('label-archivo');

function abrirModal() {
    fotoOriginal = avatarPrincipal.src;
    modal.style.display = "block";
}

function cerrarModal() {
    modal.style.display = "none";
    if (cropper) { cropper.destroy(); cropper = null; }
    
    // Resetear visibilidad de elementos
    inputFoto.value = "";
    wrapperEditor.style.display = 'none';
    mensajeExito.style.display = 'none';
    if (inventarioSelector) {
        inventarioSelector.style.display = 'block';
        document.querySelector('.grid-scroll').style.opacity = '1';
    }
    labelArchivo.style.display = 'block';
    if (btnConfirmarInv) btnConfirmarInv.style.display = 'none';
    
    // Si no confirmó nada, restaurar foto
    if (!croppedDataInput.value) avatarPrincipal.src = fotoOriginal;
}

// Lógica para SUBIR FOTO NUEVA
inputFoto.addEventListener('change', function (e) {
    const files = e.target.files;
    if (files && files.length > 0) {
        const reader = new FileReader();
        reader.onload = function (event) {
            if (inventarioSelector) inventarioSelector.style.display = 'none';
            
            imageToCrop.src = event.target.result;
            wrapperEditor.style.display = 'block';
            mensajeExito.style.display = 'none';
            
            if (cropper) cropper.destroy();
            cropper = new Cropper(imageToCrop, {
                aspectRatio: 1,
                viewMode: 1,
                autoCropArea: 1
            });
        };
        reader.readAsDataURL(files[0]);
    }
});

function confirmarRecorte() {
    if (!cropper) return;
    const canvas = cropper.getCroppedCanvas({ width: 400, height: 400 });
    const dataURL = canvas.toDataURL('image/jpeg');

    croppedDataInput.value = dataURL;
    avatarPrincipal.src = dataURL;

    wrapperEditor.style.display = 'none';
    mensajeExito.style.display = 'block';
    mensajeExito.innerText = "Foto recortada con exito";
    cropper.destroy();
    cropper = null;
}

// Lógica para SELECCIONAR DEL INVENTARIO
document.querySelectorAll('.radio-inventario').forEach(radio => {
    radio.addEventListener('change', function() {
        if (this.checked) {
            btnConfirmarInv.style.display = 'block';
            // Al seleccionar inventario, nos aseguramos de limpiar cualquier recorte previo
            if (cropper) { cropper.destroy(); cropper = null; wrapperEditor.style.display = 'none'; }
        }
    });
});

if (btnConfirmarInv) {
    btnConfirmarInv.addEventListener('click', function() {
        const seleccionada = document.querySelector('.radio-inventario:checked');
        if (seleccionada) {
            document.getElementById('cropped_data').value = seleccionada.value;
            avatarPrincipal.src = "/static/uploads/tienda/" + seleccionada.value;
            mensajeExito.style.display = 'block';
            mensajeExito.innerText = "¡ALMA EQUIPADA! HAZ CLIC EN 'GUARDAR CAMBIOS'.";
        }
    });
}

document.addEventListener('submit', function (e) {
    
    if (e.target && e.target.classList.contains('form-perfil')) {
        e.preventDefault(); 
        
        const form = e.target;
        const formData = new FormData(form);
        const url = form.getAttribute('action');

        fetch(url, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error('Error 404 o servidor no encontrado');
            return response.json();
        })
        .then(data => {
            if (data.success) {
                crearFlashDinamico(data.message, 'success');
                cerrarModal();
            } else {
                crearFlashDinamico(data.message, 'error');
            }
        })
        .catch(error => {
            console.error('Error en la petición:', error);
        });
    }
});

window.onclick = function(event) {
    if (event.target == modal) cerrarModal();
}
