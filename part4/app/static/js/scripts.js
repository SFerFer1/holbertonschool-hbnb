/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  
  const LoginForm = document.getElementById('login-form');
 
  if (LoginForm) {
    LoginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const email = LoginForm.querySelector("#email").value;
        const password = LoginForm.querySelector("#password").value;
        await.loginUser(email, password);
  });
  
  
  
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
      document.cookie = `token=${data.access_token}; path=/;
      window.location.href = 'index.html';
  } else {
      alert('Login failed: ' + response.statusText);
  }
}
