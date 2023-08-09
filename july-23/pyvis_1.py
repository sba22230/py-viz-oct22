# %%
from pyvis import network as net
from IPython.core.display import display, HTML
import random

# %%
g_only_nodes =  net.Network(height='600px',width='90%',
                  bgcolor='white',font_color="red",
                  heading="Networkx Graph with only Nodes")
 
for i in range(1,11):  
  g_only_nodes.add_node(i)
 
g_only_nodes.show('Only_Nodes.html')
display(HTML('Only_Nodes.html'))

# %%
def generate_edge():
  s = random.randint(1,10)
  d = random.randint(1,10)
  return (s,d)

# %%
g =  net.Network(height='600px',width='90%',
                  bgcolor='white',font_color="red",
                  heading="A Simple Networkx Graph")
 
for i in range(1,11):  
  g.add_node(i)
 
i=0
chosen_set = []
while(i!=20):
  eg = generate_edge()
  if(eg[0]!=eg[1] and not (eg in chosen_set)):
      chosen_set.append(eg)
      g.add_edge(eg[0],eg[1])
      i+=1
 
g.show('Simple_Network_Graph.html')
display(HTML('Simple_Network_Graph.html'))



# %%
