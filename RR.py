"""Round Robin scheduling implementation and simple CLI runner.

This module exposes `round_robin(burst, quantum, arrival=None)` which returns
completion, turnaround and waiting times and their averages.
"""

from collections import deque
from typing import List, Optional, Dict, Tuple


def round_robin(burst: List[int], quantum: int, arrival: Optional[List[int]] = None) -> Dict[str, List[int]]:
    """Simulate Round Robin scheduling.

    Args:
        burst: list of burst times (integers) for each process.
        quantum: time quantum (must be > 0).
        arrival: optional list of arrival times (default all zeros).

    Returns:
        A dict with keys: 'completion_times', 'turnaround_times', 'waiting_times',
        'avg_waiting_time', 'avg_turnaround_time', 'execution_log'.
    """
    if quantum <= 0:
        raise ValueError("Time quantum must be > 0")

    n = len(burst)
    if arrival is None:
        arrival = [0] * n
    if len(arrival) != n:
        raise ValueError("arrival list must have same length as burst list")

    remaining = burst.copy()
    completion = [0] * n
    turnaround = [0] * n
    waiting = [0] * n

    time = 0
    ready = deque()

    # Order processes by arrival time so we can add them to ready queue as time advances
    arrival_order = sorted(range(n), key=lambda i: arrival[i])
    idx = 0

    # Seed ready queue with any processes that have arrived at time 0 (or current time)
    while idx < n and arrival[arrival_order[idx]] <= time:
        ready.append(arrival_order[idx])
        idx += 1

    # If nothing has arrived yet, jump time to first arrival
    if not ready and idx < n:
        time = arrival[arrival_order[idx]]
        ready.append(arrival_order[idx])
        idx += 1

    # execution log: list of (pid_index, start_time, end_time)
    execution_log = []

    while ready:
        i = ready.popleft()

        # Execute process i for up to `quantum` or remaining time
        exec_time = min(quantum, remaining[i])
        start_time = time
        time += exec_time
        remaining[i] -= exec_time

        # record execution interval
        execution_log.append((i, start_time, time))

        # Add any processes that arrived while we executed
        while idx < n and arrival[arrival_order[idx]] <= time:
            ready.append(arrival_order[idx])
            idx += 1

        if remaining[i] > 0:
            # Process not finished — requeue it
            ready.append(i)
        else:
            # Process finished
            completion[i] = time
            turnaround[i] = completion[i] - arrival[i]
            waiting[i] = turnaround[i] - burst[i]

    avg_wait = sum(waiting) / n if n else 0
    avg_turnaround = sum(turnaround) / n if n else 0

    return {
        "completion_times": completion,
        "turnaround_times": turnaround,
        "waiting_times": waiting,
        "avg_waiting_time": avg_wait,
        "avg_turnaround_time": avg_turnaround,
        "execution_log": execution_log,
    }


def print_results(burst: List[int], arrival: List[int], results: Dict[str, List[int]]) -> None:
    n = len(burst)
    print("\nProcess ID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(f"P{i+1}\t\t{arrival[i]}\t{burst[i]}\t{results['completion_times'][i]}\t\t{results['turnaround_times'][i]}\t\t{results['waiting_times'][i]}")
    print(f"\nAverage Waiting Time: {results['avg_waiting_time']:.2f}")
    print(f"Average Turnaround Time: {results['avg_turnaround_time']:.2f}")


def plot_gantt(execution_log: List[tuple], burst: List[int], arrival: Optional[List[int]] = None, filename: Optional[str] = None) -> None:
    """Plot a simple Gantt chart from an execution log.

    execution_log: list of (pid_index, start_time, end_time)
    If `filename` is provided the plot will be saved to that path; otherwise it will be shown.
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except Exception:
        print("matplotlib is required to generate Gantt charts. Install it with: pip install matplotlib")
        return

    n = max((pid for pid, s, e in execution_log), default=-1) + 1
    if arrival is None:
        arrival = [0] * n

    fig, ax = plt.subplots(figsize=(8, max(2, n * 0.5)))

    # For each process, plot horizontal bars for each of its execution segments
    colors = plt.cm.tab20.colors
    for pid in range(n):
        segments = [(s, e) for p, s, e in execution_log if p == pid]
        for (s, e) in segments:
            ax.barh(pid, e - s, left=s, height=0.4, color=colors[pid % len(colors)], edgecolor='k')

    ax.set_yticks(range(n))
    ax.set_yticklabels([f"P{i+1}" for i in range(n)])
    ax.set_xlabel("Time")
    ax.set_ylabel("Process")
    ax.set_title("Round Robin Gantt Chart")
    ax.grid(axis='x', linestyle='--', alpha=0.4)

    # Legend showing burst times
    patches = [mpatches.Patch(color=colors[i % len(colors)], label=f"P{i+1} (burst={burst[i]})") for i in range(n)]
    ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    if filename:
        plt.savefig(filename)
        print(f"Gantt chart saved to {filename}")
    else:
        plt.show()


def _parse_input() -> Tuple[List[int], List[int], int]:
    n = int(input("Enter the number of processes: "))
    burst = []
    arrival = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process {i+1}: "))
        at_input = input(f"Enter Arrival Time for Process {i+1} (default 0): ").strip()
        at = int(at_input) if at_input else 0
        burst.append(bt)
        arrival.append(at)
    quantum = int(input("Enter Time Quantum: "))
    return burst, arrival, quantum


if __name__ == "__main__":
    try:
        burst_list, arrival_list, tq = _parse_input()
        res = round_robin(burst_list, tq, arrival_list)
        print_results(burst_list, arrival_list, res)
    except Exception as e:
        print("Error:", e)

