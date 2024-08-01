# Sistema Bancário em Python

## Descrição
Este projeto é um sistema bancário simplificado implementado em Python. Ele simula as principais operações bancárias, como depósito, saque, exibição de extrato, criação de contas e cadastro de clientes. A aplicação é interativa, operando por meio de um menu de opções acessado pelo terminal. O sistema possui um controle de limite de saques por dia e por transação, garantindo uma simulação mais realista das operações bancárias.

## Funcionalidades
- **Cadastro de Clientes**: Permite o registro de novos clientes no sistema.
- **Criação de Contas**: Gera novas contas bancárias associadas a clientes.
- **Depósito e Saque**: Executa operações financeiras, registrando-as no histórico da conta.
- **Extrato Bancário**: Exibe um relatório de todas as transações realizadas em uma conta específica.
- **Limite de Saques**: Controla o número máximo de saques permitidos por dia e o valor limite de cada saque.

## Estrutura do Projeto
- **`Cliente` e `PessoaFisica`**: Representam os clientes do banco, com dados pessoais e contas associadas.
- **`Conta` e `ContaCorrente`**: Implementam as contas bancárias, com métodos para saque e depósito, além de controle de limite de saques.
- **`Historico`**: Gerencia o histórico de transações realizadas nas contas.
- **`Transacao`, `Saque` e `Deposito`**: Definem e registram as operações financeiras executadas.
- **`ContasIterador`**: Implementa o padrão de design Iterator para percorrer as contas cadastradas.
- **Funções auxiliares**: Como `menu`, `log_transacao`, `filtrar_cliente`, entre outras, para gerir o fluxo da aplicação.

## Como Executar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o script `main.py` para iniciar a aplicação.
5. Siga as instruções no terminal para interagir com o sistema.

## Requisitos
- Python 3.x

## Melhorias Futuras
- Implementar persistência de dados utilizando um banco de dados ou arquivos de texto.
- Adicionar funcionalidades de transferência entre contas.
- Implementar interface gráfica para uma melhor experiência do usuário.
