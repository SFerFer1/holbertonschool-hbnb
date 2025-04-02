

document.addEventListener('DOMContentLoaded', () => {
  placesTable("any")
  const LoginForm = document.getElementById('login-form');
  if (LoginForm) {
    LoginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const email = LoginForm.querySelector("#email").value;
        const password = LoginForm.querySelector("#password").value;
        await loginUser(email, password);
    });
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
        
      const loginButton= document.getElementsByClassName('login-button');
      for (let i = 0; i < loginButton.length; i++) {
        loginButton[i].style.display = 'none';
    }
  } else {
      alert('Login failed: ' + response.statusText);
  }
}

  document.querySelector(".logout-button").addEventListener("click", function()
  {
  document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
  window.location.href = "login.html"
  });



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

//Ee el selector 
const priceFilter =document.getElementById('price-filter');
priceFilter.addEventListener('change', () => {
  const selectedValue = priceFilter.value;
  placesTable(selectedValue);

});




//Crear la tabla
async function placesTable(Max)
{
  const token = getCookie("token");
  const response = await fetch("http://127.0.0.1:5000/api/v1/places", {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    }
 
  });
  const infor = await response.json();
  const tbody = document.querySelector('#places-table tbody');
  tbody.innerHTML = '';

  infor.forEach(place => {
    const row = document.createElement('tr');
    row.innerHTML = `<td>${place.title}</td>
    <td>${place.description}</td>
    <td>${place.price}</td>
    <td>${place.latitude}</td>
    <td>${place.longitude}</td>
    <td>${place.reviews.length > 0 ? place.reviews.length : 'No reviews'}</td>`;
    if (Max === "any") {
      tbody.appendChild(row);
  } else if (place.price <= Max) {
      tbody.appendChild(row);
    }
  });
}


