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
    
    current_time = 0
    self.gantt_chart = []
    self.completed_processes = {}
    
    for process in sorted_processes:  # FIXED: Clean iteration without popping
        pid = process['pid']
        arrival_time = process['arrival_time']
        burst_time = process['burst_time']
        
        # NEW: Handle CPU idle time properly
        if current_time < arrival_time:
            idle_time = arrival_time - current_time
            self.gantt_chart.extend(['Idle'] * idle_time)
            current_time = arrival_time
        
        # NEW: Added response time calculation
        start_time = current_time
        completion_time = current_time + burst_time
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time
        response_time = start_time - arrival_time  

        gantt.extend([pID] * burst_time)  #update gantt chart
        completed[pID] = [arrival_time, burst_time, completion_time, turnaround_time, waiting_time]  #store results for processes

    #print results in table
    print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Start':<10}{'Completion':<12}{'Turnaround':<12}{'Waiting':<10}{'Response':<10}")
    for pID, data in completed.items():
        print(f"{pID:<10}{data[0]:<10}{data[1]:<10}{data[2]:<12}{data[3]:<12}{data[4]:<10}")

    print("\nGantt Chart:")
    # NEW: Gantt chart with timeline
print("+" + "-" * (len(self.gantt_chart) * 4 - 1) + "+")

# Complex formatting to center process IDs in segments
chart_line = "|"
current_process = None
process_count = 0

for i, process in enumerate(self.gantt_chart):
    if process != current_process:
        if current_process is not None:
            spaces_before = (process_count - len(str(current_process))) // 2
            spaces_after = process_count - len(str(current_process)) - spaces_before
            chart_line += " " * spaces_before + str(current_process) + " " * spaces_after + "|"
        current_process = process
        process_count = 1
    else:
        process_count += 1

print(chart_line)
print("+" + "-" * (len(self.gantt_chart) * 4 - 1) + "+")

# NEW: Timeline numbers
timeline = "0"
current_time = 0
for process in self.gantt_chart:
    current_time += 1
    timeline += str(current_time).rjust(4)
print(timeline)

# NEW SECTION FOR SUMMARY OF STATS:
num_processes = len(self.completed_processes)
avg_waiting = self.time_metrics['total_waiting_time'] / num_processes
avg_turnaround = self.time_metrics['total_turnaround_time'] / num_processes
avg_response = self.time_metrics['total_response_time'] / num_processes

print(f"\nSUMMARY STATISTICS:")
print(f"Average Waiting Time:    {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")
print(f"Average Response Time:   {avg_response:.2f}")        # NEW
print(f"CPU Utilization:         {self.time_metrics['cpu_utilization']:.2f}%") 
#execution of the code
if __name__ == '__main__':
    while True:
        try:
            n = int(input("Enter number of processes: "))
            if n <= 0:
                print("Number of processes must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    #user enters process details
    process_list = []
    for i in range(n):
        pid = input(f"Enter Process ID for process {i+1}: ")

        while True:
            try:
                arrival = int(input(f"Enter Arrival Time for {pid}: "))
                if arrival < 0:
                    print("Arrival time cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                burst = int(input(f"Enter Burst Time for {pid}: "))
                if burst <= 0:
                    print("Burst time must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        process_list.append([arrival, burst, pid])

    fcfs(process_list)  #calls on function and runs it

# NEW Analysis
def generate_analysis_report(self):
    max_waiting_process = max(self.completed_processes.items(), 
                            key=lambda x: x[1]['waiting_time'])
    
    report = f"""
FCFS SCHEDULING ANALYSIS REPORT
{'=' * 40}

Performance Metrics:
- Average Waiting Time:    {avg_waiting:.2f} units
- Average Turnaround Time: {avg_turnaround:.2f} units
- CPU Utilization:         {self.time_metrics['cpu_utilization']:.2f}%
