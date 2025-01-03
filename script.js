function updateGauges() {
    const speedElement = document.getElementById("speed");
    const rpmElement = document.getElementById("rpm");
    const locationElement = document.getElementById("location");
    const distanceElement = document.getElementById("distance");

    // Example values for demonstration
    let speed = Math.floor(Math.random() * 120);
    let rpm = Math.floor(Math.random() * 80);
    let location = Math.floor(Math.random() * 20) + 10; // Random location between 10 and 30 Km
    let distance = Math.floor(Math.random() * 100) + 20; // Random distance between 20 and 120 Km

    speedElement.textContent = speed;
    rpmElement.textContent = rpm;
    locationElement.textContent = `${location} Km`;
    distanceElement.textContent = `${distance} Km`;
}

// Update gauges and info every second
setInterval(updateGauges, 1000);
