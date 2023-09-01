'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to cats.

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

Cats adds:

- a cat breed attribute

'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from numeric_series import NumericSeries

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


class NumericCatSeries(NumericSeries):
    """
    A class representing a numeric series customized for cat data.

    (Additional) Attributes:
       breed (string): the breed of cats
    """

    def __init__(self, name, units, data, breed):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            breed (str): the breed of cats data collected

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.breed = breed

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericCatSeries with name={self.name}, units={self.units}, breed={self.breed}, and {len(self.data)} data points: {self.data}"
        return str




if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Cats_A"
    units1 = "lbs"
    data1 = [9.6, 11.9, 10.0]
    breed = "tabby"

    object1 = NumericCatSeries(name1, units1, data1, breed)

  
    name2 = "Cats_B"
    units2 = "lbs"
    data2 = [16.4, 15.3, 20.1]
    breed2 = "Maine Coon"

    object2 = NumericCatSeries(name2, units2, data2, breed2)

    
    # Create another object 

    data3 = [13.7, 9.3, 12.8]
    name3 = "Cats_C"
    units3 = "lbs"
    breed3 = "Siamese"

    object3 = NumericCatSeries(name3, units3, data3, breed3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]


    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")

