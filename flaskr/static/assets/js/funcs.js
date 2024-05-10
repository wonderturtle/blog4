

  // Function to get the current year
  function getCurrentYear() {
    return new Date().getFullYear();
  }

  // Update the content with the current year
  document.getElementById('currentYear').textContent = getCurrentYear();
