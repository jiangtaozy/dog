import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from servos_config import servos_config

def init_servos():
    #init pca9685
    i2c = busio.I2C(SCL, SDA)
    pca9685_address = 0x40
    pca9685_reference_clock_speed = 25000000
    pca9685_frequency = 50
    pca9685 = PCA9685(
        i2c,
        address=pca9685_address,
        reference_clock_speed=pca9685_reference_clock_speed,
    )
    pca9685.frequence = pca9685_frequency
    #init servos
    servos = {}
    for position, joins in servos_config.items():
        servos[position] = {}
        for join, config in joins.items():
            servos[position][join] = servo.Servo(
                pca9685.channels[config["channel"]]
            )
    return servos
