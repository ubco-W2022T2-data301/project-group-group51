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

airlinedata3=pd.read_csv('../data/raw/airline_data_filtered.csv').drop(['Unnamed: 0','carrier_ct'],axis=1)

airlinedata1['not_carrier_rltd']=airlinedata1['nas_delay']+airlinedata1['weather_delay']
df1 = airlinedata1.groupby('carrier_name')['not_carrier_rltd'].sum().reset_index()
airlinedata1['carrier_rltd']=airlinedata1['arr_cancelled']+airlinedata1['arr_diverted']+airlinedata1['arr_delay']+airlinedata1['carrier_delay']+airlinedata1['security_delay']+airlinedata1['late_aircraft_delay']
df2=airlinedata1.groupby('carrier_name')['carrier_rltd'].sum().reset_index()
df3 = airlinedata1.groupby('carrier_name')['arr_flights'].sum().reset_index()

airlinedata4=airlinedata1.drop(['carrier_ct','weather_ct','nas_ct','security_ct','late_aircraft_ct'],axis=1)
pv1 = airlinedata3.pivot_table("weather_delay", index = "month", columns = ["Statecode"], aggfunc = np.sum)
pv2 = airlinedata1.pivot_table("late_aircraft_delay", index = "carrier_name", columns = ["month"], aggfunc = np.sum)