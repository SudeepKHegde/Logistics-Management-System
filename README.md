## Logistics-Management-System:
A system called the Logistics Management System (LMS) was created to offer package information at any time. The fundamental problems in logistics, such as product theft and inadequate product information during transportation from point A to point B, were addressed by this concept. 

![My Image](LMS(Ckt)-Setup.jpg)
## Advantages of LMS:
- Provides Information at any time about the package
* Control Window to monitor the data provided by the module
+ Sensing Modules to prevent theft and unknown replacements
- Works with the Vehicle's battery as the supply

## Hardware Setup:
A microcontroller board that makes calculations based on several sensor inputs. Sensors include temperature, humidity, vibration sensors, and a GPS module.
The LM7805CV, which is used to down convert the vehicle supply from the vehicle's battery (which provides 12–24 volts), is housed in a separate external circuit. The external circuit acts as the supply for the sensors and the microcontroller.

## Software Setup:
For the user to readily grasp the state of his package, a Python application is set up to accept inputs from the hardware and display the data in an accessible manner. Using TeraTerm, the data from the hardware is saved in a.csv file, and the python application then displays that data. 
