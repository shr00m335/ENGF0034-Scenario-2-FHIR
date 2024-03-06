const loginUrl = "/login"

async function sha256(message) {
  // encode as UTF-8
  const msgBuffer = new TextEncoder().encode(message);                    

  // hash the message
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

  // convert ArrayBuffer to Array
  const hashArray = Array.from(new Uint8Array(hashBuffer));

  // convert bytes to hex string                  
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
}

async function validateForm() {
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



  const data = new URLSearchParams();
  data.append("username", username);
  password = await sha256(password);
  data.append("password", password);
  let res = await fetch(loginUrl, {
    method: "post",
    body: data
  })
  let resData = await res.json()
  if (res.status != 200) {
    alert(resData.message);
    return false;
  }
  document.cookie = "token=" + resData.token;
  window.location.href = "/details"
  return true;
}