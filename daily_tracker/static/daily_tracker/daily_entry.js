function selectMood(value, event) {
    document.getElementById('id_mood').value = value;
    
    document.querySelectorAll('.mood-button').forEach(b => {
        b.style.filter = '';
    });

    event.currentTarget.style.filter = 'brightness(0.9)'; 
}