Task = input ("Enter your task: ")
Priority = input ("Priortiy (high/medium/low): ")
Time_bound = input ("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print (f"Reminder: {task} is a {priority} priority task that requires immediate attention today.")
        else:
            print (f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print (f"Reminder: {task} is a {priority} priority task that requires immediate attention today.")
        else:
            print (f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print (f"Reminder: {task} is a {priority} priority task that requires immediate attention today.")
        else:
            print (f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
            
            

