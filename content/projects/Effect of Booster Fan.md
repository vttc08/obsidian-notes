### Introduction
- booster or register fan blow air from the vent which could increase airflow to rooms where HVAC has weak airflow
- the internet is split on whether it's effective
- booster fans make noise when operating
- the object also block airflow especially when the fan is not running
#### Initial Observation
More detailed in Excel form. Fans are audible and consumes around 3-7W during operation.
### Hypothesis
There will be insignificant reduction in temperature (or effectiveness) after installing the booster fan.
- upon initial testing, the airflow output of the fan is minimal
- when the fan is not spinning, airflow is blocked

### Method
#### Materials
**Hardware**
- Honeywell T10 Thermostat
- 2x Honeywell RedLink sensor
- Smart Cocoon Booster Fan
**Software**
- Home Assistant
- InfluxDB
#### Design
Two rooms (Kevin, Ella), 2 days of heat wave of similar temperature
- upon looking at the forecast, 5pm to 10pm on Monday and Tuesday is used as experiment time
- one room will have a fan while the other won't
The Booster fan will be set using its app to "Eco" mode, where it will only spin when it detects there is air in the vent. The fan speed is set to 41%, it is measured to be at a reasonable noise level and power consumption while maintaining airflow
The door is closed in both rooms, blind folded down, same sensors placed on the pillow.
HVAC target temp is set to 23.5 when cooling. 
#### Variables
Outside Temperature - Celsius (measured using weather.com API in home assistant)
Kevin/Ella Temperature - Celsius (measured using RedLink sensor on Honeywell T10 Pro, integration with home assistant HomeKit)
- due to potential range issues, I did not use the Sonoff/Tuya Zigbee sensor; however, the RedLink sensor are less accurate which could be a weakness
Temperature Delta - the difference between outside temperature and room temperature **-> Derived Continuous Response Variable**
- Delta = `outside - room temp`
HVAC Mode - Boolean (cooling or idle)
Rooms - Kevin/Ella **-> Categorical Explanatory Variable**
Fan Presence - Boolean (Present/Absent) **-> Categorical Explanatory Variable**

#### Design
Systematic sampling, query the InfluxDB
- sample data every 10 minutes 
- each data point is the average value of the last 2 minute if its continuous
- categorical variables are defined manually

#### Stats
Using Two-Way ANOVA. 
- whether there are significant difference in temperature delta between the rooms and the presence of fans

### Experiment

| Timestamp | Kevin | Ella | Outside | Fan | Cooling |
| --------- | ----- | ---- | ------- | --- | ------- |
|           |       |      |         |     |         |
