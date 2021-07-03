import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
from pandas.core.frame import DataFrame
#
#Hakutaulu ja koheesio
#
daterows={'2011':[0,12],'2012':[12,24],'2013':[24,36],'2014':[36,48],'2015':[48,60],'2016':[60,72],'2017':[72,84],'2018':[84,96],'2019':[96,108],'2020':[106,109]}
#values from england 2011-2020
sunMinValue=float(35)
sunMaxValue=float(299.4)
def Setplot(df):
    fig, ax = plt.subplots()
    ax.plot(df.iloc[:,0],df.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax.format_xdata = mdates.DateFormatter('%Y-%m')
    ax.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax.grid(True)
    
    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    fig.autofmt_xdate()

def GetTrends(filepath,yearstart,yearend):

    depression=pd.read_csv(filepath,parse_dates=[0])


    months=depression.iloc[yearstart:yearend,0]
    _Val=depression.iloc[yearstart:yearend,1]
    #maximumvalue=max(_Val)
    maximumvalue=max(depression.iloc[0:109,1])
    #print('maximumvalue')
   #print(maximumvalue)
    #min_value=min(_Val)
    min_value=min(depression.iloc[0:109,1])
    print("min_value")
    print(min_value)
    normalized_values=[]
    for x in _Val:
        normalized_values.append((x-min_value)/(maximumvalue-min_value))
    print("normalized values:")
    print(normalized_values)
    dsmonths=pd.Series(months)
    dsValues=pd.Series(normalized_values)
    df_all=pd.DataFrame(dsmonths)
    dfvalues=pd.DataFrame(dsValues)
    df_all['normalized_values']=normalized_values
    print('df_all')
    print(df_all)
    return df_all

def GetWeather(filepath,yearstart,yearend):
    weather=pd.read_csv(filepath,parse_dates=[0])


    months=weather.iloc[yearstart:yearend,0]
    _Val=weather.iloc[yearstart:yearend,1]
    #maximumvalue=max(_Val)
    maximumvalue=max(weather.iloc[0:109,1])
    #print('maximumvalue')
   #print(maximumvalue)
    #min_value=min(_Val)
    min_value=min(weather.iloc[0:109,1])
    print("min_value")
    print(min_value)
    normalized_values=[]
    for x in _Val:
        normalized_values.append((x-min_value)/(maximumvalue-min_value))
    print("normalized values:")
    print(normalized_values)
    dsmonths=pd.Series(months)
    dsValues=pd.Series(normalized_values)
    df_all=pd.DataFrame(dsmonths)
    dfvalues=pd.DataFrame(dsValues)
    df_all['normalized_values']=normalized_values
    print('df_all')
    print(df_all)
    return df_all
months=[]
year=2013
yearend=2013
sunvalues=pd.read_csv('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',sep=";",header=0)
#print(sunvalues)
c=2011-year
if c<0:
    c=c*(-1)
ye=2011-yearend
if ye<0:
    ye=ye*(-1)
# print('c: ')
# print(c)
for_length=sunvalues.iloc[94:104,0]
sun_scope=sunvalues.iloc[94:104,:13]
sun_dated=[]
sun_val_ser=[]
# print(sun_scope.iloc[c,:13])
allSunValues=sun_scope.iloc[:,1:13]
#print(allSunValues)
allSunValuesInArray=[]
#print(allSunValues)
u=sun_scope.iloc[c,:13]
for x in range(0,10):
    normalized=[]
    for y in range(1,13):
        u=sun_scope.iloc[x,y]
        d=float(u)
       # print(d)
        i=(d-sunMinValue)/(sunMaxValue-sunMinValue)
        normalized.append(i)
    allSunValuesInArray.append(normalized)
#print(allSunValuesInArray[0])    


sun_dated_array=[]
# print(sunMinValue)
for x in for_length:
    sun_dated_array=[]
    for y in range(1,13):        
        if y<10:
            yeartoint=int(x)
            t=str(yeartoint)+'-0'+str(y)+'-01'
            #print(x)
            sun_dated_array.append(t)
            u=sun_scope.iloc[c,1:13]
            d=u.values
            sun_val_ser=d
        if y>=10:
            yeartoint=int(x)
            yeartoint=int(x)
            t=str(yeartoint)+'-'+str(y)+'-01'
           
            sun_dated_array.append(t)
    sun_dated.append(sun_dated_array)
#print(sun_dated[0])
sun_to_series=[]
if yearend>year:
    for x in range(c,ye):
        for y in range(0,12):
            months.append(sun_dated[x][y])
            sun_to_series.append(allSunValuesInArray[x][y])
        
if yearend==year:
    for y in range(0,12):
            months.append(sun_dated[ye][y])
            sun_to_series.append(allSunValuesInArray[ye][y])
 
dsmonths=pd.Series(months)
datetimed_months=pd.to_datetime(dsmonths)
print('datetimed.dtypes')
print(datetimed_months.dtypes)
df_all=pd.DataFrame(datetimed_months)    
dssunvalues=pd.Series(sun_to_series)
df_all['Sun']=dssunvalues
print(df_all.dtypes)
#Setplot(df_all)







#datetime_rev=
#print(d['2019'][1])
DepEngMonth=GetTrends('BY MONTH/Depression/Depression monthlyGB-Eng.csv',daterows['2013'][0],daterows['2013'][1])
print('DepEngMonth.dtypes')
print(DepEngMonth.dtypes)
#DepEngMonth2=GetTrends('BY MONTH/Depression/Depression monthlyGB-Eng.csv',daterows['2013'][0],daterows['2013'][1])
# fig = plt.figure()

# fig.subplots(sharex=True, sharey=True)

plt.plot(DepEngMonth.iloc[:,0],DepEngMonth.iloc[:,1],label='Depression' )#df_all.iloc[:,0],df_all.iloc[:,1]
plt.plot(df_all.iloc[:,0],df_all.iloc[:,1], label='Sun')
plt.legend() 
# print(df_all.iloc[:,0])

#print(DepEngMonth)
#Setplot(DepEngMonth)
plt.show()
























# fig, ax = plt.subplots()
# ax.plot(DepEngMonth.iloc[:,0],DepEngMonth.iloc[:,1])

# # Major ticks every 6 months.
# fmt_half_year = mdates.MonthLocator(interval=1)
# ax.xaxis.set_major_locator(fmt_half_year)

# # Minor ticks every month.
# fmt_month = mdates.MonthLocator()
# ax.xaxis.set_minor_locator(fmt_month)


# # Text in the x axis will be displayed in 'YYYY-mm' format.
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# # Round to nearest years.
# # datemin = np.datetime64(months[0], 'Y')
# # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
# # ax.set_xlim(datemin, datemax)

# # Format the coords message box, i.e. the numbers displayed as the cursor moves
# # across the axes within the interactive GUI.
# ax.format_xdata = mdates.DateFormatter('%Y-%m')
# ax.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
# ax.grid(True)

# # Rotates and right aligns the x labels, and moves the bottom of the
# # axes up to make room for them.
# fig.autofmt_xdate()

