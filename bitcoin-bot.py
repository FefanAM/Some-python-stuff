from random import randrange
from os import system as s

graph_up = """

|              /
|             /
|       _____/
|      /
|     /   
|  __/
|_/______________

"""

graph_down = """

|
|_____
|     \  
|      \_____
|            |
|            | 
|____________|___
             |
             |
"""

while True:
    s('cls')
    print('Should I invest in bitcoin?')
    input()
    if randrange(0,2) == 1:
        print('nah its going down')
        print(graph_down)
    else:
        print('hell yeah we ricjh')
        print(graph_up)
    input()
