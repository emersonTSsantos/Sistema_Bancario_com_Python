# Simulador de Operações Bancárias

Este é um programa de simulação de operações bancárias em Python, permitindo ao usuário realizar depósitos, saques, e visualizar o extrato da conta.

## Funcionalidades

1. **Depositar**
2. **Sacar**
3. **Extrato**
4. **Sair**

## Variáveis Iniciais

- `saldo`: Armazena o saldo atual da conta, inicializado em 0.
- `limite`: Define o limite máximo permitido para um saque, fixado em R$ 500,00.
- `extrato`: Armazena um histórico de transações como uma string.
- `numero_saques`: Conta o número de saques realizados no dia, inicializado em 0.
- `LIMITE_SAQUES`: Define o número máximo de saques permitidos por dia, fixado em 3.

## Menu Interativo

Um menu interativo é apresentado ao usuário dentro de um loop `while` infinito, que só termina quando o usuário seleciona a opção de sair (`0`). O menu oferece quatro opções:

### Opção 1: Depositar

Quando o usuário seleciona a opção de depósito (`1`):
- Solicita-se o valor do depósito.
- Verifica-se se o valor é negativo, e caso seja, a operação falha.
- Caso o valor seja positivo, adiciona-se ao saldo atual e registra-se a transação no extrato.
- Em seguida, oferece-se a opção de imprimir um comprovante ou encerrar a sessão.

### Opção 2: Sacar

Ao escolher a opção de saque (`2`):
- O programa entra em um loop que permite até três saques por dia (`LIMITE_SAQUES`).
- Solicita-se o valor do saque.
- Verifica-se se o valor excede o limite permitido (R$ 500,00) ou se o saldo é insuficiente. Em ambos os casos, a operação falha e o número de saques não é incrementado.
- Caso o valor seja válido, deduz-se do saldo e registra-se a transação no extrato.
- Se o limite de saques diários for atingido, informa-se ao usuário.
- Após cada saque, o usuário pode optar por encerrar a sessão ou realizar outro saque.

### Opção 3: Extrato

Selecionando a opção de extrato (`3`):
- Imprime-se o histórico de transações armazenado na variável `extrato`.
- Caso não haja transações, informa-se que nenhuma operação foi realizada.
- Exibe-se o saldo atual.

### Opção 0: Sair

Escolhendo a opção de sair (`0`):
- O programa exibe uma mensagem de saída e encerra o loop, finalizando a execução.

## Tratamento de Erros e Validações

O código inclui verificações para garantir que os valores inseridos são válidos:
- Depósitos e saques não podem ser negativos.
- Saques não podem exceder o limite diário nem o saldo disponível.
- Mensagens de erro informam o usuário sobre qualquer operação inválida, garantindo uma experiência de uso robusta.

## Considerações Finais

Este programa oferece uma interface simples para simular operações bancárias básicas, com validações adequadas para evitar erros comuns. A lógica do loop permite que o usuário realize várias operações consecutivas sem precisar reiniciar o programa, proporcionando uma experiência contínua e interativa.
