import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from rank_based_INT import *
import pandas as pd
from pandas.core.frame import DataFrame
#
#Hakutaulu ja koheesio
#
#daterows={'2011':[0,12],'2012':[12,24],'2013':[24,36],'2014':[36,48],'2015':[48,60],'2016':[60,72],'2017':[72,84],'2018':[84,96],'2019':[96,108],'2020':[108,120]}
daterows={'2006':[0,12],'2007':[12,24],'2008':[24,36],'2009':[36,48],'2010':[48,60],'2011':[60,72],'2012':[72,84],'2013':[84,96],'2014':[96,108],'2015':[108,120],'2016':[120,132],'2017':[132,144],'2018':[144,156],'2019':[156,168],'2020':[168,180]}
#values from england 2011-2020
#pd.read_csv('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',sep=";",header=0)
sunMinValue=float(35)
sunMaxValue=float(299.4)
def SetMultiplePlots(df,df2,df3,df4,df5,df6,df7):
    fig,(ax1, ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(7, 1)
    ax1.plot(df.iloc[:,0],df.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax1.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax1.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax1.format_xdata = mdates.DateFormatter('%Y-%m')
    ax1.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax1.grid(True)
    
    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    
    ax2.plot(df2.iloc[:,0],df2.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax2.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax2.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax2.format_xdata = mdates.DateFormatter('%Y-%m')
    ax2.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax2.grid(True)
    ax3.plot(df3.iloc[:,0],df3.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax3.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax3.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax3.format_xdata = mdates.DateFormatter('%Y-%m')
    ax3.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax3.grid(True)
    ax4.plot(df4.iloc[:,0],df4.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax4.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax4.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax4.format_xdata = mdates.DateFormatter('%Y-%m')
    ax4.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax4.grid(True)
    ax5.plot(df5.iloc[:,0],df5.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax5.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax5.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax5.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax5.format_xdata = mdates.DateFormatter('%Y-%m')
    ax5.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax5.grid(True)
    ax6.plot(df6.iloc[:,0],df6.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax6.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax6.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax6.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax6.format_xdata = mdates.DateFormatter('%Y-%m')
    ax6.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax6.grid(True)


    ax7.plot(df7.iloc[:,0],df7.iloc[:,1])

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=1)
    ax7.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()   
    ax7.xaxis.set_minor_locator(fmt_month)
    
    
    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax7.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Round to nearest years.
    # datemin = np.datetime64(months[0], 'Y')
    # datemax = np.datetime64(months[-1], 'Y') + np.timedelta64(1, 'Y')
    # ax.set_xlim(datemin, datemax)
    
    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax7.format_xdata = mdates.DateFormatter('%Y-%m')
    ax7.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax7.grid(True)


    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    ax1.set_ylabel('Mean')
    ax2.set_ylabel('Max')
    ax3.set_ylabel('Min')
    ax4.set_ylabel('Sun')
    ax5.set_ylabel('Rain')
    ax6.set_ylabel('Depression')
    ax7.set_ylabel('Exercise')
    fig.autofmt_xdate()
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

    print(depression)
    months=depression.iloc[yearstart:yearend,0]
    _Val=depression.iloc[yearstart:yearend,1]
    
    #print('yksikkötarkistus' +filepath)
    #print("Vuosi")
    #print(yearstart)
    #print(_Val)
    int_VALS=rank_INT(_Val,stochastic=False)
    _Val=int_VALS
   # print('int_VALS')
    #print(int_VALS)
    #maximumvalue=max(_Val)
    #maximumvalue=max(depression.iloc[0:109,1])
    #print('_Vals')
    #print(_Val)
    #min_value=min(_Val)
    #min_value=min(depression.iloc[0:109,1])
    #print("min_value")
    #print(min_value)
    summa=0.0
    normalized_values=[]
    for x in _Val:
        summa+x
        normalized_values.append(x)
    
    #print('filename of normalized values')
    #print(filepath)
    #print(summa/12.0)
    #print("normalized values:")
    #print(normalized_values)
    dsmonths=pd.Series(months)
    dsValues=pd.Series(normalized_values)
    df_all=pd.DataFrame(dsmonths)
    dfvalues=pd.DataFrame(dsValues)
    df_all['normalized_values']=normalized_values
    #print('describe')
    #print(df_all['normalized_values'].describe())
    #print('df_all')
    #print(df_all)
    return df_all

def GetWeather(filepath,yearstart,yearend):
    months=[]
    weather=pd.read_csv(filepath,sep=";",header=0)
    

    c=2006-yearstart
    if c<0:
        c=c*(-1)
    ye=2006-yearend
    if ye<0:
        ye=ye*(-1)
    # print('c: ')
    # print(c)
    for_length=weather.iloc[89:104,0]
    sun_scope=weather.iloc[89:104,:13]
    sun_dated=[]
    
    # print(sun_scope.iloc[c,:13])
    allSunValues=sun_scope.iloc[:,1:13]
    #print(allSunValues)
    allSunValuesInArray=[]
    #print(allSunValues)
    u=sun_scope.iloc[c,:13]
    
    #print('u')
    #print(u) 
    for x in range(0,15):
        normalized=[]
        for y in range(1,13):
           # u=df_u_INT.iloc[x,y]
            u=sun_scope.iloc[x,y]
            d=float(u)
            #print("Float d")
            #print(type(d))
            
            normalized.append(d)
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
                #u=sun_scope.iloc[c,1:13]
                #d=u.values
            
            if y>=10:
                yeartoint=int(x)
                yeartoint=int(x)
                t=str(yeartoint)+'-'+str(y)+'-01'

                sun_dated_array.append(t)
        sun_dated.append(sun_dated_array)
    #print(sun_dated[0])
    sun_to_series=[]
    if yearend>yearstart:
        for x in range(c,ye):
            for y in range(0,12):
                months.append(sun_dated[x][y])
                sun_to_series.append(allSunValuesInArray[x][y])

    if yearend==yearstart:
        for y in range(0,12):
                months.append(sun_dated[ye][y])
                sun_to_series.append(allSunValuesInArray[ye][y])
    
    dsmonths=pd.Series(months)
    datetimed_months=pd.to_datetime(dsmonths)
    #print('datetimed.dtypes')
    #print(datetimed_months.dtypes)
    df_all=pd.DataFrame(datetimed_months)       
    dssunvalues=pd.Series(sun_to_series)
    #print('filename of normalized values')
    #print(filepath)
    #print('weather values before INT')
    #print(dssunvalues)
    ds_INT_Values=rank_INT(dssunvalues,stochastic=False)
    # print('weather values after INT')
    # print(ds_INT_Values)
    # print('is average 0?')
    summarum=0.0
    for x in ds_INT_Values:
        summarum+x

    if summarum!=0.0:
        print('NO')
        # print(summarum)
    else:
        print('YES')
        # print(summarum)
    df_all['Weather']=ds_INT_Values
    return df_all
#months=[]
year=2006
yearend=2020
# 



# SunEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',year,yearend)
# MeanEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Mean/England_MEAN.csv',year,yearend)
# MinEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/MinTemp/England_MIN.csv',year,yearend)
# #MaxEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/MaxTemp/EnglandMax.csv',year,yearend)


# # DepEngMonth=GetTrends('BY MONTH/Depression/Depression monthlyGB-Eng.csv',daterows[str(year)][0],daterows[str(yearend)][1])
# # ExeEngMonth=GetTrends('BY MONTH/Exercise/Exercise monthlyGB-Eng.csv',daterows[str(year)][0],daterows[str(yearend)][1])
# #ZoomEngMonth=GetTrends('BY MONTH/zoom/zoom monthlyGB-Eng.csv',daterows[str(year)][0],daterows[str(yearend)][1])


# # plt.plot(DepEngMonth.iloc[:,0],DepEngMonth.iloc[:,1],label='Depression' )
# # plt.plot(ExeEngMonth.iloc[:,0],ExeEngMonth.iloc[:,1],label='Exercise' )
# # #plt.plot(ZoomEngMonth.iloc[:,0],ZoomEngMonth.iloc[:,1],label='Zoom' )
# # plt.plot(SunEngMonthly.iloc[:,0],SunEngMonthly.iloc[:,1], label='Sun')
# # plt.plot(MeanEngMonthly.iloc[:,0],MeanEngMonthly.iloc[:,1], label='Mean')
# # plt.plot(MinEngMonthly.iloc[:,0],MinEngMonthly.iloc[:,1], label='Min')
# #plt.plot(MaxEngMonthly.iloc[:,0],MaxEngMonthly.iloc[:,1], label='Max')


# #print(DepEngMonth)
# #Setplot(SunEngMonthly)
# # Setplot(DepEngMonth)
# # Setplot(ExeEngMonth)
# # Setplot(ZoomEngMonth)

# plt.legend() 
# plt.show()

# 
# for x in range(2012,2021):
#     SunEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',x,x)
#     sunarray=sunarray.append(SunEngMonthly,ignore_index=True)
#     #plt.plot(SunEngMonthly.iloc[:,0],SunEngMonthly.iloc[:,1], label='Sun')
# print('sunarray')
# print(sunarray)
# Setplot(sunarray)
# plt.legend() 
# plt.show()

# fig, (ax1, ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9) = plt.subplots(9, 1,sharex=True, sharey=True)
# sunarray=SunEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',2006,2006)
# meanarray=MeanEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Mean/England_MEAN.csv',2006,2006)
maxarray=MaxEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/MaxTemp/EnglandMax.csv',2006,2006)
# minarray=MinEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/MinTemp/England_MIN.csv',2006,2006)
# rainarray=RainEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Rain/England_RAIN.csv',2006,2006)
# deparray=DepEngMonth=GetTrends('BY MONTH/Depression_2006/Depression monthlyGB-Eng.csv',daterows[str(2006)][0],daterows[str(2006)][1])
# exearray=ExeEngMonth=GetTrends('BY MONTH/Exercise_2006/Exercise monthlyGB-Eng.csv',daterows[str(2006)][0],daterows[str(2006)][1])
# happyarray=HappyEngMonth=GetTrends('BY MONTH/Happy/Happy monthlyGB-Eng.csv',daterows[str(2006)][0],daterows[str(2006)][1])
# happinessarray=HappinessEngMonth=GetTrends('BY MONTH/Happiness/Happiness monthlyGB-Eng.csv',daterows[str(2006)][0],daterows[str(2006)][1])

for x in range(2007,yearend):
    # print('Vuosi: ')
    # print(x)
    # MeanEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Mean/England_MEAN.csv',x,x)
    # meanarray=meanarray.append(MeanEngMonthly,ignore_index=True)

    # MinEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/MinTemp/England_MIN.csv',x,x)
    # minarray=minarray.append(MinEngMonthly,ignore_index=True)

    MaxEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/MaxTemp/EnglandMax.csv',x,x)
    maxarray=maxarray.append(MaxEngMonthly,ignore_index=True)

    # SunEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',x,x)
    # sunarray=sunarray.append(SunEngMonthly,ignore_index=True)   

    # RainEngMonthly=GetWeather('BY MONTH/CSV_files_with_dot/Rain/England_RAIN.csv',x,x)
    # rainarray=rainarray.append(RainEngMonthly,ignore_index=True)

    # DepEngMonth=GetTrends('BY MONTH/Depression_2006/Depression monthlyGB-Eng.csv',daterows[str(x)][0],daterows[str(x)][1])
    # deparray=deparray.append(DepEngMonth,ignore_index=True) 

    # ExeEngMonth=GetTrends('BY MONTH/Exercise_2006/Exercise monthlyGB-Eng.csv',daterows[str(x)][0],daterows[str(x)][1])
    # exearray=exearray.append(ExeEngMonth,ignore_index=True) 

    # HappyEngMonth=GetTrends('BY MONTH/Happy/Happy monthlyGB-Eng.csv',daterows[str(x)][0],daterows[str(x)][1])
    # happyarray=happyarray.append(HappyEngMonth,ignore_index=True) 
    
    # HappinessEngMonth=GetTrends('BY MONTH/Happiness/Happiness monthlyGB-Eng.csv',daterows[str(x)][0],daterows[str(x)][1])
    # happinessarray=happinessarray.append(HappinessEngMonth,ignore_index=True) 


compression_opts = dict(method='zip',
                        archive_name='MaxTempEng.csv')  

maxarray.to_csv('MaxTempEng.zip', index=False,
          compression=compression_opts) 

# ax1.plot(meanarray.iloc[:,0],meanarray.iloc[:,1] )
# ax2.plot(maxarray.iloc[:,0],maxarray.iloc[:,1] )
# ax3.plot(minarray.iloc[:,0],minarray.iloc[:,1] )
# ax4.plot(sunarray.iloc[:,0],sunarray.iloc[:,1])
# ax5.plot(rainarray.iloc[:,0],rainarray.iloc[:,1])
# ax6.plot(deparray.iloc[:,0],deparray.iloc[:,1])
# ax7.plot(exearray.iloc[:,0],exearray.iloc[:,1])
# ax8.plot(happyarray.iloc[:,0],happyarray.iloc[:,1])
# ax9.plot(happinessarray.iloc[:,0],happinessarray.iloc[:,1])


# ax1.set_ylabel('Mean')
# ax2.set_ylabel('Max')
# ax3.set_ylabel('Min')
# ax4.set_ylabel('Sun')
# ax5.set_ylabel('Rain')
# ax6.set_ylabel('Depression')
# ax7.set_ylabel('Exercise')
# ax8.set_ylabel('Happy')
# ax9.set_ylabel('Happiness')
# # SetMultiplePlots(meanarray,maxarray,minarray,sunarray,rainarray,deparray,exearray)
# # plt.legend() 
# plt.show()




# fig = plt.figure()
# fig.subplots(sharex=True, sharey=True)












#sunvalues=pd.read_csv('BY MONTH/CSV_files_with_dot/Sun/England_SUN.csv',sep=";",header=0)
# #print(sunvalues)
# c=2011-year
# if c<0:
#     c=c*(-1)
# ye=2011-yearend
# if ye<0:
#     ye=ye*(-1)
# # print('c: ')
# # print(c)
# for_length=sunvalues.iloc[94:104,0]
# sun_scope=sunvalues.iloc[94:104,:13]
# sun_dated=[]
# sun_val_ser=[]
# # print(sun_scope.iloc[c,:13])
# allSunValues=sun_scope.iloc[:,1:13]
# #print(allSunValues)
# allSunValuesInArray=[]
# #print(allSunValues)
# u=sun_scope.iloc[c,:13]
# for x in range(0,10):
#     normalized=[]
#     for y in range(1,13):
#         u=sun_scope.iloc[x,y]
#         d=float(u)
#        # print(d)
#         i=(d-sunMinValue)/(sunMaxValue-sunMinValue)
#         normalized.append(i)
#     allSunValuesInArray.append(normalized)
# #print(allSunValuesInArray[0])    


# sun_dated_array=[]
# # print(sunMinValue)
# for x in for_length:
#     sun_dated_array=[]
#     for y in range(1,13):        
#         if y<10:
#             yeartoint=int(x)
#             t=str(yeartoint)+'-0'+str(y)+'-01'
#             #print(x)
#             sun_dated_array.append(t)
#             u=sun_scope.iloc[c,1:13]
#             d=u.values
#             sun_val_ser=d
#         if y>=10:
#             yeartoint=int(x)
#             yeartoint=int(x)
#             t=str(yeartoint)+'-'+str(y)+'-01'
           
#             sun_dated_array.append(t)
#     sun_dated.append(sun_dated_array)
# #print(sun_dated[0])
# sun_to_series=[]
# if yearend>year:
#     for x in range(c,ye):
#         for y in range(0,12):
#             months.append(sun_dated[x][y])
#             sun_to_series.append(allSunValuesInArray[x][y])
        
# if yearend==year:
#     for y in range(0,12):
#             months.append(sun_dated[ye][y])
#             sun_to_series.append(allSunValuesInArray[ye][y])
 
# dsmonths=pd.Series(months)
# datetimed_months=pd.to_datetime(dsmonths)
# print('datetimed.dtypes')
# print(datetimed_months.dtypes)
# df_all=pd.DataFrame(datetimed_months)    
# dssunvalues=pd.Series(sun_to_series)
# df_all['Sun']=dssunvalues
# print(df_all.dtypes)







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

