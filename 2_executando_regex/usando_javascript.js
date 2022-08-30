const texto = '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'

const regexNove = RegExp('9')

// verificando se existe
console.log(regexNove.test(texto))  // true

// verificando se existe e em qual index
console.log(regexNove.exec(texto))  // [ '9', index: 18, input: '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f', groups: undefined ]




const regexLetras = /[a-f]/g
// verificando se conjunto existem naquele intervalo
console.log(texto.match(regexLetras))   // [ 'a', 'b', 'c', 'd', 'e', 'f' ]

// O primeiro elemento dentro daquele intervalo
console.log(texto.search(regexLetras))  // 20

// Subistituindo o regex
console.log(texto.replace(regexLetras,'OK'))  // 0,1,2,3,4,5,6,7,8,9,OK,OK,OK,OK,OK,OK

// Gerando um Split partindo do Regex
console.log(texto.split(regexLetras))  // [ '0,1,2,3,4,5,6,7,8,9,', ',', ',', ',', ',', ',', '' ]
