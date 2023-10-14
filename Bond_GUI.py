import random
import numpy as np
import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.create_viewport(title ="Bond Simulation GUI", width =1500, height =1500)
dpg.setup_dearpygui()


def calcYTMupdate():
    """
    calcYTMupdate takes the user input Yield to Maturity and inputs it into the Bond Price fomula and returns the Bond Price.

    Args:
        None

    Returns:
        Returns the Bond Price based on the user input Yield to Maturity variable.

    Raises:
        TypeError: 'int' object is not callable
    """
    bond_yield_to_maturity = (dpg.get_value(ytm_input)) #Bond Yield to Maturity
    compounding_periods= (dpg.get_value(Comp_input))#Compounding Periods
    duration_input = (dpg.get_value(Dur_input)) #Year to Maturity
    face_value = (dpg.get_value(Face_Value_input)) #Bond Face Value 
    coupon_rate = (dpg.get_value(Coupon_Rate_input)) #Bond Coupon Rate 
    BONDPRICE = ((face_value*coupon_rate/compounding_periods*(1-(1+ bond_yield_to_maturity/compounding_periods)**(-compounding_periods*duration_input)))/(bond_yield_to_maturity/compounding_periods))+face_value*(1+(bond_yield_to_maturity/compounding_periods))**(-compounding_periods*duration_input)
    return dpg.set_value(ytm_display_label, f"Bond Price: {BONDPRICE:.2f}")


def RandomYTMupdate():
    """
    RandomYTupdate takes Random YTM and puts it into the Bond Price Formula.

    Args:
        None

    Returns:
        Returns the Bond Price based on the Randomly calculated YTM.

    Raises:
        TypeError: 'int' object is not callable
    """
    bond_yield_to_maturity = random.uniform(0.01,0.25) #Bond Yield to Maturity
    compounding_periods = random.uniform(1,8) #Compounding periods
    face_value = random.uniform(500,10000) #Bond Face Value 
    Coupon_Rate = random.uniform(0.01,0.25) #Bond Coupon Rate
    bond_duration = random.uniform(1,25) #Bond Duration 
    RBONDPRICE = ((face_value*Coupon_Rate/compounding_periods*(1-(1+ bond_yield_to_maturity/compounding_periods)**(-compounding_periods*bond_duration)))/(bond_yield_to_maturity/compounding_periods))+face_value*(1+(bond_yield_to_maturity/compounding_periods))**(-compounding_periods*bond_duration)
    return dpg.set_value(RYTM_display_label, f"Random Bond Price: {RBONDPRICE:.2f}")


def BondPresentValue():
    """
    BondPresentValue takes given Number of Compounding period input and finds Bond PV.

    Args:
        None

    Returns:
        Returns the Bond Present Value based on the input Number of Compounding Periods.

    Raises:
        TypeError: 'int' object is not callable
    """
    compounding_periods = (dpg.get_value(PV_Comp_input)) #Number of Compounding periods
    face_value = (dpg.get_value(PV_Face_Value_input)) #Face Value
    bond_payment = (dpg.get_value(PV_Payment_input)) #Bond Periodic Payments
    bond_yield_to_maturity = (dpg.get_value(PV_YTM_input)) #Bond Yield to Maturity
    BondPresentValue = (bond_payment * ((1-(1+bond_yield_to_maturity)**-compounding_periods)/bond_yield_to_maturity) + ((face_value/(1+bond_yield_to_maturity)**compounding_periods)))
    return dpg.set_value(BondPVdisplaylabel, f"Bond Present Value: {BondPresentValue:.2f}")

    
def Portfolio_Standard_Deviation():    
    """
    Portfolio_Standard_Deviation takes user inputs from the GUI and outputs the corresponding Portfolio Standard Deviation

    Args:
        None

    Returns:
        Returns the Portfolio Standard Deviation based on the user input individual asset Standard Deviations, Weights, and correlation.

    Raises:
        TypeError: 'int' object is not callable
    """
    a_standard_deviation = (dpg.get_value(SA_SD_input)) #Standard deviation of Security A
    b_standard_deviation = (dpg.get_value(SB_SD_input)) #Standard deviation of Security B
    a_weight = (dpg.get_value(SA_W_input)) #Portfolio Weight of Security A
    b_weight = (dpg.get_value(SB_W_input)) #Portfolio Weight of Security B
    portfolio_correlation = (dpg.get_value(PAC_input)) #Correlation of both securities in the portfolio
    PortSTDEVFormula = np.sqrt(((a_standard_deviation)**2)*(a_weight)**2 + ((b_standard_deviation)**2)*(b_weight)**2 + (a_weight*b_weight*a_standard_deviation*b_standard_deviation*portfolio_correlation))
    return dpg.set_value(PortSTDEVdisplaylabel, f"Portfolio Variance Result: {PortSTDEVFormula:.2f}")


