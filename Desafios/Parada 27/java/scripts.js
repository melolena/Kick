function caravana(){
    let nome = document.getElementById('nome').value;
    
    if (nome == ''){
        alert ('Escreva seu nome');
        document.getElementById('nome').focus;
        return false
    }

    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    
    if(email.value.match(mailformat)){
    } else{
       alert('email inválido');
       mail.focus();
       return false;
    }

}
