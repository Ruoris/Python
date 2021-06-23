import pandas as pd

from pytrends.request import TrendReq

pytrend = TrendReq(retries=2, backoff_factor=0.1)
kw_list=['post partum']
location='GB'
year='2020'
filetype='.csv'
archivename='4words_'+location+'_'+year
#GB
pytrend.build_payload(kw_list,cat=0,timeframe='all',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name='post Partum monthlyGB.csv')  
                        
historical_Interest_DF.to_csv('Post Partum monthlyGB.zip', index=True,
          compression=compression_opts) 
#england
location='GB-ENG'
pytrend.build_payload(kw_list,cat=0,timeframe='all',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name='post Partum monthlyGB-Eng.csv')  
                        
historical_Interest_DF.to_csv('Post Partum monthlyGB-Eng.zip', index=True,
          compression=compression_opts) 
#Scotland
location='GB-SCT'
pytrend.build_payload(kw_list,cat=0,timeframe='all',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name='post Partum monthlyGB-SCT.csv')  
                        
historical_Interest_DF.to_csv('Post Partum monthlyGB-SCT.zip', index=True,
          compression=compression_opts) 

#NI
location='GB-NIR'
pytrend.build_payload(kw_list,cat=0,timeframe='all',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name='post Partum monthlyGB-NIR.csv')  
                        
historical_Interest_DF.to_csv('Post Partum monthlyGB-NIR.zip', index=True,
          compression=compression_opts) 
#WaLeS
location='GB-WLS'
pytrend.build_payload(kw_list,cat=0,timeframe='all',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name='post Partum monthlyGB-WLS.csv')  
                        
historical_Interest_DF.to_csv('Post Partum monthlyGB-WLS.zip', index=True,
          compression=compression_opts) 

