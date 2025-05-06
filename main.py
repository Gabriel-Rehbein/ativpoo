from Atividade import Categoria, Desktop, Notebook #Puxando o arquivo para executar aqui!

def main():
   
    categoria1 = Categoria(1, "Informática")
    categoria2 = Categoria(2, "Portáteis")

    
    desktop = Desktop(
        modelo="computador_1",
        cor="Preto chumbo",
        preco=6000.00,
        categoria=categoria1,
        potenciaDaFonte=750
    )

   
    notebook = Notebook(
        modelo="computador_2",
        cor="Prata Bonito",
        preco=7000.00,
        categoria=categoria2,
        tempoDeBateria=10
    )

    
    desktop.cadastrar()
    notebook.cadastrar()

    
    print("\nInformações do Desktop:")
    print(desktop.getInformacoes())

    print("\nInformações do Notebook:")
    print(notebook.getInformacoes())

if __name__ == "__main__":
    main()


#Precisei de ajuda da IA para fazer o main, achei confuso na hora de executar. Não consegui fazer a inteface GUI... 
#Estou recem me lembrando de POO, vou dar uma estudada es TKinter que era a ineface que eu usava.
#Fiquei meio confuso na diferença entre get e set... não entendi na real o que elas fazem na partica.
