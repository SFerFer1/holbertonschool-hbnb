/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const LoginForm = document.getElementById('login-form');
 
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = FormData(LoginForm);
        const email = LoginForm.getElementById("email");
        const password = LoginForm.getElementById("password")
    });
    
    await loginUser(email, password)
  });

