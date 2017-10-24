filename = "ganesh.txt"
file_obj = open(filename, "w")
file_obj.write("#!/bin/bash"+"\n")
file_obj.write("*nat"+"\n")
file_obj.write(":CIRCULAR_POOL - [0:0]"+"\n")
for i in range (1,292):
              file_obj.write(":CIRCULAR_POOL_"+str(i)+" - [0:0]"+"\n")
file_obj.write("-A PREROUTING -j CIRCULAR_POOL"+"\n")

increment=1
#first level  four chains
for i in range(0,256,64):
              file_obj.write("-A CIRCULAR_POOL -s 10.1."+str(i)+".0/18 -i source0 -j CIRCULAR_POOL_"+str(increment)+"\n")
              increment+=1

#second level four times eight chains      4*8 = 32 chains
for i in range(0,64,8):
              file_obj.write("-A CIRCULAR_POOL_1 -s 10.1."+str(i)+".0/18 -i source0 -j CIRCULAR_POOL_"+str(increment)+"\n")
              increment+=1
              
for i in range(64,128,8):
              file_obj.write("-A CIRCULAR_POOL_2 -s 10.1."+str(i)+".0/18 -i source0 -j CIRCULAR_POOL_"+str(increment)+"\n")
              increment+=1

for i in range(128,192,8):
              file_obj.write("-A CIRCULAR_POOL_3 -s 10.1."+str(i)+".0/18 -i source0 -j CIRCULAR_POOL_"+str(increment)+"\n")
              increment+=1

for i in range(192,256,8):
              file_obj.write("-A CIRCULAR_POOL_4 -s 10.1."+str(i)+".0/18 -i source0 -j CIRCULAR_POOL_"+str(increment)+"\n")
              increment+=1
              
#third level eight times eight chains      8*8 =64 chains
count_max =8
count_min = 0
for j in range(5,37):
              for i in range(count_min, count_max):
                            file_obj.write("-A CIRCULAR_POOL_"+str(j)+" -s 10.1."+str(i)+".0/24 -i source0 -j CIRCULAR_POOL_"+str(increment)+"\n")
                            increment+=1
              if count_max == 256:
                            break
              else:
                            count_max = count_max + 8
                            count_min = count_min + 8

#final chains 256
start=37                            
for i in range(0,256):
              for j in range(0,256):
                            file_obj.write("-A CIRCULAR_POOL_"+str(start)+" -i source0  --src 10.1."+str(i)+"."+str(j)+"  -j ACCEPT"+"\n")
              start+=1
file_obj.close()
                            
