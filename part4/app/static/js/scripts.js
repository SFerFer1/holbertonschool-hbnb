

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
  const data = await response.json();
  const articlesContainer = document.querySelector('#place-list');
  let articlesHTML = '';

      data.forEach(item => {
        if (Max === "any") {
          articlesHTML += `<article><h2>${item.title}</h2><br><p>Descripción: ${item.description}</p><br><p>Precio: ${item.price}</p> <input type="button" value="Ver Mas" class="btnPlaces">  </article> <br>`;
        }
        else if (item.price <= Max) {
          articlesHTML += `<article><h2>${item.title}</h2><br><p>Descripción: ${item.description}</p><br><p>Precio: ${item.price}</p> <input type="button" value="Ver Mas" class="btnPlaces">  </article> <br>`;
        } 
        });

      articlesContainer.innerHTML = articlesHTML;

      document.querySelectorAll('.btnPlaces').forEach(button => {
        button.addEventListener('click', IrPlaces);
      });
      function IrPlaces() {
        
        window.location.href = 'place.html';
      }
}

