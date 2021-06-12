
import pandas as pd

from pytrends.request import TrendReq

pytrend = TrendReq()

pytrend.build_payload(kw_list=['depression','exercise'])


interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='sad')
print(suggestions_dict)



related_queries_dict = pytrend.related_queries()
print(related_queries_dict)