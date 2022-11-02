# Uber
Análise de dados de utilização dos serviços da Uber

## Aquisição de dados
Por meio de solicitação no website da empresa, é possível obter um arquivo CSV com dados de utilização dos serviços de transporte e delivery da Uber. As informações fornecidas conssitem no local, data e hora da solicitação do transporte, horário de início da corrida, horário de finalização, valor da corrida, moeda utilizada no pagamento, etc.

## Problematização
Minha intenção era avaliar os padrões de utilização dos serviços, as questões principais eram:
1. Há relação direta entre distância da viagem e o preço cobrado? 
2. Quais foram as cidades em que mais foi pedido o serviço de transporte?
3. Quais horas do dia são as que mais são solicitadas viagens?

## Proposta de solução
Utilizar das bibliotecas `Pandas` e `Matplotlib` para tratar os dados e plotá-los, na intenção de responder as questões expostas acima, considerando apenas as informações relacionadas a transporte de pessoas
