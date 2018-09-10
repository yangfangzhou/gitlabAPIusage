#!/usr/bin/python
# -*-coding:utf-8 -*-
from gitlabapi import *

# jsonOFArgvReturn = argvDef()
# listOfReturn = json.loads(jsonOFArgvReturn)
GitlabApi = GitlabApi()

def dic_for_newG(name, path, visibility):
    dic = {}
    dic['name'] = name
    dic['path'] = path
    dic['visibility'] = visibility
    return dic

def dic_for_newP(namespace_id, name, visibility):
    dic = {}
    dic['namespace_id'] = namespace_id
    dic['path'] = name
    dic['visibility'] = visibility
    return dic

def dic_for_GmOrPm(user_id, access_level):
    dic = {}
    dic['user_id'] = user_id
    dic['access_level'] = access_level
    return dic

dicOFAccessLevel = {"Guest":"10","Reporter":"20","Developer":"30","Master":"40","Owner":"50"}



# print AccessLevelEnum['Guest'].value
# print AccessLevelEnum(10).name

file_object = open('CreateCustomMadeGroup.json')
try:
    all_the_text = json.loads(file_object.read())
    GitlabApi.postToGitlab(sys.argv[1], "groups",dic_for_newG(all_the_text['group'], all_the_text['groupPath'], all_the_text['group_visibility_level']))

    projectName = all_the_text['project']
    namespace_id = GitlabApi.getListOrId([sys.argv[1], '-sgi', all_the_text['group']])
    for i in projectName:
        GitlabApi.postToGitlab(sys.argv[1], "projects",dic_for_newP(namespace_id,i,projectName[i]))

    groups_id = namespace_id
    userName = all_the_text['user']
    for i in userName:
        user_id = GitlabApi.getListOrId([sys.argv[1], "-sui", i])
        for j in userName[i]:
            # print j, userName[i][j]
            if j == 'group_right':
                http_path_one = "groups/" + str(groups_id) + "/members"
                # print http_path_one
                # print i,user_id
                GitlabApi.postToGitlab(sys.argv[1], http_path_one, dic_for_GmOrPm(user_id, dicOFAccessLevel[userName[i]['group_right']]))
            else:
                pathOfProjects = all_the_text['groupPath'] + "/" + str(j)
                # print pathOfProjects
                projects_id = GitlabApi.getListOrId([sys.argv[1], '-spi', pathOfProjects])
                # print projects_id
                http_path_one = "projects/" + str(projects_id) + "/members"
                # print http_path_one
                # print i,user_id
                GitlabApi.postToGitlab(sys.argv[1], http_path_one, dic_for_GmOrPm(user_id, dicOFAccessLevel[userName[i][j]]))


finally:
    file_object.close()
