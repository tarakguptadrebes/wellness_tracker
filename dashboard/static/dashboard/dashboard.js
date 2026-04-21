document.addEventListener('DOMContentLoaded', () => {
    console.log("Dashboard script loaded!");

    const moodCanvas = document.getElementById('moodChart');
    if (moodCanvas) {
        const moodData = JSON.parse(moodCanvas.dataset.moods || "[]");
        const moodDates = JSON.parse(moodCanvas.dataset.dates || "[]");
        
        new Chart(moodCanvas, {
            type: 'line',
            data: {
                labels: moodDates,
                datasets: [{
                    label: 'Mood',
                    data: moodData,
                    borderColor: '#4f46e5',
                    tension: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: { 
                    y: { 
                        min: 1, 
                        max: 5,
                        ticks: {
                            stepSize: 1,
                            font: {
                                size: 20,
                            },
                            callback: function(value) {
                                const moodLabels = {
                                    1: '😭',
                                    2: '😢',
                                    3: '😐',
                                    4: '😊',
                                    5: '🤩',
                                };
                                return moodLabels[value] || value;
                            }
                        }
                    } 
                } 
            }
        });
    }

    const sleepCanvas = document.getElementById('sleepChart');
    if (sleepCanvas) {
        const sleepData = JSON.parse(sleepCanvas.dataset.sleeps || "[]");
        const sleepDates = JSON.parse(sleepCanvas.dataset.dates || "[]");

        new Chart(sleepCanvas, {
            type: 'line',
            data: {
                labels: sleepDates,
                datasets: [{
                    label: 'Sleep',
                    data: sleepData,
                    borderColor: '#4f46e5',
                    tension: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: { y: { min: 0, max: 24 } }
            }
        });
    }
});
