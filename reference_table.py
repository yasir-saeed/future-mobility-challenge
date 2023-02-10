obd_ii_codes = {
# Column name : {PID, Description}

    "Time (sec)": {

    "PID": "1F", 
    "Description:": "The time shows how much time has passed since the start of recording data."
    },

    " Latitude (deg)": {

    "PID":"N/A", 
    "Description:": "The Latitude is the coordinate that specifies the north-south position of the vehicle on the y-axis"
    },

    " Longitude (deg)": {

    "PID":"N/A", 
    "Description:": "The Longitude is the coordinate that specifies the east-west position of the vehicle on the y-axis"
    },

    " Vehicle speed (MPH)": {

    "PID":"0D", 
    "Description:": "Vehicle speed is the rate at which the vehicle is currently travelling at, in Miles Per Hour (MPH)"
    },

    " Instant fuel economy (MPG)": {

    "PID":"N/A", 
    "Description:": "The Instant fuel economy shows many miles the car is getting per gallon of gasoline, at the current moment."
    },

    " Fuel rate (gal/hr)": {

    "PID":"N/A", 
    "Description:": "The fuel rate is the ratio of the amount of fuel used per unit of time, in hours."
    },
    
    
    " Input voltage read by the scan tool (V)": {

    "PID":"N/A", 
    "Description:": "The Input Voltage is probably the voltage, or electrical potential of the car battery."
    },
    
    " Engine Power (hp)": {

    "PID":"N/A", 
    "Description:": "Engine Power is how much power the vehicle's engine can potentially put out, in horsepower."
    },
     
    " Trip Distance (miles)": {

    "PID":"N/A", 
    "Description:": "Trip Distance is how far the vehicle has travelled during the current trip, in miles."
    },
    
    " Trip Fuel (gal)": {

    "PID":"N/A", 
   "Description:":  "Trip Fuel is how much fuel the vehicle has consumed during the current trip, in gallons."
    },
    
    " Trip Duration (min)": {

    "PID":"N/A", 
    "Description:": "Trip Duration is how long the vehicle has been travelling during the current trip, in minutes."
    },
    
    " Hard Brake Count": {

    "PID":"N/A", 
    "Description:": "The Hard Brake Count keeps track how many times the driver of the vehicle has suddenly braked, with more force than usual."
    },
    
    " Hard Accel Count": {

    "PID":"N/A", 
    "Description:": "The Hard Acceleration Count keeps track how many times the driver of the vehicle has suddenly braked, with more force than usual."
    },
    
    " Idling Count": {

    "PID":"N/A", 
    "Description:": "The Idling Count keeps track how many times the vehicle's engine was running despite not any motion."
    },
    
    " Seconds Idling (sec)": {

    "PID":"N/A", 
    "Description:": "The Seconds Idling Count keeps track how long the vehicle's engine was running despite not any motion, in seconds."
    },
    
    " Accel X (ft/s²)": {

    "PID":"N/A", 
    "Description:": "Acceleration X shows the acceleration-time graph with respect to the x-axis"
    },
    
    " Accel Y (ft/s²)": {

    "PID":"N/A", 
    "Description:": "Acceleration Y shows the acceleration-time graph with respect to the y-axis"
    },
    
    " Accel Z (ft/s²)": {

    "PID":"N/A", 
    "Description:": "Acceleration Z shows the acceleration-time graph with respect to the z-axis"
    },
    
    " Accel (Grav) X (ft/s²)": {

    "PID":"49", 
   "Description:":  "Acceleration (Grav) shows the acceleration-time gravity graph with respect to the x-axis"
    },
    
    " Accel (Grav) Y (ft/s²)": {

    "PID":"4A", 
   "Description:":  "Acceleration (Grav) shows the acceleration-time gravity graph with respect to the y-axis"
    },
    
    " Accel (Grav) Z (ft/s²)": {

    "PID":"4B", 
   "Description:":  "Acceleration (Grav) shows the acceleration-time gravity graph with respect to the z-axis"
    },
    
    " Rotation Rate X (deg/s)": {

    "PID":"N/A", 
  "Description:":   "Rotation Rate X shows the Rotation-time graph with respect to the x-axis"
    },
    
    " Rotation Rate Y (deg/s)": {

    "PID":"N/A", 
   "Description:":  "Rotation Rate X shows the Rotation-time graph with respect to the x-axis"
    },
    
    " Rotation Rate Z (deg/s)": {

    "PID":"N/A", 
   "Description:":  "Rotation Rate X shows the Rotation-time graph with respect to the x-axis"
    },
    
    " Roll (deg)": {

    "PID":"N/A", 
  "Description:":   "Roll (deg) shows the roll of a vehicle, in degrees which shows the rotation of the vehicle among the roll axis"
    },
    
    " Pitch (deg)": {

    "PID":"N/A", 
   "Description:":  "Pitch (deg) shows the roll of a vehicle, in degrees, which shows the rotation of the vehicle among the pitch axis"
    },
    
    " Magnetometer X (µT)": {

    "PID":"N/A", 
   "Description:":  "The Magnetometer X measures the magnetic field among the X-axis, in µT."
    },
    
    " Magnetometer Y (µT)": {

    "PID":"N/A", 
 "Description:":    "The Magnetometer Y measures the magnetic field among the Y-axis, in µT"
    },
    
    " Magnetometer Z (µT)": {

    "PID":"N/A", 
  "Description:":   "The Magnetometer X measures the magnetic field among the Z-axis, in µT"
    },
    
    " Calculated load value (%)": {

    "PID":"04", 
  "Description:":   "The Calculated Load Value indicates the peak available torque, in %."
    },
    
    " Engine coolant temperature (°F)": {

    "PID":"67", 
  "Description:":   "This is the temperature of the engine coolant, read by the engine coolant sensor, in Fahrenheit."
    },
    
    " Intake manifold absolute pressure (inHg)": {

    "PID":"0B", 
  "Description:":   "This is the absolute pressure inside the intake manifold of the vehicle's engine, measured by the Manifold Absolute Pressure Sensor."
    },
    
    " Engine RPM (RPM)": {

    "PID":"0C", 
   "Description:":  "The Engine RPM shows how many times the engine's crankshit has made a rotation, in rotations per minute."
    },
    
    " Intake air temperature (°F)": {

    "PID":"0F", 
    "Description:": "This is the temperature of air inside the intake manifold"
    },
    
    " Absolute throttle position (%)": {

    "PID":"11", 
    "Description:": "This monitors the actual position of the throttle"
    },
    
    " O2 voltage (Bank 1  Sensor 1) (V)": {

    "PID":"34", 
    "Description:": "This indicates the voltage of a specific oxygen sensor is below a certain threshold."
    },
    
    " O2 voltage (Bank 1  Sensor 2) (V)": {

    "PID":"35", 
    "Description:": "This indicates the voltage of a specific oxygen sensor is below a certain threshold."
    },
    
    " Distance traveled while MIL is activated (miles)": {

    "PID":"21", 
    "Description:": "This signifies the distance travelled while the Malfunction Indicator Lamp was on, in miles"
    },
    
    " Mass air flow rate (lb/min)": {

    "PID":"10", 
    "Description:": "This signifies the mass flow rate of air entering the engine of a vehicle."
    },
    
    " Boost (psi)": {

    "PID":"70", 
    "Description:": "Boost signifies the manifold air pressure inside the engine of the vehicle, in pounds per square inch."
    },
    
    " Acceleration (ft/s²)": {

    "PID":"N/A", 
    "Description:": "This shows the accleration of the car in terms of ft per second, squared."
    },
    
    " Engine Torque (lb•ft)": {

    "PID":"63", 
    "Description:": "The Engine torque signifies the rotational force inside the vehicle's engine, measured in pound-feet."
    },
    
    " Altitude (ft)": {

    "PID":"N/A", 
    "Description:": "The Altitude shows the height of an object the vehicle is currently at, relative to ground level, in feet."
    }
}    