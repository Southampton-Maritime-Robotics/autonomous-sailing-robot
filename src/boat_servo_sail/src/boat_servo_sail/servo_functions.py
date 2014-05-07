"""
test PWM

"""
import Adafruit_BBIO.PWM as PWM
import time
pinA = "P8_19"
pinB = "P8_13"
print('init PWM')
PWM.stop(pinA)
PWM.stop(pinB)
PWM.cleanup()

PWM.start(pinA, 0)
PWM.start(pinB, 0)
time.sleep(1)
print('switch')
PWM.set_duty_cycle(pinA, 97)
PWM.set_duty_cycle(pinB, 97)
time.sleep(2)
print('switch')
#PWM.set_frequency(pinA, 60)
PWM.set_duty_cycle(pinA, 97)
PWM.set_duty_cycle(pinB, 97)
time.sleep(2)


print('stop')
PWM.stop(pinA)
PWM.stop(pinB)
PWM.cleanup()
print('done')

