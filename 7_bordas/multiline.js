const texto = `
Leo é muito legal
Emanuel foi jogar em Sergipe
Bianca é casada com Habib
`

console.log(texto.match(/\n/gi))
// [ '\n', '\n', '\n', '\n' ]

console.log(texto.match(/^(\w).+\1$/gi)) // NULL, não da Match
// null

console.log(texto.match(/^(\w).+\1$/gim)) // com Multiline da Match
// [
//     'Leo é muito legal',
//     'Emanuel foi jogar em Sergipe',
//     'Bianca é casada com Habib'
//   ]
