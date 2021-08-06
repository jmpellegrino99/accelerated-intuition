#euclid_dist calculates the Euclidean distance between two points 
def euclid_dist(p1, p2):
    #gives the Euclidean distance if the points are tuples
    if type(p1) == type(p2) == tuple:
        sum = 0
        for i in range(len(p1)):
            sum += (p2[i] - p1[i])**2
        return sum**(1/2)
    #gives the Euclidean distance if the points are integers or floats
    else:
        return abs(p2-p1)

#defines the most common element in a list; will be useful when selecting from the final list of k nearest neighbors 
def most_common(lst):
    return max(set(lst), key=lst.count)

#here, examples of a dictionary, a point, and a parameter k are given
#set up a keys list, a values list, and a blank dictionary; then, populate the dictionary with the keys and corresponding values 
key_list = []
values_list = []
dict1 = {}
for i in range(len(key_list)):
    dict1[key_list[i]] = values_list[i]
#use an example point
point = (3,4)
#use an example k parameter 
k = 2

#define a function for the most common type among the k nearest neighbors to a point 
def knn(dict1, point, k):
    #create an empty distance list; we'll end up choosing the k smallest distances
    distance_list = []
    #calculate the distances and append them to distance_list
    for key in list(dict1.keys()):
        distance_list.append(euclid_dist(point,key))
    #we need an unsorted distance list to match up to the dictionary entries 
    unsorted_distance_list = []
    #populate that unsorted distance list; we can't just copy the list since we'll end up sorting the distance list to find the minima
    for element in distance_list:
        unsorted_distance_list.append(element)
    #sort the distance list 
    distance_list.sort()
    #create a sorted nearest neighbors list and populate it with the corresponding entries from the dictionary
    sorted_nearest_neighbors_list = []
    for i in range(k):
        sorted_nearest_neighbors_list.append(dict1.get(list(dict1)[unsorted_distance_list.index(distance_list[i])]))
    #if the final list contains all unique values, just choose the smallest one (i.e., the one in first position)
    if len(sorted_nearest_neighbors_list) == len(set(sorted_nearest_neighbors_list)):
        return sorted_nearest_neighbors_list[0]
    #if this is not so, just return the most common element
    else:
        return most_common(sorted_nearest_neighbors_list)