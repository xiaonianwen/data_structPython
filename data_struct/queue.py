#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    @Author mantou
    @Date 2020/8/12 20:23
    @Describe 
"""
class Mqueue:
    def __init__(self,maxLength):
        self.maxLength = maxLength
        self.head = -1
        self.end = -1

    def init_queue(self):
        self.q = []

    def add(self,data):
        if(len(self.q) > self.maxLength):
            print("队列已满")
        else:
            self.end+=1
            self.q.append(data)


    def get_one(self):
        if(self.end == self.head):
            print("队列已空")
            exit(-1)
        else:
            val = self.q[self.head]
            self.head+=1
            return val

    def show_queue(self):
        if(self.end == self.head):
            print("队列已空")
            exit(-1)
        for d in self.q[self.head:self.end+1]:
            print("{}\t".format(d))

if __name__ == '__main__':
    qu = Mqueue(5)
    qu.init_queue()
    qu.add(1)
    qu.add(3)
    # qu.show_queue()
    qu.add(5)
    print qu.get_one()
    print qu.get_one()
    print qu.get_one()
    print qu.get_one()
