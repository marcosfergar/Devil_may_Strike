document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("game-audio");
    const playlistContainer = document.getElementById("playlist-items");
    const trackNameDisplay = document.getElementById("track-name");
    const playPauseBtn = document.getElementById("play-pause");
    const musicIcon = document.getElementById("music-icon");
    const widget = document.getElementById("music-widget");
    const volumeControl = document.getElementById("volume-control");

    let playlist = [];
    let currentTrackIndex = 0;

    function cargarMusica() {
        fetch('/home/mis-canciones')
            .then(response => response.json())
            .then(data => {
                playlist = data;
                if (playlist.length > 0) {
                    const savedIndex = localStorage.getItem("music_index");
                    if (savedIndex !== null && playlist[savedIndex]) {
                        currentTrackIndex = parseInt(savedIndex);
                    }
                    
                    renderPlaylist();
                    
                    const savedVol = localStorage.getItem("music_volume");
                    if (savedVol !== null) {
                        audio.volume = savedVol;
                        volumeControl.value = savedVol;
                    }

                    if (localStorage.getItem("music_playing") === "true") {
                        prepararCancion();
                        audio.currentTime = localStorage.getItem("music_time") || 0;
                        audio.play().catch(() => {
                            console.log("Reproducción automática esperando interacción del usuario.");
                            playPauseBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
                        });
                    }
                } else {
                    trackNameDisplay.innerText = "Sin música en inventario";
                    playlistContainer.innerHTML = "<li class='track-item'>Visita la tienda</li>";
                }
            })
            .catch(err => console.error("Error cargando música:", err));
    }

    function renderPlaylist() {
        playlistContainer.innerHTML = "";
        playlist.forEach((track, index) => {
            const li = document.createElement("li");
            li.classList.add("track-item");
            if (index === currentTrackIndex) li.classList.add("active-track");
            
            li.innerText = track.name;
            li.addEventListener("click", (e) => {
                e.stopPropagation();
                currentTrackIndex = index;
                loadAndPlay();
            });
            playlistContainer.appendChild(li);
        });
    }

    function prepararCancion() {
        if (playlist.length === 0) return;
        audio.src = playlist[currentTrackIndex].src;
        trackNameDisplay.innerText = playlist[currentTrackIndex].name;
        renderPlaylist();
    }

    function loadAndPlay() {
        prepararCancion();
        audio.play();
        playPauseBtn.innerHTML = '<i class="fa-solid fa-pause"></i>';
    }

    playPauseBtn.addEventListener("click", (e) => {
        e.stopPropagation(); // IMPORTANTE: evita que el widget se cierre
        if (audio.paused) {
            if (!audio.src) prepararCancion();
            audio.play();
            playPauseBtn.innerHTML = '<i class="fa-solid fa-pause"></i>';
        } else {
            audio.pause();
            playPauseBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
        }
    });

    document.getElementById("next-track").addEventListener("click", (e) => {
        e.stopPropagation();
        if (playlist.length === 0) return;
        currentTrackIndex = (currentTrackIndex + 1) % playlist.length;
        loadAndPlay();
    });

    document.getElementById("prev-track").addEventListener("click", (e) => {
        e.stopPropagation();
        if (playlist.length === 0) return;
        currentTrackIndex = (currentTrackIndex - 1 + playlist.length) % playlist.length;
        loadAndPlay();
    });

    volumeControl.addEventListener("click", (e) => e.stopPropagation());
    volumeControl.addEventListener("input", (e) => {
        audio.volume = e.target.value;
        localStorage.setItem("music_volume", e.target.value);
    });

    audio.onended = () => {
        currentTrackIndex = (currentTrackIndex + 1) % playlist.length;
        loadAndPlay();
    };

    if (musicIcon && widget) {
        musicIcon.addEventListener("click", (e) => {
            e.stopPropagation();
            widget.classList.toggle("show");
        });

        widget.addEventListener("click", (e) => {
            e.stopPropagation();
        });

        document.addEventListener("click", () => {
            widget.classList.remove("show");
        });
    }

    audio.onplay = () => musicIcon.querySelector("i").classList.add("spinning");
    audio.onpause = () => musicIcon.querySelector("i").classList.remove("spinning");

    window.addEventListener("beforeunload", () => {
        localStorage.setItem("music_time", audio.currentTime);
        localStorage.setItem("music_playing", !audio.paused);
        localStorage.setItem("music_index", currentTrackIndex);
    });

    cargarMusica();
});