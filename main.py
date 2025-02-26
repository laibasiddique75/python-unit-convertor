import streamlit as st

# Title of the app
st.title("Unit Converter")

# Available units
units = ["mm", "cm", "m"]

# Dropdowns for selecting units
unit1 = st.selectbox("Select the unit of the input value:", units)
unit2 = st.selectbox("Select the unit to convert to:", units)

# Input for number
num = st.number_input("Enter the number:", min_value=0.0, format="%.4f")

# Conversion logic
def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "mm" and to_unit == "cm":
        return value / 10
    elif from_unit == "mm" and to_unit == "m":
        return value / 1000
    elif from_unit == "cm" and to_unit == "mm":
        return value * 10
    elif from_unit == "cm" and to_unit == "m":
        return value / 100
    elif from_unit == "m" and to_unit == "mm":
        return value * 1000
    elif from_unit == "m" and to_unit == "cm":
        return value * 100
    else:
        return None

# Convert button
if st.button("Convert"):
    converted_value = convert_units(num, unit1, unit2)
    if converted_value is not None:
        st.success(f"Converted Value: {converted_value} {unit2}")
    else:
        st.error("Invalid conversion!")

