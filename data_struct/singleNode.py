#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    @Author mantou
    @Date 2020/8/17 20:29
    @Describe 
"""

class heroNode:
    def __init__(self,id,name,nickName):
        self.id = id
        self.name = name
        self.nickname = nickName
        self.nextNode = None

    def insertNOde(self,newNode: heroNode ):
        tempNode = self
        flag = True
        while True:
           if tempNode.nextNode == None:
              print("链表到头了")
              break
           elif tempNode.nextNode.id == newNode.id:
               flag = False
               break
           elif tempNode.nextNode.id > newNode.id:
               break
           tempNode = tempNode.nextNode

        if not flag:
            print("已存入id=%d的节点"%newNode.id)
        else:
            newNode.nextNode = tempNode.nextNode.nextNode
            tempNode.nextNode = newNode

    def showNode(self):
        tempNode = self
        while tempNode.nextNode != None:
            print("%d\t%s\t%s\n"%(tempNode.id,tempNode.name,tempNode.nickname))
            tempNode = tempNode.nextNode

if __name__ == '__main__':
    node1 = heroNode(1,"汪雯倩","豹子头")
    node2 = heroNode(2,"王小琴","花和尚")
    node3 = heroNode(3,"马丹丹","行者")
    node1.insertNOde(node2)
    node1.insertNOde(node3)
    node1.showNode()



