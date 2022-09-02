const texto1 = 'O José Simão é muito engraçado... hehehehehehe'
console.log(texto1.match(/(he)+/g))
// [ 'hehehehehehe' ]

const texto2 = 'http://www.site.info www.escola.ninja.br google.com.ag'
console.log(texto2.match(/(http:\/\/)?(w{3}\.)?\w+\.\w{2,}(\.\w{2})?/g))
// [ 'http://www.site.info', 'www.escola.ninja.br', 'google.com.ag' ]