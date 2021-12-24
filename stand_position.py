import time
import json
from init_servos import init_servos
from servos_config import servos_config

def stand_position():
    servos = init_servos()
    #servos = {
    #    "rear_left": {
    #        "shoulder": {},
    #        "leg": {},
    #        "feet": {},
    #    },
    #    "rear_right": {
    #        "shoulder": {},
    #        "leg": {},
    #        "feet": {},
    #    },
    #    "front_left": {
    #        "shoulder": {},
    #        "leg": {},
    #        "feet": {},
    #    },
    #    "front_right": {
    #        "shoulder": {},
    #        "leg": {},
    #        "feet": {},
    #    },
    #}
    variation_shoulder = 10
    variation_leg = 50
    variation_feet = 70
    #后肢
    variation_rear = {
        "rear_left": {
            "shoulder": variation_shoulder,
            "leg": -variation_leg,
            "feet": variation_feet,
        },
        "rear_right": {
            "shoulder": -variation_shoulder,
            "leg": variation_leg,
            "feet": -variation_feet,
        },
    }
    for position, joins in variation_rear.items():
        for join, variation in joins.items():
            servos[position][join].angle = servo_config[position][join]["rest_angle"] + variation
            #servos[position][join]["angle"] = servos_config[position][join]["rest_angle"] + variation
    #0.05秒
    time.sleep(0.05)
    #前肢
    variation_front = {
        "front_left": {
            "shoulder": -variation_shoulder,
            "leg": -variation_leg + 5,
            "feet": variation_feet - 5,
        },
        "front_right": {
            "shoulder": variation_shoulder,
            "leg": variation_leg - 5,
            "feet": -variation_feet + 5,
        },
    }
    for position, joins in variation_front.items():
        for join, variation in joins.items():
            servos[position][join].angle = servo_config[position][join]["rest_angle"] + variation
            #servos[position][join]["angle"] = servos_config[position][join]["rest_angle"] + variation
    #print("servos: ", json.dumps(servos, indent=4))

if __name__ == '__main__':
    stand_position()
