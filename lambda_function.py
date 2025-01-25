import boto3
import jwt

dynamodb_client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Obter o token JWT do header Authorization
    token = event['headers']['Authorization'].split(" ")[1]

    # Decodificar o token JWT
    try:
        decoded_token = jwt.decode(
            token, 
            algorithms=["RS256"], 
            options={"verify_signature": False}
        )
        user_id = decoded_token['sub']
    except Exception as e:
        return {
            "statusCode": 401,
            "body": f"Token inválido: {str(e)}"
        }
    
    table = dynamodb_client.Table("VideosTable")
    
    # Query para buscar vídeos do usuário
    response = table.query(
        KeyConditionExpression="userId = :userId",
        ExpressionAttributeValues={
            ":userId": user_id
        }
    )

    return {
        "statusCode": 200,
        "body": response['Items']
    }
