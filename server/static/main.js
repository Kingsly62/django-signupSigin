let firstname = document.getElementById('id_firstname');
let lastname = document.getElementById('id_lastname');
let email = document.getElementById('id_email');
let password = document.getElementById('id_password');
let retype_password = document.getElementById('id_retype_password');

function register() {
   if(firstname.value == '' && lastname.value == '' && email.value == '' && password.value == '' && retype_password.value == '') {
     alert('No Value');
     return false;
   }
   if(firstname.value == '') {
     alert('Enter a Firstname');
     return false;
   }
   if(lastname.value == '') {
    alert('Enter a Lastname');
    return false;
  }
  if(email.value == '') {
    alert('Enter a Email');
    return false;
  }
  if(password.value == '') {
    alert('Enter a Password');
    return false;
  }
  if(retype_password.value == '') {
    alert('Retype_Password Must Enter');
    return false;
  }
  if(password.value.length < 10) {
    alert('Password Atleast 10 Digits');
    return false;
  }
  if(password.value !== retype_password.value) {
    alert('Password Not Matched');
    return false;
  }
  if(email.value.indexOf('@') == -1) {
    alert('Missing @ in Email');
    return false;
  }
}
function login() {
   if(email.value == '' && password.value == '') {
     alert('No Value');
     return false;
   }
   if(email.value == '') {
     alert('Enter a Email');
     return false;
   }
   if(password.value == '') {
    alert('Enter a Password');
    return false;
  }
  if(email.value.indexOf('@') == -1) {
    alert('Missing @ in Email');
    return false;
  }
}