#!/usr/bin/python3
import time
import kuimaze
import os
import  math

class Agent(kuimaze.BaseAgent):
    '''
    Simple example of agent class that inherits kuimaze.BaseAgent class
    '''
    def __init__(self, environment):
        self.environment = environment
    def h(self,curr, goal):
        h = math.sqrt(((curr[0] - goal[0])**2) + ((curr[1]-goal[1])**2))
        return h

    def find_path(self):
        observation = self.environment.reset()
        start = observation[0][0:2]##start
        goal = observation[1][0:2]##goal

        open_lst = []
        open_lst.append(start)
        close_lst=[]
        poo ={}
        poo [start]=0
        par ={}
        par[start]= start
        while len(open_lst)>0 :
            n =None
            for v in open_lst:
                if n == None or  poo[v] + self.h(v,goal)< poo[n] +self.h(n,goal):
                    n=v
            if n==None:
                return None
            if n == goal:
                path=[]

                while par[n]!= n:
                    path.append(n)
                    n = par[n]
                path.append(start)
                path.reverse()
                return path
            for (m,weight) in self.environment.expand(n):
                if m not in open_lst and m not in close_lst:
                    open_lst.append(m)
                    par[m]=n
                    poo[m]=poo[n]+weight
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
                        if m in close_lst:
                            close_lst.remove(m)
                            open_lst.append(m)
            open_lst.remove(n)
            close_lst.append(n)
            #self.environment.render()
            #time.sleep(0.10)
if __name__ == '__main__':

    MAP = 'maps/normal/normal9.bmp'
    MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), MAP)
    GRAD = (0, 0)
    SAVE_PATH = False
    SAVE_EPS = False

    env = kuimaze.InfEasyMaze(map_image=MAP, grad=GRAD)       # For using random map set: map_image=None
    agent = Agent(env)

    path = agent.find_path()
    print(path)
    env.set_path(path)          # set path it should go from the init state to the goal state
    if SAVE_PATH:
        env.save_path()         # save path of agent to current directory
    if SAVE_EPS:
        env.save_eps()          # save rendered image to eps
    env.render(mode='human')
    time.sleep(3)
