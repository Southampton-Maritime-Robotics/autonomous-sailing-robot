"""
test PWM

"""
import Adafruit_BBIO.PWM as PWM
import time
pinA = "P8_19"
pinB = "P8_13" #13
print('init PWM')
#PWM.stop(pinA)
PWM.stop(pinB)
PWM.cleanup()

PWM.start(pinA, 0)
PWM.start(pinB, 0)
time.sleep(1)
print('switch')
#PWM.set_frequency(pinA, 50)
# fine if one servo is commented
# as soon as both are used:
# all following commands for the servo
# don't result in a change

#PWM.set_frequency(pinB, 50)
PWM.set_duty_cycle(pinA, 97)
PWM.set_duty_cycle(pinB, 97)
time.sleep(2)
print('switch')
#PWM.set_frequency(pinA, 50)
#PWM.set_frequency(pinB, 50)
PWM.set_duty_cycle(pinA, 30)
PWM.set_duty_cycle(pinB, 30)
time.sleep(2)


print('stop')
#PWM.stop(pinA)
PWM.stop(pinB)
PWM.cleanup()
print('done')

