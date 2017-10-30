from __future__ import print_function
import mysql.connector
import Adafruit_MCP3008

# Software SPI configuration:
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

measurearray = [0] * 10
measurement = 0

for i in range(10):
    measurearray[i] = mcp.read_adc(0)
    measurement += measurearray[i]

returnmiddle = measurement / 10
print(returnmiddle)

cnx = mysql.connector.connect(user='root', database='xx', password='xx')
cursor = cnx.cursor()

cursor.execute("INSERT INTO measurement (measure) VALUES (%s)", (returnmiddle,))

cnx.commit()

cursor.close()
cnx.close()
