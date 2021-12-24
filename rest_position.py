from init_servos import init_servos
from servos_config import servos_config

def rest_position():
    servos = init_servos()
    #set rest angle
    for position, joins in servos_config.items():
        for join, config in joins.items():
            servos[position][join].angle = config["rest_angle"]

if __name__ == '__main__':
    rest_position()
