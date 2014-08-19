import Adafruit_BBIO.PWM as PWM
import time
servo1 = "EHRPWM2B"
servo2 = "EHRPWM2A"
PWM.start(servo1, 95.0, 60)
PWM.start(servo2, 95.0, 60)
time.wait(5)
PWM.set_duty_cycle(servo1, 97.0)
PWM.set_duty_cycle(servo2, 97.0)
time.wait(5)
PWM.stop(servo1)
PWM.stop(servo2)
