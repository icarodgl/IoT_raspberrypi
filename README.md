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
Agora você já possui o python configurado para rodar o projeto.

Vamos configurar o raspberry para niciar o script ao ligar:

abra o .profile  `nano .profile` e adicione a seguinte linha no final do arquivo:
````shell
run ./IoT_raspberrypi/src/run_sender.sh
````
ao reiniciar o seu raspberry ele irá executar automaticamente o comando após login


# comandos Rabbitmq

### configurando usuario
```shell
rabbitmqctl add_user pi raspberry
rabbitmqctl set_user_tags pi administrator
rabbitmqctl set_permissions -p / pi ".*" ".*" ".*"
```