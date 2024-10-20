# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')
model = joblib.load("C:/Users/AKIN-JOHNSON/school_record.joblib")

input_data = [[40, 70, 55, 34, 75, 54, 43, 50]]
prediction = model.predict(input_data)
print('Pass' if prediction[0] == 1 else 'Fail')