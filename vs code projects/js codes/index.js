
function clickbutton()
{

    var username = document.getElementById('username').value;
    console.log(username);
    document.getElementById('greet').innerHTML = 'hello ' + username;
}