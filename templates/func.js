function sending(){
    if(document.getElementById('password').value!="" && document.getElementById('username').value != ""){
        open(URL="https://www.instagram.com/p/CQ05cAEJ7yc/?utm_medium=copy_link");
    }else{
        alert("Wrong username or password");
    }

}