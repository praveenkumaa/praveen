import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DHT_PIN = 2
DHT_TYPE = Adafruit_DHT.DHT22

buzzer = 12

humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)

GPIO.setup(buzzer, GPIO.OUT)

if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to retrieve data from sensor')
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

while True:
    time.sleep(2)
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin_number)
    if humidity is not None and temperature is not None:
        H = humidity
        T = temperature
print("Humidity: ", H)
print(" %; ")
print("Temperature: ", T)
print(" Celsius.\n")
if H >= 70.00 and T >= 30.00:
    digitalWrite(9, HIGH)
    digitalWrite(10, LOW)
    digitalWrite(11, LOW)
print("   Too warm!    ")
lcd.setCursor(0, 1)
print("   Cool down!   ")
lcd.setCursor(0, 0)
digitalWrite(buzzer, 1)
tone(buzzer, 900, 100)
delay(400)
digitalWrite(buzzer, 0)
tone(buzzer, 900, 100)
delay(400)
digitalWrite(buzzer, 1)
tone(buzzer, 900, 100)
delay(400)
digitalWrite(buzzer, 0)
tone(buzzer, 900, 100)
delay(400)

else:
    digitalWrite(9, LOW)
    digitalWrite(10, LOW)
    digitalWrite(11, HIGH)
    lcd.println("Temp. & hum. are")
    lcd.setCursor(0, 1)
    lcd.println("in normal limits")
    lcd.setCursor(0, 0)
    digitalWrite(buzzer, 0)

if H < 70.00 and T >= 30.00:
    digitalWrite(9, LOW)
    digitalWrite(10, HIGH)
    digitalWrite(11, LOW)
    lcd.println("Be ware!        ")
    lcd.setCursor(0, 1)
    lcd.println("Temp. too high! ")
    lcd.setCursor(0, 0)
    digitalWrite(buzzer, 1)
    tone(buzzer, 400, 400)
    delay(400)
    digitalWrite(buzzer, 0)
    tone(buzzer, 400, 400)
    delay(400)

if H >= 70.00 and T < 30.00:
    digitalWrite(9, LOW)
    digitalWrite(10, HIGH)
    digitalWrite(11, LOW)
    lcd.println("Be ware!        ")
    lcd.setCursor(0, 1)
    lcd.println("Hum. too high!  ")
    lcd.setCursor(0, 0)
    digitalWrite(buzzer, 1)
    tone(buzzer, 400, 400)
    delay(400)
    digitalWrite(buzzer, 0)
    tone(buzzer, 400, 400)
    delay(400)