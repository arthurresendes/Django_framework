function gritar(){
    let resposta = document.getElementById('res')
    resposta.innerHTML = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
}

function helloWorld() {
    let titulo = document.getElementById('tit')
    titulo.innerHTML = 'Hello World'
}

function olaMundo() {
    let titulo = document.getElementById('tit')
    titulo.innerHTML = 'Olá mundo'
}

function questionario(){
    let nome = prompt("Qual seu nome: ")
    let idioma = prompt("Ingles ou portugues (I or P)").toLocaleUpperCase()
    let titulo = document.getElementById('tit')
    idioma == 'I' ? titulo.innerHTML = 'Hello world ' + nome :     titulo.innerHTML = 'Olá mundo ' + nome
}