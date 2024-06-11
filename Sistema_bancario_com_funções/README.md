# Sistema Bancário em Python

Este é um sistema bancário simples implementado em Python que permite aos usuários realizar operações como depósito, saque, exibir extrato, criar contas e usuários, e listar contas existentes. O sistema utiliza funções para organizar as operações e a interação com o usuário é feita através do terminal.

## Funcionalidades

1. **Depósito**
2. **Saque**
3. **Exibir Extrato**
4. **Criar Nova Conta**
5. **Listar Contas**
6. **Criar Novo Usuário**
7. **Sair**

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o código em um arquivo chamado `sistema_bancario.py`.
3. Abra o terminal e navegue até o diretório onde o arquivo está salvo.
4. Execute o script usando o comando:
    ```sh
    python sistema_bancario.py
    ```

## Menu de Operações

### Depósito

Para realizar um depósito, selecione a opção `[d]` e informe o valor do depósito. O valor será adicionado ao saldo e registrado no extrato.

### Saque

Para realizar um saque, selecione a opção `[s]` e informe o valor do saque. O sistema verificará se:
- O saldo é suficiente.
- O valor não excede o limite de saque.
- O número máximo de saques diários não foi excedido.

### Exibir Extrato

Para exibir o extrato da conta, selecione a opção `[e]`. O sistema mostrará todas as transações realizadas e o saldo atual.

### Criar Nova Conta

Para criar uma nova conta, selecione a opção `[nc]` e informe o CPF do usuário. Se o usuário for encontrado, a conta será criada com sucesso.

### Listar Contas

Para listar todas as contas existentes, selecione a opção `[lc]`. O sistema exibirá as informações de todas as contas criadas.

### Criar Novo Usuário

Para criar um novo usuário, selecione a opção `[nu]` e forneça as informações solicitadas:
- CPF
- Nome completo
- Data de nascimento
- Endereço

### Sair

Para sair do sistema, selecione a opção `[q]`.

## Estrutura do Código

- **menu()**: Exibe o menu e captura a opção selecionada pelo usuário.
- **depositar(saldo, valor, extrato)**: Realiza o depósito e atualiza o saldo e o extrato.
- **sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)**: Realiza o saque, verifica o saldo, limite e o número de saques diários.
- **exibir_extrato(saldo, extrato)**: Exibe o extrato das transações.
- **criar_usuario(usuarios)**: Cria um novo usuário.
- **filtrar_usuario(cpf, usuarios)**: Filtra e retorna o usuário pelo CPF.
- **criar_conta(agencia, numero_conta, usuarios)**: Cria uma nova conta para um usuário existente.
- **listar_contas(contas)**: Lista todas as contas existentes.
- **main()**: Função principal que controla o fluxo do programa.

## Exemplo de Uso

```sh
=============== MENU ================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
=> d
Informe o valor do depósito: 1000
=== Depósito realizado com sucesso! ===

=============== MENU ==============
