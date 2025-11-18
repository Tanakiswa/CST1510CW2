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

    for p in processes:
        pid = p['pid']
        arrival = p['arrival']
        burst = p['burst']

        # idle until arrival
        if time < arrival:
            idle_len = arrival - time
            gantt.extend(['Idle'] * idle_len)
            time = arrival

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
            print('Invalid input. Please enter an integer.')

    plist = []
    for i in range(1, n + 1):
        pid = input(f'Enter Process ID for process {i}: ').strip() or f'P{i}'
        while True:
            try:
                arrival = int(input(f'Enter Arrival Time for {pid}: '))
                if arrival < 0:
                    print('Arrival time cannot be negative.')
                    continue
                break
            except ValueError:
                print('Invalid input. Please enter an integer.')
        while True:
            try:
                burst = int(input(f'Enter Burst Time for {pid}: '))
                if burst <= 0:
                    print('Burst time must be positive.')
                    continue
                break
            except ValueError:
                print('Invalid input. Please enter an integer.')
        plist.append({'pid': pid, 'arrival': arrival, 'burst': burst})
    return plist


def main():
    plist = _read_input()
    gantt, completed, metrics = fcfs(plist)
    print_results(gantt, completed, metrics)


if __name__ == '__main__':
    main()
