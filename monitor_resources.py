from threading import Thread
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

class monitor_resources(Thread):
    def __init__(self,inp_func,time_sleep=1.0):
        Thread.__init__(self)
        self.running = True
        self.inp_func = inp_func
        self.time_sleep = time_sleep
        if time_sleep<1.0:
            self.round_n=10
        else:
            self.round_n=0
        self.out={}
        
    def run(self):
        while self.running:
            time.sleep(self.time_sleep)
            self.out.update({ np.round(time.time(),self.round_n) : eval(self.inp_func)})
            
    def stop(self):
        self.running = False
    
    def get(self):
        return self.out
    
    def pd(self,add_pd=None):
        self.out_pd = pd.DataFrame.from_dict(self.get(), orient='index',columns=[self.inp_func])
        self.out_pd.index = self.out_pd.index-min(self.out_pd.index)
        try:
            self.out_pd = pd.concat([self.out_pd, add_pd ], axis=1)
        except:
            pass
        return self.out_pd
    
    def plot(self):
        return self.pd().plot() 
