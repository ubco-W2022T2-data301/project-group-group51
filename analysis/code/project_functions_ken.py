import pandas as pd
import numpy as np

def processed_Without_Time(file):
    
    timedrop = (
        pd.read_csv(file)
        .drop(columns= ['carrier_ct', 'weather_ct','nas_ct', 'security_ct', 'late_aircraft_ct', 'year', 'month','airport', 'airport_name'])
    )
    return timedrop

        
#df6 = airlinedatafiltered.groupby('month')['carrier_delay','weather_delay','nas_delay','security_delay', 'late_aircraft_delay'].sum().reset_index()

def grouped_Month(file):
    processed_month = (
    pd.read_csv(file)
    .groupby('month')['carrier_delay','weather_delay','nas_delay','security_delay', 'late_aircraft_delay'].sum().reset_index()   
    )
    return processed_month
