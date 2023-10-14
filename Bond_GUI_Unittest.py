import unittest
import numpy as np

class Bond_GUI_Tests(unittest.TestCase):
    

    def test_YTMCorrect(self):
        face_value = 1000
        coupon_rate = 0.05
        compounding_periods = 2
        bond_yield_to_maturity = 1
        bond_duration = 4
        result = ((face_value*coupon_rate/compounding_periods*(1-(1+bond_yield_to_maturity/compounding_periods)**(-compounding_periods*bond_duration)))/(bond_yield_to_maturity/compounding_periods))+face_value*(1+(bond_yield_to_maturity/compounding_periods))**(-compounding_periods*bond_duration)
        self.assertEqual(result, 87.06752019509221)
    

    def test_YTM_InCorrect(self):
        face_value = 1000
        coupon_rate = 0.05
        compounding_periods = 2
        bond_yield_to_duration = 1
        bond_duration = 4
        result = ((face_value*coupon_rate/compounding_periods*(1-(1+bond_yield_to_duration/compounding_periods)**(-compounding_periods*bond_duration)))/(bond_yield_to_duration/compounding_periods))+face_value*(1+(bond_yield_to_duration/compounding_periods))**(-compounding_periods*bond_duration)
        self.assertNotEqual(result, 100)


    def test_Bond_Present_Value_Correct_Value(self):
        compounding_periods = (1)#Number of Compounding periods
        face_value = (1000) #Face Value
        payment = (100)#Bond Periodic Payments
        bond_yield_to_maturity = (0.05) #Bond Yield to Maturity
        BondPresentValue = (payment * ((1-(1+bond_yield_to_maturity)**-compounding_periods)/bond_yield_to_maturity) + ((face_value/(1+bond_yield_to_maturity)**compounding_periods)))
        self.assertEqual(BondPresentValue,1047.6190476190477)


    def test_Bond_Present_Value_Incorrect_Value(self):
        componding_periods = (1)#Number of Compounding periods
        face_value = (1000) #Face Value
        payment = (100)#Bond Periodic Payments
        bond_yield_to_maturity = (0.05) #Bond Yield to Maturity
        BondPresentValue = (payment * ((1-(1+bond_yield_to_maturity)**-componding_periods)/bond_yield_to_maturity) + ((face_value/(1+bond_yield_to_maturity)**componding_periods)))
        self.assertNotEqual(BondPresentValue, 1500)


    def test_Portfolio_Standard_Deviation_Correct(self):    
        a_standard_deviation = (0.15) #Standard deviation of Security A
        b_standard_deviation = (0.25) #Standard deviation of Security B
        a_weight = (0.35) #Portfolio Weight of Security A
        b_weight = (0.65) #Portfolio Weight of Security B
        portfolio_correlation = (0.4) #Correlation of both securities in the portfolio
        PortSTDEVFormula = np.sqrt(((a_standard_deviation)**2)*(a_weight)**2 + ((b_standard_deviation)**2)*(b_weight)**2 + (a_weight*b_weight*a_standard_deviation*b_standard_deviation*portfolio_correlation))
        self.assertEqual(PortSTDEVFormula, 0.18048545647780045)
    

    def test_Portfolio_Standard_Deviation_Incorrect(self):    
        a_standard_deviation = (0.15) #Standard deviation of Security A
        b_standard_deviation = (0.25) #Standard deviation of Security B
        a_weight = (0.35) #Portfolio Weight of Security A
        b_weight = (0.65) #Portfolio Weight of Security B
        portfolio_correlation = (0.4) #Correlation of both securities in the portfolio
        PortSTDEVFormula = np.sqrt(((a_standard_deviation)**2)*(a_weight)**2 + ((b_standard_deviation)**2)*(b_weight)**2 + (a_weight*b_weight*a_standard_deviation*b_standard_deviation*portfolio_correlation))
        self.assertNotEqual(PortSTDEVFormula, 0.52)


if __name__ == '__main__':
    unittest.main()