import pandas as pd

from pytrends.request import TrendReq

pytrend = TrendReq(retries=2, backoff_factor=0.1)
kw_list=['Depression']
location='GB'
year='2021'
filetype='.csv'
archivename='Depression'
#GB
pytrend.build_payload(kw_list,cat=0,timeframe='2011-01-01 2021-01-01',geo=location)


historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+' monthlyGB.csv')  
                        
historical_Interest_DF.to_csv(archivename+' monthlyGB.zip', index=True,
          compression=compression_opts) 
#england
location='GB-ENG'
pytrend.build_payload(kw_list,cat=0,timeframe='2011-01-01 2021-01-01',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+' monthlyGB-Eng.csv')  
                        
historical_Interest_DF.to_csv(archivename+' monthlyGB-Eng.zip', index=True,
          compression=compression_opts) 
#Scotland
location='GB-SCT'
pytrend.build_payload(kw_list,cat=0,timeframe='2011-01-01 2021-01-01',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+' monthlyGB-SCT.csv')  
                        
historical_Interest_DF.to_csv(archivename+' monthlyGB-SCT.zip', index=True,
          compression=compression_opts) 

#NI
location='GB-NIR'
pytrend.build_payload(kw_list,cat=0,timeframe='2011-01-01 2021-01-01',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+' monthlyGB-NIR.csv')  
                        
historical_Interest_DF.to_csv(archivename+' monthlyGB-NIR.zip', index=True,
          compression=compression_opts) 
#WaLeS
location='GB-WLS'
pytrend.build_payload(kw_list,cat=0,timeframe='2011-01-01 2021-01-01',geo=location)

historical_Interest_DF=pytrend.interest_over_time()
print(historical_Interest_DF)
compression_opts = dict(method='zip',
                        archive_name=archivename+' monthlyGB-WLS.csv')  
                        
historical_Interest_DF.to_csv(archivename+' monthlyGB-WLS.zip', index=True,
          compression=compression_opts) 

