document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission for demo purposes
        alert('Form submitted!'); // Alert message
        // Add further processing or AJAX submission here
    });
});

