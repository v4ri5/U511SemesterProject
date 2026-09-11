from Process import Process
from harvest import harvest_processes
from PrioritySchedule import priority_scheduling
processes, dropped = harvest_processes()

"""
processes = [
    Process(0, 4, 5, 1, 3),
    Process(1, 4, 5, 2, 2), 
    Process(2, 4, 5, 3, 1),
    Process(3, 100, 5, 4, 0)
]
"""
    
    
print("Priority Scheduled Processes:")
print(priority_scheduling(processes))
print(len(dropped))
for _ in dropped:
    print(dropped)
    
    
## The data presented isnt normalizes and there is no filtering of actually schedulable processes.
##The data is just raw data from the system.