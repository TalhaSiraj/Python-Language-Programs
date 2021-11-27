from collections import defaultdict
from queue import PriorityQueue
import math

class BreadthFirstSearch:

    def __init__(self):
        self.graph=defaultdict(lambda:defaultdict(list))

    def Add_value(self,key1,key2,value):
       self.graph[key1][key2].append(value)
    
    def BFS(self,target_Node):
        self.Visited=[]
        self.Queue=[]
        self.last_parent=0
        self.keyS=[self.graph.keys()]
        self.lenght=len(self.keyS)
        self.pathcost=[]
        i=0
        self.Gate=1
        self.Gate1=0
        while(self.Gate == 1):
            for k in self.keyS.pop(i):
                self.Queue.append(k)
                if(self.Queue.__contains__(target_Node)):
                    if(self.Visited.__contains__(k)):
                        self.Gate =0
                        print("Goal Node: ",target_Node," Has Been Found.")
                        self.place=self.Visited.index(target_Node)
                        self.diff=len(self.Visited)-self.place
                        self.place +=1
                        self.place1 =self.place+(self.diff-1)
                        del self.Visited[int(self.place):int(self.place1)]
                        print("Cost Of Goal Node: ",sum(self.pathcost))
                        print("Total Number Of Visited Nodes :",len(self.Visited))
                        print("Future Expandable Nodes : ",len(self.Queue))
                        print("Visited Nodes: ",self.Visited)
                        print("Queue Nodes: ",self.Queue)
                        print("Node Place At : ",(self.place-1))
                        self.pathcost=self.cal_path_cost((self.place-2))
                        self.Gate1=1
                        break
                    else:
                        self.Gate =0
                        self.Visited.append(k)
                        print("Goal Node: ",target_Node," Has Been Found.")
                        self.place=self.Visited.index(target_Node)
                        self.diff=len(self.Visited)-self.place
                        self.place +=1
                        self.place1 =self.place+(self.diff-1)
                        del self.Visited[int(self.place):int(self.place1)]
                        print("Cost Of Goal Node: ",sum(self.pathcost))
                        print("Total Number Of Visited Nodes :",len(self.Visited))
                        print("Future Expandable Nodes : ",len(self.Queue))
                        print("Visited Nodes: ",self.Visited)
                        print("Queue Nodes: ",self.Queue)
                        print("Node Place At : ",(self.place-1))
                        self.pathcost=self.cal_path_cost((self.place-2))
                        self.Gate=0
                        self.Gate1=1
                        break
                else:
                    if(self.Visited.__contains__(k)):
                        pass
                    else:
                        self.Visited.append(k)   
                    self.Queue.pop(0)
                self.last_parent=k
                for val in self.graph[k]:        
                    self.Queue.append(val)
                    self.Visited.append(val)
                    self.s=self.graph[k][val]
                    self.pathcost.append(self.s[0])
                if(i<self.lenght):
                    i +=1
                if(i<self.lenght):
                    break
            if(self.Gate1 == 1 ):
                break
            else:
                if(self.Queue.__contains__(target_Node)):
                    self.Gate =0
                    print("Goal Node: ",target_Node," Has Been Found.")
                    self.place=self.Visited.index(target_Node)
                    self.diff=len(self.Visited)-self.place
                    self.place +=1
                    self.place1 =self.place+(self.diff-1)
                    del self.Visited[int(self.place):int(self.place1)]
                    print("Cost Of Goal Node: ",sum(self.pathcost))
                    print("Total Number Of Visited Nodes :",len(self.Visited))
                    print("Future Expandable Nodes : ",len(self.Queue))
                    print("Visited Nodes: ",self.Visited)
                    print("Queue Nodes: ",self.Queue)
                    print("Node Place At : ",(self.place-1))
                    self.pathcost=self.cal_path_cost((self.place-2))
                else:
                    print("Invalid Node.")
                    break
    def cal_path_cost(self ,V):
        
        last_index=len(self.pathcost)-1
        if(V == last_index):
            A=sum(self.pathcost)
        else:
            if(V<last_index):
                V=V+1    
                del self.pathcost[int(V):int(last_index)]
                A=sum(self.pathcost)
            else:
                A=sum(self.pathcost)
        return A
print("****************************************************")        
print("Result Of BreadthFirstSearch: ")
gbfs=BreadthFirstSearch()
gbfs.Add_value(1,2,803)
gbfs.Add_value(1,3,803)
gbfs.Add_value(2,4,158)
gbfs.Add_value(2,5,178)
gbfs.Add_value(3,6,774)
gbfs.Add_value(3,7,724)
gbfs.Add_value(4,10,1531)
gbfs.Add_value(5,10,1231)
gbfs.Add_value(5,6,1673)
gbfs.Add_value(6,8,1173)
gbfs.Add_value(6,9,1400)
gbfs.Add_value(7,9,1400)
gbfs.Add_value(7,13,842)
gbfs.Add_value(13,14,712)
gbfs.Add_value(13,19,591)
gbfs.Add_value(10,11,875)
gbfs.Add_value(10,12,1371)
gbfs.Add_value(8,12,1171)
gbfs.Add_value(8,16,1659)
gbfs.Add_value(9,14,1012)
gbfs.Add_value(11,15,1012)
gbfs.Add_value(16,17,912)
gbfs.Add_value(16,18,1226)
gbfs.Add_value(19,20,1026)
gbfs.Add_value(19,21,1012)
gbfs.Add_value(14,17,912)
gbfs.Add_value(14,18,1326)
gbfs.Add_value(15,22,1046)
gbfs.Add_value(15,23,1012)
gbfs.Add_value(21,24,912)
gbfs.Add_value(21,25,952)

