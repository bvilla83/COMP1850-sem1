# Week 1.2, Session 2: Task 6
# Week 1.2, Session 2: Task 6

machine_temp = int(input("Enter machine temperature in °C: "))
machine_pressure = int(input("Enter machine pressure in PSI: "))
machine_status = int(input("Enter operating status (1/0): "))

if (machine_status == 0):
    print("Machine is off.")
else:
    if (machine_temp > 80): print("Temperature is too high, shut down machine.")
    elif (50 <= machine_temp <= 80): print("Temperature is stable.")
    else: print("Temperature is low.") 

    if (machine_pressure > 100): print("Pressure is too high, shut down machine.")
    elif (70 <= machine_pressure <= 100): print("Pressure is stable.")
    else: print("Pressure is low.")

    if (machine_pressure <= 100 and machine_temp <= 80): print("Machine is running normally.")