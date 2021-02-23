# test_one.py

import math
import pytest

def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

# test_exception.py
def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

def test_palindrom(): #should fail with TypeError: Please provide a string argument
    with pytest.raises(TypeError):
        palindrome(44)

# ex 1 

def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
    # use math.isclose() function instead of ‘==’ to compare floating-point numbers
    assert  math.isclose(get_average([1, 2, 3, 4, 5]), 3)

# ex 2 
T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if 0 < carbon_14_ratio < 1:
        return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 
    else: 
        return "carbon_14_ratio should be between 0 < percent < 1"

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
#  test fails with input of negatice or 0 
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case. ✅

def test_get_age_carbon_14_dating():
    assert get_age_carbon_14_dating(0.35) # 8680.34
    assert get_age_carbon_14_dating(0.00) # special case 
    assert get_age_carbon_14_dating(-0.35) # special case 

# ex 3 
# Example for Compose Methods: Extract Method.
# Refactored.

def display_grade_stat():
    """Gathers stats and print them out."""
    grade_list = read_input()
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

display_grade_stat()

def test_calculate_stat():
    mean, sd = calculate_stat([1, 2, 3, 4, 5, 6])
    assert math.isclose(mean, 3.5)
    assert math.isclose(sd, 1.87082)

# ex 4 
# Replace nested conditional with gaurd clauses

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)

def test_extract_position():
    assert extract_position("") == None
    assert extract_position("error numerical calculations could not converge") == None
    assert extract_position("the positron location in the particle accelerator is x:21.432") == '21.432'