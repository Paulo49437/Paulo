def main():
   email = input("Digite o email do paciente: ")
   idade = int ( input ("Digite a idade do paciente"))
   altura = float(input(" Digite a altura do paciente"))
   isSaudavel = input("Ele esta saudavel? ")

   print("Email do paciente", email, " a sua idade é ", idade, "E sua", altura)
   if isSaudavel == "Sim" or isSaudavel == "S": 
      print("O paciente está saudavel")
   elif isSaudavel =="Esta":
      print("O paciente está saudavel")
   else:
      print("O paciente não está saudavel")
   return 0
main()