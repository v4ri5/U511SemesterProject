from U511SemesterProject.Process import Process
from U511SemesterProject.harvest import harvest_processes

processes = harvest_processes()

print("Processes to be scheduled:")
for process in processes:
    print(process)
## The data presented isnt normalizes and there is no filtering of actually schedulable processes.
##The data is just raw data from the system.