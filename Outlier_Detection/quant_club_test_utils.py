import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
import random

def read_csv_with_index(file_name,size=None):
    """
    Input:
        file_name : name of file with extension
        size : how many points to read. The default value is None.
    
    Output:
        Return a dictionary with time and value as its keys.    
    """
    f=open(file_name,'r')
    s=f.read()
    s=s.split('\n')
    if type(size) == type(2):
        s=s[0:size]
    keys=s[0].split(',')
    #print(keys)
    s=s[1:-1]
    s=[i.split(',') for i in s]
    
    df=dict()
    c=0
    for key in keys:
        df[key]=[]
        for i in s :
            #print(i)
            df[key].append(float(i[c]))
        c+=1
    
    f.close()
    return df

def plot_anomaly(df,anomaly_times,figsize=(40,20),markersize=15):
    """
    Input:
        Takes a input dataframe with columns 'time' & 'value' and a list named anomaly_time which has the index of the outliers 
    
        Input Dataframe : a dict such that 
            df['time'] = list of times where we have data
            df['value'] = list of value at that time
        anomaly_times : list of time/index when there is anomaly
    
    Output:
        It plots the anomalies on the supplied data
    
    """
    plt.figure(figsize=figsize)
    plt.plot(df['time'],df['value'],markevery=anomaly_times,marker='o',markersize=markersize,markerfacecolor='red')
    
def make_and_save_data_file(working_on = 'Colab'):
  """
  This function creates the data file and saves it in your drive folder.
  It returns the name of the saved file: which is "testfile + UNIX time stamp"

  Parameters:
    working_on : 'Colab' or 'Local' , if working on Colab or Local
                  The default value is Colab.
  """
  n=500
  T= np.arange(1,500,1)
  T=[10]
  for i in range(10000):
    T.append(np.random.standard_normal(1)+T[-1])
  outliers = random.sample(list(np.arange(1,10000,1)), 20)
  for i in outliers:
    T[i] = T[i] + 70*np.random.standard_normal(1)

  ## comment out if time interval are non-uniform
  times=range(len(T))

  ## comment out if time interval are uniform
  #times=[1+np.abs(np.random.standard_normal(1)) for i in range(len(T))]

  df=pd.DataFrame({'value':[(float(t*100)//1)/100 for t in T],'time':times})
  timenow=time.time()
  print("Plot of the Generated Data")
  plt.figure(figsize=(40,20))
  plt.plot(df['value'])

  if working_on == 'Local':
    df.to_csv('testfile'+str(int(time.time()))+'.csv',index=False)
  elif working_on == 'Colab':
    df.to_csv('/content/gdrive/My Drive/Coding Challenge/testfile'+str(int(timenow))+'.csv',index=False)
  else:
    print('Wrong Input!! give one of the options only [\'Local\',\'Colab\']')
    return

  return 'testfile'+str(int(timenow))+'.csv'