# The processes to be scheduled is defined in this file. 
# The Process class represents a process with its attributes 
# and methods to calculate turnaround time, wait time, and response time.
class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.start = None
        self.completion = None
        self.state = "new"


    def turnaround_time(self):
        return self.completion - self.arrival

    def wait_time(self):
        return self.start - self.arrival

    def response_time(self):
        return self.start - self.arrival

    def __str__(self):
        return f"Process {self.pid}: Arrival={self.arrival}, Burst={self.burst}, Start={self.start}, Completion={self.completion}, State={self.state}"