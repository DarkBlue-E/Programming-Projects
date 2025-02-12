const env = document.querySelector('.env');
const lettre = document.querySelector('.lettre');
const heartContainer = document.querySelector('.heart-container');

env.addEventListener('click', () => {
    if (!env.classList.contains('open')) {
        // Open the envelope
        env.classList.add('open');
        lettre.classList.remove('letter-down');
        lettre.classList.add('letter-up');
        heartContainer.classList.add('hidden'); // Hide the heart
    } else {
        // Close the envelope
        env.classList.remove('open');
        lettre.classList.remove('letter-up');
        lettre.classList.add('letter-down');
        heartContainer.classList.remove('hidden'); // Show the heart
    }
});

const messageElement = document.getElementById('message');

// Fetch and load the message content from message.txt
fetch('message.txt')
    .then(response => response.text())
    .then(data => {
        messageElement.textContent = data;
    })
    .catch(error => {
        console.error('Error loading message.txt:', error);
        messageElement.textContent = 'Failed to load message content.';
    });