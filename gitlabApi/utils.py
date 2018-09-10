# -*-coding:utf-8 -*-
import urllib, urllib2, ssl

# 取消urllib2对ssl自证书的验证
ssl._create_default_https_context = ssl._create_unverified_context

class HttpHelper:
    def __init__(self):
        pass

    name = 'http helper'
    # header
    __reqHeader = {}
    # url
    __reqUrl = ''
    # time
    __reqTimeOut = 0

    # 构建Get请求
    def __buildGetRequest(self):
        if len(self.__reqHeader) == 0:
            request = urllib2.Request(self.__reqUrl)
        else:
            request = urllib2.Request(self.__reqUrl, headers=self.__reqHeader)
        return request

    # 构建post,put,delete请求
    def __buildPostPutDeleteRequest(self, postData):
        if len(self.__reqHeader) == 0:
            request = urllib2.Request(self.__reqUrl, data=postData)
        else:
            request = urllib2.Request(self.__reqUrl, headers=self.__reqHeader, data=postData)
        return request

    # 添加header
    def headers(self, headers):
        self.__reqHeader = headers
        return self

    # 添加url 
    def url(self, url):
        #print url
        self.__reqUrl = url
        return self

    # 添加超时
    def timeOut(self, time):
        self.__reqTimeOut = time
        return self

    # 是否debug
    def debug(self):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)
        urllib2.install_opener(opener)
        return self

    # 处理response
    def __handleResponse(self, request):
        try:
            if self.__reqTimeOut == 0:
                res = urllib2.urlopen(request)
            else:
                res = urllib2.urlopen(request, self.__reqTimeOut)
            return res.read()
        except urllib2.HTTPError, e:
            print e.code

    # get请求
    def get(self):
        request = self.__buildGetRequest()
        return self.__handleResponse(request)

    # post请求
    def post(self, postData):
        request = self.__buildPostPutDeleteRequest(postData=postData)
        return self.__handleResponse(request)

    # put请求
    def put(self, putData):
        request = self.__buildPostPutDeleteRequest(postData=putData)
        request.get_method = lambda: 'PUT'
        return self.__handleResponse(request)

    # delete请求
    def delete(self, putData):
        request = self.__buildPostPutDeleteRequest(postData=putData)
        request.get_method = lambda: 'DELETE'
        return self.__handleResponse(request)
