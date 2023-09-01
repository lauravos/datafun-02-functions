""" Laura Vos 
08/31/23
practiced writing and calling functions per project 2, task 4 instructions"""


import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


def get_area_of_room(length, width):
    sum = length * width
    return sum

print(get_area_of_room(8,10))




def get_circle_area_given_radius(radius):
    """
    Return area of a circle given the radius.

    @param radius: the radius of the circle
    @return: the area of the circle
    @raise Exception: if radius is not a number

    """

    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_circle_area({radius})")

    try: 
        area = 2 * math.pi * radius
        logger.info(f"The circle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None


def get_circle_areas_given_list(radius_list):
    """
    This function should return a list with the areas of each circle

    Keyword arguments:
    radius_list -- a list of radius values (items may be invalid)
    """
    logger.info(f"CALLING get_circle_area({radius_list})")

    if len(radius_list) == 0:
        logger.error("Please add some items to the list. Nothing to do.")
        quit() # quit the program

    area_list = [] # empty list to hold the areas

    # for every element in the list passed in 
    for r in radius_list:

        try:
            area = get_circle_area_given_radius(r)
            logger.info(f"r = {r}, area={area}")
            area_list.append(area)

        except Exception as ex:
            logger.error(f"radius = {r}, Error: {ex}")




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# Literally: "if this module name == the name of the main running module"
# (as opposed to being imported by another module like we do the logger),
# then, follow these instructions.
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
#new examples of comb and perm ()
    logger.info(f"math.comb(4,2) = {math.comb(4,2)}")
    logger.info(f"math.perm(1,9) = {math.perm(1,9)}")
    logger.info(f"math.comb(3,8) = {math.comb(3,8)}")
    logger.info(f"math.perm(4,5) = {math.perm(4,5)}")


#Calling method again: (Then, call the method you just created with several different arguments. 
# For example, call get_area_of_rectangle(6, 2) and display the result. Call it again with different values for height and weight.)

    logger.info(f"get_area_of_room(6,2) = {get_area_of_room(6,2)}")
    logger.info(f"get_area_of_room(20,4) = {get_area_of_room(20,4)}")
    logger.info(f"get_area_of_room(16,15) = {get_area_of_room(16,15)}")


#3 added examles


def inches_to_cm(inches):
    return inches * 2.54

logger.info(f"3 inches converted to cm = {inches_to_cm(3)} cm")


def feet_to_inches(feet):
    return feet * 12

logger.info(f"2 feet converted to inches = {feet_to_inches(2)} inches")




def cost_of_food(quantity, price):
    return quantity * price

logger.info(f"The cost of food is {cost_of_food(2,18)}")



def roundDown(num):
    return math.floor(num)

logger.info(f"4.32 rounded down = {roundDown(4.32)}")

def roundup(num):
    return math.ceil(num)

logger.info(f"9.463 = {roundup(9.463)}")

def absolute(num):
    return math.fabs(num)

logger.info(f"the absolute value of -6.2 is {absolute(-6.2)}")




