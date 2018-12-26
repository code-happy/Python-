# -*- coding:utf-8 -*-
import threading
import time

def Sorry():
    print("亲爱的，对不起")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=Sorry)
        t.start()