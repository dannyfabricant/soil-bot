# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


def read_moisture(CHANNEL ,CLK, MISO, MOSI, CS):
    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    moisture = mcp.read_adc(CHANNEL)

    return moisture


# uncomment bollow to test individual mcp3008 channels bellow
# while 1:

# 	print(read_moisture(0,18,23,24,25));
# 	print(read_moisture(1,18,23,24,25));
# 	time.sleep(1)