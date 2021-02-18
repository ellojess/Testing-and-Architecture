# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

time = 30 # [min]
temperature = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

class Doneness_Level:
    def __init__(self, time, temperature, pressure, desired_state):
        self.time = time
        self.temperature = temperature 
        self.pressure = pressure
        self.desired_state = desired_state


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if desired_state == 'well-done':
        get_cooking_progress(time, temperature, pressure) >= WELL_DONE

    if desired_state == 'medium': 
        get_cooking_progress(time, temperature, pressure) >= MEDIUM
    
    return desired_state

def get_cooking_progress(time, temperature, pressure):
    if desired_state < 'medium': 
        print('ongoing cooking.')
    else: 
        print('cooking is done.')
    return time * temperature * pressure * COOKED_CONSTANT