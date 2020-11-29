#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    @Author mantou
    @Date 2020/8/31 19:19
    @Describe 
"""
import sys


class Node():
    def __init__(self,id=None,name=None,tickeName=None):
        self.id = id
        self.name = name
        self.tickeName = tickeName
        self.pre = None
        self.next = None

class testNode():
    def __init__(self,maxLength=10):
        self.node = Node()
        self.length = 0
        self.maxLength = maxLength

    def _isEmpty(self):
        return True if self.length == 0 else False

    def _isFull(self):
        return True if self.length == self.maxLength else False

    def hasNode(self,node):
        tmpPreNode = self.node.pre
        tmpNextNode = self.node.next
        count = 0
        while count == self.length:
            if(self.node.name == node.name or
                tmpPreNode.name == node.name or
                tmpNextNode.name == node.name
              ):
                print("已存在叫%s的节点"%node.name)
                return True
            tmpNextNode = tmpNextNode.pre
            tmpNextNode = tmpNextNode.next
            count+=1
        return  False


    def appendNode(self,node):
        if self._isFull():
            print("链表已满")
            return

        if self.hasNode(node):
            return
        tmpNode = None
        for i in range(self.maxLength):
            if node.id










