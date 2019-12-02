equacoes = document.getElementsByClassName("equacao")

for(var i = 0; i < equacoes.length; i ++) {
    var equacao = equacoes[i]
    botoes = equacao.getElementsByTagName("button")

    for(var j = 0; j < botoes.length; j++) {
        criaBotao(equacao, botoes[j], equacao.id)
    }
}

function criaBotao(equacao, botao, url) {
    botao.onclick = function() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                resp = JSON.parse(this.responseText);
                //alert(botao.value + " = " + resp)
                var resposta = document.getElementById(equacao.id +botao.value);
                resposta.innerHTML = "<b>" + resp + "</b>"
            }
        }
        var endereco = url + botao.value
        var valores = equacao.getElementsByClassName(botao.value + botao.value)
        for(var i = 0; i < valores.length; i++) {
            if (valores[i].value != ""){
                endereco = endereco + '/' + valores[i].value
            }
        }
        //alert(endereco)
        xhttp.open("GET", endereco, true);
        xhttp.send();
    }
}

/*
for(var i = 0; i < botoes.length; i++)
{
    alert(botoes[i].value)
}

calculaF = document.getElementById("calculaF");
calculaF.onclick = function()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            resp = JSON.parse(this.responseText);
            alert(calculaF.value + " = " + resp)
            var resposta = document.getElementById(calculaF.value);
            resposta.innerHTML = calculaF.value + " = " + resp
        }
    }
    var B = document.getElementById(calculaF.value + "B").value
    var I = document.getElementById(calculaF.value + "I").value
    var L = document.getElementById(calculaF.value + "L").value
    var T = document.getElementById(calculaF.value + "T").value
    var url = '/equacao8/' + calculaF.value + '/' + B + '/' + I + '/' + L + '/' + T;
    //alert(url)
    xhttp.open("GET", url, true);
    xhttp.send();
}

calculaB = document.getElementById("calculaB");
calculaB.onclick = function()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            resp = JSON.parse(this.responseText);
            alert(calculaB.value + " = " + resp)
            var resposta = document.getElementById(calculaB.value);
            resposta.innerHTML = calculaB.value + " = " + resp
        }
    }
    var F = document.getElementById(calculaB.value + "F").value
    var I = document.getElementById(calculaB.value + "I").value
    var L = document.getElementById(calculaB.value + "L").value
    var T = document.getElementById(calculaB.value + "T").value
    var url = '/equacao8/' + calculaB.value + '/' + F + '/' + I + '/' + L + '/' + T;
    //alert(url)
    xhttp.open("GET", url, true);
    xhttp.send();
}
*/