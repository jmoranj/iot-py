import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_TEMPERATURA = "casa/temperatura"
TOPIC_VENTILACAO = "casa/ventilacao"

def on_message(client, userdata, msg):
    try:
        temperatura = float(msg.payload.decode())
        print(f"Temperatura recebida: {temperatura}°C")

        if temperatura > 28.0:
            client.publish(TOPIC_VENTILACAO, "LIGAR")
            print("Comando enviado: LIGAR ventilador")
        else:
            client.publish(TOPIC_VENTILACAO, "DESLIGAR")
            print("Comando enviado: DESLIGAR ventilador")
    except ValueError:
        print("Mensagem inválida recebida:", msg.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.subscribe(TOPIC_TEMPERATURA)

print("Cliente MQTT rodando, esperando temperaturas...")
client.loop_forever()
