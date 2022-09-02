const texto = 'João é calmo, mas no transito fica nervoso.'

console.log(texto.match(/[\wÀ-ú]+/gi))
// ['João', 'é', 'calmo', 'mas', 'no', 'transito', 'fica', 'nervoso']



// ----------- Positive LookaHead '?='  ----------- //
console.log(texto.match(/[\wÀ-ú]+(?=,)/gi)) // Virgula na frente da palavra
// [ 'calmo' ]

console.log(texto.match(/[\wÀ-ú]+(?=\.)/gi))
// [ 'nervoso' ]

console.log(texto.match(/[\wÀ-ú]+(?=, mas)/gi))
// [ 'calmo' ]



// ----------- Negative LookaHead '?!'  ----------- //
console.log(texto.match(/[\wÀ-ú]+\b(?!,)/gi)) // Não tem virgula na frente
// [ 'João', 'mas', 'no', 'transito', 'fica', 'nervoso' ]

console.log(texto.match(/[\wÀ-ú]+[\s|\.](?!,)/gi)) // corrigindo o problema com o 'é'
// [ 'João ', 'é ', 'mas ', 'no ', 'transito ', 'fica ', 'nervoso.' ]


