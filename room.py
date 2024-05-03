import sys
import json
filename=(sys.argv[1])
print(filename)
fiobj=open(filename)
data=json.load(fiobj)
fiobj.close()
print(data)
room_type=input("enter room type:")
room_info=[]
for p in data:
    for v in p:
        for k,v in v.items():
            if k==("dow"):
                print(k,v)
            elif k==("time"):
                print(k,v)
            elif k==("conference-categories-count"):
                  room_available= v
                  if room_type in room_available:
                      print(room_type, room_available[room_type])
                  elif room_type in room_available:
                      tot_rooms=tot_rooms+room_available
                  else:
                      print("Room type is not available")
tot_rooms=0
for p in data:
    tot_rooms=tot_rooms+len(p)
    avg_rooms=tot_rooms/len(data)
print("The total average is:",avg_rooms)

            



            





    

                
