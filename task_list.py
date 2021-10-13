tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompletedTasks(taskList):
    unComp = []
    for task in taskList:
        if task["completed"] == False:
            unComp.append(task["description"])
    return unComp
   
k = uncompletedTasks(tasks)
print(k)

def completedTask(taskList):
    Comp = []
    for task in taskList:
        if task['completed'] == True:
            Comp.append(task['description'])
    return Comp

i = completedTask(tasks)
print(i)

def allTask(taskList):
    allTs = []
    for task in taskList:
        allTs.append(task['description'])
    return allTs

j = allTask(tasks)
print(j)

def timeTaken(taskList):
    minTime = []
    for task in taskList:
        if task['time_taken'] == 15:
            minTime.append(task['description'])
    return minTime

g = timeTaken(tasks)
print(g)

def giveDescription(taskList, string):
    for task in taskList:
        if task['description'] == string:
            return task

h = giveDescription(tasks, "Make Dinner")
print(h)
###Answer 7
print ("Answer 7")
def giveDescription(taskList, string):
    for task in taskList:
        if task['description'] == string:
            task['completed'] = True
            return task['description'], task['completed']

p = giveDescription(tasks, "Wash Dishes")
print(p)
###Answer 8
print ("Answer 8")

tasks.append({ "description": "Dust TV", "completed": False, "time_taken": 2 })
print(tasks)


# menu = [
#     {
#     "Menu:"
# "1: Display All Tasks"
# "2: Display Uncompleted Tasks"
# "3: Display Completed Tasks"
# "4: Mark Task as Complete"
# "5: Get Tasks Which Take Longer Than a Given Time"
# "6: Find Task by Description"
# "7: Add a new Task to list"
# "M or m: Display this menu"
# "Q or q: Quit"
#     }
# ]

# menu = {}
# menu['1']="Display All Tasks" 
# menu['2']="Display Uncompleted Tasks"
# menu['3']="Display Completed Tasks"
# menu['4']="Mark Task as Complete"
# menu['5']="Get Tasks Which Take Longer Than a Given Time"
# menu['6']="Find Task by Description"
# menu['7']="Add a new Task to list"

# while True: 
#   options=menu.keys()
#   options.sort()
# for entry in options: 
#  print entry, menu[entry]

#     selection=raw_input("Please Select:") 
#     if selection =='1': 
#       print "add" 
#     elif selection == '2': 
#       print "delete"
#     elif selection == '3':
#       print "find" 
#     elif selection == '4': 
#       break
#     else: 
#       print "Unknown Option Selected!" 


