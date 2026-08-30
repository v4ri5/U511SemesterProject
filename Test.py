from U511SemesterProject.Process import Process

# Testing the process class and its methods
p = Process("P1", 0, 5)
p.start = 2
p.completion = 7

print(p.turnaround_time())   # 7
print(p.wait_time())         # 2
print(p.response_time())     # 2