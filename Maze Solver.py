from microbit import*
import time
import machine
trig_pin=pin1
echo_pin=pin2
def distance_cm():
    trig_pin.write_digital(0)
    time.sleep_us(2)
    trig_pin.write_digital(1)
    time.sleep_us(2)
    trig_pin.write_digital(0)
    pulse=machine.time_pulse_us(echo_pin,1)
    distance=(pulse*0.0343)/2
    return distance
def motor_left(speed,direction):
    buf=bytearray(3)
    buf[0]=0x00
    buf[1]=direction
    buf[2]=speed
    i2c.write(0x10,buf)
def motor_right(speed,direction):
    buf=bytearray(3)
    buf[0]=0x02
    buf[1]=direction
    buf[2]=speed
    i2c.write(0x10,buf)
def motor_forward():
    motor_left(255,0)
    motor_right(255,0)
def motor_backward():
    motor_left(255,1)
    motor_right(255,1)
def motor_stop():
    motor_left(0,0)
    motor_right(0,0)
def turn_left():
    motor_left(255,1)
    motor_right(255,0)
    sleep(115)
    motor_left(0,0)
    motor_right(0,0)
def turn_right():
    motor_left(255,1)
    motor_right(255,0)
    sleep(115)
    motor_left(0,0)
    motor_right(0,0)
def one_eighty_left():
    motor_left(255,1)
    motor_right(255,0)
    sleep(230)
    motor_left(0,0)
    motor_right(0,0)
def one_eighty_right():
    motor_left(255,0)
    motor_right(255,1)
    sleep(230)
    motor_left(0,0)
    motor_right(0,0)
while True:
    distance=distance_cm()
    motor_forward()
    distance=distance_cm()
    if distance<30:
        motor_stop()
        turn_left()
        distance=distance_cm()
        if distance<30:
            one_eighty_right()
            distance=distance_cm()
            if distance<30:
                motor_stop()
            else:
                motor_forward()
        else:
            motor_forward()
    else:
        motor_forward()