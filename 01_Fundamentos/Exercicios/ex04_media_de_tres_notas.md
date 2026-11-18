# Exercício 04 · Média de três notas

← [Exercício 03](ex03_entrada_de_dados.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 05](ex05_conversao_de_temperatura.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | operadores aritméticos (`+` e `/`) · variável que guarda o resultado calculado · f-string · formatação `:.2f` |
| **Para executar** | [`ex04_media_de_tres_notas.py`](ex04_media_de_tres_notas.py) |

## 🎯 Objetivo

Fazer um cálculo com operadores aritméticos, guardar o resultado em uma variável e exibi-lo formatado.

## 📝 Enunciado

Guarde três notas em variáveis (8.5, 7.0 e 9.0), calcule a média aritmética e exiba o resultado com duas casas decimais.

## 💻 Solução comentada

```python
# 1. Variáveis das notas
# Utilizamos variáveis para armazenar as notas dos usuários.
nota1 = 8.5
nota2 = 7.0
nota3 = 9.0


# 2. Variável da média
# Criamos outra variável para armazenar o resultado de uma operação matemática.
# Dessa forma, podemos chamar media posteriormente para acessar o resultado,
# sem precisar realizar o cálculo novamente.
media = (nota1 + nota2 + nota3) / 3


# 3. Exibição do resultado
# O print() vai exibir o resultado do código na tela.
# O f antes das aspas indica que estamos utilizando uma f-string.
# Esse recurso permite combinar textos com valores de variáveis na mesma frase.
# As chaves {} indicam onde queremos inserir o valor de uma variável.
# Por exemplo, {media} será substituído pelo valor armazenado em media.
# :.2f define que o número será apresentado com duas casas decimais.
# Por exemplo, 8.1666 será exibido como 8.17.
print(f"Média final: {media:.2f}")
```

## ▶️ Resultado esperado

```text
Média final: 8.17
```

## 📓 O que fica deste exercício

- A variável `media` guarda o resultado calculado, e não a conta: a expressão é executada no momento da atribuição.
- O operador `/` faz divisão e sempre devolve um `float`.
- A f-string combina texto e variáveis, e `:.2f` ajusta apenas a exibição (duas casas decimais), sem alterar o valor guardado.

## 🔌 Aplicação prática

Médias são um dos indicadores mais comuns em análise de dados. No módulo 06, o Pandas calcula a média de colunas inteiras; entender o cálculo feito à mão ajuda a conferir esses resultados.

---

← [Exercício 03](ex03_entrada_de_dados.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 05](ex05_conversao_de_temperatura.md) →
