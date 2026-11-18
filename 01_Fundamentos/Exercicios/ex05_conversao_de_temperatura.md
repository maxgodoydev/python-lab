# Exercício 05 · Conversão de tipos: Celsius para Fahrenheit

← [Exercício 04](ex04_media_de_tres_notas.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 06](ex06_maior_de_idade.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | conversão de tipos com `float()` · ordem das operações · f-string com `:.1f` |
| **Para executar** | [`ex05_conversao_de_temperatura.py`](ex05_conversao_de_temperatura.py) |

## 🎯 Objetivo

Converter o texto recebido por `input()` em número e usá-lo em uma fórmula.

## 📝 Enunciado

Peça uma temperatura em graus Celsius, converta para Fahrenheit com a fórmula `F = C × 9 ÷ 5 + 32` e exiba o resultado com uma casa decimal.

## 💻 Solução comentada

```python
# 1. Leitura da temperatura
# O input() sempre devolve texto, mesmo quando digitamos um número.
# Para fazer contas, precisamos converter esse texto em número.
# Por isso colocamos o input() dentro de float(), que transforma o texto em decimal.
# Escolhemos float (e não int) porque temperaturas podem ter casas decimais, como 36.5.
# A conversão acontece de dentro para fora: o input() recebe o texto,
# o float() converte esse texto, e só então o número é armazenado em celsius.
celsius = float(input("Temperatura em Celsius: "))


# 2. Conversão para Fahrenheit
# Aplicamos a fórmula F = C * 9 / 5 + 32 e armazenamos o resultado em fahrenheit.
# O Python segue a ordem da matemática: multiplicação e divisão acontecem
# antes da soma, então não precisamos de parênteses nessa fórmula.
fahrenheit = celsius * 9 / 5 + 32


# 3. Exibição do resultado
# Reutilizamos a f-string do exercício anterior.
# Aqui usamos :.1f para mostrar uma casa decimal.
# Por exemplo, 97.7 continua 97.7, e o número 32 aparece como 32.0.
print(f"{celsius:.1f} °C equivalem a {fahrenheit:.1f} °F")
```

## ▶️ Exemplos de entrada e saída

O que o usuário digita aparece logo depois de cada pergunta.

**Entrada comum**

```text
Temperatura em Celsius: 36.5
36.5 °C equivalem a 97.7 °F
```

**Caso-limite: -40 °C (o ponto em que as duas escalas coincidem)**

```text
Temperatura em Celsius: -40
-40.0 °C equivalem a -40.0 °F
```

## 📓 O que fica deste exercício

- `input()` devolve `str`; `float()` e `int()` convertem o texto em número antes das contas.
- A ordem das operações segue a matemática: `*` e `/` antes de `+`.
- Se o usuário digitar algo que não é número (como `abc`), o Python interrompe com `ValueError`. Tratar esse erro será assunto do módulo 04.

## 🔌 Aplicação prática

Ao ler um CSV, os valores chegam como texto e precisam virar números antes de qualquer cálculo. A conversão de tipos é uma etapa comum na preparação de dados.

---

← [Exercício 04](ex04_media_de_tres_notas.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 06](ex06_maior_de_idade.md) →
