# AWS Lambda com Decodificação de JWT e Integração com DynamoDB

Este repositório contém uma função Lambda em Python que utiliza o token JWT para autenticar e buscar vídeos de um usuário específico armazenados no DynamoDB.

## Funcionalidades

- **Decodificação de JWT**: Decodifica o token JWT enviado no cabeçalho `Authorization`.
- **Validação de Usuário**: Extrai o `userId` do token JWT para identificar o usuário no DynamoDB.
- **Consulta ao DynamoDB**: Realiza uma query na tabela `VideosTable` para buscar os vídeos associados ao usuário autenticado.

## Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `boto3` para interação com serviços AWS
- Biblioteca `PyJWT` para decodificação de tokens JWT
- Uma tabela no DynamoDB chamada `VideosTable` configurada com a chave primária `userId`.

## Configuração

1. **Configurar Dependências**

   Instale as bibliotecas necessárias utilizando o `pip`:

   ```bash
   pip install boto3 PyJWT
   ```

2. **Configurar a Tabela DynamoDB**

   Certifique-se de que a tabela `VideosTable` exista no DynamoDB e que esteja configurada com:

   - Chave Primária: `userId`

3. **Substituir Chave Pública (opcional)**

   Para validação do token JWT, configure a chave pública do Cognito ou use o JWKS.

## Como Funciona

1. **Receber Token JWT**

   O token JWT deve ser enviado no cabeçalho `Authorization` da requisição HTTP, no formato:

   ```text
   Authorization: Bearer <seu_token_jwt>
   ```

2. **Decodificar Token**

   O token é decodificado para extrair o identificador único do usuário (`sub`).

3. **Consultar DynamoDB**

   O identificador do usuário é utilizado para realizar uma consulta na tabela `VideosTable`.

4. **Resposta**

   A função retorna os vídeos associados ao usuário autenticado no seguinte formato:

   ```json
   {
       "statusCode": 200,
       "body": [
           {
               "videoId": "123",
               "title": "Exemplo de Vídeo"
           }
       ]
   }
   ```

## Segurança

Certifique-se de:

- Configurar a validação correta da assinatura do token JWT em produção.
- Usar variáveis de ambiente para armazenar segredos e configurações sensíveis.