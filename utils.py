# Freddy @DC, uWaterloo, ON, Canada
# Nov 16, 2017

def one_hot(x):
    if(x>=0): return 1
    else: return -1


def dataset_printer(object):
    for i in range(len(object)):
        sample = object[i]
        print(i, sample['image'].size(), sample['labels'].size())
        
        if i == 3:break