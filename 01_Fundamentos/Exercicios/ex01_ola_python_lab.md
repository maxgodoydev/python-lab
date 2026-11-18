# Exercício 01 · Olá, Python Lab

← [Módulo 01](../README.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 02](ex02_variaveis_e_tipos.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | `print()` · strings (texto entre aspas) · comentários com `#` · execução de cima para baixo |
| **Para executar** | [`ex01_ola_python_lab.py`](ex01_ola_python_lab.py) |

## 🎯 Objetivo

Exibir mensagens na tela com `print()` e entender o que é uma string.

## 📝 Enunciado

Escreva um programa que exiba na tela, uma mensagem por linha:

1. `Olá, Python Lab!`
2. `Learning Python, one problem at a time.`
3. `Exercício 01 executado com sucesso.`

## 💻 Solução comentada

```python
# 1. Mensagem de boas-vindas
# As linhas que começam com # são comentários: o Python as ignora,
# e nós as usamos para explicar o raciocínio.
# O print() é a função que exibe um texto na tela.
# O texto vai entre aspas porque, para o Python, tudo o que está entre aspas
# é uma string: uma sequência de caracteres que ele deve tratar como texto.
print("Olá, Python Lab!")


# 2. Frase do projeto
# Cada print() escreve em uma linha nova, então a frase aparece logo abaixo da primeira.
# Utilizamos aspas duplas, mas aspas simples também funcionariam.
# O importante é abrir e fechar o texto com o mesmo tipo de aspas.
print("Learning Python, one problem at a time.")


# 3. Confirmação
# O Python lê o código de cima para baixo, uma linha por vez.
# Por isso a ordem dos print() no arquivo é a ordem das mensagens na tela.
print("Exercício 01 executado com sucesso.")
```

## ▶️ Resultado esperado

```text
Olá, Python Lab!
Learning Python, one problem at a time.
Exercício 01 executado com sucesso.
```

## 📓 O que fica deste exercício

- `print()` exibe texto na tela, e cada chamada termina em uma linha nova.
- Texto entre aspas é uma *string*; abrir e fechar com o mesmo tipo de aspas.
- O Python executa linha por linha, de cima para baixo; linhas com `#` são comentários.

## 🔌 Aplicação prática

Toda saída de um script, como mensagens de acompanhamento, avisos e relatórios simples, começa com `print()`. Em rotinas de dados, mensagens assim indicam em que etapa o processo está.

---

← [Módulo 01](../README.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 02](ex02_variaveis_e_tipos.md) →
