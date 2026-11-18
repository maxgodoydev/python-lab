# Exercício 08 · Repetição: tabuada com for

← [Exercício 07](ex07_situacao_do_aluno.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Módulo 01](../README.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | laço `for` · `range()` · variável do laço · f-string |
| **Para executar** | [`ex08_tabuada_com_for.py`](ex08_tabuada_com_for.py) |

## 🎯 Objetivo

Repetir um bloco de código com `for` e `range()`.

## 📝 Enunciado

Peça um número inteiro e exiba a tabuada dele de 1 a 10, uma multiplicação por linha.

## 💻 Solução comentada

```python
# 1. Leitura do número
# Convertemos para int porque a tabuada trabalha com números inteiros.
numero = int(input("Tabuada de qual número? "))


# 2. Repetição
# O for repete um bloco de código para cada valor de uma sequência.
# range(1, 11) gera os números de 1 até 10:
# o início (1) é incluído, mas o fim (11) não.
# Por isso usamos 11, para que o 10 também apareça.
# A variável multiplicador assume um valor novo a cada volta do laço (1, 2, 3, ... 10).
# Dentro do bloco, que fica indentado, calculamos o resultado da volta atual
# e exibimos uma linha da tabuada.
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
```

## ▶️ Exemplos de entrada e saída

O que o usuário digita aparece logo depois de cada pergunta.

```text
Tabuada de qual número? 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

## 📓 O que fica deste exercício

- O `for` repete o bloco indentado uma vez para cada valor da sequência.
- `range(1, 11)` começa em 1 e termina em 10: o valor final nunca é incluído.
- A variável do laço (`multiplicador`) muda a cada volta, e é ela que torna cada linha diferente.

## 🔌 Aplicação prática

Percorrer itens um a um é a base para processar uma base de dados linha por linha, ideia que será retomada com listas (módulo 02) e com o Pandas (módulo 06).

---

← [Exercício 07](ex07_situacao_do_aluno.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Módulo 01](../README.md) →
