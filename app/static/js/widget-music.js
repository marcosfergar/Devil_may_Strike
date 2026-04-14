document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("game-audio");
    const playlistContainer = document.getElementById("playlist-items");
    const trackNameDisplay = document.getElementById("track-name");

    const playlist = [
        { name: "Devils Never Cry", src: "/static/music/devils-never-cry.mp3" },
        { name: "Bury the Light", src: "/static/music/bury-the-light.mp3" },
        { name: "Devil Trigger", src: "/static/music/devil-trigger.mp3" }
    ];

    let currentTrackIndex = 0;

    // Función para renderizar la lista en el HTML
    function renderPlaylist() {
        playlistContainer.innerHTML = ""; // Limpiar
        playlist.forEach((track, index) => {
            const li = document.createElement("li");
            li.classList.add("track-item");
            if (index === currentTrackIndex) li.classList.add("active-track");
            
            li.innerText = track.name;
            li.addEventListener("click", () => {
                currentTrackIndex = index;
                loadAndPlay();
            });
            playlistContainer.appendChild(li);
        });
    }

    function loadAndPlay() {
        audio.src = playlist[currentTrackIndex].src;
        trackNameDisplay.innerText = playlist[currentTrackIndex].name;
        renderPlaylist(); // Actualizar cuál está activa
        audio.play();
        document.getElementById("play-pause").innerHTML = '<i class="fa-solid fa-pause"></i>';
    }

    // Inicializar la lista al cargar
    renderPlaylist();

    // Eventos de los botones (Next/Prev)
    document.getElementById("next-track").addEventListener("click", () => {
        currentTrackIndex = (currentTrackIndex + 1) % playlist.length;
        loadAndPlay();
    });

    document.getElementById("prev-track").addEventListener("click", () => {
        currentTrackIndex = (currentTrackIndex - 1 + playlist.length) % playlist.length;
        loadAndPlay();
    });
});