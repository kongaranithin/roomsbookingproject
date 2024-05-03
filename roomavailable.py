import sys
import json
filename=(sys.argv[1])
print(filename)
fiobj=open(filename)
data=json.load(fiobj)
fiobj.close()
print(data)
room_type=input("enter room type:")
total_rooms=0
room_count = 0
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
                      total_rooms=total_rooms+room_available
                  else:
                      print("Room type is not available")
                  if room_type in room_available:
                    room_count =room_count+1
                    total_rooms =total_rooms+room_available[room_type]

if room_count > 0:
    average_rooms = total_rooms / room_count
    print(f"The average number:",average_rooms)





            





    

                
