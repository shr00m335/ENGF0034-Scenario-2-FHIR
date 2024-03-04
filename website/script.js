function validateForm() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var usernameError = document.getElementById("usernameError");
  var passwordError = document.getElementById("passwordError");

  usernameError.innerHTML = "";
  passwordError.innerHTML = "";

  if (username.trim() === "") {
    usernameError.innerHTML = "Username is required";
    return false;
  }
  if (password.trim() === "") {
    passwordError.innerHTML = "Password is required";
    return false;
  }
  return true;
}