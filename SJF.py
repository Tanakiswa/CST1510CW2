def sjf(process_list):
    t = 0
    gantt = []
    completed ={}

    while process_list != []:
        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)
        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available.sort()
            process = available[0]
            burst_time = process[0]
            pID = process[2]
            arrival_time = process[1]
            t += burst_time
            gantt.append(pID)
            ct = t
            tt = ct - arrival_time
            wt = tt - burst_time
            process_list.remove(process)
            completed[pID] = [ct, tt, wt]
    print(gantt)
    print(completed)

if __name__ == "__main__":
    process_list=[]
    sjf(process_list)