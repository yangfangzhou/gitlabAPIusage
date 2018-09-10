#!/usr/bin/python
# -*-coding:utf-8 -*-
from gitlabapi import *

list_argv1 = ['1', '2', '3']
list_argv2 = ['-sg', '-sp', '-su', '-sgi', '-spi', '-sui', '-sgm', '-sgp', '-spm', "cg", "cp", "cu", "tp",
              "cgm", "cpm", "egm", "epm", "rgm", "rpm", "dg", "dp", "du", "bu", "ubu"]

list_argv2_help = {'sg': 'search allgroups   usage: python xxx.py user_right sg',
                   'sp': 'search allprojects    usage: python xxx.py user_right sp', 'su': 'search allusers     usage: python xxx.py user_right su',
                   'sgi': 'search group id    usage: python xxx.py user_right sgi group_name', 'spi': 'search project id    usage: python xxx.py user_right spi project_name',
                   'sui': 'search user id usage: python xxx.py user_right sui user_name', 'sgm': 'search group members usage: python xxx.py user_right sgm group_name',
                   'sgp': 'search group projects    usage: python xxx.py user_right sgp group_name', 'spm': 'search project members    usage: python xxx.py user_right sgm project_name',
                   "cg": 'create group    usage: python xxx.py user_right cg group_name group_path groups_visibility_level',
                   "cp": 'create project    usage: python xxx.py user_right cp project_name project_path project_visibility_level',
                   "cu": 'create user    usage: python xxx.py user_right cu user_name user_username user_email user_password user_can_create_group',
                   "tp": 'transfer project to group    usage: python xxx.py user_right tp group_name project_name',
                   "cgm": 'create group member    usage: python xxx.py user_right cgm group_name user_name access_level', "cpm": 'create project member    usage: python xxx.py user_right cpm project_name user_name access_level',
                   "egm": 'edit group member    usage: python xxx.py user_right egm group_name user_name access_level', "epm": 'edit project member    usage: python xxx.py user_right epm project_name user_name access_level',
                   "rgm": 'remomve group member    usage: python xxx.py user_right rgm group_name user_name', "rpm": 'remove group member    usage: python xxx.py user_right rpm project_name user_name',
                   "dg": 'delete group    usage: python xxx.py user_right dg group_name', "dp": 'delete project    usage: python xxx.py user_right dp project_name', "du": 'delete user     usage: python xxx.py user_right du user_name',
                   "bu": 'block user    usage: python xxx.py user_right bu user_name', "ubu": 'unblock user    usage: python xxx.py user_right ubu user_name'}


list_search_all = ['sg', 'sp', 'su']
list_search_id = ['sgi', 'spi', 'sui']

# 用字典存储发送所需的参数


def dic_for_newGOrP(name, path, visibility_level):
    dic = {}
    dic['name'] = name
    dic['path'] = path
    dic['visibility'] = visibility_level
    return dic


def dic_for_newU(name, username, email, password, can_create_group):
    dic = {}
    dic['name'] = name
    dic['username'] = username
    dic['email'] = email
    dic['password'] = password
    dic['can_create_group'] = can_create_group
    return dic


def dic_for_GmOrPm(user_id, access_level):
    dic = {}
    dic['user_id'] = user_id
    dic['access_level'] = access_level
    return dic

# 获取id并转换成字符串


def getid(right, search_type, search_key):
    arr0 = getListOrId(right, search_type, search_key, "I")
    return bytes(arr0)

    GitlabApi = GitlabApi()
    if sys.argv[2] == "-spm":
        projectSignalId =  GitlabApi.getListOrId([sys.argv[1],"-spi",sys.argv[3]])
        print GitlabApi.getListOrId([sys.argv[1],sys.argv[2],projectSignalId])
    else:
        print GitlabApi.getListOrId(sys.argv[1:])

