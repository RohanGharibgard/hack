import framebuf

class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.poweron()
        self.init_display()

    def init_display(self):
        for cmd in (
            0xae, 0x20, 0x00, 0x40, 0xa1, 0xc8, 0xda, 0x12, 0x81, 0xcf, 0xa4,
            0xa6, 0xd5, 0x80, 0x8d, 0x14, 0xaf
        ):
            self.write_cmd(cmd)

    def poweron(self):
        pass

    def write_cmd(self, cmd):
        raise NotImplementedError

    def write_data(self, buf):
        raise NotImplementedError

    def fill(self, col):
        self.framebuf.fill(col)

    def pixel(self, x, y, col):
        self.framebuf.pixel(x, y, col)

    def scroll(self, dx, dy):
        self.framebuf.scroll(dx, dy)

    def text(self, string, x, y, col=1):
        self.framebuf.text(string, x, y, col)

    def show(self):
        raise NotImplementedError

class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)

    def show(self):
        for page in range(0, self.height // 8):
            self.write_cmd(0xb0 | page)
            self.write_cmd(0x02)
            self.write_cmd(0x10)
            start = self.width * page
            end = start + self.width
            self.write_data(self.buffer[start:end])

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0))

oled = SSD1306_I2C(128, 64, i2c)
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

