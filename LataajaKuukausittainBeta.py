import pandas as pd

from pytrends.request import TrendReq

pytrend = TrendReq(retries=2, backoff_factor=0.1)
kw_list=['post partum']
location='GB'
year='2020'
filetype='.csv'
archivename='Post partum'
#GB
pytrend.build_payload(kw_list,cat=0,timeframe='2019-02-01 2019-02-28',geo=location)

historical_Interest_DF=pytrend.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=True)
print(historical_Interest_DF)
# historical_Interest_DF=pytrend.interest_over_time()
# print(historical_Interest_DF)
# compression_opts = dict(method='zip',
#                         archive_name=archivename+' monthlyGB.csv')  
                        
# historical_Interest_DF.to_csv(archivename+' monthlyGB.zip', index=True,
#           compression=compression_opts) 
