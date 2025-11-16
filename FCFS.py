 #First Come First Serve CPU scheduling alogorithm
 #function to define process list
def fcfs(process_list):
    process_list.sort(key=lambda x: x[0])  #sort process by arrival time

    t = 0
    gantt = []
    completed = {}

    #while loop that runs until are processes are executed
    while process_list:
        available = [p for p in process_list if p[0] <= t]
        process = process_list.pop()
        #if no process available then CPU is idle
        if not available:
            gantt.append("Idle")
            t += 1
            continue
        #pick first available process and remove it from list
        process = available[0]
        process_list.remove(process)

        #calculate times
        arrival_time, burst_time, pID = process
        start_time = t
        t += burst_time
        completion_time = t
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time

        gantt.extend([pID] * burst_time)  #update gantt chart
        completed[pID] = [arrival_time, burst_time, completion_time, turnaround_time, waiting_time]  #store results for processes

    #print results in table
    print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<12}{'Turnaround':<12}{'Waiting':<10}")
    for pID, data in completed.items():
        print(f"{pID:<10}{data[0]:<10}{data[1]:<10}{data[2]:<12}{data[3]:<12}{data[4]:<10}")

    print("\nGantt Chart:")
    print(" | ".join(gantt))

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
