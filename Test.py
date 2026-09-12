from Process import Process
from harvest import harvest_processes
from SJF import non_preemptive_sjf

#processes = harvest_processes()

print("Processes to be scheduled:")

completed = non_preemptive_sjf(processes)

for p in completed:
    print(p)

#tells us total time to complete algorithm
total_time = max(p.completion for p in completed)
print(f"\nTotal scheduling time: {total_time:.2f}")
