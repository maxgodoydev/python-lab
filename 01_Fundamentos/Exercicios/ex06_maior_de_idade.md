# Exercício 06 · Condicional: maior ou menor de idade

← [Exercício 05](ex05_conversao_de_temperatura.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 07](ex07_situacao_do_aluno.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | `if` e `else` · operadores de comparação · indentação · caso-limite |
| **Para executar** | [`ex06_maior_de_idade.py`](ex06_maior_de_idade.py) |

## 🎯 Objetivo

Tomar uma decisão no programa com `if` e `else`.

## 📝 Enunciado

Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.

## 💻 Solução comentada

```python
# 1. Leitura da idade
# Convertemos a entrada para int porque a idade é um número inteiro
# e precisamos compará-la com outro número.
idade = int(input("Qual é a sua idade? "))


# 2. Decisão
# O if testa uma condição. Se ela for verdadeira (True),
# o bloco abaixo dele é executado.
# Caso contrário, o Python executa o bloco do else.
# Usamos >= ("maior ou igual") em vez de >, porque quem tem exatamente 18 anos
# já é maior de idade. Esse é o caso-limite que precisamos acertar.
# Os dois-pontos (:) abrem cada bloco, e a indentação (4 espaços) indica
# quais linhas pertencem a ele.
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

## ▶️ Exemplos de entrada e saída

O que o usuário digita aparece logo depois de cada pergunta.

**Entrada comum**

```text
Qual é a sua idade? 20
Você é maior de idade.
```

**Caso-limite: exatamente 18**

```text
Qual é a sua idade? 18
Você é maior de idade.
```

**Menor de idade**

```text
Qual é a sua idade? 17
Você é menor de idade.
```

## 📓 O que fica deste exercício

- O `if` executa um bloco quando a condição é verdadeira; o `else` cobre o restante dos casos.
- Operadores de comparação: `==`, `!=`, `>`, `<`, `>=` e `<=`; cada comparação resulta em `True` ou `False`.
- A indentação faz parte da sintaxe, e o caso-limite (18) mostra por que escolhemos `>=` e não `>`.
- Este exercício não trata idades negativas; esse tipo de validação aparece no exercício 07.

## 🔌 Aplicação prática

Regras de negócio simples, como elegibilidade, desconto ou acesso, viram condicionais. Em análise de dados, a mesma lógica reaparece como filtros sobre uma base.

---

← [Exercício 05](ex05_conversao_de_temperatura.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 07](ex07_situacao_do_aluno.md) →
