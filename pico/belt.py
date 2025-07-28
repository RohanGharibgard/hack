from machine import ADC, Pin, time_pulse_us, I2C
import dht
import time

trig = Pin(10, Pin.OUT)
echo = Pin(11, Pin.IN)
temp_humidity_sensor = dht.DHT11(Pin(5))
client_id = b'belt_pico'
def get_distance():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()

    duration = time_pulse_us(echo, 1, 30000)

    if duration < 0:
        return -1
    
    distance = (duration * 0.0343) / 2
    return distance


def get_temp():
    temp_humidity_sensor.measure()
    temp = temp_humidity_sensor.temperature()
    return temp

def get_humidity():
    temp_humidity_sensor.measure()
    humidity = temp_humidity_sensor.humidity()
    return humidity


ldr = ADC(Pin(26))
def read_light():
    light_adc = ldr.read_u16()
    lumens = (light_adc - 176) / 65359
    return lumens


"""
while True:

    dist = get_distance()
    if dist >= 0:
        print("Distance: {:.2f} cm".format(dist))
    else:
        print("Out of range")

    lumens = read_light()
    print("Light level: ", lumens, "lumens")

    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print("Temperature:", temp, "*C")
    print("Humidity:", humidity, "%")

    time.sleep(2)

"""

callbacks = {

}
def init_client(client, callback):
    client.set_callback(callback)


actions = {
    'temp': get_temp,
    'humidity': get_humidity,
    'distance': get_distance
}

prev_measurement_times = {
    'temp': time.time(),
    'humidity': time.time(),
    'distance': time.time()
}

intra_action_periods = {
    'temp': 1,
    'humidity': 1,
    'distance': 1
}

update_list = ['temp', 'humidity', 'distance']

def update(client):
    current_time = time.time()
    for item in update_list:
        if current_time - prev_measurement_times[item] >= intra_action_periods[item]:
            client.publish(item, str(actions[item]()))
            prev_measurement_times[item] = current_time
