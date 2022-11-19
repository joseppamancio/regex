const aplicarCor = (txt, reg, cor) => txt.replace(reg, `<span style="color: #${cor}"><b>$1</b></span>`)

const files = require('./files')                        // carrega arquivo 
const texto = files.read('codigoFonte.html')            // carrega o html da pasta originais

const codeRegex = /<code>[\s\S]*<\/code>/i              // obtendo contexto de code
let codigo = texto.match(codeRegex)[0]                  // retornando apenas o texto  com [0]

// String...
codigo = aplicarCor(codigo, /(\".*\")/g, 'ce9178')      // codigo, regex, cor

// Palavras Reservadas...
codigo = aplicarCor(codigo, /\b(package|public|class|static|if|else)\b/g, 'd857cf')

// Tipos...
codigo = aplicarCor(codigo, /\b(void|int)\b/g, '1385e2')

// Comentários de Múltiplas Linhas...
codigo = aplicarCor(codigo, /(\/\*[\s\S]*\*)/g, '267703')

// Comentários de uma linha...
codigo = aplicarCor(codigo, /(\/\/.*?\n)/g, '267703')

const conteudoFinal = texto.replace(codeRegex, codigo)
files.write('codigoFonte.html', conteudoFinal)