with dpg.window(label ="Bond Simulator", height = 1500, width = 1500):


    with dpg.group(horizontal=True):
        dpg.add_text("Bond Price Calculation")


    with dpg.group(horizontal=True):
        dpg.add_text("Yield to Maturity Input")
        ytm_input = dpg.add_input_float(label ="",default_value =0.01, max_value =25.00 ,callback = calcYTMupdate, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Duration Input")
        Dur_input = dpg.add_input_float(label ="",default_value =0.01, max_value =25.00 ,callback = calcYTMupdate, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Compounding Periods Input")
        Comp_input = dpg.add_input_float(label ="",default_value =1, max_value =25.00 ,callback = calcYTMupdate, on_enter = True)

    
    with dpg.group(horizontal=True):
        dpg.add_text("Face Value Input")
        Face_Value_input = dpg.add_input_float(label ="",default_value =1000, max_value =100000000.00 ,callback = calcYTMupdate, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Bond Coupon Rate Input")
        Coupon_Rate_input = dpg.add_input_float(label ="",default_value =0.05, max_value =1 ,callback = calcYTMupdate, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Bond Price Result:")
        ytm_display_label = dpg.add_text("", color=(255, 255, 0), id="ytm_display_label")


    with dpg.group(horizontal=True):
        dpg.add_text("Random Inputs Bond Price Calculation")

    with dpg.group(horizontal =True):
        dpg.add_text("Random Yield to Maturity Input")
        dpg.add_button(label="Calculate",callback = RandomYTMupdate)
    

    with dpg.group(horizontal =True):
        dpg.add_text("Random Compounding Periods Input")
        dpg.add_button(label="Calculate",callback = RandomYTMupdate)
    

    with dpg.group(horizontal =True):
        dpg.add_text("Random Face Value Input")
        dpg.add_button(label="Calculate",callback = RandomYTMupdate)
    

    with dpg.group(horizontal =True):
        dpg.add_text("Random Coupon Rate Input")
        dpg.add_button(label="Calculate",callback = RandomYTMupdate)
    

    with dpg.group(horizontal =True):
        dpg.add_text("Random Bond Duration Input")
        dpg.add_button(label="Calculate",callback = RandomYTMupdate)
    

    with dpg.group(horizontal=True):
        dpg.add_text("Bond Price Result:")
        RYTM_display_label = dpg.add_text("", color=(255, 255, 0), id="RYTM_display_label")

    
    with dpg.group(horizontal=True):
        dpg.add_text("Bond Present Value Calculation")


    with dpg.group(horizontal=True):
        dpg.add_text("Compounding Periods Input")
        PV_Comp_input = dpg.add_input_float(label ="",default_value =0.01, max_value =25.00 ,callback = BondPresentValue, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Face Value Input")
        PV_Face_Value_input = dpg.add_input_float(label ="",default_value =1000, max_value =100000000 ,callback = BondPresentValue, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Bond Payment Input")
        PV_Payment_input = dpg.add_input_float(label ="",default_value =100, max_value =100000000 ,callback = BondPresentValue, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Bond Yield to Maturity Input")
        PV_YTM_input = dpg.add_input_float(label ="",default_value =0.01, max_value =1 ,callback = BondPresentValue, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Bond Present Value Result:")
        BondPVdisplaylabel = dpg.add_text("", color=(255, 255, 0), id="BondPVdisplaylabel")


    with dpg.group(horizontal=True):
        dpg.add_text("Portfolio Standard Deviation Calculation")


    with dpg.group(horizontal=True):
        dpg.add_text("Security A Standard Deviation Input")
        SA_SD_input = dpg.add_input_float(label ="",default_value =0.01, max_value =1 ,callback = Portfolio_Standard_Deviation, on_enter = True)

    
    with dpg.group(horizontal=True):
        dpg.add_text("Security B Standard Deviation Input")
        SB_SD_input = dpg.add_input_float(label ="",default_value =0.01, max_value =1 ,callback = Portfolio_Standard_Deviation, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Security A Portfolio Weight Input")
        SA_W_input = dpg.add_input_float(label ="",default_value =0.01, max_value =1 ,callback = Portfolio_Standard_Deviation, on_enter = True)


    with dpg.group(horizontal=True):
        dpg.add_text("Security B Portfolio Weight Input")
        SB_W_input = dpg.add_input_float(label ="",default_value =0.01, max_value =1 ,callback = Portfolio_Standard_Deviation, on_enter = True)
    

    with dpg.group(horizontal=True):
        dpg.add_text("Portfolio Asset Correlation Input")
        PAC_input = dpg.add_input_float(label ="",default_value =0.01, max_value =1 ,callback = Portfolio_Standard_Deviation, on_enter = True)
    

    with dpg.group(horizontal=True):
        dpg.add_text("Two Asset Portfolio Standard Deviation Result:")
        PortSTDEVdisplaylabel = dpg.add_text("", color=(255, 255, 0), id="PortSTDEVdisplaylabel")


dpg.set_viewport_resizable(True)
dpg.set_viewport_width(1000)
dpg.set_viewport_height(1000)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()