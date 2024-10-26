document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('reservationForm');
    const ticket = document.getElementById('ticket');
    const ticketPassengerName = document.getElementById('ticketPassengerName');
    const ticketNumPassengers = document.getElementById('ticketNumPassengers');
    const ticketSeatPreference = document.getElementById('ticketSeatPreference');
    const ticketEmail = document.getElementById('ticketEmail');
    const ticketPhone = document.getElementById('ticketPhone');
    const confirmationMessage = document.getElementById('confirmationMessage');
    const confirmButton = document.getElementById('confirmButton');
    const updateButton = document.getElementById('updateButton');
    

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get values from the form
        const passengerName = document.getElementById('passengerName').value;
        const numPassengers = document.getElementById('numPassengers').value;
        const seatPreference = document.getElementById('seatPreference').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;

        // Update ticket display
        ticketPassengerName.textContent = passengerName;
        ticketNumPassengers.textContent = numPassengers;
        ticketSeatPreference.textContent = seatPreference;
        ticketEmail.textContent = email;
        ticketPhone.textContent = phone;

        // Show the ticket
        ticket.style.display = 'block';
    });

    // Confirm booking
    confirmButton.addEventListener('click', function() {
        // Hide the ticket and show the confirmation message
        ticket.style.display = 'none';
        confirmationMessage.style.display = 'block';
    });

    // Update reservation
    updateButton.addEventListener('click', function() {
        // Allow the form to be updated
        ticket.style.display = 'none';
    });
});
