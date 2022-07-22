  var login_submit = document.getElementById("login_submit");
  login_submit.addEventListener("click", function () {
  var login_form = document.getElementById("login_form");
  var id = document.getElementById("ID");
  var pw = document.getElementById("PW");

  if (pw.value.trim() == "" || id.value.trim() == "") {
    alert("잘못된 아이디 / 패스워드");
    return false;
  }

  var chk_id = localStorage.getItem("ID");
  var chk_pw = localStorage.getItem("PW");
  var username = localStorage.getItem("name");
  var jumin_number = localStorage.getItem("jumin_number");
  var address = localStorage.getItem("address");
  var hp = localStorage.getItem("hp");

  if(id.value === chk_id){
    if(pw.value === chk_pw){
        // login_form.action = "http://www.naver.com";
        // login_form.mothod = "GET";
        // login_form.submit();
        alert('로그인 성공');
        document.write(`${id.value}님 어서오세요.<br>`);
        document.write("회원 정보<br>");
        document.write(`아이디: ${id.value}<br>`);
        document.write(`비밀번호: ${pw.value}<br>`);
        document.write(`이름: ${username}<br>`);
        document.write(`주민등록번호: ${jumin_number}<br>`);
        document.write(`주소: ${address}<br>`);
        document.write(`핸드폰: ${hp}<br>`);
    }
    else{
        alert('잘못된 비밀번호입니다.');
    }
  }
  else{
    alert('잘못된 아이디입니다.');
  } 
});