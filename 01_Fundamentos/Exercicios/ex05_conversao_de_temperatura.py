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
