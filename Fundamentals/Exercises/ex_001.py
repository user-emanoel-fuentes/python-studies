### 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.
print("Alo mundo")

### 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."
numero = input("Informe um número: ")
texto = "O número informado foi {}".format(numero)
print(texto)

### 3. Faça um Programa que peça dois números e imprima a soma.
numero_1 = input("Informe um número: ")
numero_2 = input("Informe outro número: ")
texto = f"A soma dos números é {int(numero_1) + int(numero_2)}"
print(texto)

### 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
nota_1 = input("Informe a nota do primeiro bimestre: ")
nota_2 = input("Informe a nota do segundo bimestre: ")
nota_3 = input("Informe a nota do terceiro bimestre: ")
nota_4 = input("Informe a nota do quarto bimestre: ")
media = (int(nota_1) + int(nota_2) + int(nota_3) + int(nota_4)) / 4 
texto = f"A média das notas é {float(media)}"
print(texto)

### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).
metros = input("Informe um comprimento em metros(m), e retornarei o seu valor em centímetros(cm): ")
centimentros = float(metros) * 100
texto = f"O valor de {metros}m é igual a {centimentros}cm."
print(texto)

### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
largura = input("Informe a largura da sala em metros(m): ")
comprimento = input("Informe o comprimento da sala em metros(m): ")
area = float(comprimento) * float(largura)
texto = f"A área da sala é de {area}m²."
print(texto)

### 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = input("informe quanto você ganha por hora: ")
horas_trabalhadas = input("Informe o número de horas trabalhadas no mês: ")
salario = float(valor_hora) * float(horas_trabalhadas)
texto = f"O total do seu salário no referido mês é de R${salario:,.2f}."
print(texto)