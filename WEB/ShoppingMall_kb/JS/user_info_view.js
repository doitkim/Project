var chk_id = localStorage.getItem("ID");
var chk_pw = localStorage.getItem("PW");
var username = localStorage.getItem("name");
var jumin_number = localStorage.getItem("jumin_number");
var address = localStorage.getItem("address");
var hp = localStorage.getItem("hp");

function getDownloadRecord(event) {
    downloadTemplate('회원 정보.txt', chk_id,chk_pw,username,jumin_number,address,hp); //현재 웹페이지 전체 소스 선택
}
// document.addEventListener('DOMContentLoaded', ()=>{
// })        

//Download HTML Template Source
function downloadTemplate(filename,chk_id,chk_pw,username,jumin_number,address,hp) {
    let element = document.createElement('a');
    element.setAttribute('href','data:text/plain;charset=utf-8,' + 
    '아이디:' + encodeURIComponent(chk_id) + 
    ':비밀번호:'+ encodeURIComponent(chk_pw) + 
    ':이름:' + encodeURIComponent(username) +
    ':주민등록번호:' + encodeURIComponent(jumin_number) +
    ':주소:' + encodeURIComponent(address) +
    ':핸드폰:' + encodeURIComponent(hp)
    );
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
}

async function loadFile(file) {
    let text = await file.text();
    document.getElementById('output').textContent = text;
    text = text.split(":");
    
    localStorage.setItem("ID", text[1]);
    localStorage.setItem("PW", text[3]);
    localStorage.setItem("name", text[5]);
    localStorage.setItem("jumin_number", text[7]);
    localStorage.setItem("address", text[9]);
    localStorage.setItem("hp", text[11]);
    
    
    
  }
// data:text/plain;charset=utf-8
