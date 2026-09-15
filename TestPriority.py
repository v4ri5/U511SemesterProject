from Process import Process
from harvest import harvest_processes
from PrioritySchedule import priority_scheduling
processes, dropped = harvest_processes()
    
    
print("Priority Scheduled Processes:")
print(priority_scheduling(processes))
print(len(dropped))
for _ in dropped:
    print(dropped)
    
    
## The data presented isnt normalizes and there is no filtering of actually schedulable processes.
##The data is just raw data from the system.