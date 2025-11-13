#function to define process lists
def fcfs (process_list):
    t = 0
    gantt = [] #empty gantt
    completed = {} #empty dictionary
    process_list.sort()
    #while loop that runs until process list is emtpy
    while process_list != []:
        if process_list in completed > t:
            t += 1
            gantt.append("Idle") #shows that CPU is idle because no process is being executed
            continue
        else:
        process = process_list.pop()
        gantt.append(process[2])
        t += 1 process[1]
        pID = process[0] #process ID
        ct = t #completion time
        tt = ct - process[1] #turnaround time
        wt = tt - process[1] #waiting time
        completed[pID] = [ct, tt,wt]
        print (gantt)
        print (completed)

if __name__ == '__main__':
    process_list = []
    fcfs(process_list)


