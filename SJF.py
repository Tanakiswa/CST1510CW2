def sjf(process_list):
    t = 0
    gantt = []
    completed ={}

    while process_list:
        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)

        if not available:
            gantt.append(("Idle", t, t+1))
            t += 1
            continue

        available.sort(key=lambda x: x[0])
        process = available[0]

        burst_time = process[0]
        arrival_time = process[1]
        pID = process[2]

        start_time = t
        t += burst_time
        ct = t
        tt = ct - arrival_time
        wt = tt - burst_time

        gantt.append((pID, start_time, ct))
        completed[pID] = [burst_time, arrival_time, wt, tt]

        process_list.remove(process)

    return gantt, completed

def main():
    process_list = []

    while True:
        try:
            n = int(input("Enter number of processes: "))
            if n <= 0:
                print("Enter a positive integer")
                continue
             break
        except ValueError:
            print("Enter an integer")

burst_times = []
for i in range(1, n + 1):
         while True:
             try:
                bt = int(input(f"Enter burst time for P{i}: "))
                if bt <= 0:
                    print("Enter a positive integer")
                    continue
                burst_times.append(bt)
                break
             except ValueError:
                print("Enter a positive integer")

arrival_times = []
for i range(1, n + 1):
    while True:
            try:
                at = int(input(f"Enter arrival time for P{i}: "))
                if at < 0:
                    print("Enter a positive integer")
                    continue
                arrival_times.append(at)
                break
            except ValueError:
                print("Enter a positive integer")

for i in range(1, n + 1):
    pID = f"P{i}"
    process_list.append([burst_times[i-1], arrival_times[i-1], pID])

gantt, completed = sjf(process_list)

print("\nRESULTS (Shortest Job First)\n")
print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<12}{'Waiting Time':<12}{'Turnaround Time':<15}")
print("-" * 65)

total_wt = 0
total_tt = 0

for pID in sorted(completed.keys()):
    burst, arrival, wt, tt = completed[pID]
    total_wt += wt
    total_tt += tt

    print(f"{pID:<10}{burst:<10}{arrival:<15}{wt:<10}{tt:<15}

avg_wt = total_wt / n
avg_tt = total_tt / n

print("-" * 65)
print(f"{'Average':<10}{avg_wt:<12.2f}{'':>12}{'':>12}{avg_tt:>15.2f}")

print("\nGantt Chart Order:")

for pID, start, end in gantt:
    print(f"| {pID} ", end="")
print("|")

print("0", end="")
for pID, start, end in gantt:
    print(f"{'' * (len(pID)+1)}{end}", end="")
print()

if __name__ == "__main__":
main()
