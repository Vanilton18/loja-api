## Lojs API - Para curso de Performance utilizando JMETER

### Autenticando no DockerHub (caso esteja em algum outro registry)

docker login 

- username: usuario_dockerhub
- password: senha_dockerhub

### Build imagem

#### Dependencias

docker build -t vaniltonpinheiro/dep-loja -f Dockerfile .

#### Api Loja

docker build -t vaniltonpinheiro/api-loja -f Dockerfile .

### Baixar imagem

docker pull vaniltonpinheiro/api-loja:latest

### Executar container API

- Executar o comando abaixo

docker-compose up -d

### Verificar containers sendo executados

docker-compose ps

### Criar um superuser para o Django admin (para autenticação na API)

docker exec -it <container_name>_web_1 sh -c "python manage.py createsuperuser"

### Acessar a aplicação em:

http://localhost:8000/admin

### Observação

O serviço web irá consumir a porta 8000 e o banco de dados a porta 5432 (PostgreSQL) 
