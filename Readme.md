<h1 align="center"> Controle de Estoque - iFood </h1>
<h4 align="center"> Vem ser Tech | Dados - <a href="https://www.linkedin.com/school/adatechbr">Ada Tech</a> (Primavera 2023) </h4>

<br></br>

<p align="center"> 
  <a href="https://cdn.myportfolio.com/c8489c04-75f1-4bdc-b062-ae01d51f5d5a/2fd05462-bfe4-425f-a5c0-2bf47941914e_rwc_0x0x1244x1656x1244.gif?h=e226d8389a084ed355a8e3f7929c7357" target="_blank"><img src="https://cdn.myportfolio.com/c8489c04-75f1-4bdc-b062-ae01d51f5d5a/2fd05462-bfe4-425f-a5c0-2bf47941914e_rwc_0x0x1244x1656x1244.gif?h=e226d8389a084ed355a8e3f7929c7357" alt="image host" height="200px"/></a>
</p>

<h4>
  <p align="center">
    <a href="#creditos">Créditos</a> | <a href="#contexto">Contexto e objetivo</a> | <a href="#especificacao">Especificação</a> | <a href="#tecnologias">Tecnologias</a> | <a href="#organizacao">Organização dos arquivos </a> | <a href="#execucao">Instalação e Execução</a> | <a href="#equipe">Equipe</a>
  </p>
</h4>

<h2 id="creditos"> :scroll: CRÉDITOS</h2>

- Instituição: Let's Code <a href="https://www.linkedin.com/school/adatechbr/">(Ada Tech)</a>
- Curso: Vem ser Tech | Dados
- Disciplina: Lógica de Programação II
- Professor(es): Alex Lima Cavalera

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="contexto"> 📊: CONTEXTO E OBJETIVO</h2>

O desenvolvimento do projeto dar-se-á conclusão do módulo II do curso Vem ser Tech | Dados, consistindo em um sistema simples de controle de estoque para restaurantes.

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="especificacao"> :books: ESPECIFICAÇÃO</h2>

A especificação completa pode ser encontrada em [Projeto Final](./utils/projeto_final.md)

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="tecnologias"> 🛠️ TECNOLOGIAS UTILIZADAS </h2>

<ul>
  <li>Python</li>
  <p>A linguagem utilizada para o desenvolvimento fora <strong>Python</strong>, tanto por ser a ferramenta de aprendizado utilizada durante o curso, quanto por ser uma linguagem de alto nível, orientada a objetos, funcional e de tipagem dinâmica e forte.</p>

  <li>JSON</li>
  <p>Sendo uma importante ferramenta utilizada para trocar informações entre um servidor e um cliente, além de seu formato de dados leve e de fácil leitura, o JSON, neste projeto, fora utilizado de forma que cada entrada representa um restaurante e é definida como um objeto detentor de várias propriedades, como uma matriz de objetos que descrevem os itens do cardápio ou vendas anteriores.</p>

  <li>OS</li>
  <p>A biblioteca <strong>OS</strong> fornece funcionalidades para interagir com o sistema operacional, como manipular arquivos, pastas e variáveis de ambiente.</p>

  <li>Platform</li>
  <p>A biblioteca <strong>Platform</strong> permite ao programa obter informações sobre a plataforma na qual ele está sendo executado, como o sistema operacional e a arquitetura do sistema.</p>

  <li>Termcolor</li>
  <p>A biblioteca <strong>Termcolor</strong> é utilizada para exibir textos coloridos no terminal.</p>

  <li>Pynput</li>
  <p>A biblioteca <strong>Pynput</strong> é utilizada para monitorar e controlar os dispositivos de entrada, como mouse e teclado.</p>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="organizacao"> 📂 ORGANIZAÇÃO DOS ARQUIVOS </h2>

<p>Este projeto inclui arquivos executáveis e de destino, além de acesso ao diretório fonte (repositório), como a seguir:</p>

```sh
Controle-de-Estoque-iFood
├── controle_de_estoque
│   ├── database
│   │   └── json_db.json
│   ├── __init__.py
│   └── src
│       ├── json_manipulation.py
│       ├── main.py
│       ├── Menu.py
│       └── restaurant.py
├── Readme.md
└── utils
    ├── environment.yml
    ├── projeto_final.md
    └── requirements.txt
```

<h4>➔ Arquivos executáveis:</h4>
<ul>
  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/main.py"><b>main.py</b></a> - Contém o código-fonte responsável pelos menus disponíveis para o restaurante parceiro e para o cliente (incluindo procedimentos de cadastro, validação de pedidos através da disponibilidade do produto em estoque, mensagens de erro para entradas inválidas etc.). </li>
  
  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/json_manipulation.py"><b>json_manipulation.py</b></a> - Define um conjunto de funções para lidar com a criação, leitura, validação, gravação e manipulação dos dados em formato JSON no arquivo importado no cabeçalho do código. </li>
  
  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/restaurant.py"><b>restaurant.py</b></a> - As funcionalidades deste código reduzem o estoque do item quando este é confirmado, incrementam o contador de pedidos do restaurante, criam um dicionário representando a solicitação e adicionam o pedido ao histórico de vendas do restaurante. </li>

  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/Menu.py"><b>Menu.py</b></a> - As funcionalidades deste código foram desenvolvidas utilizando o paradigma de programação orientada a objetos, sendo responsável por criar os menus dinâmicos, exibindo as opções disponíveis e retornando a opção escolhida pelo usuário. </li>
