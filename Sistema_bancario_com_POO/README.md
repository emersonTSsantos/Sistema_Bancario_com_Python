# Sistema Bancário Simples

## Visão Geral

Este projeto é um sistema bancário simples desenvolvido em Python. O sistema permite a gestão de clientes e contas bancárias, além da realização de transações financeiras como depósitos e saques. O objetivo é fornecer uma base prática para a compreensão dos conceitos de programação orientada a objetos, uso de classes abstratas, e manipulação de dados de maneira segura e eficiente.

## Funcionalidades

### 1. Criação de Clientes
- **Pessoa Física:** Cadastro de clientes do tipo pessoa física, armazenando informações como nome, data de nascimento, CPF e endereço.

### 2. Gestão de Contas
- **Conta Corrente:** Criação de contas correntes para os clientes cadastrados, com atributos como número da conta, agência e histórico de transações.
- **Limite de Saques:** Controle de limite diário de saques e número máximo de saques permitidos.

### 3. Transações Financeiras
- **Depósitos:** Permite a realização de depósitos em contas cadastradas.
- **Saques:** Permite a realização de saques, respeitando limites de saldo e de transações diárias.
- **Histórico de Transações:** Registro de todas as transações realizadas, acessível para consulta.

### 4. Consultas e Relatórios
- **Extrato Bancário:** Geração de extrato detalhado com todas as transações realizadas e saldo atual.
- **Listagem de Contas:** Exibição de todas as contas cadastradas no sistema.

## Habilidades Técnicas Utilizadas

### 1. Programação Orientada a Objetos (POO)
- **Classes e Objetos:** Uso extensivo de classes para representar clientes, contas, transações e históricos.
- **Herança:** Implementação de herança para especialização de classes, como `Cliente` e `PessoaFisica`.
- **Encapsulamento:** Controle de acesso aos atributos das classes através de propriedades e métodos.

### 2. Classes Abstratas
- **ABC (Abstract Base Classes):** Utilização de classes abstratas para definir a interface padrão para transações (`Transacao`), garantindo que métodos específicos sejam implementados nas subclasses (`Saque` e `Deposito`).

### 3. Manipulação de Datas
- **Módulo datetime:** Uso do módulo `datetime` para registrar a data e hora das transações.

### 4. Interação com o Usuário
- **Entrada e Saída de Dados:** Uso de funções para capturar dados do usuário e exibir informações de forma clara e organizada.
- **Menus Interativos:** Implementação de um menu interativo para navegação pelas funcionalidades do sistema.

### 5. Tratamento de Exceções
- **Validação de Dados:** Verificação de condições como saldo insuficiente, limite de saques excedido e CPF duplicado, garantindo a integridade das operações.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Execute o arquivo principal do projeto:
   ```bash
   python main.py
