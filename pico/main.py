from connections import connect_mqtt, connect_internet
from time import sleep

device = 'watch'

if device == 'watch':
    from watch import callbacks, init_client, update, client_id
elif device == 'belt':
    from belt import callbacks, init_client, update, client_id

def cb(topic, msg):
    print(f"message: {msg.decode()}")
    topic = topic.decode()
    if topic in callbacks:
        callbacks[topic](msg.decode())
    else:
        raise ValueError(f"topic '{topic}' doesn't have callback.")




def main():
    # with open("config.cfg") as f:
    #     config = eval(f.read())
    WIFI_SSID = "bruins"
    WIFI_PASS = "connect12"

    CONNECT_URL="2f21e0950dd145e09fa19455d4aafedf.s1.eu.hivemq.cloud"
    MQTT_USER="fabulous4"
    MQTT_PASS="Theydontknowaboutthefabulous4"

    try:
        # connect_internet(config["WIFI_SSID"],password=config["WIFI_PASS"]) #ssid (wifi name), pass
        # client = connect_mqtt(config["CONNECT_URL"], config["MQTT_USER"], config["MQTT_PASS"]) # url, user, pass
        connect_internet(WIFI_SSID,password=WIFI_PASS) #ssid (wifi name), pass
        client = connect_mqtt(client_id, CONNECT_URL, MQTT_USER, MQTT_PASS) # url, user, pass

        init_client(client, cb)

        while True:
            client.check_msg()
            update(client)
            #TODO: REMOVE THE SLEEP
            sleep(0.1)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()



