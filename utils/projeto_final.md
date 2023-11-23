# Projeto - Lógica de Programação II

**Professor**: Alex Lima<br>
**Empresa**: Ada<br>
**Projeto**: ifood - vem ser tech | DS

**Descrição**<br>
Este notebook contém a descrição do projeto prático do módulo: Lógica de programação II. Neste projeto aplicaremos as técnicas aprendidas em aula para criarmos um sistema de controle de estoque.

**Objetivo**: Criar um sistema de controle de estoque. O programa deve forncer as seguintes funcionalidades:
- Cadastrar produto
- Consultar produto
- Listar produtos cadastrados
- Atualizar cadastro
- Excluir cadastro

## Especificação das funcionalidades

### Menu principal
```
Crie uma tela de boas-vindas com um menu informando ao usuário as opções do programa:
Boas vindas ao nosso sistema:

1 - Cadastrar produto
2 - Consultar produto
3 - Listar produtos cadastrados
4 - Atualizar cadastro
5 - Excluir cadastro
6 - Sair
```

### 1 - Cadastrar produto
Ao selecionar a opção `1 - Cadastrar produto`, o programa deve exibir uma tela de cadastro com campos para que o usuário cadastre um produto. O sistema deve possibilitar o cadastro de diferentes tipos de produtos. Cada produto deve ter:

- ID (número identificador único);
- Nome;
- Especificações (características como peso, altura, cor, tamanho, etc. As especificações e a quantidade de especificações podem variar de acordo com o produto);
- Quantidade do produto no estoque;
- Texto descritivo opcional para cada produto.

### 2 - Consultar produto
Ao selecionar a opção `2 - Consultar produto`, o programa deve exibir um campo para o usuário inserir o id de um produto. Em seguida, caso o ID exista na base, os dados do produto devem ser exibidos, caso não exista, uma mensagem informando que o produto não existe deve ser exibida.

### 3 - Listar produtos cadastrados
Ao selecionar a opção `3 - Listar produtos cadastrados`, o programa deve exibir ID e nome de todos os produtos cadastrados.

### 4 - Atualizar cadastro
Ao selecionar a opção `4 - Atualizar cadastro`, o programa deve exibir um campo para o usuário inserir o id de um produto. Em seguida, caso o ID exista na base, uma tela de cadastro deve ser exibida e os dados inseridos devem substituir os dados já existentes para o produto selecionado. Caso o ID não exista na base, uma mensagem informando que o produto não existe deve ser exibida.

### 5 - Excluir cadastro
Ao selecionar a opção `5 - Excluir cadastro`, o programa deve exibir um campo para o usuário inserir o id de um produto. Em seguida, caso o ID exista na base, os dados do produto devem ser excluídos, caso não exista, uma mensagem informando que o produto não existe deve ser exibida.

### 6 - Sair
Ao selecionar a opção `Sair`, o programa deve encerrar com sucesso.

### Base de dados
A base de dados deve ser mantida em um arquivo de texto. A base deve armazenar todos os produtos cadastrados, não excluídos e com dados atualizados.

### Tratamento de erros
Lembramos que podem ser inseridos dados que não condizem exatamente com o tipo esperado. Neste caso, é importante realizar o tratamento de erros quando necessário.

### Avaliação e prazo
O projeto deve ser entregue via e-mail até o dia 24/11/2023 às 23:59 contendo todos os artefatos relacionados (arquivos .py, jupyter notebooks e bases de dados). A apresentação do projeto será dia 24/11/2023 durante o horário da aula com tempo máximo de 20 min.

**Todo progresso apresentado ou encaminhado contará de forma positiva na avaliação.**
**E-mail para envio do projeto e solução de dúvidas**: alexlimacavalera@gmail.com