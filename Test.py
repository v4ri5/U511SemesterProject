from Process import Process
from harvest import harvest_processes

#processes = harvest_processes()

#print("Processes to be scheduled:")
#for process in processes:
    #print(process)
## The data presented isnt normalizes and there is no filtering of actually schedulable processes.
##The data is just raw data from the system.


if __name__ == "__main__":
    procs = harvest_processes()
    print("Processes to be scheduled:")
    for p in procs:
        print(p.pid, p.arrival, p.burst, p.threads)