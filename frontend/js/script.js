// Add event listener to the contact form
document.querySelector('form').addEventListener('submit', (e) => {
    // Prevent the default form submission behavior
    e.preventDefault();
    
    // Get the form data
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;
    
    // Send the form data to the server using AJAX or Fetch API
    // For demonstration purposes, we'll just log the data to the console
    console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);
});