gbfs.BFS(16)
 

class UniformCostSearch:
  
    def __init__(self):
        self.graph1=defaultdict(lambda:defaultdict(list))
    
    def find_neighbours(self,node):
        return self.graph1[node]
    
    def get_cost(self,node1,node2):
        return self.graph1[node1][node2]
    
    def Add_value(self,key1,key2,value):
       self.graph1[key1][key2].append(value)

    def ucs(self,start,goal):
        visited=set()
        self.total_cost=0
        cost=0
        queue=PriorityQueue()
        queue1=PriorityQueue()
        queue.put((0,start))
        queue1.put((0,start))
        while queue:
            cost,node=queue.get()
            if node not in visited:
                visited.add(node)
                if node == goal:
                    print("Goal Node: ",node," Has Been Found.")
                    print("Cost Of Goal Node: ",cost)
                    print("Total Number Of Visited Nodes :",len(visited))
                    print("Visited Nodes: ",visited)
                    break
                for i in self.find_neighbours(node):
                    if i not in visited:
                        self.list_cost=self.get_cost(node,i)
                        self.total_cost=cost+self.list_cost.pop(0)
                        queue.put((self.total_cost,i))

print("****************************************************")
print("Result Of Uniformcost: ")
gucs=UniformCostSearch()
gucs.Add_value(1,2,803)
gucs.Add_value(1,3,803)
gucs.Add_value(2,4,158)
gucs.Add_value(2,5,178)
gucs.Add_value(3,6,774)
gucs.Add_value(3,7,724)
gucs.Add_value(4,10,1531)
gucs.Add_value(5,10,1231)
gucs.Add_value(5,6,1673)
gucs.Add_value(6,8,1173)
gucs.Add_value(6,9,1400)
gucs.Add_value(7,9,1400)
gucs.Add_value(7,13,842)
gucs.Add_value(13,14,712)
gucs.Add_value(13,19,591)
gucs.Add_value(10,11,875)
gucs.Add_value(10,12,1371)
gucs.Add_value(8,12,1171)
gucs.Add_value(8,16,1659)
gucs.Add_value(9,14,1012)
gucs.Add_value(11,15,1012)
gucs.Add_value(16,17,912)
gucs.Add_value(16,18,1226)
gucs.Add_value(19,20,1026)
gucs.Add_value(19,21,1012)
gucs.Add_value(14,17,912)
gucs.Add_value(14,18,1326)
gucs.Add_value(15,22,1046)
gucs.Add_value(15,23,1012)
gucs.Add_value(21,24,912)
gucs.Add_value(21,25,952)

gucs.ucs(1,16)


class GreedyAlgorithm:
 
    def __init__(self):
       self.graph_cord=defaultdict(lambda:defaultdict(list))
       self.graph_path=defaultdict(lambda:defaultdict(list))

    def Add_value_cord(self,node,x_cord,y_cord):
       self.graph_cord[node][x_cord].append(y_cord)
    def Add_value(self,node1,node2,path_cost):
       self.graph_path[node1][node2].append(path_cost)
       
    def find_Heuristics(self,current_node,goal_node):
        x1=self.get_x_cord(current_node)
        x2=self.get_x_cord(goal_node)
        y1=self.get_y_cord(current_node,x1)
        y2=self.get_y_cord(goal_node,x2)
        distance=(((x2-x1)**2)+((y2-y1)**2))**0.5
        return distance
    
    def find_neighbours(self,node):
        return self.graph1[node]
    
    def get_x_cord(self,node1):
        x=self.graph_cord[node1]
        self.forword=0
        for i in x:
            self.forword=i
            break
        return self.forword

    def get_y_cord(self,node,x_cor):
        y=self.graph_cord[node][x_cor]
        for i in y:
            self.forw=i
            break
        return self.forw
    def get_cost(self,node1,node2):
        return self.graph_path[node1][node2]
        
    def greedy_search(self,start,goal):
        self.temp_lst=[]
        self.temp_dis={}
        self.pathcost=[]
        self.list=[]
        self.list.append(start)
        self.curr_node_pre=0

        while(len(self.list)>0):
            self.current_node=self.list.pop()
            self.shortest_path=self.find_Heuristics(self.current_node,goal)
            if(self.current_node == goal):
                print("Goal Node: ",self.current_node," Has Been Found.")
                print("Cost Of Goal Node: ",sum(self.pathcost))
                print("Total Number Of Visited Nodes :",len(gga.pathcost))
                break
            for child in self.graph_path[self.current_node]:
                self.curr_node_pre=self.current_node
                self.shortest_path=self.find_Heuristics(child,goal)
                self.shortest_path=int(math.floor(self.shortest_path))
                self.temp_dis.update({self.shortest_path:child})
                self.temp_lst.append(self.shortest_path)
            if(len(self.temp_lst) == 0):
                print("Last nearest node is : ",self.current_node)
                print("Goal Node Has Not Been Found.")
            else:
                val1=self.temp_lst.pop()
                val2=self.temp_lst.pop()
                if(val1>val2):
                    self.curr_node=self.temp_dis[val2]
                    self.list.append(self.curr_node)
                    self.temp_dis.clear()
                    self.t1=[]
                    self.t1=self.get_cost(self.current_node,self.curr_node)
                    self.t2=self.t1.pop()
                    self.pathcost.append(self.t2) 
                elif(val1<val2):
                    self.curr_node=self.temp_dis[val1]
                    self.list.append(self.curr_node)
                    self.temp_dis.clear()
                    self.t1=[]
                    self.t1=self.get_cost(self.current_node,self.curr_node)
                    self.t2=self.t1.pop()
                    self.pathcost.append(self.t2)                    
                else:
                    self.curr_node=self.temp_dis[val2]
                    self.list.append(self.curr_node)
                    self.temp_dis.clear()
                    self.t1=[]
                    self.t1=self.get_cost(self.current_node,self.curr_node)
                    self.t2=self.t1.pop()
                    self.pathcost.append(self.t2)        

