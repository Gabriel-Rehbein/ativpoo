Construir código necessário em Python para implementar o seguinte projeto: 

-> Uma classe Categoria que possui os atributos id e nome. 

-> Uma classe abstrata chamada de Produto que contém os atributos/propriedades: modelo, cor, preço e categoria. 

     -> Esta classe possui um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

--> O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Produto.
    A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. Esta classe reimplementa o método getInformacoes() herdado de Produto.

--> A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. Esta classe reimplementa o método getInformacoes() herdado de Produto.
 
---> Construa getters e setters para os atributos que não forem públicos. Todas as classes devem ter um método construtor.

-----> Construa uma interface gráfica que permita ao usuário cadastrar Desktops e Notebooks. 

Crie um repositório no github, faça commit e push para este repositório e entreque aqui apenas o link do repositório.
