"""
Author - 
Name: Rachit Agarwal
unitityId: ragarwa7

"""

import sys
import Queue
import math
import heapq

"""
    Class to store the city information and other details of USA Map 
    Param: city (name), latitude, longitude
"""
class Map:
    def __init__(self, city, latitude, longitude):
        self.city = city
        self.longitude = longitude
        self.latitude = latitude
        self.paths = None
        self.visited = False
        self.distance = None
        

    """
        This fucntion updates the all the connected path from the city 
        Param: path
    """
    def neigbhors(self, path):
        self.paths = path

    """
        This fucntion updates the heuristic distance between the city and the destination
        Param: heuristic distance
    """
    def gdistance(self, distance):
        self.distance = distance

"""
    Class to search source and destination in USA map.
"""
class SearchUSA:
    cities = {}
    roads = []
    goalFound = False
    cityDistance = {}


    """
        This fucntion reads and populate the city data from road.txt
    """
    def populateCities(self):
        file = open("roads.txt","r")
        line = file.read()
        city_data = line[line.rindex("Cities")+1:]
        city_list = city_data.split("\n\n")[1].split("\n")
        for city in city_list:
            data = city.strip().split(",")
            self.cities[data[0]] = [float(data[1]), float(data[2])]
        file.close()

    
    """
        This fucntion reads and populate the connected roads rom road.txt
    """
    def populateRoads(self):
        file = open("roads.txt","r")
        line = file.read()
        road_data = line[line.rindex("Roads")+1:]
        road_m = road_data.split("\n\n")[1].split("\n")
        for road in road_m:
            data = road.split(",")
            SearchUSA.roads.append([[data[0].strip(),data[1].strip()], float(data[2])])
            self.cityDistance[data[0].strip() + "-" + data[1].strip()] =  float(data[2])
            self.cityDistance[data[1].strip() + "-" + data[0].strip()] =  float(data[2])
        file.close()


    """
        This fucntion populate the map details of USA and apply bfs, dfs or A* for 
        Param: source, destination and searchType (bfs, dfs or astar)
    """
    def populateUSAMap(self, source, destination, searchType):
        city_list = {}
        for key, value in self.cities.iteritems():
            city_list[key] = Map(key, value[0], value[1])
    
        for key,value in city_list.iteritems():
            neigbhors = []
            for path in self.roads:
                if value.city in path[0]:
                    temp = list(path[0])
                    temp.remove(value.city)
                    neigbhors.append(city_list[temp[0]])
            neigbhors.sort(key=lambda x: x.city, reverse=False)

            """sets all the connected paths from the city"""
            value.neigbhors(neigbhors) 

            """sets the heuristic distance between a city and a destination city for A* search"""  
            value.gdistance(float(self.getHeuristicDist(value.city,city_list[destination].city)))
        
        if searchType == "bfs":
            self.breadthFirstSearch(city_list[source],city_list[destination]) 
        elif searchType == "dfs":
            self.depthFirstSearch(city_list[source],city_list[destination])
        else:
            self.astar(city_list[source],city_list[destination])  

    """
        This fucntion apply BFS and prints the nodes expanded, number of nodes expanded, 
        solution path and number of nodes in solution path.
        Param: source, destination.
    """      

    def breadthFirstSearch(self, source, destination):

        bfsNodeExpanded = []
        if source.city == destination.city:
            return destination

        """stores the information of nodeExpapnded and path travelled through the node"""
        queue = Queue.Queue()
        queue.put([source, [source]])
        bfsNodeExpanded.append(source.city)
        source.visited = True
        while not queue.empty():
            (node, path) = queue.get()
            for neighbor in node.paths: 
                if not neighbor.visited:
                    neighbor.visited = True
                    if neighbor.city == destination.city:
                        print "BFS Nodes expanded: " 
                        print bfsNodeExpanded
                        print "\n Number of BFS Node expanded: " + str(len(bfsNodeExpanded))
                        print "\n \n Solution Path BFS: "
                        solution = []
                        for sol in path:
                            solution.append(sol.city)
                        solution.append(destination.city)
                        print solution
                        print "\n Size of solution path BFS: " + str(len(solution))
                        return bfsNodeExpanded
                    bfsNodeExpanded.append(neighbor.city)
                    queue.put((neighbor, path + [neighbor]))
        return destination


    """
        This fucntion apply DFS and prints the nodes expanded, number of nodes expanded, 
        solution path and number of nodes in solution path.
        Param: source, destination.
    """  
    def depthFirstSearch(self, source, destination):
        dfsNodeExpanded = self.search(source,destination,[])
        print "DFS Nodes expanded: " 
        print dfsNodeExpanded
        print "Number of DFS nodes expanded: " + str(len(dfsNodeExpanded))
        paths = self.dfs_paths(source,destination)
        solution = []
        for path in paths:
            solution.append(path.city)
        print "Solution Path DFS: "
        print solution
        print "Size of solution path DFS: " + str(len(solution)) 
        return dfsNodeExpanded


    """
        This recusrsive function returns the number of nodes expanded for DFS
        Param: source, destination, dfsNodeExpanded.
    """  
    def search(self, source, destination, dfsNodeExpanded):
        if source.city == destination.city:
            self.goalFound = True 
        if not self.goalFound:
            if source.city not in dfsNodeExpanded:
                dfsNodeExpanded.append(source.city)
                for node in source.paths:
                    self.search(node,destination, dfsNodeExpanded)
        return dfsNodeExpanded


    """
        This recusrsive function returns the solution path for DFS
        Param: source, destination, dfsNodeExpanded.
    """
    def dfs_paths(self, source, destination):

         """stores the list of city expanded and path travelled through that node"""
         nodePaths = [(source, [source])]
         visited = set()
         while nodePaths:
            (node, path) = nodePaths.pop()
            if node not in visited:
                if node.city == destination.city:
                    return path
                visited.add(node)
                for neighbor in node.paths:
                    nodePaths.append((neighbor, path + [neighbor]))

    """
        This fucntion apply A* and prints the nodes expanded, number of nodes expanded, 
        solution path and number of nodes in solution path.
        Param: source, destination.
    """  
    def astar(self, source, destination):

        bfsNodeExpanded = []
        if source.city == destination.city:
            return destination

        cost = {source:0} 

        """
        stores the list of city expanded and the priority of the city for expansion on the 
        basis of the cost of expansion (least cost expanded first.
        """   
        heap = []
        heapq.heappush(heap, (0, [source, [source]]))
        source.visited = True
        while heap:
            node, path = heapq.heappop(heap)[1]
            bfsNodeExpanded.append(node.city)
            for neighbor in node.paths: 
                g_cost = cost[node] + self.cityDistance[node.city + "-" + neighbor.city]
                if neighbor not in cost or g_cost < cost[neighbor]:
                    neighbor.visited = True
                    cost[neighbor] = g_cost
                    f_cost = g_cost + neighbor.distance
                    if neighbor.city == destination.city:
                        print "A* Nodes expanded: " 
                        print bfsNodeExpanded
                        print "\n Number of Node expanded for A*: " + str(len(bfsNodeExpanded))
                        print "\n \n Solution Path A*: "
                        solution = []
                        for sol in path:
                            solution.append(sol.city)
                        solution.append(destination.city)
                        print solution
                        print "\n Size of solution path A*: " + str(len(solution))
                        print "\n Cost of solution path A*: "
                        print g_cost
                        return bfsNodeExpanded
                    heapq.heappush(heap, (f_cost, (neighbor, path + [neighbor])))
        return destination

    """
        This function returns heuristic distance bwtween two cities
        Param: source, destination.
    """  
    def getHeuristicDist(self, source, destination):
        
        Lat1 = self.cities[source][0]
        Lat2 = self.cities[destination][0]

        Long1 = self.cities[source][1]
        Long2 = self.cities[destination][1]

        hdistance = math.sqrt((69.5 * (Lat1 - Lat2)) ** 2 + (69.5 * math.cos((Lat1 + Lat2)/360 * math.pi) * (Long1 - Long2)) ** 2)
        return hdistance;



"""
    Main method : SearchUSA.py
    Arguments: searchType, source, destination.
"""  
if __name__ == "__main__":
        param = sys.argv
        searchType = param[1]
        source = param[2]
        destination = param[3]

        source = source[0].lower() + source[1:]
        destination = destination[0].lower() + destination[1:]
            
        usa = SearchUSA()
        usa.populateCities()
        usa.populateRoads()
        usa.populateUSAMap(source, destination, searchType)
    

