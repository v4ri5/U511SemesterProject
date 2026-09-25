from Process import Process
from harvest import harvest_processes

def fcfs_schedule(processes):
    scheduled = sorted(processes, key=lambda p: p.arrival)
    clock = scheduled[0].arrival

    for process in scheduled:
        if process.arrival > clock:
            clock = process.arrival
        process.start = clock
        clock += process.burst
        process.completion = clock
        process.state = 'completed'
    return scheduled

if __name__ == "__main__":
    procs = harvest_processes()
    scheduled = fcfs_schedule(procs)

    total_wait = 0
    total_turnaround = 0

    for p in scheduled:
        print(p)
        total_wait += p.wait_time()
        total_turnaround += p.turnaround_time()

    n = len(scheduled)
    print(f"\nAverage Wait Time: {total_wait / n:.4f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.4f}")