### List

lst = [1,2,"ram","tom",1.3,7+2j,True,"A"]  #making a list (using square brackets)
lst[2]  # accessing a list element
lst[2:] # accessing multiple list elements together
lst[2]="rem"  # updating an element

cities = [[1,2,3],[5,[4,6,7],8],9]
cities[1][1][1]  #inherent index accessing

# List methods
lst.append(1) # add element at the last
lst.insert(1,5) # add at element at a desires index (index, element)
lst2 = [6,7,7,8,9]
lst.extend(lst2) # adding a whole collection at the end
lst+lst2 # adding a whole list at the end (only same type of collections can be concatenated)
lst.remove("rem") # delete an element (if multiple then the first element index-wise get deleted)
lst.pop() # pops out the last element
lst.pop(2) # pops out the element at desired index
lst.reverse() # reverses the list
lst2.sort() # sorts the list 
lst2.sort(reverse=True) # sorts the list in reverse
lst.clear()  # clears the whole list
lst = lst2.copy() # copying a list

### Tuple

tup = (1,2,"ram","tom",1.3,7+2j,True,"A")   #making a tuple (using brackets)
tup[2]   # accessing a tuple element
tup[:-1]   # accessing multiple tuple elements together

# Tuple methods
tup.index(2) #tell the index of an element
tup.count("ram") #tell the count of the element

### Set (No Order)

st1 = {1,2,"ram","tom",1.3,7+2j,True,"A"}   #making a set (using curly brackets)
st2 = {1,2,6,8,90,22}

# Set Methods
st1.add(7) # adds an element to any arbitrary position
st2.difference(st1) # tells the difference (shows the elements of st2 which are not in st1)
st1.union(st2) # mathematical union
st1.intersection(st2) # mathematical intersection

### Dictionary

dct = {"name":"akhil","college":"bvp","roll":"412"}  #making a dictionary {"key":"value"}
dct["name"]   # accessing a value using the key
dct["name"]="arjun"   # updating a value
dct["phone"]=19299349001

students = {"roll":[1,2,3,4],"name":["a","b","c","d"]}
students["roll"][2]

# Dictionary methods
nam = dct.get("name")  # gets the value using the key
dct.keys()  # gives us all the keys
dct.values()  # gives us all the values
dct.items()  # gives the key:value pair in tuple form
dct.update({"address":"delhi"})
dct.pop("roll")  # pops the item using key
dct.popitem()  # pops the whole dictionary
dct.fromkeys(tup) # we can create a dictionary using the an collection and these will become the keys
students.clear()  # clears the dictionary
for col,row in dct.items():      # looping thru the dict
    print(col,row)

# Making a dictionary using zip method
x = ["name","age","clg"]
y = ["akhil","20","bvp"]
newdct = dict(zip(x,y))


## IF ELSE and ELIF

per = int(input("Enter Your Percentage "))
if per >= 80:
    print("Grade A+")
elif per < 80 and per >= 60:
    print("Grade A")
elif per < 60 and per >= 40:
    print("Grade B")
else:
    print("Fail")


## NESTED IF ELSE

print("Write Y for Yes and N for No")
lk = input("Battery Leakage? ")
ch = input("Chargable? ")
wt = input("Weight?(L or H) ")
bckup = int(input("Enter Backup "))
if lk=="Y":
    print("Battery has leakage problem")
else:
    if ch=="Y":
        if wt=="L":
            if bckup>7:
                print("Battery is best")
            else:
                print("Battery has leakage problem")
        else:
            print("Battery has weight problem")
    else:
        print("Battery is not chargable")


## Using range

#range(n)
#range(start, stop)
#range(start, stop, diff)


## FOR LOOP

#for iterator in iterable:
#       statements

for i in range(1,11):
    print(i)

## NESTED FOR LOOP

for i in range(1,11):
    for j in range(2,11):
        #print(i,"x",j,"=",i*j,end='   ')
        print("%4d" %(i*j),end=" ")
    print()

## WHILE LOOP

#while cond:
#    statement
#    increment

i=1
while i<=10:
    j=2
    while j<=10:
        print("%4d" %(i*j),end=" ")
        j+=1
    print()
    i+=1