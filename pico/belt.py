from machine import ADC, Pin, time_pulse_us, I2C
import dht
import time

trig = Pin(10, Pin.OUT)
echo = Pin(11, Pin.IN)
sensor = dht.DHT11(Pin(5))
ldr = ADC(Pin(26))

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

def read_light():
    return ldr.read_u16()

while True:

    dist = get_distance()
    if dist >= 0:
        print("Distance: {:.2f} cm".format(dist))
    else:
        print("Out of range")

    light = read_light()
    lumens = (light - 176) / 65359
    print("Light level: ", lumens, "lumens")

    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print("Temperature:", temp, "*C")
    print("Humidity:", humidity, "%")

    time.sleep(2)