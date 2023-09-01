# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

# Descriptive: Univariant Data..................................

# univariant data (one variable, many readings)
uni_data = [9609, 9637, 8119, 11924, 12399, 11821, 10634]

logger.info("uni_data = " + str(uni_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread 

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)
range = highest - lowest

# TODO: change to f-strings and display 2 decimal places (like we did above)
'''
logger.info("var    = " + str(var))
logger.info("stdev  = " + str(stdev))
logger.info("lowest = " + str(lowest))
logger.info("highest = " + str(highest))

'''
logger.info(f"var    = " + str(round(var,2)))
logger.info(f"stdev  = " + str(round(stdev,2)))
logger.info(f"lowest = " + str(round(lowest,2)))
logger.info(f"highest= " + str(round(highest,2)))
logger.info("range = " + str(round(range, 2)))

# Descriptive: Univariant Time Series Data.........................

# describe relationships
# univariant time series data (one variable over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)

# number of pet adoptions per year from the Wisconsin Humane Society
xyear = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
yvalues = [10634, 11821, 12399, 11924, 8119, 9637, 9609]

# if the lists are not the same size,
# log an error and quit the program
if len(xyear) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xyear)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(xyear, xyear)
xy_corr = statistics.correlation(xyear, yvalues)

# log the information
logger.info("Here's some annual data:")
logger.info(f"xyear:{xyear}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xyear and xyear = {xx_corr:.2f}")
logger.info(f"correlation between xyear and yvalues = {xy_corr:.2f}")


