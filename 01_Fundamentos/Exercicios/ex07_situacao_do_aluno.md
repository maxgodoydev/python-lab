# Exercício 07 · if, elif e else: situação do aluno

← [Exercício 06](ex06_maior_de_idade.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 08](ex08_tabuada_com_for.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | `if` / `elif` / `else` · operador lógico `or` · validação de entradas · casos-limite |
| **Para executar** | [`ex07_situacao_do_aluno.py`](ex07_situacao_do_aluno.py) |

## 🎯 Objetivo

Classificar um resultado em faixas e validar as entradas antes de calcular.

## 📝 Enunciado

Peça duas notas (de 0 a 10) e calcule a média. Classifique o aluno:

- média de 7 ou mais: **Aprovado**
- média de 5 até menos de 7: **Recuperação**
- média abaixo de 5: **Reprovado**

Se alguma nota estiver fora do intervalo de 0 a 10, exiba um aviso e não calcule a média.

## 💻 Solução comentada

```python
# 1. Leitura das notas
# Convertemos as entradas para float, como no exercício 05, para poder calcular.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))


# 2. Validação das notas
# Antes de calcular, conferimos se as notas fazem sentido (de 0 a 10).
# O operador or significa "ou": a condição é verdadeira
# se qualquer uma das partes for verdadeira.
# Guardamos o resultado dessa checagem em notas_invalidas (True ou False)
# para deixar o if logo abaixo mais fácil de ler.
notas_invalidas = nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10


# 3. Decisão
# Se as notas forem inválidas, apenas avisamos o usuário e não calculamos nada.
# Caso contrário, calculamos a média e classificamos o aluno.
if notas_invalidas:
    print("Notas inválidas: use valores entre 0 e 10.")
else:
    media = (nota1 + nota2) / 2

    # O if / elif / else testa as condições na ordem, de cima para baixo,
    # e executa apenas o primeiro bloco cuja condição for verdadeira.
    # Por isso a ordem importa: se a média chegou até o elif,
    # já sabemos que ela é menor que 7, então basta testar se é pelo menos 5.
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # 4. Exibição
    # Cada bloco apenas guarda o texto em situacao,
    # e exibimos o resultado uma única vez aqui.
    # Assim não repetimos os print() em cada ramo do if.
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
```

## ▶️ Exemplos de entrada e saída

O que o usuário digita aparece logo depois de cada pergunta.

**Aprovado**

```text
Nota 1: 8
Nota 2: 7
Média: 7.50
Situação: Aprovado
```

**Caso-limite: média exatamente 7**

```text
Nota 1: 7
Nota 2: 7
Média: 7.00
Situação: Aprovado
```

**Caso-limite: média exatamente 5**

```text
Nota 1: 4.5
Nota 2: 5.5
Média: 5.00
Situação: Recuperação
```

**Reprovado**

```text
Nota 1: 4
Nota 2: 3.5
Média: 3.75
Situação: Reprovado
```

**Nota inválida**

```text
Nota 1: 11
Nota 2: 5
Notas inválidas: use valores entre 0 e 10.
```

## 📓 O que fica deste exercício

- No `if` / `elif` / `else`, vence o primeiro bloco verdadeiro; por isso a ordem das condições importa.
- O operador `or` combina condições, e guardar o resultado em uma variável deixa o `if` mais legível.
- Validar antes de calcular evita resultados sem sentido, e os casos-limite (7 e 5) precisam ser testados.
- Guardar a classificação em uma variável e exibir uma única vez evita repetir `print()` em cada ramo.

## 🔌 Aplicação prática

Classificar registros em faixas (desempenho, risco, categoria) é muito comum em indicadores. A validação antes do cálculo é a versão básica da checagem de qualidade de dados.

---

← [Exercício 06](ex06_maior_de_idade.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 08](ex08_tabuada_com_for.md) →
