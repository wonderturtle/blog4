document.addEventListener('DOMContentLoaded', function () {
    var alertElement = document.getElementById('alert_msg');
    var divAlert = document.getElementById('divAlert');
    // Close the alert after 5000 milliseconds (5 seconds)
    setTimeout(function () {
        alertElement.classList.remove('show');
        alertElement.style.display = 'none';
        divAlert.style.display = 'none';
        // divAlert.classList.remove('mt-2', 'mb-1', 'd-flex');
        // divAlert.remove()
    }, 5000);
});