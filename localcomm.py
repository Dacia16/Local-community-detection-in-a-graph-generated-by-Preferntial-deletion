#install networkx
#install matplotlib
#install random
#install community
#Packages
import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import community
G = nx.Graph()
g=nx.Graph()


edgelist = [];
class Node(object):
    def __init__(self, name):
        self.name = name;
        self.adjacentnode = [];
        self.numOfEdges = 0;


def start():
    global i;
    global totdeg;
    i = 1;
    nodeList.append(Node(i));
    edgelist.append([Node(i), Node(i)])
    i = i + 1;
    nodeList[0].adjacentnode.append(nodeList[0]);
    nodeList[0].numOfEdges = 1;
    totdeg = 1;
    Blist.append(1);
    Dlist.append(1);


def Birthnode(NodeSelect):
    global i;
    global totdeg;
    node1 = Node(i);
    nodeList.append(node1);
    node1.adjacentnode.append(NodeSelect);
    edgelist.append([NodeSelected,node1]);

    node1.numOfEdges = 1;
    NodeSelect.adjacentnode.append(node1);
    NodeSelect.numOfEdges = (NodeSelect.numOfEdges) + 1;
#    for k in range(len(nodeList)):
#        print("nodelist values:", nodeList[k].name)
#        print("nodelist value edge", nodeList[k].numOfEdges)
#    for o in edgelist:
#        print("Edge list values:", o[0].name, o[-1].name)
    i = i + 1;
    totdeg = totdeg + 2;
    numOfNodes = len(nodeList);
    for k in range(len(nodeList)):
        Blist.append((nodeList[k].numOfEdges) / (totdeg));
        Dlist.append((numOfNodes - (nodeList[k].numOfEdges)) / ((numOfNodes ** 2) - (totdeg)));


def Deathnode(NodeSelected):
    global totdeg;
    pos = nodeList.index(NodeSelected);
    nodeList.remove(NodeSelected);
    totdeg = totdeg - len(NodeSelected.adjacentnode);
    length = len(nodeList);
    if pos > 0:
        for j in range(length):
            if NodeSelected in nodeList[j].adjacentnode:
                nodeList[j].adjacentnode.remove(NodeSelected);
#                print(" nodeselected ,nodelist j adjacent node ")
                for o in edgelist:
                    if o[0] ==  NodeSelected and o[-1] == nodeList[j] :
#                        print(" remove nodeselected, nodeList[j]",o[0].name, o[-1].name)
                        edgelist.remove(o)

                        edgelist.remove(o);
                    elif o[0] == nodeList[j] and o[-1] == NodeSelected:
#                        print("remove nodelis[j], nodeselected", o[0].name, o[-1].name)
                        edgelist.remove(o)



                nodeList[j].numOfEdges = (nodeList[j].numOfEdges) - 1;
                totdeg = totdeg - 1;
        numOfNodes = len(nodeList);
#        for k in range(len(nodeList)):
#            print("nodelist values:", nodeList[k].name);
#            print("nodelist value edge", nodeList[k].numOfEdges);
#        for l in edgelist:
#            print("Edge list values:", l[0].name, l[-1].name);
        if numOfNodes == 1:
            Dlist.append(1);
            Blist.append(1);
        else:
            for k in range(len(nodeList)):
                Blist.append((nodeList[k].numOfEdges) / (totdeg));
                Dlist.append((numOfNodes - (nodeList[k].numOfEdges)) / ((numOfNodes ** 2) - (totdeg)));


def CumulativeProb():
    Cum_BProb = 0;
    for k in range(len(nodeList)):
        Cum_BProb = Cum_BProb + Blist[k];
        CumulativeBlist.append(Cum_BProb);
    y = random.randint(0, 10);
    y = y / 10;
    for k in range(len(CumulativeBlist)):
        if CumulativeBlist[k] >= y:
            node = nodeList[k];
            return node;
        if k == (len(CumulativeBlist) - 1):
            return nodeList[k];


nodeList = [];
Blist = [];
Dlist = [];

start();

for j in range(100):
    x = random.randint(0, 10);
    x = x / 10;
    if x <= 0.6:
#        print("birth")
        CumulativeBlist = [];
        NodeSelected = CumulativeProb();
        Blist = [];
        Dlist = [];
        Birthnode(NodeSelected);
    else:
 #       print("death")
        maxpos = Dlist.index(max(Dlist));
        NodeSelected = nodeList[maxpos];
        Blist = [];
        Dlist = [];
        Deathnode(NodeSelected);
        length = len(nodeList);
        if length == 0:
            start();