print("****************************************************")
print("Result Of GreedyAlgorithm: ")
gga=GreedyAlgorithm()
gga.Add_value(1,2,803)
gga.Add_value(1,3,803)
gga.Add_value(2,4,158)
gga.Add_value(2,5,178)
gga.Add_value(3,6,774)
gga.Add_value(3,7,724)
gga.Add_value(4,10,1531)
gga.Add_value(5,10,1231)
gga.Add_value(5,6,1673)
gga.Add_value(6,8,1173)
gga.Add_value(6,9,1400)
gga.Add_value(7,9,1400)
gga.Add_value(7,13,842)
gga.Add_value(13,14,712)
gga.Add_value(13,19,591)
gga.Add_value(10,11,875)
gga.Add_value(10,12,1371)
gga.Add_value(8,12,1171)
gga.Add_value(8,16,1659)
gga.Add_value(9,14,1012)
gga.Add_value(11,15,1012)
gga.Add_value(16,17,912)
gga.Add_value(16,18,1226)
gga.Add_value(19,20,1026)
gga.Add_value(19,21,1012)
gga.Add_value(14,17,912)
gga.Add_value(14,18,1326)
gga.Add_value(15,22,1046)
gga.Add_value(15,23,1012)
gga.Add_value(21,24,912)
gga.Add_value(21,25,952)

gga.Add_value_cord(1,-73530767,41085396)
gga.Add_value_cord(2,-73530538,41086098)
gga.Add_value_cord(3,-73519366,41048796)
gga.Add_value_cord(4,-73519377,41048654)
gga.Add_value_cord(5,-73524567,41093796)
gga.Add_value_cord(6,-73525490,41093834)
gga.Add_value_cord(7,-73531927,41110484)
gga.Add_value_cord(8,-73530106,41110611)
gga.Add_value_cord(9,-73529341,41125895)
gga.Add_value_cord(10,-73529746,41127369)
gga.Add_value_cord(11,-73530583,41125051)
gga.Add_value_cord(12,-73529763,41085358)
gga.Add_value_cord(13,-73529834,41086062)
gga.Add_value_cord(14,-73613384,41065086)
gga.Add_value_cord(15,-73615019,41065131)
gga.Add_value_cord(16,-73693133,41058075)
gga.Add_value_cord(17,-73694273,41059296)
gga.Add_value_cord(18,-73512230,41287431)
gga.Add_value_cord(19,-73511896,41286556)
gga.Add_value_cord(20,-73501634,41286067)
gga.Add_value_cord(21,-73501424,41284975)
gga.Add_value_cord(22,-73500122,41286141)
gga.Add_value_cord(23,-73554632,41132182)
gga.Add_value_cord(24,-73554531,41129747)
gga.Add_value_cord(25,-73663848,41025429)

gga.greedy_search(1,16)

print("****************************************************")
if sum(gga.pathcost) < gucs.total_cost and sum(gga.pathcost) < gbfs.pathcost:
    print("Greedy Alogrithm Is The Most Optimal")
if gucs.total_cost < sum(gga.pathcost) and gucs.total_cost < gbfs.pathcost:
    print("UniformCostSearch Is The Most Optimal")
if gbfs.pathcost < gucs.total_cost and gbfs.pathcost < sum(gga.pathcost):
    print("BreadthFirstSearch Is The Most Optimal") 
 