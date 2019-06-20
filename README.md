# IoT_raspberrypi
Controle de pressão temperatura e umidade com raspberry e controlando dados com RabbitMQ



# configurando raspberry
Primeiro clone o repositório:
```shell
git clone https://github.com/icarodgl/IoT_raspberrypi.git
```
Agora instale o pip e o pipenv
```shell
sudo apt update
sudo apt install python3-pip
pip install pipenv
```

vá até a pasta do projeto e instale as dependencias utilizando o pipenv:
```shell
cd IoT_raspberrypi
pipenv install
```
Agora você já possui uma env configurada para rodar o projeto.

Vamos configurar o raspberry para niciar o script ao ligar:

abra o .profile  `nano .profile` e adicione a seguinte linha:
````shell

````



# comandos Rabbitmq

### configurando usuario
```shell
rabbitmqctl add_user pi raspberry
rabbitmqctl set_user_tags pi administrator
rabbitmqctl set_permissions -p / pi ".*" ".*" ".*"
```