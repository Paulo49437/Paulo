def main ():
  
    idade = int (input("Digite a idade da pessoa:"))
    if idade >= 18:
        print("Entrada liberada")
    elif idade >= 16:
         acomp = input("está acompanhado")

         if acomp == "Sim":
            print("Entrada liberada")

         else:
            print("entrada proibida")
    else:
        print("entrada proibida")
    return 0
main()