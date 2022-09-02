texto = 'supermercado superação hiperMERCADO Mercado'

puts texto.scan(/(?:super)[\wÀ-ú]+/i).join(' ')

# Positive Lookbehind
puts texto.scan(/(?<=super)[\wÀ-ú]+/i).join(' ') # Palavras que tem o prefixo super

# Negative Lookbehind
puts texto.scan(/(?<!super)mercado/i) # Palavras que NÃO tem o prefixo super