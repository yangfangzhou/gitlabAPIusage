#!/usr/bin/python
# -*-coding:utf-8 -*-
from gitlabapi import *

# jsonOFArgvReturn = argvDef1()

GitlabApi = GitlabApi()
if sys.argv[2] == "-spm":
    projectSignalId =  GitlabApi.getListOrId([sys.argv[1],"-spi",sys.argv[3]])
    jsonOFArgvReturn = GitlabApi.getListOrId([sys.argv[1],sys.argv[2],projectSignalId])
else:
    jsonOFArgvReturn = GitlabApi.getListOrId(sys.argv[1:])
listOfReturn = json.loads(jsonOFArgvReturn)

if sys.argv[2] == "-su":
    listOfReturn.sort(key=lambda x: x["username"])
    print("\033[1;34;40m")
    if sys.argv[1] != "-admin":
        print format(' ', "<5") + format('username', "<20")
        print ""
        for i in range(len(listOfReturn)):
            print format(' ', "<5") + format(listOfReturn[i]['username'], "<20")
    else:
        print format(' ', "<5") + format('username', "<20") + format('can_create_group', "<20") + format('can_create_project', "<20") + format('projects_limit', "<20") + format('organization', "<20")
        print ""
        for i in range(len(listOfReturn)):
            can_create_group = "true" if listOfReturn[i]['can_create_group'] else "false"
            can_create_project = "true" if listOfReturn[i]['can_create_project'] else "false"
            print format(' ', "<5") + format(listOfReturn[i]['username'], "<20") + format(can_create_group, "<20") + format(can_create_project, "<20") + format(listOfReturn[i]['projects_limit'], "<20") + format(listOfReturn[i]['organization'], "<20")
    # print jsonOFArgvReturn
    print('\033[0m')
elif sys.argv[2] == "-sp":
    listOfReturn.sort(key=lambda x: x["path_with_namespace"])
    for i in range(len(listOfReturn)):
        projectMembers = json.loads(GitlabApi.getListOrId([sys.argv[1], "-spm", GitlabApi.getListOrId([
            sys.argv[1], "-spi", listOfReturn[i]['path_with_namespace']])]))
        visibility_level = "NotPrivate" if listOfReturn[i]['visibility_level'] else "Private"
        print("\033[1;37;40m")
        print 'namespace_kind: ' + listOfReturn[i]['namespace']['kind']
        print 'path_with_namespace: ' + listOfReturn[i]['path_with_namespace']
        print 'Project_visibility_level: ' + visibility_level
        print("\033[0m")
        if len(sys.argv) > 3:
            if sys.argv[3] == "-a":
                print ''
                print ''
                print format(' ', "<5") + format('\033[1;37;40mProjectUsers\033[0m', "<54") + format('\033[1;37;40mUsers_access_level\033[0m', "<20")
                for k in range(len(projectMembers)):
                    projectMembers_access_level = AccessLevelEnum(projectMembers[k]['access_level']).name
                    print format(' ', "<5") + format(projectMembers[k]['username'], "<40") + format(projectMembers_access_level, "<20")
    # print jsonOFArgvReturn
        print "_________________________________________________________________________________________________________________________________________________"
elif sys.argv[2] == "-sg":
    listOfReturn.sort(key=lambda x: x["name"])

    for i in range(len(listOfReturn)):
        groupProjects = json.loads(GitlabApi.getListOrId([sys.argv[1], "-sgp", GitlabApi.getListOrId([
            sys.argv[1], "-sgi", listOfReturn[i]['name']])]))
        groupMembers = json.loads(GitlabApi.getListOrId([sys.argv[1], "-sgm", GitlabApi.getListOrId([
            sys.argv[1], "-sgi", listOfReturn[i]['name']])]))
        visibility_level = "NotPrivate" if listOfReturn[i]['visibility_level'] else "Private"
        print("\033[1;37;40m")
        print 'Group_name:' + listOfReturn[i]['name']
        print 'Group_visibility_level:' + visibility_level
        print("\033[0m")
        if len(sys.argv) > 3:
            if sys.argv[3] == "-a":
                print ''
                print ''
                print format(' ', "<5") + format('\033[1;37;40mgroupProjects\033[0m', "<54") + format('\033[1;37;40mgroupProjects_visibility_level\033[0m', "<20")
                for j in range(len(groupProjects)):
                    groupProjects_visibility_level = "NotPrivate" if groupProjects[j]['visibility_level'] else "Private"
                    print format(' ', "<5") + format(groupProjects[j]['path_with_namespace'], "<40") + format(groupProjects_visibility_level, "<20")
                print ""
                print format(' ', "<5") + format('\033[1;37;40mgroupUsers\033[0m', "<54") + format('\033[1;37;40mUsers_access_level\033[0m', "<20")
                for k in range(len(groupMembers)):
                    groupMembers_access_level = AccessLevelEnum(groupMembers[k]['access_level']).name
                    print format(' ', "<5") + format(groupMembers[k]['username'], "<40") + format(groupMembers_access_level, "<20")
        print "___________________________________________________________________________________________________________________________________________________"
    # print('\033[0m')
    # print jsonOFArgvReturn
elif sys.argv[2] == "-sgm" or sys.argv[2] == "-spm":
    print jsonOFArgvReturn
elif sys.argv[2] == "-sgp":
    if len(sys.argv) > 3:
        if sys.argv[4] == "-m":
            for i in range(len(listOfReturn)):
                projectMembers = json.loads(GitlabApi.getListOrId([sys.argv[1], "-spm", GitlabApi.getListOrId([
                    sys.argv[1], "-spi", listOfReturn[i]['path_with_namespace']])]))
                visibility_level = "NotPrivate" if listOfReturn[i]['visibility_level'] else "Private"
                print("\033[1;37;40m")
                print 'path_with_namespace: ' + listOfReturn[i]['path_with_namespace']
                print 'Project_visibility_level: ' + visibility_level
                print("\033[0m")
                print ''
                print ''
                print format(' ', "<5") + format('\033[1;37;40mProjectUsers\033[0m', "<54") + format('\033[1;37;40mUsers_access_level\033[0m', "<20")
                for k in range(len(projectMembers)):
                    projectMembers_access_level = AccessLevelEnum(projectMembers[k]['access_level']).name
                    print format(' ', "<5") + format(projectMembers[k]['username'], "<40") + format(projectMembers_access_level, "<20")
                print "___________________________________________________________________________________________________________________________________________________"
    else:
        print jsonOFArgvReturn
