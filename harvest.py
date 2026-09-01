import psutil
from U511SemesterProject.Process import Process

##Collects the processes to be scheduled and their attributes from the system using the psutil library.

def harvest_processes():
    processes = []                  #List of processes to be scheduled
    for proc in psutil.process_iter(['pid','create_time','cpu_times', 'num_threads']): # Get process information
        try:
            pid = proc.info['pid']
            arrival = proc.info['create_time']
            burst = proc.info['cpu_times'].user + proc.info['cpu_times'].system
            threads = proc.info['num_threads']
            processes.append(Process(pid, arrival, burst, threads))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): ## Handles exceptions from process extra process information that we cant use 
            pass
    return processes
        
        