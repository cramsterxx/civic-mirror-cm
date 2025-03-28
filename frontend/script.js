// Example: Fetch and display user balance
document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/user/balance')
        .then(response => response.json())
        .then(data => {
            document.getElementById("user-balance").textContent = data.balance;
        })
        .catch(error => console.error('Error fetching user balance:', error));
});
