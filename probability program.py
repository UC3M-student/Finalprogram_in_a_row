import numpy as np
import time
import pandas as pd

start_time = time.time()

df = open("datacollector.txt","w")
b = 2
t = 0
a = 1

while a <= 10:
    userlist = np.arange(0,b).tolist()
    d = 0
    while d <= 100000:
        d += 1
        n = 0
        while 1 == int(np.random.choice(userlist)):
            n +=1


        if n != 0:
            matrix = (a + 1), n, b
            df.write(repr(matrix) + "\n")

    a +=1
    b +=1
    print("calculando probabilidades del numero:", a - 1)


df.close()

df = open("datacollector.txt","rt")
data1 = df.read()
data1 = data1.replace("(","")
data1 = data1.replace(")","")

df.close()

df = open("datacollector.txt","wt")

df.write(data1)

df.close()

df = pd.read_csv("datacollector.txt")
df.columns = ["number","times","probability"]

finaldata = df.groupby(["number","times"]).count()
finaldata.to_csv("countdata.txt")

df_x = pd.read_csv("countdata.txt")
df_x["probability"] = df_x["probability"].div(1000)

df_x.to_csv("FINALCOPY.txt", index= False)

print("--- %s seconds ---" % (time.time() - start_time))