const fs = require('fs')

const read = nomeArquivo =>
    fs.readFileSync(`${__dirname}/originais/${nomeArquivo}`, { encoding: 'utf8'})

const write = (nomeArquivo, conteudo) => {
    const dirname = `${__dirname}/alterados`    // caminha para gravação
    if (!fs.existsSync(dirname)){               // caso o diretório não exista, crie ele
        fs.mkdirSync(dirname)
    }
    fs.writeFileSync(`${dirname}/${nomeArquivo}`, conteudo, { encoding: 'utf8'})       // gravando conteudo no caminho
}

module.exports = { read, write }