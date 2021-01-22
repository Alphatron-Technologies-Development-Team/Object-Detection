import project_file as pf
import real_time as rt
user_input = int(input('Press 1 for single image testing\nPress 2 for Real Time Testing'))
if user_input == 1:
    pf.Object_Detection()
elif user_input == 2:
    rt.Object_Detection_RealTime()
