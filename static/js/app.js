async function loadChart(symbol = "^DJI") {

    const response = await fetch("/api/history/" + encodeURIComponent(symbol));

    const data = await response.json();

    const labels = [];
    const prices = [];

    data.forEach(item => {

        // Convert timestamp into local time
        const time = new Date(item.fetch_time);

        labels.push(
            time.toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit"
            })
        );

        prices.push(parseFloat(item.price));

    });

    const ctx = document.getElementById("marketChart");

    new Chart(ctx, {

        type: "line",

        data: {

            labels: labels,

            datasets: [{

                label: "Dow Jones",

                data: prices,

                borderWidth: 3,

                tension: 0.3,

                fill: false

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false

        }

    });

}

loadChart();