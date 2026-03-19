let cpuChart, diskChart, memoryChart, polling, lastScore;

function createCharts() {

    cpuChart = new Chart(document.getElementById("cpuChart"), {
        type: "bar",
        data: {
            labels: ["CPU Time"],
            datasets: [{
                label: "Seconds",
                data: [0]
            }]
        }
    });

    diskChart = new Chart(document.getElementById("diskChart"), {
        type: "bar",
        data: {
            labels: ["Write", "Read"],
            datasets: [{
                label: "MB/s",
                data: [0, 0]
            }]
        }
    });

    memoryChart = new Chart(document.getElementById("memoryChart"), {
        type: "doughnut",
        data: {
            labels: ["Used", "Free"],
            datasets: [{
                data: [0, 100]
            }]
        }
    });
}

function startTest() {
    document.getElementById("score").innerText = "--";
    lastScore = null;
    
    fetch('/start')
        .then(() => {
            startPolling(); // start polling only after test starts
        });
}

function updateUI(data) {
    document.getElementById("status").innerText = data.status;

    if (data.cpu) {
        cpuChart.data.datasets[0].data = [data.cpu.duration];
        cpuChart.update();
    }

    if (data.disk) {
        diskChart.data.datasets[0].data = [
            data.disk.write_speed,
            data.disk.read_speed
        ];
        diskChart.update();
    }

    if (data.memory) {
        memoryChart.data.datasets[0].data = [
            data.memory.allocated_mb,
            100 - data.memory.allocated_mb
        ];
        memoryChart.update();
    }

    if (data.score !== undefined && data.score !== lastScore) {
        animateScore(data.score);
        lastScore = data.score;
    }
}

function animateScore(target) {
    let el = document.getElementById("score");
    let current = 0;

    let interval = setInterval(() => {
        current += 1;
        el.innerText = current;

        if (current >= target) {
            clearInterval(interval);
        }
    }, 20);
}

function startPolling() {
    if (polling) return; // prevent duplicate polling

    polling = setInterval(() => {
        fetch('/status')
            .then(res => res.json())
            .then(data => {
                updateUI(data);

                // Stop when completed
                if (data.status === "completed") {
                    clearInterval(polling);
                    polling = null;
                }
            });
    }, 1000);
}


createCharts();