from multiprocessing import Process, Queue
import os, time, random


# д���ݽ���ִ�еĴ���:
def write(q):
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

# �����ݽ���ִ�еĴ���:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


if __name__=='__main__':
    # �����̴���Queue�������������ӽ��̣�
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # �����ӽ���pw��д��:
    pw.start()
    # �ȴ�pw����:
    pw.join()
    # �����ӽ���pr����ȡ:
    pr.start()
    pr.join()
    # pr����������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ:
    print('')
    print('�������ݶ�д�벢�Ҷ���')