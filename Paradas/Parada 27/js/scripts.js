//dicionário contendo chave e valor

var cidadesPorEstado = {
    SP: ["São Paulo", "Campinas", "Santos", "..."],
    RJ: ["Rio de Janeiro", "Volta Redonda", "Angra"],
    MG: ["Belo Horizonte", "Viçosa", "Uberlândia"]
};

function mostrarCidades(){
    var estadoSelect = document.getElementById("estado");
    var cidadeSelect = document.getElementById("cidade");

//limpa as opções de cidade

cidadeSelect.innerHtml = "";

//pegar o estado selecionado 

var estadoSelecionado = estadoSelect.value;

//verifica o estado selecionado e add as cidades correspondentes
if(estadoSelecionado){
    var cidades = cidadesPorEstado[estadoSelecionado];
    if(cidades){
        cidades.forEach(function(cidade){
            adicionarCidade(cidade,cidadeSelect);
            
        });
    }
}

function adicionarCidade(cidade,select){
    var option = document.createElement("option");
    option.text = cidade;
    select.add(option);
}
}