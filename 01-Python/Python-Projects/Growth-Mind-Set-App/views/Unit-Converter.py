import streamlit as st


def convertUnits(value, from_unit, to_unit, category):
    conversionFactors = {
        "Length": {
            "Meters": 1000, "Kilometers": 1, "Centimeters": 100, "Millimeters": 1000,
            "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
        },
        "Weight": {
            "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        },
        "Volume": {
    "Liters": 1,            
    "Milliliters": 1000,    
    "Cubic Meters": 0.001, 
    "Cubic Centimeters": 1000,  
    "Cubic Inches": 61.0237, 
    "Cubic Feet": 0.0353147, 
    "Cubic Yards": 0.00130795, 
    "Gallons (US)": 0.264172,  
    "Gallons (UK)": 0.219969,  
    "Quarts (US)": 1.05669,    
    "Pints (US)": 2.11338      
},
"Time": {
    "Seconds": 1,
    "Milliseconds": 1000,
    "Microseconds": 1e6,
    "Minutes": 1/60,
    "Hours": 1/3600,
    "Days": 1/86400,
    "Weeks": 1/604800,
    "Months (30 days)": 1/2.628e+6,
    "Years": 1/3.154e+7
},
"Speed": {
    "Meters per Second": 1,
    "Kilometers per Hour": 3.6,
    "Miles per Hour": 2.23694,
    "Feet per Second": 3.28084,
    "Knots": 1.94384
},

"Pressure": {
    "Pascals": 1,
    "Kilopascals": 0.001,
    "Bars": 1e-5,
    "Atmospheres": 9.8692e-6,
    "Torr": 0.00750062,
    "Pounds per Square Inch": 0.000145038
}
    }

    if category == "Temperature":
        return conversionFactors[category][to_unit](conversionFactors[category][from_unit](value))

    return value * (conversionFactors[category][to_unit] / conversionFactors[category][from_unit])


st.title("Unit Converter!")

categories = ["Length", "Weight", "Temperature","Volume","Time","Speed","Pressure"]


category = st.selectbox("Select Category:", categories)


units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liters", "Milliliters", "Cubic Meters", "Cubic Centimeters", "Cubic Inches", "Cubic Feet", "Cubic Yards", "Gallons (US)", "Gallons (UK)", "Quarts (US)", "Pints (US)"],
    "Time": ["Seconds", "Milliseconds", "Microseconds", "Minutes", "Hours", "Days", "Weeks", "Months (30 days)", "Years"],
    "Pressure": ["Pascals", "Kilopascals", "Bars", "Atmospheres", "Torr", "Pounds per Square Inch"],
    "Speed": ["Meters per Second", "Kilometers per Hour", "Miles per Hour", "Feet per Second", "Knots"]
}


value = st.number_input("Enter Value:", min_value=1)


col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From:", units[category])
with col2:
    to_unit = st.selectbox("To:", units[category])


if st.button("Convert"):
    result = convertUnits(value, from_unit, to_unit, category)
    st.success(f"Converted Value: {result} {to_unit}")
