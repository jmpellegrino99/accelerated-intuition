#NEW SECTION
#Search Volume Proxies (SVP):
#Import packages:
from youtubesearchpython import *
import pandas as pd
#Begin entering queries and specifying parameters
queries = ['honda accord', 'honda civic', 'honda del sol', 'carmax', 'kia telluride', 'kia telluride review']
limit_actual = 10
svp_df = pd.DataFrame(columns = ['Query', 'Views', 'Duration', 'Subscribers'])
#Define function for average number of subscribers:
def remove(subscriber_count_text):
    subscriber_count_text = subscriber_count_text.replace(' subscribers', '')
    if 'K' in list(subscriber_count_text):
        return float(subscriber_count_text.replace('K',''))*1000
    elif 'M' in list(subscriber_count_text):
        return float(subscriber_count_text.replace('M', ''))*1000000
    else:
        return float(subscriber_count_text)
def avg_subscribers(video):
    video = VideosSearch(video,limit = limit_actual).result(mode=ResultMode.dict).get('result')
    empty_list_test = []
    try:      
        for i in range(len(video)):
            empty_list_test.append(video[i].get('channel').get('name'))
        total_subscribers = 0
        for element in empty_list_test:
            total_subscribers += float(remove(ChannelsSearch(element,limit=1,region='US').result().get('result')[0].get('subscribers')))
        return int(total_subscribers/limit_actual) 
    except: 
        return "NaN"
average_views = []
average_duration = []
average_subscribers = []
for query in queries: 
    return_list_1 = []
    return_list_2 = []
    x = VideosSearch(query, limit=limit_actual).result(mode = ResultMode.dict).get('result')
    try:
        for index in range(limit_actual):
            if x[index].get('viewCount').get('text').replace(' views', '').replace(' view', '').replace(',','') == 'No':
                return_list_1.append(float(0))
                return_list_2.append(float(0))
            else:
                return_list_1.append(float(x[index].get('viewCount').get('text').replace(' views', '').replace(' view', '').replace(',','')))
                return_list_2.append(float(x[index].get('duration').split(":")[0]) + float(x[index].get('duration').split(":")[1])/60)
        z1 = 0
        z2 = 0
        for element1 in return_list_1:
            z1 += element1
        for element2 in return_list_2:
            z2 += element2
        w1 = z1/limit_actual
        w2 = z2/limit_actual
        average_views.append(w1)
        average_duration.append(w2)
        average_subscribers.append(avg_subscribers(query))
    except:
        average_views.append('NaN')
        average_duration.append('NaN')
        average_subscribers.append(avg_subscribers(query))
query_tally = []
view_tally = []
duration_tally = []
for i in range(len(queries)):
    query_tally.append(queries[i])
for i in range(len(queries)):
    view_tally.append(int(average_views[i]))
for i in range(len(queries)):
    duration_tally.append(round(average_duration[i],1))
svp_df.Query = query_tally
svp_df.Views = view_tally
svp_df.Duration = duration_tally
svp_df.Subscribers = average_subscribers
#return the data frame
svp_df






#NEW SECTION
#Ranking:
from youtubesearchpython import *
import pandas as pd
channel_name = 'CarMax'
rankings_df = pd.DataFrame(columns=['Query','Rank','Video'])
queries = ['best suv for towing', 'used cars', 'used ford mustang', 'dodge durango suv', 
'telluride 2020', 'telluride', 'carmax kia telluride', 'kia telluride interior',
'carmax rav4', 'carmax nissan rogue', 'dodge challenger vs charger', 'charger vs challenger', 'challenger vs charger',
'civic vs accord', 'accord vs civic', 'honda civic vs honda accord']
counter = 0
queries_list = []
rank_order = []
video_titles_list = []
for query in queries:
    x = VideosSearch(query, limit=10).result().get('result')
    empty = 0
    for i in range(10):
        if x[i].get('channel').get('name') == channel_name and empty == 0:
            counter += 1
            empty += 1
            queries_list.append(query)
            rank_order.append('#{}'.format(i+1))
            video_titles_list.append(x[i].get('title'))
rankings_df.Query = queries_list
rankings_df.Rank = rank_order
rankings_df.Video = video_titles_list
rankings_df
