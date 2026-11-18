# Exercício 03 · Entrada de dados: saudação personalizada

← [Exercício 02](ex02_variaveis_e_tipos.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 04](ex04_media_de_tres_notas.md) →

| | |
|---|---|
| **Módulo** | [01 · Fundamentos e lógica de programação](../README.md) |
| **Conceitos** | `input()` · retorno sempre em texto (`str`) · concatenação com `+` |
| **Para executar** | [`ex03_entrada_de_dados.py`](ex03_entrada_de_dados.py) |

## 🎯 Objetivo

Receber informações digitadas pelo usuário com `input()` e montar uma mensagem com elas.

## 📝 Enunciado

Peça ao usuário o nome e o curso. Em seguida, exiba duas mensagens usando as respostas:

- `Olá, <nome>!`
- `Bem-vindo(a) ao curso de <curso>.`

## 💻 Solução comentada

```python
# 1. Pergunta do nome
# O input() mostra a mensagem na tela, espera o usuário digitar e apertar Enter,
# e devolve o que foi digitado.
# Armazenamos esse retorno na variável nome para poder usá-la nas próximas etapas.
# Importante: o input() sempre devolve texto (str),
# mesmo que o usuário digite um número.
nome = input("Qual é o seu nome? ")


# 2. Pergunta do curso
# Repetimos a ideia para guardar a segunda informação em outra variável.
curso = input("Qual é o seu curso? ")


# 3. Mensagem personalizada
# O operador + junta (concatena) textos: montamos a frase unindo pedaços fixos
# com o conteúdo das variáveis.
# Atenção aos espaços dentro das aspas: sem o espaço depois da vírgula em "Olá, ",
# o nome ficaria colado na palavra anterior.
print("Olá, " + nome + "!")
print("Bem-vindo(a) ao curso de " + curso + ".")
```

## ▶️ Exemplos de entrada e saída

O que o usuário digita aparece logo depois de cada pergunta.

**Entrada comum**

```text
Qual é o seu nome? Ana
Qual é o seu curso? DSM
Olá, Ana!
Bem-vindo(a) ao curso de DSM.
```

**Caso-limite: nome em branco (só Enter)**

```text
Qual é o seu nome?
Qual é o seu curso? DSM
Olá, !
Bem-vindo(a) ao curso de DSM.
```

## 📓 O que fica deste exercício

- O `input()` pausa o programa, mostra a pergunta e devolve sempre uma `str`.
- O `+` junta textos, mas só entre `str`; por isso os espaços precisam estar dentro das aspas.
- Limitação: sem validação, um nome em branco gera `Olá, !`. Validar entradas com condicionais vem nos exercícios 06 e 07.

## 🔌 Aplicação prática

Programas que dependem de informação externa, seja digitada, vinda de arquivo ou de uma API, começam recebendo e guardando valores em variáveis, como fazemos aqui com `input()`.

---

← [Exercício 02](ex02_variaveis_e_tipos.md) &nbsp;·&nbsp; [📚 Módulo 01](../README.md) &nbsp;·&nbsp; [Exercício 04](ex04_media_de_tres_notas.md) →
