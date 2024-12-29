// Form validation for registration
function validateRegistrationForm() {
  const form = document.getElementById("registration-form");
  const username = document.getElementById("id_username");
  const email = document.getElementById("id_email");
  const password1 = document.getElementById("id_password1");
  const password2 = document.getElementById("id_password2");
  const roleCheckboxes = document.querySelectorAll('input[type="checkbox"]');

  let isValid = true;

  // Username validation
  if (username.value.length < 3) {
    showError(username, "Username must be at least 3 characters long");
    isValid = false;
  }

  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
    showError(email, "Please enter a valid email address");
    isValid = false;
  }

  // Password validation
  if (password1.value.length < 8) {
    showError(password1, "Password must be at least 8 characters long");
    isValid = false;
  }

  if (password1.value !== password2.value) {
    showError(password2, "Passwords do not match");
    isValid = false;
  }

  // Role validation
  let roleSelected = false;
  roleCheckboxes.forEach((checkbox) => {
    if (checkbox.checked) roleSelected = true;
  });

  if (!roleSelected) {
    showError(roleCheckboxes[0], "Please select at least one role");
    isValid = false;
  }

  return isValid;
}

function showError(element, message) {
  const errorDiv = document.createElement("div");
  errorDiv.className = "error-message";
  errorDiv.textContent = message;

  // Remove any existing error messages
  const existingError = element.parentElement.querySelector(".error-message");
  if (existingError) existingError.remove();

  element.parentElement.appendChild(errorDiv);
}
