const texto = 'Pedrinho (filho do Pedro Silva) é doutor do ABCabc!'

console.log(texto.match(/[(abc)]/g)) // Não é um grupo, '[]' prevalece sobre '()'
// [ '(', 'a', ')', 'a', 'b', 'c' ]

console.log(texto.match(/([abc])/g)) // '[]' sobrevive dentro de um conjunto
// [ 'a', 'a', 'b', 'c' ]

console.log(texto.match(/(abc)/g)) // Não precisa de grupo não Use, deixe mais simples
console.log(texto.match(/abc/g))
// [ 'abc' ]


