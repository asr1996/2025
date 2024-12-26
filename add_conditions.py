# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
      offset-=1
    else : 
      offset+=1    
    print(offset)

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for i,j in house:
    print("the " + i + " is", str(j) + " sqm")
