LIST = [0, 1, 3]
def loop(loop_num_times):
    to_return = []
    for j in range(loop_num_times):
        for i in range(len(LIST)):
            to_return = to_return + [LIST[i]]
    return to_return    
    
print(loop(5))