for f in nodeList:
    G.add_node(f.name)

for y in edgelist:
    G.add_edge(y[0].name,y[-1].name)
plt.title('Random graph using preferential deletion');
nx.draw(G, with_labels=True)
plt.show()
print("no of node", nx.number_of_nodes(G))




def filterneighbour(nodeList,comm,n1,n2):
    q = [];
    a = [];
    print("number of values in n1", len(n1));
    for v in n1:
        c0v = calc0v(v, comm);
        c1v = calc1v(v, n1);
        c2v = calc2v(v, n2);
        co = 0;
        if c0v - c2v >= 0 or c1v - c2v >= 0:
            if not q:
                q.append(v);

#                print("values in q", v.name)
            else:
                for h in q:
                    if h == v:
                        co = co + 1;
                if co == 0:
                    q.append(v);
#                    print("values in q", v.name)
        else:
            if not a:
                a.append(v);
#                print("values in a", v.name)
            else:
                for h in a:
                    if h == v:
                        co = co + 1;
                if co == 0:
                    a.append(v);
#                    print("values in a", v.name);
    return q,a;


def calc0v(v,comm):
    count=0
    for r in v.adjacentnode:
        if r in comm:
            count = count + 1;
#    print("count of no of c0v",count)
    return count;

def calc1v(v,n1):
    count=0
    for r in v.adjacentnode:
        if r in n1 and r != v:

            count = count + 1;
#    print("count of no of c1v", count)
    return count;

def calc2v(v,n2):
    count=0
    for r in v.adjacentnode:
        if r in n2:
            count = count + 1;
#    print("count of no of c2v", count)
    return count;



#FIND-COMMUNITY
q = [];
a = [];
comm = [];
n1 = [];
n2 = [];
if len(nodeList)<1:
    print("Length of nodelist les than 1");
comm.append(nodeList[1]);
comm.append(nodeList[1].adjacentnode[0])
print("Value of seed node 1",nodeList[1].name)
#print("Length of nodes in adje",len(nodeList[1].adjacentnode))
print("value of seed 2",comm[1].name)
#print("length of nodes n adj of comm 2",len(comm[1].adjacentnode))
for c in comm:
    for x in c.adjacentnode:
        if x in comm:
            print("n1 and comm values hit same",x.name)
        else:
            n1.append(x);
#            print("Value appended to n1", x.name)
temp = [];
for k in n1:
    for t in k.adjacentnode:
        if t in n1 or t in comm:
            print("n1 and n2 and comm value hit",t.name)

        else:
            temp.append(t);
#            print("value in temp", t.name)
for t in temp:
    if t not in comm:
        n2.append(t);
#        print("value in n2",t.name)

nodes_notincluded=[];
while len(n1)>0 or len(n2)>1:
    # FILTER-NEIGHBORHOOD
    q, a = filterneighbour(nodeList, comm, n1, n2);
    for s in a:
        nodes_notincluded.append(s);
    comm = list(set(comm) | set(q))
#    print("number of elements in new c", len(comm))
#    for k in comm:
#        print("comm values", k.name);

    # new n1:{first neighour} of q intersection n2
    neighour_q = [];
    for j in q:
        for k in j.adjacentnode:
            neighour_q.append(k);
    n1 = list(set(neighour_q) & set(n2));
#    print("number of elements in new n1", len(n1));
#    for w in n1:
#        print("new n1", w.name);

    # new n2 = first neighbourhood of n1 -C
    neighour_n1 = [];
    for j in n1:
        for k in j.adjacentnode:
            neighour_n1.append(k);
    n2 = list(set(neighour_n1).difference(comm));
#    print("number of elements in new n2", len(n2));
#    for b in n2:
#        print("new n2", b.name);

for c in comm:
    g.add_node(c.name)
    for o in c.adjacentnode:
        if o in set(nodes_notincluded):
            print("node not included",o.name);
        else:
            g.add_edge(c.name, o.name)



plt.title('community detected')
nx.draw(g, with_labels=True)
plt.show()
print("no of node", nx.number_of_nodes(g))


#for y in comm:
#    print("final comm value",y.name);


print("Communities detected by modularity model");


communities_mod = community.greedy_modularity_communities(G)
modularity_list = {}
for e in enumerate(communities_mod):
    for name in e:
        modularity_list[name] = e

nx.set_node_attributes(G, modularity_list, 'modularity')

for e,c in enumerate(communities_mod):
    if len(c) > 2:
        print('Class '+str(e)+':', list(c))










