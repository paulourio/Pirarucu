# -*- encoding: utf-8 -*-

class Braille:
	MAIUSCULA = 1
	CAPS = 2
	ALLCAPS = 3
	NUMERO = 4
	EXPOENTE = 5
	INDICE_INFERIOR = 6
	DESTAQUE = 7 # Itálico, negrito ou sublinado
	INFORMATICA = 6 # Usado quando for apresentar um site, por exemplo.
	
	MEC2002 = {	
		# Vogais (página 23)
		'a': ['⠁', '100000', 'vogal'],
		'á': ['⠷', '111011', 'vogal'],
		'à': ['⠫', '110101', 'vogal'],
		'â': ['⠡', '100001', 'vogal'],
		'ã': ['⠜', '001110', 'vogal'],
		
		'e': ['⠑', '100010', 'vogal'],
		'é': ['⠿', '111111', 'vogal'],
		'ê': ['⠣', '110001', 'vogal'],
		
		'i': ['⠊', '010100', 'vogal'],
		'í': ['⠌', '001100', 'vogal'],
		
		'o': ['⠕', '101010', 'vogal'],
		'ó': ['⠬', '001101', 'vogal'],
		'ô': ['⠹', '100111', 'vogal'],
		'õ': ['⠪', '010101', 'vogal'],
		
		'u': ['⠥', '101001', 'vogal'],
		'ú': ['⠾', '011111', 'vogal'],
		'ü': ['⠞', '110011', 'vogal'],
		
		'ç': ['⠯', '111101', 'cedilha'],

		# Consoantes (A-J)
		#'a': ['⠁', '100000', 'vogal'],
		'b': ['⠃', '110000', 'consoante'],
		'c': ['⠉', '100100', 'consoante'],
		'd': ['⠙', '100110', 'consoante'],
		#'e': ['⠑', '100010', 'vogal'],
		'f': ['⠋', '110100', 'consoante'],
		'g': ['⠛', '110110', 'consoante'],
		'h': ['⠓', '110010', 'consoante'],
		#'i': ['⠊', '010100', 'vogal'],
		'j': ['⠚', '010110', 'consoante'],
		
		# Consoantes (K-T)
		'k': ['⠅', '101000', 'consoante'],
		'l': ['⠇', '111000', 'consoante'],
		'm': ['⠍', '101100', 'consoante'],
		'n': ['⠝', '101110', 'consoante'],
		#'o': ['⠕', '101010', 'vogal'],
		'p': ['⠏', '111100', 'consoante'],
		'q': ['⠟', '111110', 'consoante'],
		'r': ['⠗', '111010', 'consoante'],
		's': ['⠎', '011100', 'consoante'],
		't': ['⠞', '011110', 'consoante'],
		
		# Consoantes (U-W)
		#'u': ['⠥', '101001', 'vogal'],
		'v': ['⠧', '111001', 'consoante'],
		'x': ['⠭', '101101', 'consoante'],
		'y': ['⠽', '101111', 'consoante'],
		'z': ['⠵', '101011', 'consoante'],
		'w': ['⠺', '010111', 'consoante'],
		
		# Números (precisam ser enviador com "sinal de número")
		'1': ['⠁', '100000', 'número 1'],
		'2': ['⠃', '110000', 'número 2'],
		'3': ['⠉', '100100', 'número 3'],
		'4': ['⠙', '100110', 'número 4'],
		'5': ['⠑', '100010', 'número 5'],
		'6': ['⠋', '110100', 'número 6'],
		'7': ['⠛', '110110', 'número 7'],
		'8': ['⠓', '110010', 'número 8'],
		'9': ['⠊', '010100', 'número 9'],
		'0': ['⠚', '010110', 'número 0'],
		
		# Pontuação e sanais acessórios (pagina 24)
		',': ['⠂', '010000', 'vírgula'],
		';': ['⠆', '011000', 'ponto-e-vírgula'],
		':': ['⠒', '010010', 'dois-pontos'],
		'.': ['⠄', '001000', 'ponto'],
		'`': ['⠄', '001000', 'apóstrofo'],
		'?': ['⠢', '010001', 'ponto de interrogação'],
		'!': ['⠖', '011010', 'ponto de exclamação'],
		'...': ['⠄⠄⠄', ['001000', '001000', '001000'], 'reticências'],
		'-': ['⠤', '001001', 'hífen ou traço de união'],
		'⎯ ': ['⠤⠤', ['001001', '001001'], 'travessão'],		
		'•': ['⠪⠕', ['010101', '101010'], 'círculo'],
		'(': ['⠣', '110001', 'abre parênteses'],
		')': ['⠜', '001110', 'fecha parênteses'],
		'[': ['⠷', '111011', 'abre colchetes'],
		']': ['⠾', '011111', 'fecha colchetes'],
		'“': ['⠦', '011001', 'abre aspas'],
		'”': ['⠦', '011001', 'fecha aspas'],
		'"': ['⠦', '011001', 'vírgulas altas'],
		'«': ['⠠⠦', ['000001', '011001'], 'abre aspas angular'],
		'»': ['⠠⠦', ['000001', '011001'], 'fecha aspas angular'],
		"'": ['⠰⠦', ['000011', '011001'], 'aspas simples'],	
		'*': ['⠔', '111011', 'asterisco'],
		'&': ['⠯', '110101', 'e comercial'],
		'/': ['⠠⠂', ['000001', '010000'], 'barra'],
		'|': ['⠸', '001110', 'barra vertical'],
		'→': ['⠒⠕', ['010010', '101010'], 'seta para a direita'],
		'←': ['⠪⠒', ['010101', '010010'], 'seta para a esquerda'],
		'↔': ['⠪⠒⠕', ['010101', '010010', '101010'], 'seta de duplo sentido'],
		
		# Sinais usados com números (página 25)
		'€': ['⠈⠑', ['000100', '100010'], 'Euro'],
		'$': ['⠰', '000011', 'cifrão'],
		'%': ['⠸⠴', ['000111', '001011'], 'por centro'],
		'‰': ['⠸⠴⠴', ['000111', '001011', '001011'], 'por mil'],
		'§': ['⠎⠎', ['011100', '011100'], 'parágrafo único'],
		'+': ['⠖', '011010', 'mais'],
		'-': ['⠤', '001001', 'menos'],
		'X': ['⠦', '011001', 'multiplicado por'],
		'/': ['⠲', '010011', 'divido por'],
		'=': ['⠶', '011011', 'igual a'],
		'>': ['⠕', '101010', 'maior que'],
		'<': ['⠪', '010101', 'menor que'],
		'°': ['⠴', '001011', 'graus'],
		'’': ['⠳', '110011', 'minutos'],
		'′': ['⠳⠳', ['110011', '110011'], 'segundos'], # ′′
		
		# Sinais exclusivos da escrita braille (página 25)
		MAIUSCULA: ['⠨', '000101', 'sinal de letra maiúscula'],
		CAPS: ['⠨⠨', ['000101', '000101'], 'sinal de todas letras maiúsculas'],
		ALLCAPS: ['⠒⠨⠨', ['010010', '000101', '000101'], 'sinal de série de palavras em caixa alta'],
		NUMERO: ['⠼', '001111', 'sinal de número'],
		DESTAQUE: ['⠔', '001010', 'sinal de destaque (negrito, itálico, sublinhado)'],
		INFORMATICA: ['⠐⠂', ['000010', '010000'], 'expressão informática'],
		
		# Símbolos usados em contexto informático (página 68)
		'@': ['⠱', '100011', 'arroba'],
		'#': ['⠼⠅', ['001111', '101000'], 'cardinal'],
		
		# Alfabeto grego clássico (página 75)
		'α': ['⠈⠁', '100000', 'alfa'],
		'β': ['⠈⠃', '110000', 'beta'],
		'γ': ['⠈⠛', '110110', 'gama'],
		'δ': ['⠈⠙', '100110', 'delta'],
		'ε': ['⠈⠑', '100010', 'épsilon'],
		'ζ': ['⠈', '110011', 'zeta'],
		'η': ['⠈', '110011', 'eta'],
		'θ': ['⠈', '110011', 'teta'],
		'ι': ['⠈⠊', '010100', 'iota'],
		'κ': ['⠈', '110011', 'capa'],
		'λ': ['⠈', '110011', 'lambda'],
		'μ': ['⠈', '110011', 'mi'],
		'ν': ['⠈', '110011', 'ni'],
		'ξ': ['⠈', '110011', 'xi'],	
		'ο': ['⠈', '110011', 'omicron'],
		'π': ['⠈', '110011', 'pi'],
		'ρ': ['⠈', '110011', 'rô'],
		'σ': ['⠈', '110011', 'sigma'],
		'τ': ['⠈', '110011', 'tau'],
		'υ': ['⠈', '110011', 'úpsilon'],
		'φ': ['⠈', '110011', 'fi'],
		'χ': ['⠈', '110011', 'chi'],
		'ψ': ['⠈', '110011', 'psi'],
		'ω': ['⠈', '110011', 'ômega'],
		
		'3': ['⠉', '100100', 'número 3'],
		'4': ['⠙', '100110', 'número 4'],
		'5': ['⠑', '100010', 'número 5'],
		'6': ['⠋', '110100', 'número 6'],
		'7': ['⠛', '110110', 'número 7'],
		'8': ['⠓', '110010', 'número 8'],
		'9': ['⠊', '010100', 'número 9'],
		'0': ['⠚', '010110', 'número 0']
	}