def argvDef():

    # 判定传入的参数
    if len(sys.argv) < 2:
        print "user -h for usage of %s " % (sys.argv[0])
        sys.exit()

    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("\033[1;34;40m")
        print "nomarlly second parameter is user_right(1 for normalUser;2 for managerUser;3 for Admin),thrid parameter is" + '\n'
        for i in list_argv2_help:
            print i + ":" + list_argv2_help[i] + '\n'
        print "parameter user_username can not use chinese "
        print "parameter user_email need @"
        print "to konw more details , use -h with one of thrid parameter"
        print('\033[0m')
        sys.exit()

    if len(sys.argv) == 3 and sys.argv[1] == "-h":
        if sys.argv[2] in list_argv2_help:
            print list_argv2_help[sys.argv[2]]
            sys.exit()
        else:
            print "user -h for usage of %s " % (sys.argv[0])
            sys.exit()

    if 1 is not list_argv2.count(sys.argv[2]):
        print "second parameter not exists user -h for usage of %s " % (sys.argv[0])
        sys.exit()

    if len(sys.argv) > 2:
        # # 根据命令行参数打印组,项目或人员的列表
        # if list_search_all.count(sys.argv[2]):
        #     arr = getListOrId(sys.argv[1], sys.argv[2], "", "L")
        #     # print("\033[1;34;40m")
        #     return arr
        #     # print('\033[0m')
        #
        # # 根据命令行参数打印组,项目或人员列表中某一项的id
        # if list_search_id.count(sys.argv[2]):
        #     arr = getid(sys.argv[1], sys.argv[2], sys.argv[3])
        #     return arr
        #
        # # 根据命令行参数打印组项目列表,组成员列表或项目成员列表
        # if sys.argv[2] == "sgm" or sys.argv[2] == "sgp":
        #     arr = getListOrId(sys.argv[1], sys.argv[2], getid(
        #         sys.argv[1], "sgi", sys.argv[3]), "L")
        #     return arr
        # if sys.argv[2] == "spm":
        #     arr = getListOrId(sys.argv[1], sys.argv[2], getid(
        #         sys.argv[1], "spi", sys.argv[3]), "L")
        #     return arr


        # 创建新的组,项目或人员
        if sys.argv[2] == "cg":
            postToGitlab(sys.argv[1], "groups", dic_for_newGOrP(
                sys.argv[3], sys.argv[4], sys.argv[5]))
        if sys.argv[2] == "cp":
            postToGitlab(sys.argv[1], "projects", dic_for_newGOrP(
                sys.argv[3], sys.argv[4], sys.argv[5]))
        if sys.argv[2] == "cu":
            postToGitlab(sys.argv[1], "users", dic_for_newU(
                sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]))

        # 移动项目到特定组
        if sys.argv[2] == "tp":
            groups_id = getid(sys.argv[1], "sgi", sys.argv[3])
            project_id = getid(sys.argv[1], "spi", sys.argv[4])
            http_path_one = "groups/" + groups_id + "/projects/" + project_id
            postToGitlab(sys.argv[1], http_path_one, "")

        # 增加组,项目成员
        if sys.argv[2] == "cgm":
            groups_id = getid(sys.argv[1], "sgi", sys.argv[3])
            user_id = getid(sys.argv[1], "sui", sys.argv[4])
            http_path_one = "groups/" + groups_id + "/members"
            postToGitlab(sys.argv[1], http_path_one,
                         dic_for_GmOrPm(user_id, sys.argv[5]))
        if sys.argv[2] == "cpm":
            project_id = getid(sys.argv[1], "spi", sys.argv[3])
            user_id = getid(sys.argv[1], "sui", sys.argv[4])
            http_path_one = "projects/" + project_id + "/members"
            postToGitlab(sys.argv[1], http_path_one,
                         dic_for_GmOrPm(user_id, sys.argv[5]))

        # 编辑组,项目成员
        if sys.argv[2] == "egm":
            groups_id = getid(sys.argv[1], "sgi", sys.argv[3])
            user_id = getid(sys.argv[1], "sui", sys.argv[4])
            http_path_one = "groups/" + groups_id + "/members/" + user_id
            putToGitlab(sys.argv[1], http_path_one,
                        dic_for_GmOrPm(user_id, sys.argv[5]))
        if sys.argv[2] == "epm":
            projects_id = getid(sys.argv[1], "spi", sys.argv[3])
            user_id = getid(sys.argv[1], "sui", sys.argv[4])
            http_path_one = "projects/" + projects_id + "/members/" + user_id
            putToGitlab(sys.argv[1], http_path_one,
                        dic_for_GmOrPm(user_id, sys.argv[5]))

        # 移除组,项目成员
        if sys.argv[2] == "rgm":
            groups_id = getid(sys.argv[1], "sgi", sys.argv[3])
            user_id = getid(sys.argv[1], "sui", sys.argv[4])
            http_path_one = "groups/" + groups_id + "/members/" + user_id
            deleteToGitlab(sys.argv[1], http_path_one, "")
        if sys.argv[2] == "rpm":
            projects_id = getid(sys.argv[1], "spi", sys.argv[3])
            user_id = getid(sys.argv[1], "sui", sys.argv[4])
            http_path_one = "projects/" + projects_id + "/members/" + user_id
            deleteToGitlab(sys.argv[1], http_path_one, "")

        # 删除组,项目或人员
        if sys.argv[2] == "dg":
            groups_id = getid(sys.argv[1], "sgi", sys.argv[3])
            http_path_one = "groups/" + groups_id
            deleteToGitlab(sys.argv[1], http_path_one, "")
        if sys.argv[2] == "dp":
            projects_id = getid(sys.argv[1], "spi", sys.argv[3])
            http_path_one = "projects/" + projects_id
            deleteToGitlab(sys.argv[1], http_path_one, "")
        if sys.argv[2] == "du":
            users_id = getid(sys.argv[1], "sui", sys.argv[3])
            http_path_one = "users/" + users_id
            deleteToGitlab(sys.argv[1], http_path_one, "")

        # 封禁,解禁用户
        if sys.argv[2] == "bu":
            user_id = getid(sys.argv[1], "sui", sys.argv[3])
            http_path_one = "users/" + user_id + "/block"
            putToGitlab(sys.argv[1], http_path_one, "")
        if sys.argv[2] == "ubu":
            user_id = getid(sys.argv[1], "sui", sys.argv[3])
            http_path_one = "users/" + user_id + "/unblock"
            putToGitlab(sys.argv[1], http_path_one, "")


# argvDef()
