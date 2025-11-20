 #First Come First Serve CPU scheduling alogorithm
 #class structure
class FCFSScheduler:
    def __init__(self): 
        self.process_list = []
        self.completed_processes = {}
        self.gantt_chart = {
        'total_waiting_time': 0,
        'total_turnaround_time': 0,
        'total_response_time': 0,
        'cpu_utilization': 0
        }

#function to define process list
def run_simulation(self):
    sorted_processes = sorted(self.process_list, key=lambda x: x['arrival_time'])
    def fcfs(process_list):
        """Run FCFS scheduling.

        process_list: list of dicts with keys 'pid', 'arrival', 'burst'
        Returns: gantt(list), completed(dict), metrics(dict)
        completed[pID] = {arrival, burst, start, completion, turnaround, waiting, response}
        metrics: average times and cpu utilization
        """
        # Sort by arrival time (stable)
        processes = sorted(process_list, key=lambda p: p['arrival'])

        time = 0
        gantt = []
        completed = {}
        total_busy = 0

        for p in processes:
            pid = p['pid']
            arrival = p['arrival']
            burst = p['burst']

            # idle until arrival
            if time < arrival:
                idle_len = arrival - time
                gantt.extend(['Idle'] * idle_len)
                time = arrival
def fcfs(process_list):
    """Run FCFS scheduling.

    process_list: list of dicts with keys 'pid', 'arrival', 'burst'
    Returns: gantt(list), completed(dict), metrics(dict)
    completed[pID] = {arrival, burst, start, completion, turnaround, waiting, response}
    metrics: average times and cpu utilization
    """
    # Sort by arrival time (stable)
    processes = sorted(process_list, key=lambda p: p['arrival'])

    time = 0
    gantt = []
    completed = {}
    total_busy = 0

<<<<<<< HEAD
    for p in processes:
        pid = p['pid']
        arrival = p['arrival']
        burst = p['burst']
=======
    #while loop that runs until are processes are executed
    while process_list:
        available = [p for p in process_list if p[0] <= t]

        if not available:
            gantt.append(("Idle", t, 1))
            t += 1
            continue

        #pick first available process and remove it from list
        process = available[0]
        process_list.remove(process)
>>>>>>> 49e42a75b35a00e5f7f083abfae25dc557b951e9

        # idle until arrival
        if time < arrival:
            idle_len = arrival - time
            gantt.extend(['Idle'] * idle_len)
            time = arrival

<<<<<<< HEAD
        start = time
        completion = start + burst
        turnaround = completion - arrival
        waiting = start - arrival
        response = start - arrival

        # record timeline
        gantt.extend([pid] * burst)
        total_busy += burst

        completed[pid] = {
            'arrival': arrival,
            'burst': burst,
            'start': start,
            'completion': completion,
            'turnaround': turnaround,
            'waiting': waiting,
            'response': response,
        }
=======
        gantt.append((pID, start_time, burst_time))  #update gantt chart
        completed[pID] = [arrival_time, burst_time, completion_time, turnaround_time, waiting_time]  #store results for processes

    #print results in table
    print(f"\n{'Process':<10}{'Arrival':>10}{'Burst':>10}{'Completion':>12}{'Turnaround':>12}{'Waiting':>10}")
    for pID, data in completed.items():
        print(f"{pID:<10}{data[0]:>10}{data[1]:>10}{data[2]:>12}{data[3]:>12}{data[4]:>10}")

    n = len(completed)
    avg_wt = sum(data[4] for data in completed.values()) / n
    avg_tat = sum(data[3] for data in completed.values()) / n
    print(f"\nAverage Waiting Time: {avg_wt:>12.2f}")
    print(f"Average Turnaround Time: {avg_tat:>12.2f}")

    print("\nGantt Chart:")
    chart = ""
    timeline = ""
    for pID, start_time, burst_time in gantt:
        block = f"|{pID.center(burst_time*3)}"
        chart += block
        timeline += f"{str(start_time).rjust(3)}{' '*(burst_time*3)}"
    chart += "|"
    timeline += f"{t:>3}"


    print(chart)
    print(timeline)
>>>>>>> 49e42a75b35a00e5f7f083abfae25dc557b951e9

        time = completion

    total_time = len(gantt) if gantt else 0
    cpu_util = (total_busy / total_time * 100) if total_time > 0 else 0.0

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


def print_results(gantt, completed, metrics):
    # Print table
    print(f"{'Process':<8}{'Arr':>6}{'Burst':>8}{'Start':>8}{'Comp':>8}{'Turn':>8}{'Wait':>8}{'Resp':>8}")
    for pid, data in completed.items():
        print(f"{pid:<8}{data['arrival']:>6}{data['burst']:>8}{data['start']:>8}{data['completion']:>8}{data['turnaround']:>8}{data['waiting']:>8}{data['response']:>8}")

    # Gantt simple print
    print('\nGantt chart:')
    if not gantt:
        print('(no timeline)')
    else:
        timeline = ' | '.join(gantt)
        print(timeline)

    print('\nSUMMARY:')
    print(f"Average Waiting Time:    {metrics['avg_waiting']:.2f}")
    print(f"Average Turnaround Time: {metrics['avg_turnaround']:.2f}")
    print(f"Average Response Time:   {metrics['avg_response']:.2f}")
    print(f"CPU Utilization:         {metrics['cpu_utilization']:.2f}%")


def _read_input():
    while True:
        try:
            n = int(input('Enter number of processes: '))
            if n <= 0:
                print('Number of processes must be positive.')
                continue
            break
        except ValueError:
<<<<<<< HEAD
            print('Invalid input. Please enter an integer.')
=======
            print("Invalid input. Please enter a number.")

    #user enters process details
    process_list = []
    for i in range(n):
        pID = input(f"Enter Process ID for process {i + 1}: ")
>>>>>>> 49e42a75b35a00e5f7f083abfae25dc557b951e9

    plist = []
    for i in range(1, n + 1):
        pid = input(f'Enter Process ID for process {i}: ').strip() or f'P{i}'
        while True:
            try:
<<<<<<< HEAD
                arrival = int(input(f'Enter Arrival Time for {pid}: '))
=======
                arrival = int(input(f"Enter Arrival Time for {pID}: "))
>>>>>>> 49e42a75b35a00e5f7f083abfae25dc557b951e9
                if arrival < 0:
                    print('Arrival time cannot be negative.')
                    continue
                break
            except ValueError:
                print('Invalid input. Please enter an integer.')
        while True:
            try:
<<<<<<< HEAD
                burst = int(input(f'Enter Burst Time for {pid}: '))
=======
                burst = int(input(f"Enter Burst Time for {pID}: "))
>>>>>>> 49e42a75b35a00e5f7f083abfae25dc557b951e9
                if burst <= 0:
                    print('Burst time must be positive.')
                    continue
                break
            except ValueError:
                print('Invalid input. Please enter an integer.')
        plist.append({'pid': pid, 'arrival': arrival, 'burst': burst})
    return plist

<<<<<<< HEAD
=======
        process_list.append([arrival, burst, pID])
>>>>>>> 49e42a75b35a00e5f7f083abfae25dc557b951e9

def main():
    plist = _read_input()
    gantt, completed, metrics = fcfs(plist)
    print_results(gantt, completed, metrics)


if __name__ == '__main__':
    main()
