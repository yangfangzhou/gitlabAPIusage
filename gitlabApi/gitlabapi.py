#!/usr/bin/python
# -*-coding:utf-8 -*-
import json
import sys
from utils import *
from enum import Enum
reload(sys)
sys.setdefaultencoding('utf-8')


tokenNogroup = "WXqqs33SsYkffMxGPZUd"
# token_nogroup = "eEYKpmF3udKVg2PYBs7X"
tokenGroup = "RvMxg_eraVyqkwCt4hw_"
tokenAdmin = "zLRmx2cR5xriFpjZcs95"
apiPath = "http://gitlabyang.autoio.org/api/v3/"
# apiPath = "https://gitlab.autoio.org/api/v3/"

def tokenRightFunc(tokenRight):
    if tokenRight == "-normal":
        tokenValue = tokenNogroup
    elif tokenRight == "-manager":
        tokenValue = tokenGroup
    elif tokenRight == "-admin":
        tokenValue = tokenAdmin
    return tokenValue

listReturnStr = ['-sg','-sp','-su','-sgm','-sgp','-spm']
listReturnSingleStr = ['-sgm','-sgp','-spm']
listReturnId = ['-sui','-spi','-sgi']

class AccessLevelEnum(Enum):
    Guest = 10
    Reporter = 20
    Developer = 30
    Master = 40
    Owner = 50


class GitlabApi:
    def __init__(self):
        pass

    list_search_groups = ['sg', 'sgi', 'sgm']
    list_search_projects = ['sp', 'spi', 'spm']
    list_search_users = ['su', 'sui']



    def searchIdResult(self,qDic,keyName,itemId):
        for i in qDic:
            if i[keyName] == itemId.decode("utf-8"):
                return i["id"]
    def searchResult(self,qDic):
            return json.dumps(qDic, sort_keys=True, indent=2)


    def createHttpPath(self,searchType,search_id):
        firstPathParm = searchType
        if firstPathParm == "-sg":
            httpPath = "groups"
            listOrId = "-L"
        elif firstPathParm == "-sp":
            httpPath = "projects"
            listOrId = "-L"
        elif firstPathParm == "-su":
            httpPath = "users"
            listOrId = "-L"
        elif firstPathParm == "-sgp":
            httpPath = "groups/" + str(search_id) + "/projects"
            listOrId = "-L"
        elif firstPathParm == "-sgm":
            httpPath = "groups/" + str(search_id) + "/members"
            listOrId = "-L"
        elif firstPathParm == "-spm":
            httpPath = "projects/" + str(search_id) + "/members"
            listOrId = "-L"
        return httpPath,listOrId

    def createIdHttpPath(self,searchType,itemId):
        firstPathParm = searchType
        if firstPathParm == "-sgi":
            httpPath = "groups"
            listOrId = "-I"
            keyName = "name"
            itemId = itemId
        elif firstPathParm == "-spi":
            httpPath = "projects"
            listOrId = "-I"
            keyName = "path_with_namespace"
            itemId = itemId
        elif firstPathParm == "-sui":
            httpPath = "users"
            listOrId = "-I"
            keyName = "username"
            itemId = itemId
        return httpPath,listOrId,keyName,itemId


    # get获取列表或id
    def getListOrId(self,*args):
        httpHelper = HttpHelper()
        httpPathFront = ""
        for value in args:
            personRight = tokenRightFunc(value[0])
            searchType = value[1]
            if listReturnStr.count(searchType):
                if listReturnSingleStr.count(searchType):
                    httpPathresult = self.createHttpPath(searchType,value[2])
                else:
                    httpPathresult = self.createHttpPath(searchType,"")
                httpPathFront =  httpPathresult[0]
                listOrId =  httpPathresult[1]
            elif listReturnId.count(searchType):
                httpPathresult = self.createIdHttpPath(searchType,value[2])
                httpPathFront =  httpPathresult[0]
                listOrId =  httpPathresult[1]
                keyName = httpPathresult[2]
                itemId = httpPathresult[3]
            urlGetPath = apiPath + httpPathFront + "?per_page=999&private_token=" + personRight
            res = json.loads(httpHelper.url(url=urlGetPath).get())
            if listOrId == "-L":
                return self.searchResult(res)
            elif listOrId == "-I":
                return self.searchIdResult(res,keyName,itemId)

#
# GitlabApi = GitlabApi()
# print GitlabApi.getListOrId(sys.argv[1:])
# if sys.argv[2] == "-spm":
#     projectSignalId =  GitlabApi.getListOrId([sys.argv[1],"-spi",sys.argv[3]])
#     print GitlabApi.getListOrId([sys.argv[1],sys.argv[2],projectSignalId])
# else:


    # post数据到gitlab


    def postToGitlab(self,token_right, http_path, parameters):
        httpHelper = HttpHelper()

        url_post_invite_one = apiPath + http_path + "?per_page=999&private_token=" + tokenRightFunc(token_right)
    	# print url_post_invite_one

        post_data_invite = parameters
        # print parameters
        post_data_invite_one = urllib.urlencode(post_data_invite)

        httpHelper.url(url_post_invite_one).post(post_data_invite_one)

    # put数据到gitlab


    def putToGitlab(self,token_right, http_path, parameters):
        httpHelper = HttpHelper()

        url_put_invite_one = apiPath + http_path + "?per_page=999&private_token=" + tokenRightFunc(token_right)
        put_data_invite = parameters
        put_data_invite_one = urllib.urlencode(put_data_invite)

        httpHelper.url(url_put_invite_one).put(put_data_invite_one)

    # delete数据到gitlab


    def deleteToGitlab(self,token_right, http_path, parameters):
        httpHelper = HttpHelper()

        url_delete_invite_one = apiPath + http_path + "?per_page=999&private_token=" + tokenRightFunc(token_right)
        delete_data_invite = parameters
        delete_data_invite_one = urllib.urlencode(delete_data_invite)

        httpHelper.url(url_delete_invite_one).delete(delete_data_invite_one)
