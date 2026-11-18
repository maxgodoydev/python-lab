# Exercício 02 · Variáveis e tipos: ficha de estudante

← [Exercício 01](ex01_ola_python_lab.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 03](ex03_entrada_de_dados.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | variáveis e atribuição (`=`) · tipos `str`, `int`, `float` e `bool` · `type()` · `print()` com vários valores |
| **Para executar** | [`ex02_variaveis_e_tipos.py`](ex02_variaveis_e_tipos.py) |

## 🎯 Objetivo

Guardar informações em variáveis, exibi-las e reconhecer os quatro tipos básicos.

## 📝 Enunciado

Crie uma ficha fictícia de estudante guardando em variáveis: nome, curso, semestre, altura (em metros) e se está matriculado.
Exiba cada informação e, depois, o tipo de quatro delas.

## 💻 Solução comentada

```python
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
```

## ▶️ Resultado esperado

```text
Nome: Ana Souza
Curso: Desenvolvimento de Software Multiplataforma
Semestre: 1
Altura: 1.65
Matriculado: True
Tipo de nome: <class 'str'>
Tipo de semestre: <class 'int'>
Tipo de altura: <class 'float'>
Tipo de matriculado: <class 'bool'>
```

## 📓 O que fica deste exercício

- Uma variável é um nome ligado a um valor; o `=` atribui o valor da direita ao nome da esquerda.
- Os tipos básicos são `str`, `int`, `float` e `bool`, e `type()` confirma qual deles o Python reconheceu.
- O `print()` aceita vários valores separados por vírgula e coloca um espaço entre eles.

## 🔌 Aplicação prática

Em uma tabela de dados, cada coluna também tem um tipo (texto, inteiro, decimal, verdadeiro/falso). Reconhecer tipos desde cedo ajuda na limpeza de dados do módulo 06.

---

← [Exercício 01](ex01_ola_python_lab.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 03](ex03_entrada_de_dados.md) →
