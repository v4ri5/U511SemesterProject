
from Process import Process

def priority_scheduling(processes):
    
    """
    Implements a priority scheduling algorithim for a list of processes.
    The processes are sorted based on their priority witht the smallest number being the highest priority.
    """
    
    clock = min(process.arrival for process in processes)   # Initialize clock to the earliest arrival time
    completed_processes = []
    unrun = processes.copy()  # Create a copy of the processes list to keep track of unrun processes
    
    while unrun :
        ready = [p for p in unrun if p.arrival <= clock]
        
        if not ready:
            clock = min(p.arrival for p in unrun)
            continue
        
        current = min(ready, key=lambda p: p.priority)
        current.start = clock
        clock = clock + current.burst
        current.completion = clock
        completed_processes.append(current)
        unrun.remove(current)
        
    return completed_processes
    
    