# Restaurant Orders 🍴

O Restaurant Orders é uma ferramenta de construção de cardápios que gera cardápios de acordo com a disponibilidade de produtos no estoque e considera itens com possíveis restrições alimentares. 
Neste projeto foram implementadas classes e testes visando assegurar o correto funcionamento do código. Estes serão descritos a seguir:

- A classe Dish representa um prato do cardápio e é utilizada para criar objetos que contêm informações sobre um prato específico, incluindo seu nome, preço e ingredientes.
  
- A classe Ingredient é responsável por representar um ingrediente do cardápio, contendo o nome do ingrediente e a lista de restrições associadas a ele.
  
- A classe MenuData é responsável por carregar os dados do cardápio a partir de um arquivo externo recebido como parâmetro no momento que a classe é instanciada e criar objetos Dish com suas respectivas informações de ingredientes e quantidade.
  
- A classe MenuBuilder é responsável por controlar o inventário dos ingredientes disponíveis, criar e gerenciar o cardápio.
  
- A classe InventoryMapping é responsável mapear e controlar o inventário de ingredientes.
  
- Foram desenvolvidos testes para a classe Ingredient e para a classe Dish. Eles verificam se a classes podem ser instanciadas corretamente de acordo com a assinatura esperada, e se os seus métodos e atributos funcionam conforme o esperado.


## Objetivo
Esse projeto foi desenvolvido visando praticar o conceito de *Hashmaps* através das estruturas de dados **Dict** e **Set** do Python, além de aprimorar meus conhecimentos de programção orientada a objetos e conhecimentos de teste de software.

## Tecnologias utilizadas
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pytest](https://img.shields.io/badge/-pytest-%43B02A?style=for-the-badge&logo=pytest&logoColor=white)

## Instalação e execução
Caso queira ver mais sobre o projeto em sua maquina local siga as etapas:

1. Clone o repositorio 

```bash
  git clone git@github.com:amanda-vlopes/restaurant-orders.git
```

2. Entre no diretório do projeto

```bash
  cd restaurant-orders
```

3. Crie e ative o ambiente virtual

```bash
  python3 -m venv .venv && source .venv/bin/activate
```

O que é?

O Python oferece um recurso chamado de ambiente virtual que permite rodar em sua maquina diferentes tipos de projetos em diferentes versões de bibliotecas, sem nenhum conflito.

4. Instale as dependências

```bash
  python3 -m pip install -r dev-requirements.txt
```
