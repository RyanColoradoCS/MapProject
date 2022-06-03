import urllib
import urllib.request
import json
from us_state_abbrev import us_state_to_abbrev


def getDict():
    url = 'https://gist.githubusercontent.com/meiqimichelle/7727723/raw/0109432d22f28fd1a669a3fd113e41c4193dbb5d/USstates_avg_latLong'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    #print(data)

    temp_dict = {}

    for d in data:
        # print(us_state_to_abbrev[d['state']])
        temp_dict[us_state_to_abbrev[d['state']]] = (d['latitude'], d['longitude'])

    # print(temp_dict)

    return temp_dict

d = getDict()
for d in d:
    print(d)
# print(d.keys())
#print(d['AK'])
#print(d['AK'][0])
#print(d['AK'][1])




def getWeather(state, myTuple):
    # https://api.weather.gov/points/{latitude},{longitude}
    response = urllib.request.urlopen(f"https://api.weather.gov/points/{myTuple[0]},{myTuple[1]}")
    data = json.load(response)
    forecast_url = data['properties']['forecast']

    # print(forecast_url)
    try:
        temp_info = urllib.request.urlopen(forecast_url)
    except urllib.error.HTTPError as errh:
        # print("Http Error:", errh)
        # if it fails, change the tuple to gray
        # throwing an error caused too many problems 
        return (state, '#D0D0D0')

    # print(temp_info)

    temp_data = json.load(temp_info)

    current_temp = temp_data['properties']['periods'][0]['temperature']
    # print(current_temp)

    if current_temp <= 10:
        # Blue
        return (state, '#0000FF')
    elif current_temp <= 30:
        # Cyan
        return (state, '#00FFFF')
    elif current_temp <= 50:
        # Green
        return (state, '#00FF00')
    elif current_temp <=80:
        # Orange
        return (state, '#FFA500')
    else:
        # Red
        return (state, '#FF0000')



# s = getWeather('TX', d['TX'])
# print(s)

  


