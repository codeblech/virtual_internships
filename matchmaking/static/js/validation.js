// Form validation for registration
function validatePassword(password) {
  const requirements = {
    length: password.length >= 8,
    uppercase: /[A-Z]/.test(password),
    lowercase: /[a-z]/.test(password),
    number: /[0-9]/.test(password),
    special: /[!@#$%^&*(),.?":{}|<>]/.test(password),
  };

  const messages = [];
  if (!requirements.length) messages.push("At least 8 characters long");
  if (!requirements.uppercase) messages.push("At least one uppercase letter");
  if (!requirements.lowercase) messages.push("At least one lowercase letter");
  if (!requirements.number) messages.push("At least one number");
  if (!requirements.special) messages.push("At least one special character");

  return {
    isValid: Object.values(requirements).every((req) => req),
    messages,
  };
}

function validateRegistrationForm() {
  const form = document.getElementById("registration-form");
  const username = document.getElementById("id_username");
  const email = document.getElementById("id_email");
  const password1 = document.getElementById("id_password1");
  const password2 = document.getElementById("id_password2");
  const roleCheckboxes = document.querySelectorAll('input[type="checkbox"]');

  let isValid = true;

  // Username validation
  if (!username.value.trim()) {
    showError(username, "Username is required");
    isValid = false;
  } else if (username.value.length < 3) {
    showError(username, "Username must be at least 3 characters long");
    isValid = false;
  }

  // Email validation
  if (!email.value.trim()) {
    showError(email, "Email is required");
    isValid = false;
  } else {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
      showError(email, "Please enter a valid email address");
      isValid = false;
    }
  }

  // Password validation
  const passwordValidation = validatePassword(password1.value);
  if (!passwordValidation.isValid) {
    showError(password1, "Password requirements:\n" + passwordValidation.messages.join("\n"));
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
