let audio;

function playSound(soundfile) {
    if(audio) {
        audio.pause(); // Stop any playing sound
    }
    audio = new Audio(soundfile);
    audio.play();
}

function stopSound() {
    if(audio) {
        audio.pause();
        audio.currentTime = 0; // Reset audio to start position
    }
}