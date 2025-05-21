# Lets Make A BMI Calculator

import streamlit as st

# Title
st.title("BMI Calculator")

# Subtitle
st.subheader("Calculate your Body Mass Index (BMI)")


# Input fields
weight = st.number_input("Enter your weight (in kg)", min_value=1.0, step=0.1)

height = st.number_input("Enter your height (in cm)", min_value=1.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    if weight and height:
        # Convert height from cm to m
        height_m = height / 100
        # Calculate BMI
        bmi = weight / (height_m ** 2)
        # Display result
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.error("Please enter both weight and height.")

# BMI Categories
st.subheader("BMI Categories")

st.write("""
- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 24.9
- Overweight: 25 ≤ BMI < 29.9
- Obesity: BMI ≥ 30
""")

# Additional Information
st.subheader("Additional Information")

st.write("""
BMI is a simple calculation using a person's height and weight. It is defined as the individual's body mass divided by the square of their height. The formula is:
```
BMI = weight (kg) / (height (m) ^ 2)
```
""")

