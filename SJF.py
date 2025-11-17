def sjf(process_list):
    t = 0
    gantt = []
    completed ={}

    while process_list []:
        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)
        if not available:
            t += 1
            gantt.append("Idle")
            continue
            available.sort(key=lambda x: x[0])
            process = available[0]
            burst_time = process[0]
            arrival_time = process[1]
            pID = process[2]

            t += burst_time
            ct = t
            tt = ct - arrival_time
            wt = tt - burst_time

            gantt.append(pID)
            completed[pID] = [burst_time, wt, tt]

            process_list.remove(process)

return gantt, completed

def main():
    process_list = []

    while True:
        try:
            n = int(input("Enter number of process: "))
            if n <= 0:
                print("Enter a positive integer")
                continue
                break
        except ValueError:
            print("Enter an integer")

for i in range(1, n + 1):
         while True:
             try:
                 bt = int(input(f"Enter burst time for P{i}: "))
                if bt < 0:
print("Enter a positive integer")
continue
except ValueError:
                print("Enter a positive integer")
continue

arrival_time = 0
pID = f"P{i}"

process_list.append([bt, arrival_time, pID])
gantt, completed = sjf(process_list)