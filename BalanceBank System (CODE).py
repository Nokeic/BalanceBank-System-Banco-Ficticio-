import getpass
import random
import math

print("Bem vindo ao BalanceBank! (Banco Fictício!)\n")
print("*ATENÇÃO* Há um easter egg no sistema!\n")

while True:
    email1 = input("Porfavor, Insira um email: ")
    if email1 == "userAdmin" or email1 == "teste":
        break

    if not email1:
        print("Você não inseriu um email. Tente novamente.")
        continue # Volta ao inicio do loop

    if "@" not in email1:
        print("O Email deve conter um caractere '@'.")
        continue  # Volta ao início do loop

    if "gmail.com" in email1 or "hotmail.com" in email1 or "outlook.com" in email1:
        break # Quebra o loop
    else:
        print("O Email deve conter um dominio depois do '@' Dominios disponiveis abaixo: \n gmail.com \n hotmail.com \n outlook.com")

print("*AVISO* Sua senha será mascarada, mas ela estará sendo digitada!")
while True:
    senha1 = getpass.getpass("Porfavor, insira uma senha: ")
    if senha1 == "28082009":
        break # Quebra o loop

    if len(senha1) < 6:
        print("O minimo de caracteries para a senha é 6!")
    else:
        break # Quebra o loop

while True:
    email2 = input("\nAgora iremos logar, porfavor insira seu email registrado: ")
    if email1 == "userAdmin":
        break
    if email2 != email1:
        print("\nEmail inválido. Porfavor insira o email registrado.")
    else:
        break # Quebra o loop
while True:
    senha2 = getpass.getpass("Agora sua senha: ")
    if senha2 == "28082009" or senha1 == "28082009":
        break
    if senha2 != senha1:
        print("Senha incorreta. Pofavor insira a senha correta.")
    else:
        break # Quebra o loop

saldo_banco = random.randint(800, 2300)
saldo_mao = random.randint(200, 600)

if email2 == "userAdmin" or email1 == "userAdmin" and senha1 == "28082009" or senha2 == "28082009":
    saldo_banco = math.inf
    saldo_mao = math.inf

print("O sistema detectou que você tem R$", saldo_banco, "no banco e R$", saldo_mao, "Na mão")

d_or_s = input("\nÓtimo! Agora escolha: Depositar(D) Sacar(S) ")

if d_or_s == "D" or d_or_s == "d":
   valor1 = float(input("(Depositar escolhido) Insira o valor desejado (APENAS NUMEROS): "))
   if valor1 > saldo_mao:
        print(f"NEGADO! Você não possui valor suficiente.")
        input("Aperte enter para sair!")
        exit()
   if valor1 <= saldo_banco:
        saldo_banco += valor1
        saldo_mao -= valor1
        print(f"SUCESSO! Você depositou R${valor1:.2f} na sua conta, agora você tem R$", saldo_banco, "No banco")
        input("Aperte enter para sair!")
        exit()

if d_or_s == "S" or d_or_s == "s":
    valor2 = float(input("(Sacar escolhido) Insira o valor desejado (APENAS NUMEROS): "))
    if valor2 > saldo_banco:
        print("NEGADO! Você não tem saldo o suficiente")
        input("Aperte enter para sair!")
        exit()
    elif valor2 <= saldo_banco:
        saldo_banco -= valor2
        saldo_mao -= valor2
        print(f"SUCESSO! Você sacou R${valor2:.2f} da sua conta, agora você tem R$", saldo_banco, "No banco" )
        input("Aperte enter para sair!")
        exit()