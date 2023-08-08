from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Python", "Java", "JavaScript", "C++", "C#", "PHP", "R", "Swift", "Kotlin", "Go"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')
df = pytrends.interest_over_time()
df = df.drop(labels=['isPartial'],axis='columns')
df = df.mean().sort_values(ascending=False)
print(df)
