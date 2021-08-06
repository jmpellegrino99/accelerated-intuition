#NEW SECTION
#Search Volume Proxies (SVP):
from youtubesearchpython import *
import pandas as pd
queries = []
limit_actual = 10
average_views = []
average_duration = []
try:
    for query in queries: 
        return_list_1 = []
        return_list_2 = []
        search = VideosSearch(query, limit=limit_actual)
        result = search.result(mode = ResultMode.dict)
        x = result.get('result')
        for number in range(limit_actual):
            if x[number].get('viewCount').get('text').replace(' views', '').replace(' view', '').replace(',','') == 'No':
                return_list_1.append(float(0))
                return_list_2.append(float(0))
            else:
                return_list_1.append(float(x[number].get('viewCount').get('text').replace(' views', '').replace(' view', '').replace(',','')))
                return_list_2.append(float(x[number].get('duration').split(":")[0]) + float(x[number].get('duration').split(":")[1])/60)
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
    query_tally = []
    view_tally = []
    duration_tally = []
    for i in range(len(queries)):
        query_tally.append(queries[i])
    for i in range(len(queries)):
        view_tally.append(round(average_views[i],0))
    for i in range(len(queries)):
        duration_tally.append(round(average_duration[i],1))
    rsvp = pd.DataFrame(columns = ['Query', 'Views', 'Duration'])
    rsvp.Query = query_tally
    rsvp.Views = view_tally
    rsvp.Duration = duration_tally
#if an error is thrown, the name of the "problem" query will be printed
except:
    print(queries[len(average_views)])
#return the data frame
rsvp



#NEW SECTION
#Ranking:
queries = ['best suv for towing', 'used cars', 'used ford mustang', 'dodge durango suv', 
'telluride 2020', 'telluride', 'carmax kia telluride', 'kia telluride interior',
'carmax rav4', 'carmax nissan rogue', 'dodge challenger vs charger', 'charger vs challenger', 'challenger vs charger',
'civic vs accord', 'accord vs civic', 'honda civic vs honda accord']
counter = 0
queries_list = []
rank_order = []
titles_list = []
for query in queries:
    x = VideosSearch(query, limit=10).result().get('result')
    empty = 0
    for i in range(10):
        if x[i].get('channel').get('name') == 'CarMax' and empty == 0:
            counter += 1
            empty += 1
            queries_list.append(query)
            rank_order.append('#{}'.format(i+1))
            titles_list.append(x[i].get('title'))
import pandas as pd
table = pd.DataFrame(columns=['Query','Rank','Video'])
table.Query = queries_list
table.Rank = rank_order
table.Video = titles_list
table

#MEDIAN FUNCTION:
def median(list1):
    list1 = list(set(list1))
    if len(list1) % 2 == 0:
        return list1[len(list1)//2-1]/2 + list1[len(list1)//2]/2
    if len(list1) % 2 != 0:
        return list1[(len(list1)-1)//2]		

#HOW TO GET SUGGESTED TERMS:
def related(queries):
    output_list = []
    for element1 in queries:
        suggestion = suggestions.get(element1)
        suggestion = suggestion.get('result')
        for element2 in suggestion:
            output_list.append(element2)
    return output_list


#NEW SECTION
#MISCELLANEOUS (ideas in progress/scratch work)

#SETTING UP A DATA FRAME:
rsvp = pd.DataFrame(columns = ['Query', 'Views', 'Duration'])
rsvp.Query = query_tally
rsvp.Views = view_tally
rsvp.Duration = duration_tally
rsvp

#HOW TO GET CHANNEL SUBSCRIBER COUNT:
def remove(test_list):
    result = 0
    test_list = test_list.replace(' subscribers', '')
    if 'K' in list(test_list):
        result += float(test_list.replace('K',''))*1000
    if 'M' in list(test_list):
        result += float(test_list.replace('M', ''))*1000000
    else:
        result += float(test_list)
    return result

#GETTING CHANNEL NAMES:
video = VideosSearch('used cars',limit=2).result(mode=ResultMode.dict).get('result')
empty_list_test = []
for i in range(len(video)):
    empty_list_test.append(video[i].get('channel').get('name'))
for element in empty_list_test:
    print(ChannelsSearch(element,limit=1,region='US').result().get('result')[0].get('subscribers'))

#GETTING SUBSCRIBER COUNTS FOR CHANNELS CORREPSONDING TO TOP 10 VIDEOS:
queries_list = ['Honda Civic', 'Honda Fit', 'Honda Accord']
average_subscribers = []
for item in queries_list:
    channel_names = []
    subscribers = []
    for i in range(10):
        channel_names.append(VideosSearch(item,limit=10).result(mode=ResultMode.dict).get('result').get('channel').get('name'))
    for i in range(10):
        subscribers.append(remove(ChannelsSearch(channel_names[i],limit=1,region='US').result().get('result')[0].get('subscribers'))
    sum = 0
    for number in subscribers:
        sum += number 
    average_subscribers.append(sum//10)
    
#IN PROGRESS FOR COMPUTING SUBSCRIBER COUNTS:
def remove(test_list):
    result = 0
    test_list = test_list.replace(' subscribers', '')
    if 'K' in list(test_list):
        result += float(test_list.replace('K',''))*1000
    elif 'M' in list(test_list):
        result += float(test_list.replace('M', ''))*1000000
    else:
        result += float(test_list)
    return result
limit_actual = 5
video_ = str(input("Video: "))
video = VideosSearch(video_,limit = limit_actual).result(mode=ResultMode.dict).get('result')
empty_list_test = []
for i in range(len(video)):
    empty_list_test.append(video[i].get('channel').get('name'))
average = 0
for element in empty_list_test:
    average += float(remove(ChannelsSearch(element,limit=1,region='US').result().get('result')[0].get('subscribers')))
average = average/limit_actual
average
