var register_submit = document.getElementById("register_submit");
register_submit.addEventListener("click", function () {
var id = document.getElementById("id");
var pw = document.getElementById("pw");
var username = document.getElementById("name");
var jumin_number = document.getElementById("jumin_number");
var address = document.getElementById("address");
var hp = document.getElementById("hp");

localStorage.setItem("ID", id.value);
localStorage.setItem("PW", pw.value);
localStorage.setItem("name", username.value);
localStorage.setItem("jumin_number", jumin_number.value);
localStorage.setItem("address", address.value);
localStorage.setItem("hp", hp.value);

window.location.href = "./introduce_login.html";
});
