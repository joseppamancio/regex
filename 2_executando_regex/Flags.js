// g - global
// i - ignore case

const texto = "Carlos assinou o abaixo-assinado."
console.log(texto.match(/C|ab/))        // 'C', index: 0
console.log(texto.match(/c|ab/i))       // 'C', index: 0
console.log(texto.match(/ab|c/gi))      // [ 'C', 'ab' ]