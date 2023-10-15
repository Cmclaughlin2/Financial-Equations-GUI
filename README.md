## Project Overview

This script is a graphical user interface (GUI) application for simulating bond prices, present values, and portfolio standard deviation calculations. 
The user can adjust variables such as the Yield to Maturity, compounding periods, face value, and coupon rate to fit their individual needs. 
The script also allows for the portfolio standard deviation calculation of a two-asset portfolio based on their indiviudal standard deviations, weights, and asset correlations.

## User Manual

### Bond Price Calculation User Inputs

1. **Yield to Maturity Input:** Enter the bond yield to maturity.
2. **Duration Input:** Enter the bond duration in years.
3. **Compounding Periods Input:** Enter the amount of times the bond compounds annually.
4. **Face Value Input:** Enter the bond face value.
5. **Bond Coupon Rate Input:** Enter the bond coupon rate.

### Random Bond Price Calculation User Inputs

**All User Inputs:** When the "calculate" button widget is pressed for each user input variable a randomly generated figure is cast into the formula.

### Bond Present Value Calculation User Inputs 

1. **Compounding Periods Input:** Enter the amount of times the bond compounds annually.
2. **Face Value Input:** Enter the bond face value.
3. **Bond Payment Input:** Enter bond periodic payment.
4. **Bond Yield to Maturity Input:** Enter the bond yield to maturity.

### Portfolio Standard Deviation Calculation User Inputs

1. **Security A Standard Deviation Input:** Enter security A standard deviation.
2. **Security B Standard Deviation Input:** Enter security B standard deviation.
3. **Security A Portfolio Weight Input:** Enter portfolio weight of security A.
4. **Security B Portfolio Weight Input:** Enter portfolio weight of security B.
5. **Portfolio Asset Correlation Input:** Enter portfolio correlation between security A and security B.

## Dependencies Overview

- **Dear PyGui:** A library that provides a framework for GUI creation.
- **NumPy:** A library that provides a framework for statistical analysis. 
- **Random:** A Python standard library utilized for random statistical computations.
- **unittest:** A Python standard library utilized for comprehensive script function unit testing.

## How to Run the Application

1. **Install Dependencies:**
    - Make sure you have Python installed on your system.
    - Install the required libraries using the following terminal commands:
        ```
        pip install dearpygui numpy
        ```
2. **Run the Application:**
    - Run the Python script containing the provided code.
    - The GUI window will render allowing the user to interface with the function widgets.

3. **Unittest Functions upon adjustment:**
    - If making adjustments to the script ensure to make sure that the function logic is correct with the included unittest.py file.
  
## Variable input notes / financial standards

- **Yield to Maturity (YTM) Input:** The YTM should be entered in the floating point format.
- **Standard Deviation:** Standard deviation values should be entered in the floating point format.
- **Face Value:** Enter the face value or the issuing value of the bond. The standard bond face value is one thousand dollars. 
- **Coupon Rate:** Coupon rate should be entered in the floating point format.

## Contributions and Issues

This application is open-source with the MIT license, and contributions are welcome. If you encounter any issues or have suggestions for improvements, please create a GitHub issue in the repository associated with this code.

---

*Note: This README provides a basic overview of the Bond Simulation GUI and instructions for usage. For detailed information and troubleshooting, please refer to the source code and accompanying comments.*
