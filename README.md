## Lojs API - Para curso de Performance utilizando JMETER

### Autenticando no DockerHub

docker login 

- username: usuario_dockerhub
- password: senha_dockerhub

### Baixar imagem

docker pull vaniltonpinheiro/api-loja:latest

### Executar container API

- Acessar a pasta nfe, executar o comando abaixo

docker-compose up -d

### Verificar containers sendo executados

docker-compose ps

### Criar um superuser para o Django admin (para autenticação na API)

docker exec -it api_loja_virtual_web_1 sh -c "python manage.py createsuperuser"

### Acessar a aplicação em:

http://localhost:8000/admin

### Observação

O serviço web irá consumir a porta 8000 e o banco de dados a porta 5432 (PostgreSQL) 
