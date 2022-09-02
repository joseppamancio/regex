string = '<b>Destaque</b><strong>Forte</strong><div>Conteudo</div>'

console.log(string.match(/<(\w)>.*<\/\1>/g))
// [ '<b>Destaque</b>' ]

string = 'Lentamente é mente muito lenta.'
console.log(string.match(/(lenta)(mente)/gi))
// [ 'Lentamente' ]

console.log(string.match(/(lenta)(mente).*\2/gi))
// [ 'Lentamente é mente' ]

console.log(string.match(/(lenta)(mente).*\2.*\1\./gi)) // retrovisor 1 = lenta, retrovisor 2 = mente
// [ 'Lentamente é mente muito lenta' ]

console.log(string.match(/(?:lenta)(mente).*\1/gi)) // ?: não armazena o valor, retrovisor 1 é mente
// [ 'Lentamente é mente' ]

console.log(string.match(/(lenta)(mente)?/gi)) // mente é opcional
// [ 'Lentamente', 'lenta' ]

console.log(string.replace(/(lenta)(mente)/gi, '$2')) // $2 é o retorvisor 'mente', replace subistitui 'Lentamente' por 'mente'
// mente é mente muito lenta.

console.log(string.replace(/(lenta)(mente)/gi, '$2 lenta'))
// mente lenta é mente muito lenta.


const texto3 = 'abcdefghijkll'
console.log(texto3.match(/(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)\12/g))