"""Simple non-preemptive SJF scheduler.

Process representation: list of dicts with keys 'pid','arrival','burst'.
"""
"""Simple non-preemptive SJF scheduler.

Process representation: list of dicts with keys 'pid','arrival','burst'.
"""

def sjf(process_list):
    # copy and sort by arrival for deterministic behavior
    processes = sorted(process_list, key=lambda p: p['arrival'])
    time = 0
    gantt = []
    completed = {}

    remaining = processes.copy()

    while remaining:
        # find available processes
        available = [p for p in remaining if p['arrival'] <= time]
        if not available:
            # CPU idle one unit
            gantt.append('Idle')
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

        gantt.extend([pid] * burst)

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

    total_time = len(gantt) if gantt else 0
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

    plist = []
    for i in range(1, n + 1):
        pid = input(f'Enter Process ID for process {i}: ').strip() or f'P{i}'
        while True:
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
        print(' | '.join(gantt))
    else:
        print('(no timeline)')

    print('\nSUMMARY:')
    print(f"Average Waiting Time:    {metrics['avg_waiting']:.2f}")
    print(f"Average Turnaround Time: {metrics['avg_turnaround']:.2f}")
    print(f"Average Response Time:   {metrics['avg_response']:.2f}")
    print(f"CPU Utilization:         {metrics['cpu_utilization']:.2f}%")


def main():
    plist = _read_input()
    gantt, completed, metrics = sjf(plist)
    print_results(gantt, completed, metrics)


if __name__ == '__main__':
    main()