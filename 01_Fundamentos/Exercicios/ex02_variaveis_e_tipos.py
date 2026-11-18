# 1. Dados da ficha
# Criamos uma variável para cada informação que queremos guardar.
# Uma variável é um nome que aponta para um valor guardado na memória.
# O sinal = não significa "igual" como na matemática: ele atribui o valor da direita
# ao nome da esquerda.
# Escolhemos nomes que explicam o conteúdo, para o código ficar fácil de ler depois.
nome = "Ana Souza"
curso = "Desenvolvimento de Software Multiplataforma"
semestre = 1
altura = 1.65
matriculado = True


# 2. Exibição dos dados
# Passamos vários valores para o mesmo print(), separados por vírgula.
# O Python insere um espaço entre eles automaticamente.
# Assim combinamos um texto fixo (como "Nome:") com o valor guardado na variável.
print("Nome:", nome)
print("Curso:", curso)
print("Semestre:", semestre)
print("Altura:", altura)
print("Matriculado:", matriculado)


# 3. Conferindo os tipos
# Cada valor tem um tipo, e o tipo define o que podemos fazer com ele.
# A função type() informa o tipo do valor guardado em uma variável.
# Usamos para confirmar como o Python interpretou cada dado:
# str (texto), int (número inteiro), float (número decimal) e bool (True ou False).
# Repare que 1.65 usa ponto, e não vírgula: o Python segue a notação americana.
print("Tipo de nome:", type(nome))
print("Tipo de semestre:", type(semestre))
print("Tipo de altura:", type(altura))
print("Tipo de matriculado:", type(matriculado))
