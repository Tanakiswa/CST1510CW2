<<<<<<< HEAD
"""Simple non-preemptive SJF scheduler.
Process representation: list of dicts with keys 'pid','arrival','burst'.
"""
import sys

=======
#Shortest Job First CPU scheduling algorithm
>>>>>>> f939d0fa0bd0e4eb8a9db3d9255a228418564d85
def sjf(process_list):
    # copy and sort by arrival for deterministic behavior
    processes = sorted(process_list, key=lambda p: p['arrival'])
    time = 0
    gantt = []
    completed = {}
<<<<<<< HEAD
    remaining = processes.copy()
=======

    while process_list:
        available = [p for p in process_list if p[1] <= t]
>>>>>>> f939d0fa0bd0e4eb8a9db3d9255a228418564d85

    while remaining:
        # find available processes
        available = [p for p in remaining if p['arrival'] <= time]
        if not available:
            # CPU idle one unit
            gantt.append(('Idle', time, time+1))
            time += 1
            continue

        # choose the shortest burst among available
        available.sort(key=lambda p: p['burst'])
        proc = available[0]

        pid = proc['pid']
        arrival = proc['arrival']
        burst = proc['burst']

        start = time
        completion = start + burst

        gantt.append((pid, start, completion))

        turnaround = completion - arrival
        waiting = start - arrival
        response = start - arrival

        completed[pid] = {
            'arrival': arrival,
            'burst': burst,
            'start': start,
            'completion': completion,
            'turnaround': turnaround,
            'waiting': waiting,
            'response': response,
        }

        time = completion
        remaining.remove(proc)

    total_time = gantt[-1][2] if gantt else 0
    total_busy = sum(p['burst'] for p in processes)
    cpu_util = (total_busy / total_time * 100) if total_time else 0.0
    num = len(completed)
    avg_wait = sum(v['waiting'] for v in completed.values()) / num if num else 0
    avg_turn = sum(v['turnaround'] for v in completed.values()) / num if num else 0
    avg_resp = sum(v['response'] for v in completed.values()) / num if num else 0

    metrics = {
        'avg_waiting': avg_wait,
        'avg_turnaround': avg_turn,
        'avg_response': avg_resp,
        'cpu_utilization': cpu_util,
        'total_time': total_time,
        'total_busy': total_busy,
    }

    return gantt, completed, metrics

def _read_input():
    while True:
        try:
            n = int(input('Enter number of processes: '))
            if n <= 0:
                print('Enter a positive integer')
                continue
            break
        except ValueError:
            print('Enter an integer')

<<<<<<< HEAD
    plist = []
    for i in range(1, n + 1):
        pid = input(f'Enter Process ID for process {i}: ').strip() or f'P{i}'
        while True:
=======
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
for i in range(1, n + 1):
    while True:
>>>>>>> f939d0fa0bd0e4eb8a9db3d9255a228418564d85
            try:
                arrival = int(input(f'Enter Arrival Time for {pid}: '))
                if arrival < 0:
                    print('Arrival cannot be negative')
                    continue
                break
            except ValueError:
                print('Enter an integer')
        while True:
            try:
                burst = int(input(f'Enter Burst Time for {pid}: '))
                if burst <= 0:
                    print('Burst must be positive')
                    continue
                break
            except ValueError:
                print('Enter an integer')
        plist.append({'pid': pid, 'arrival': arrival, 'burst': burst})
    return plist

def print_results(gantt, completed, metrics):
    print(f"{'Process':<8}{'Arr':>6}{'Burst':>8}{'Start':>8}{'Comp':>8}{'Turn':>8}{'Wait':>8}{'Resp':>8}")
    for pid, data in completed.items():
        print(f"{pid:<8}{data['arrival']:>6}{data['burst']:>8}{data['start']:>8}{data['completion']:>8}{data['turnaround']:>8}{data['waiting']:>8}{data['response']:>8}")

    print('\nGantt chart:')
    if gantt:
        for pid, start, end in gantt:
            print(f"| {pid} ", end="")
        print("|")
        print("0", end="")
        for pid, start, end in gantt:
            print(f"{' ' * (len(pid)+1)}{end}", end="")
        print()
    else:
        print('(no timeline)')

    print('\nSUMMARY:')
    print(f"Average Waiting Time:    {metrics['avg_waiting']:.2f}")
    print(f"Average Turnaround Time: {metrics['avg_turnaround']:.2f}")
    print(f"Average Response Time:   {metrics['avg_response']:.2f}")
    print(f"CPU Utilization:         {metrics['cpu_utilization']:.2f}%")

def main():
    # Support a demo mode via command-line: `--demo`
    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        plist = [
            {'pid': 'P1', 'arrival': 0, 'burst': 8},
            {'pid': 'P2', 'arrival': 1, 'burst': 4},
            {'pid': 'P3', 'arrival': 2, 'burst': 9},
            {'pid': 'P4', 'arrival': 3, 'burst': 5},
        ]
    else:
        plist = _read_input()

<<<<<<< HEAD
    gantt, completed, metrics = sjf(plist)
    print_results(gantt, completed, metrics)

if __name__ == '__main__':
    main()
=======
for pID in sorted(completed.keys()):
    burst, arrival, wt, tt = completed[pID]
    total_wt += wt
    total_tt += tt
    print(f"{pID:<10}{burst:<10}{arrival:<15}{wt:<10}{tt:<15}")

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
    print(f" {end}", end="")
print()

if __name__ == "__main__":
    main()

>>>>>>> f939d0fa0bd0e4eb8a9db3d9255a228418564d85
