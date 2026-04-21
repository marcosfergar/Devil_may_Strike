// La secuencia de teclas: Arriba, Arriba, Abajo, Abajo
const secretCode = ['ArrowUp', 'ArrowUp', 'ArrowDown'];
let inputSequence = [];

document.addEventListener('keydown', (e) => {
    inputSequence.push(e.key);
    
    // Mantener solo las últimas N pulsaciones
    inputSequence = inputSequence.slice(-secretCode.length);

    // Comprobar si la secuencia coincide
    if (inputSequence.join('') === secretCode.join('')) {
        activarTruco();
    }
});

function activarTruco() {
    fetch('/tienda/truco-orbes', { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => {
        if (!response.ok) {
            // Esto nos dirá qué está pasando realmente si hay un error
            throw new Error('Error en el servidor: ' + response.status);
        }
        return response.json();
    })
    .then(data => {
        alert("🔥 JACKPOT 🔥");
        location.reload();
    })
    .catch(err => console.error("Error detallado:", err));
}