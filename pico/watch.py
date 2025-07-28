
from machine import Pin, I2C, ADC
from display import SSD1306_I2C
import time
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = SSD1306_I2C(128, 64, i2c)
client_id = b'watch_pico'
ldr = ADC(Pin(26))
def read_light():
    light_adc = ldr.read_u16()
    lumens = (65535 - light_adc) / 65359
    return lumens


def oled_display(message: str):
    print(f"Showing message '{message}' on oled")
    DISPLAY_WIDTH = 16
    oled.fill(0)
    for i in range(len(message) // DISPLAY_WIDTH + 1):
        oled.text(message[i*DISPLAY_WIDTH: (i+1) *DISPLAY_WIDTH], 0, i* DISPLAY_WIDTH)
    oled.show()

"""
oled.fill(0)

oled.fill(0)
oled.text("Awaiting input...", 0, 0)
oled.show()

while True:

    message = input("Enter message for Agent: ")
    oled.fill(0)
    oled.text(message[0:16], 0, 16)
    if len(message) > 16:
        oled.text(message[16:32], 0, 32)
    oled.show()

    time.sleep(1)

"""

# oled_display("Hello everybody how is your day going? Try going to the end of the wall.")





callbacks = {
    'display': oled_display
}

def init_client(client, callback):
    client.set_callback(callback)
    client.subscribe('display')

actions = {
    'light': read_light
}

prev_measurement_times = {
    'light': time.time()
}

intra_action_periods = {
    'light': 1
}

update_list = ['light']

def update(client):
    current_time = time.time()
    for item in update_list:
        if current_time - prev_measurement_times[item] >= intra_action_periods[item]:
            client.publish(item, str(actions[item]()))
            prev_measurement_times[item] = current_time
