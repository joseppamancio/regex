const texto1 = 'dia diatonico diafragma media wikipedia bom_dia melodia radial'

console.log(texto1.match(/\bdia\w+/gi)) // Palavras que começam com dia + é (um ou mais)
// [ 'diatonico', 'diafragma' ]

console.log(texto1.match(/\w+dia\b/gi)) // Palavras que terminam com 'dia'
// [ 'media', 'wikipedia', 'bom_dia', 'melodia' ]

console.log(texto1.match(/\w+dia\w+/gi)) // Palavras que começam e terminam com 'dia'
// [ 'radial' ]

console.log(texto1.match(/\bdia\b/gi)) // Apenas 'dia'
// [ 'dia' ]



// borda é não \w, que é [^A-Za-z0-9_]... temos problemas com acentos!

// ACENTOS SÃO CONSIDERADOS CARACTERES DE BORDA
const texto2 = 'dia diatônico diafragma, média wikipédia bom-dia melodia radial'
console.log(texto2.match(/\bdia\b/gi))
// [ 'dia', 'dia', 'dia', 'dia' ]
// dia d̶i̶a̶t̶ô̶n̶i̶c̶o d̶i̶a̶f̶r̶a̶g̶m̶a, média wikipédia bom-dia m̶e̶l̶o̶d̶i̶a ̶r̶a̶d̶i̶a̶l

console.log(texto2.match(/(\S*)?dia(\S*)?/gi)) // a vírgula entra!
// [
//     'dia',
//     'diatônico',
//     'diafragma,',
//     'média',
//     'wikipédia',
//     'bom-dia',
//     'melodia',
//     'radial'
//   ]

console.log(texto2.match(/([\wÀ-ú-]*)?dia([\wÀ-ú-]*)?/gi))
// [
//     'dia',       'diatônico',
//     'diafragma', 'média',
//     'wikipédia', 'bom-dia',
//     'melodia',   'radial'
//   ]