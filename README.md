# IoT_raspberrypi
Controle de pressão temperatura e umidade com raspberry e controlando dados com RabbitMQ



# configurando raspberry
Primeiro clone o repositório:
```shell
git clone https://github.com/icarodgl/IoT_raspberrypi.git
```
Agora instale o pip
```shell
sudo apt update
sudo apt install python3-pip
```

vá até a pasta do projeto e instale as dependencias utilizando o requirements:
```shell
cd IoT_raspberrypi
pip install requirements.txt
```
caso não funcione instale manualmente:
```shell
pip install pika
pip install python-dotenv
pip install netifaces
```
Agora você já possui o python configurado para rodar o projeto.
renomeie o arquivo .env.exemplo para .env
````shell
#use esse comando na pasta do projeto
cp .env.exemplo .env
````
Vamos configurar o raspberry para niciar o script ao ligar:

abra o .profile que fica na pasta do usuario `nano .profile` e adicione a seguinte linha no final do arquivo:
````shell
python3 iot/src/send.py
````
ao reiniciar o seu raspberry ele irá executar automaticamente o comando após login


# comandos Rabbitmq

### configurando usuario
```shell
rabbitmqctl add_user pi raspberry
rabbitmqctl set_user_tags pi administrator
rabbitmqctl set_permissions -p / pi ".*" ".*" ".*"
```