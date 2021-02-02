import argparse
import os
import random
from random import seed
from random import randint

match_list = []
unmatch_list = []
class_list = []

def generate_match_list(input_path):
    for folder in os.listdir(input_path):
        nList = os.listdir(os.path.join(input_path, folder))
        random.shuffle(nList)

        for i in range(len(nList)):
            if i < len(nList) - 1:
                match_list.append(os.path.join(folder, nList[i]) + " " + os.path.join(folder, nList[i + 1]) + " " + str(1))
                    
    return match_list

def generate_class_list(input_path):
    for folder in os.listdir(input_path):
        lks = [os.path.join(folder, j) for j in os.listdir(os.path.join(input_path, folder))]
        class_list.append(lks)
    return class_list

def generate_unmatch_list(sequence, class_list):
    for indx in range(sequence):
        k_ = []
        for index, l in enumerate(class_list):
            nList = class_list[index]
            if len(nList) > 1:
                randomNum = randint(1, len(nList)) - 1
                k_.append(nList[randomNum])
                class_list[index].remove(nList[randomNum])

        random.shuffle(k_)
        if len(k_) > 1:
            for i in range(len(k_)):
                if i < len(k_) - 1:
                    unmatch_list.append(k_[i] + " " + k_[i+1] + " " + str(0))
                    
    jj = [val[0] for val in class_list]
    for i in range(len(jj)):
        if i < len(jj) - 1:
            unmatch_list.append(jj[i] + " " + jj[i+1] + " " + str(0))
            
    return unmatch_list

def main(args):
    input_path = args.input_path
    output_path = args.output_path
    sequence = int(args.sequence)
    

    match_list = generate_match_list(input_path)
    class_list = generate_class_list(input_path)
    unmatch_list = generate_unmatch_list(sequence, class_list)
    newList = unmatch_list + match_list
    random.shuffle(newList)

    file1 = open(output_path,"w")
    for i in newList:
        file1.write(str(i) + "\n")
    file1.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', help='Input path', default="in", type=str)                                     # input                                               # 234
    parser.add_argument('--output_path', help='Output text file', default='out', type=str)                             # output
    parser.add_argument('--sequence', help='Sequence', default='20', type=str)                                         # sequence
    
    main(parser.parse_args())

# python generate_test_pair.py --input_path dataset/lfw-align-128 --output_path test_pair.txt