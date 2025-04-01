document.addEventListener('DOMContentLoaded', () => {
  
  const LoginForm = document.getElementById('login-form');
 
  if (LoginForm) {
    LoginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const email = LoginForm.querySelector("#email").value;
        const password = LoginForm.querySelector("#password").value;
        await loginUser(email, password);
    });
  
    
  }
const loginButton= document.getElementsByClassName('login-button');

const newCookie = getCookie("token");
if (!newCookie) {
  window.location.href = 'login.html';
} else {
  for (let i = 0; i < loginButton.length; i++) {
    loginButton[i].style.display = 'none'; // Ocultar cada botón
}
  
}
  
});

async function loginUser(email, password) {
    const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });
    if (response.ok) {
      const data = await response.json();
      document.cookie = `token=${data.access_token}; path=/`;
      window.location.href = 'index.html';
  } else {
      alert('Login failed: ' + response.statusText);
  }
  
}
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {

    const cookieValue = parts.pop();

    const splitValues = cookieValue.split(';');

    const finalValue = splitValues.shift();
    return finalValue;
}
return null
}

async function getPlaces() {
  const places = await fetch("http://127.0.0.1:5000/api/v1/places", {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
      },
  }

)
alert("aaaaaaaaaaaaaaaaa"); // Mostrar los lugares en un alert
return places;
};