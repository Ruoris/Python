
import pandas as pd

from pytrends.request import TrendReq

pytrend = TrendReq(retries=2, backoff_factor=0.1)
kw_list=['exercise','lose weight','depression','weight loss']
location='GB'
year='2020'
filetype='.csv'
archivename='4words_'+location+'_'+year
#January
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-01-01 '+year+'-01-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Janbyday".csv')  
                        
historical_Interest_DF.to_csv(year+'_January_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#February
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-02-01 '+year+'-02-28',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Febbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_Feb_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#March
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-03-01 '+year+'-03-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_marchbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_march_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#April
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-04-01 '+year+'-04-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_april_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_april_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#May
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-05-01 '+year+'-05-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_may_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_may_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#June
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-06-01 '+year+'-06-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_June_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_June_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#July
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-07-01 '+year+'-07-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_july_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_july_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#august
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-08-01 '+year+'-08-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_august_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_august_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#september
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-09-01 '+year+'-09-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_september_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_september_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#october
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-10-01 '+year+'-10-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_october_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_october_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#november
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-11-01 '+year+'-11-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_november_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_november_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#December
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-12-01 '+year+'-12-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_December_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_December_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#GB-eng
location='GB-ENG'
#January
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-01-01 '+year+'-01-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Janbyday".csv')  
                        
historical_Interest_DF.to_csv(year+'_January_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#February
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-02-01 '+year+'-02-28',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Febbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_Feb_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#March
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-03-01 '+year+'-03-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_marchbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_march_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#April
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-04-01 '+year+'-04-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_april_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_april_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#May
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-05-01 '+year+'-05-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_may_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_may_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#June
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-06-01 '+year+'-06-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_June_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_June_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#July
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-07-01 '+year+'-07-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_july_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_july_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#august
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-08-01 '+year+'-08-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_august_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_august_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#september
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-09-01 '+year+'-09-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_september_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_september_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#october
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-10-01 '+year+'-10-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_october_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_october_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#november
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-11-01 '+year+'-11-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_november_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_november_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#December
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-12-01 '+year+'-12-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_December_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_December_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 


#GB-sct
location='GB-SCT'
#January
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-01-01 '+year+'-01-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Janbyday".csv')  
                        
historical_Interest_DF.to_csv(year+'_January_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#February
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-02-01 '+year+'-02-28',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Febbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_Feb_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#March
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-03-01 '+year+'-03-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_marchbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_march_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#April
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-04-01 '+year+'-04-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_april_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_april_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#May
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-05-01 '+year+'-05-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_may_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_may_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#June
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-06-01 '+year+'-06-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_June_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_June_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#July
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-07-01 '+year+'-07-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_july_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_july_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#august
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-08-01 '+year+'-08-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_august_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_august_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#september
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-09-01 '+year+'-09-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_september_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_september_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#october
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-10-01 '+year+'-10-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_october_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_october_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#november
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-11-01 '+year+'-11-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_november_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_november_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#December
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-12-01 '+year+'-12-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_December_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_December_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 





#GB-WLS
location='GB-WLS'
#January
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-01-01 '+year+'-01-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Janbyday".csv')  
                        
historical_Interest_DF.to_csv(year+'_January_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#February
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-02-01 '+year+'-02-28',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Febbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_Feb_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#March
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-03-01 '+year+'-03-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_marchbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_march_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#April
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-04-01 '+year+'-04-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_april_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_april_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#May
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-05-01 '+year+'-05-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_may_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_may_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#June
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-06-01 '+year+'-06-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_June_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_June_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#July
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-07-01 '+year+'-07-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_july_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_july_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#august
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-08-01 '+year+'-08-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_august_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_august_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#september
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-09-01 '+year+'-09-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_september_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_september_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#october
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-10-01 '+year+'-10-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_october_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_october_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#november
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-11-01 '+year+'-11-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_november_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_november_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#December
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-12-01 '+year+'-12-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_December_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_December_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 



#GB-NIR
location='GB-NIR'
#January
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-01-01 '+year+'-01-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Janbyday".csv')  
                        
historical_Interest_DF.to_csv(year+'_January_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#February
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-02-01 '+year+'-02-28',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'Febbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_Feb_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#March
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-03-01 '+year+'-03-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_marchbyday.csv')  
                        
historical_Interest_DF.to_csv(year+'_march_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#April
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-04-01 '+year+'-04-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_april_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_april_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#May
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-05-01 '+year+'-05-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_may_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_may_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#June
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-06-01 '+year+'-06-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_June_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_June_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#July
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-07-01 '+year+'-07-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_july_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_july_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#august
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-08-01 '+year+'-08-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_august_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_august_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 
#september
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-09-01 '+year+'-09-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_september_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_september_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#october
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-10-01 '+year+'-10-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_october_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_october_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#november
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-11-01 '+year+'-11-30',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_november_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_november_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 

#December
pytrend.build_payload(kw_list,cat=0,timeframe=year+'-12-01 '+year+'-12-31',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+'_December_byday.csv')  
                        
historical_Interest_DF.to_csv(year+'_December_4words_'+location+'_day.zip', index=True,
          compression=compression_opts) 


# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())

# # Get Google Keyword Suggestions
# suggestions_dict = pytrend.suggestions(keyword='sad')
# print(suggestions_dict)



# related_queries_dict = pytrend.related_queries()
# print(related_queries_dict)