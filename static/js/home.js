// console.log("clcick")
// prompt("hohh")
function login() {
  document.getElementById("modal_login").style.display = "block";
}
var x = document.getElementById("modal_login");

function cancel_login_form() {
  document.getElementById("modal_login").style.display = "none";
}

// singup
function signup() {
  document.getElementById("modal_signup").style.display = "block";
}
var y = document.getElementById("modal_signup");

function cancel_signup_form() {
  document.getElementById("modal_signup").style.display = "none";
}

window.onclick = function (event) {
  if (event.target == x) x.style.display = "none";

  if (event.target == y) y.style.display = "none";
};