</ul>

<h4>➔ Bibliotecas utilizadas:</h4> 
<ul>
  » No arquivo <a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/Menu.py"><b>Menu.py</b>:</a>
  <li><b>import os</b>: fornece funcionalidades para interagir com o sistema operacional, como manipular arquivos, pastas e variáveis de ambiente. </li>
  <li><b>import platform</b>: permite ao programa obter informações sobre a plataforma na qual ele está sendo executado, como o sistema operacional e a arquitetura do sistema. </li>
  <li><b>import termcolor</b>: utilizada para exibir textos coloridos no terminal. </li>
  <li><b>import pynput</b>: utilizada para monitorar e controlar os dispositivos de entrada, como mouse e teclado. </li>
</ul>

<ul>
  » Nos arquivos 
  <a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/json_manipulation.py"><b>json_manipulation.py</b></a> e <a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/src/restaurant.py"><b>restaurant.py</b></a>

  <li><b>from uuid import uuid4</b>: sendo uma importação específica do módulo uuid, permite a geração de chaves primárias. </li>
</ul> 

<h4>➔ Módulos internos:</h4> 
<ul>
  » No arquivo <a href="https://github.com/ligianogueira1/Bot_Discord_IFPB/blob/main/main.py"><b>main.py</b>:</a> </li>
  <li><b>from src.Menu import Menu</b>: importa a classe Menu do módulo "Menu" localizado no diretório "src." </li>
  
  <li><b>from src.restaurante import *</b>: esta linha importa todas as funções, classes e variáveis definidas no módulo "restaurant", localizado no diretório "src." Isso significa que o código pode utilizar todas as definições deste módulo em todo o programa. </li>

  <li><b>from src.json_manipulation import *</b>: importa todas as funções e variáveis definidas no módulo "json_manipulation" localizado no diretório "src." </li>
</ul>

<h4>➔ Arquivos de destino:</h4> 
<ul>
  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/blob/main/controle_de_estoque/database/json_db.json"><b>json_db.json</b>:</a> Contém informações fictícias sobre usuários e restaurantes, sendo utilizado como um pequeno banco de dados para o projeto. </li>
</ul>

<h4>➔ Diretório fonte:</h4>
<ul>
  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/controle-de-estoque"><b>Controle-de-Estoque-iFood/controle_de_estoque</b>:</a> Inclui todos os arquivos listados acima. </li>
  <li><a href="https://github.com/brunorreiss/Controle-de-Estoque-iFood/utils"><b>Controle-de-Estoque-iFood/utils</b>:</a> Inclui todos os arquivos utilitários, como de dependências e especificação do projeto final. </li>
</ul>

<a href="https://imgbox.com/3tZuCnVg" target="_blank"><img src="https://images2.imgbox.com/42/88/3tZuCnVg_o.png" alt="image host" height="5px" width="900px"/></a>

<h2 id="execucao"> 🖥️ INSTALAÇÃO E EXECUÇÃO</h2>

Foi utilizado o [Python](https://www.python.org/) v3.9.18.

<h2 id="Anaconda"> :snake: ANACONDA</h2>

No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create -f environment.yml
```

- Ativar
```sh
conda activate controle_de_estoque
```

- Desativar
```sh
conda deactivate
```

<h2 id="Requirements"> :snake: REQUIREMENTS</h2>

Pode-se utilizar o arquivo requirements.txt para criar o ambiente virtual.

- Criar ambiente virtual
```sh
python -m venv controle_de_estoque
```

- Ativar
```sh
source ./controle_de_estoque/bin/activate
```

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```

<h2 id="Inicializar projeto"> :snake: Inicializar projeto</h2>

- Navegar até a pasta de destino
```sh
cd controle_de_estoque
```

- Execute o programa
```sh
python __init__.py
```

- Observação: O programa foi desenvolvido de forma dinâmica e interativa, portanto, deve-se utilizar as setas do teclado para navegar entre as opções e pressionar a tecla "Enter" para selecionar a opção desejada.

<h2 id="equipe"> :brain: EQUIPE</h2>

Projeto desenvolvido pelos Devs:

- [Anna Lígia Nogueira](https://github.com/ligianogueira1)
- [Bruno Reis](https://github.com/brunorreiss)
- [Gabriel Victor](https://github.com/gabrielvmdvital)
- [Guilherme Pereira](https://github.com/Guilhermepsilva003)
- [Matheus Miranda Brandão](https://github.com/MatBrands)