from random import randint
while True:
    comp = randint(1,10)
    tentativa = 0
    while True:


        while True:

            user = int(input("qual foi o numero escolhido por mim? "))
            if user < 1 or user > 10:
                print("digite um numero entre 1 e 10")
                continue
            else:
                break

        print(f"voce escolheu o numero {user}")
        tentativa = tentativa + 1

        if comp  == user :
            print(f"voce acertou na {tentativa} tentativa")
            break
                    


        elif comp > user:
            print("maior")

        else:
            print("menor")
        
    escolha = input("deseja continuar? [S/N]").upper().strip()

    if escolha == "N":
        print("obrigado por jogar!!")
        break
        

