import sys
import os
import time

def generate_trace(length):
    with open('trace.txt', 'w') as f:
        for i in range(0, length):
            f.write('ready_wh' + '\n')
            f.write('ready_ag' + '\n')
            f.write('left_wh' + '\n')
            f.write('move_to_A_ag' + '\n')
            f.write('set_turning_rad_1_wh' + '\n')
            f.write('right_ag' + '\n')
            f.write('set_wheels_speed_wh' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('stop_wh' + '\n')
            f.write('forward_ag' + '\n')
            f.write('set_wheels_speed_0_wh' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('wait_wh' + '\n')
            f.write('move_to_B_ag' + '\n')
            f.write('act_success_wh' + '\n')
            f.write('left_ag' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('forward_ag' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('move_to_C_ag' + '\n')
            f.write('left_ag' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('forward_ag' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('forward_ag' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('right_ag' + '\n')
            f.write('act_success_ag' + '\n')
            f.write('backward_ag' + '\n')
            f.write('act_success_ag' + '\n')

def main(argv):
    min = int(argv[1])
    max = int(argv[2])
    step = int(argv[3])
    reps = int(argv[4])
    n_models = int(argv[5])
    property = '\'(G(forward_wh->(!stop_wh U set_wheels_speed_0_wh))) & (G(move_to_A_ag->(!action_fail_ag U move_to_B_ag)))\''
    models = ''
    for i in range(0, n_models):
        models = models + './models/wheels.hoa ./models/agent.hoa '
    t = str(time.time())
    f = open('res' + t + '.csv', 'w')
    f.close()
    for i in range(min, max, step):
        generate_trace(i)
        standard_time_gen = 0
        standard_time_ver = 0
        for j in range(0, reps):
            res = os.popen('python3 monitor.py {phi} trace.txt --models {m}'.format(phi=property, m=models)).read()
            standard_time_gen = standard_time_gen + float(res.split(';')[0])
            standard_time_ver = standard_time_ver + float(res.split(';')[1])
        standard_time_gen = standard_time_gen / reps
        standard_time_ver = standard_time_ver / reps
        single_time_gen = 0
        single_time_ver = 0
        for j in range(0, reps):
            res = os.popen('python3 monitor.py {phi} trace.txt --models {m} --single'.format(phi=property, m=models)).read()
            single_time_gen = single_time_gen + float(res.split(';')[0])
            single_time_ver = single_time_ver + float(res.split(';')[1])
        single_time_gen = single_time_gen / reps
        single_time_ver = single_time_ver / reps
        multi_time_gen = 0
        multi_time_ver = 0
        for j in range(0, reps):
            res = os.popen('python3 monitor.py {phi} trace.txt --models {m} --multi'.format(phi=property, m=models)).read()
            multi_time_gen = multi_time_gen + float(res.split(';')[0])
            multi_time_ver = multi_time_ver + float(res.split(';')[1])
        multi_time_gen = multi_time_gen / reps
        multi_time_ver = multi_time_ver / reps
        with open('res' + t + '.csv', 'a') as f:
            f.write(str(i*30) + ';' + str(standard_time_gen).replace('.', ',') + ';' + str(standard_time_ver).replace('.', ',') + ';' + str(single_time_gen).replace('.', ',') + ';' +  str(single_time_ver).replace('.', ',') + ';' + str(multi_time_gen).replace('.', ',') + ';' + str(multi_time_ver).replace('.', ',') + '\n')
if __name__ == '__main__':
    main(sys.argv)
