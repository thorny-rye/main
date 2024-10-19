import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as n:
        for line in n:
            line = n.readline()
            all_data.append(line)


filenames = [f'./file/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)


#    start = datetime.datetime.now()
#    for file in filenames:
#        read_info(file)
#    end = datetime.datetime.now()
#    print(end - start)
