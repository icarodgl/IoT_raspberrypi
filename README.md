# IoT_raspberrypi
Controle de pressão temperatura e umidade com raspberry e controlando dados com RabbitMQ



# comandos Rabbitmq

### configurando usuario
```shell
rabbitmqctl add_user pi raspberry
rabbitmqctl set_user_tags pi administrator
rabbitmqctl set_permissions -p / pi ".*" ".*" ".*"
```

