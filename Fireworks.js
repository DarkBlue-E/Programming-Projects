// Example dependencies: Define `randColor`, `fireNumber`, and `range`
function randColor() {
    const colors = ["#FF5733", "#33FF57", "#3357FF", "#F0FF33"];
    return colors[Math.floor(Math.random() * colors.length)];
}

let fireNumber = 10; // Example number of fireworks
let range = 50;      // Example range

// Fixed function
function makeFullCircleFirework(fire) {
    let color = randColor();
    let velocity = Math.random() * 8 + 8;
    let max = fireNumber * 3; // Number of particles
    let fireworks = []; // Array to store firework particles

    for (let i = 0; i < max; i++) {
        let rad = (i * Math.PI * 2) / max; // Circular angle
        let firework = {
            x: fire.x,
            y: fire.y,
            size: Math.random() + 1.5,
            fill: color,
            vx: Math.cos(rad) * velocity + (Math.random() - 0.5) * 0.5,
            vy: Math.sin(rad) * velocity + (Math.random() - 0.5) * 0.5,
            ay: 0.06,
            alpha: 1,
            life: Math.round((Math.random() * range) / 2) + range / 1.5
        };
        fireworks.push(firework); // Add the particle to the array
    }

    return fireworks; // Return the array of fireworks
}

// Example usage
let fire = { x: 100, y: 200 }; // Example starting point
let fireworks = makeFullCircleFirework(fire);
console.log(fireworks);
