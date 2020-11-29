#coding=utf-8

import argparse
import requests
import sys


# r1 = requests.get(url='http://bigdata-002:50070/webhdfs/v1/temp/test', params={'op':'GETFILESTATUS'})
# print(r1.json())
class hdfsNode():
    def __init__(self, owner, modificationTime, type, length,childrenNum,pathSuffix,childrenNode=None,left=None,right=None):
        self.owner = owner
        self.modificationTime = modificationTime
        self.type = type
        self.length = length
        self.chldrenNum = childrenNum
        self.pathSuffix = pathSuffix
        self.childrenNode = childrenNode
        self.left = left
        self.right = right

    def Nprint(self,path):
        str_format="""
                      路径   :{path}
                      大小   :{length}
                      类别   :{type}
                      更新时间:{time}"""
        print(str_format.format(
            path  =path,
            length=self.length,
            type  =self.type,
            time  =self.modificationTime
        ))
class hdfsTree():

    def __init__(self,root=None):
        self.root = root

    def isEmpty(self):
        return self.root == None

    def lengthTree(self):
        if self.isEmpty():
            return 0

    def insert(self,node:hdfsNode):
        """

        :type node: hdfsNode
        """
        if self.isEmpty():
            self.root = node
            return

        hn = self.root
        while True:
            if node.length <= hn.length:
                if hn.left == None:
                    hn.left = node
                    return
                else:
                    hn = hn.left
            else:
                if hn.right == None:
                    hn.right = node
                    return
                else:
                    hn = hn.right


def get_responeJson(path,type):
    get_url = url.format(path=path,type=type)
    respone = requests.get(get_url)
    if respone.status_code != 200:
        respone.raise_for_status()
    return respone.json()



def get_all_dict(path,root_tree:hdfsTree):
    base_res = get_responeJson(path,LISTSTATUS)
    for item in base_res["FileStatuses"]["FileStatus"]:
        owner            = item["owner"]
        modificationTime = item["modificationTime"]
        type             = item["type"]
        length           = item["length"]
        chldrenNum       = item["childrenNum"]
        pathSuffix       = item["pathSuffix"]

        if parse.r == False : #不递归调用
            hdfsnode = hdfsNode(owner,modificationTime,type,length,chldrenNum,pathSuffix)
            root_tree.insert(hdfsnode)
            res_dict["%s/%s"%(path,pathSuffix)] = hdfsnode
        elif parse.r and type == "FILE": #递归查询，只返回文件
            hdfsnode = hdfsNode(owner,modificationTime,type,length,chldrenNum,pathSuffix)
            root_tree.insert(hdfsnode)
            res_dict["%s/%s"%(path,pathSuffix)] = hdfsnode
        else:
            hdfsnode = hdfsNode(owner,modificationTime,type,length,chldrenNum,pathSuffix)
            hdfsnode.childrenNode = hdfsTree()
            root_tree.insert(hdfsnode)
            get_all_dict("%s/%s"%(path,pathSuffix),hdfsnode.childrenNode)



def main():
    root = hdfsTree()
    path = parse.d
    get_all_dict(path,root)
    for k,v in res_dict.items():
        file_path = k
        v.Nprint(file_path)

res_dict = {}
root_hdfs = hdfsTree()
LISTSTATUS    = "LISTSTATUS"
GETFILESTATUS = "GETFILESTATUS"
url="http://bigdata-002:50070/webhdfs/v1{path}?op={type}"
count=0
parser = argparse.ArgumentParser()
parser.add_argument("-d",help="指定检查目录，默认为/",default="/")
parser.add_argument("-r",help="是否递归检查，默认为falase",nargs='?',type=bool,const=True,default=False,choices=[True,False])
parse = parser.parse_args()
#去掉用户输入的路径最后一个"/"
parse.d = parse.d if parse.d == "/" else parse.d.rstrip("/")

if __name__ == '__main__':

   main()
   print(parse)





