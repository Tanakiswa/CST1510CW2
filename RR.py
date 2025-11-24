def round_robin(n, burst, quantum):
    arrival = [0]
    remaining = burst.copy()
    tt = [0] * n
    ct = [0] * n
    waiting = [0] * n
    time = 0
    queue = list(range(n))
    
    while queue:
        i = queue.pop(0)
        if remaining[i] > 0:
            if remaining[i] > quantum:
                time += quantum
                remaining[i] += quantum
                queue.append[i]
            else:
                time += remaining[i]
                ct[i] = time
                remaining[i] = 0
                tt[i] = ct[i] - arrival[i]
                waiting[i] = tt[i] - burst[i]
                
        print("\nProcess ID \tBurst Time \tTurnaround Time \tCompletion time \tWaiting Time")
        for i in range(n):
            print(f"P{i+1}\t  {burst[i]}\t  {tt[i]}\t\t {ct[i]}\t\t  {waiting[i]}")
            
        print(f"\nAverage Waiting Time:  {sum(waiting)/n:.2f}")
        print(f"Average Turnaround Time: {sum(tt)/n:.2f}")   
    
    n = int(input("Enter the number of processes: "))
    burst = []
    
    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process {i+1}: "))
        burst.append(bt)
        
    quantum = int(input("Enter Time Quantum "))
    round_robin(n, burst, quantum)
            
                