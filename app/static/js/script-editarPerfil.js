let cropper;
let fotoOriginal = "";

const modal = document.getElementById("modalPerfil");
const imageToCrop = document.getElementById('image-to-crop');
const inputFoto = document.getElementById('input-foto');
const croppedDataInput = document.getElementById('cropped_data');
const avatarPrincipal = document.querySelector('.avatar');
const wrapperEditor = document.getElementById('wrapper-editor');
const mensajeExito = document.getElementById('mensaje-exito');

function abrirModal() {
    fotoOriginal = avatarPrincipal.src;
    modal.style.display = "block";
}

function cerrarModal() {
    modal.style.display = "none";
    if (!croppedDataInput.value) avatarPrincipal.src = fotoOriginal;
    if (cropper) { cropper.destroy(); cropper = null; }
    inputFoto.value = "";
    wrapperEditor.style.display = 'none';
    mensajeExito.style.display = 'none';
}

inputFoto.addEventListener('change', function (e) {
    const files = e.target.files;
    if (files && files.length > 0) {
        const reader = new FileReader();
        reader.onload = function (event) {
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
    cropper.destroy();
    cropper = null;
}

window.onclick = function(event) {
    if (event.target == modal) cerrarModal();
}