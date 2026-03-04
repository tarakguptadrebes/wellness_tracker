new Chart(
    document.getElementById('moodChart').getContext('2d'),
    {
        type: 'line',
        data: {
            labels: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
            datasets: [{
                label: 'Mood',
                data: [3,4,2,5,4,3,4],
            }]
        }
    }
);