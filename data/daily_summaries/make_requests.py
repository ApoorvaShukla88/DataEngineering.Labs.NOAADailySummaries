import requests
import json

file_counter = 0
offset_counter = 1

url = ' https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:' \
      '10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=1001'

r = requests.get(url, headers={
    'token': 'kiMomNqDkIjROzHmmalPEEzfuKLCmEeI',
    'Content-Type': 'application/json'
})
jsonResult = r.json()

jsonR = jsonResult['results']
jsonPath = '/Users/amishra/DEV/DataEngineering.Labs.NOAADailySummaries/data/daily_summaries/'
with open('daily_summaries_FIPS10003_jan_2018_1' + '.json', "w") as outfile:
    json.dump(jsonResult, outfile)
file_counter = file_counter + 1
offset_counter = offset_counter + 1000
