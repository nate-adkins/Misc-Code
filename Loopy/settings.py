"""
WVU Interactive Robotics Laboratory

Loopy 

Author: Nathan Adkins
"""
DEVICE0 = "/dev/ttyUSB1" # LINUX
DEVICE1 = "/dev/ttyUSB0" # LINUX

# DEVICE0 = "COM3" # WINDOWS
# DEVICE1 = "COM4" # WINDOWS

SHAPE_LIST_PATH = "loopy_shapes/Loopy_"

CHECKSUM_TOLERANCE = 36

DEFAULT_VALUE_POSITION_P_GAIN = 100 # True Default Values 
DEFAULT_VALUE_POSITION_I_GAIN = 1000 # True Default Values
DEFAULT_VALUE_POSITION_D_GAIN = 3600 # True Default Values 

AGENTS = 36 

BAUDRATE = 57600

#TORQUE CONTROL VALUES
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
ADDR_TORQUE_CONTROL = 64 
LEN_TORQUE_ENABLE = 1 # bytes

#LOAD VALUES
ADDR_PRESENT_LOAD = 126

#GOAL POSITION VALUES  
ADDR_GOAL_POSITION = 116
LEN_GOAL_POSITION = 4 # bytes

#PRESENT POSITION VALUES  
ADDR_PRESENT_POSITION = 132 
LEN_PRESENT_POSITION = 4 # bytes

#LED VALUES
ADDR_LED_CONTROL = 65
LEN_LED_CONTROL = 1 # bytes
LED_ON = 1
LED_OFF = 0 

# PWM VALUES 
ADDR_PRESENT_PWM = 124
ADDR_GOAL_PWM = 100
LEN_PWM = 4 # bytes 

#PID VALUES
ADDR_POSITION_D_GAIN = 80
ADDR_POSITION_I_GAIN = 82
ADDR_POSITION_P_GAIN = 84
LEN_POSITION_PID_GAIN = 2 # bytes

DXL_MINIMUM_POSITION_VALUE  = 695       
DXL_MAXIMUM_POSITION_VALUE  = 3405 
