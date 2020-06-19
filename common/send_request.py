import requests
import json


class RunMethod:
    # post请求
    def do_post(self, url, data, headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url, json=data, headers=headers)
        else:
            res = requests.post(url=url, json=data)
        return res.json()

    # get请求
    def do_get(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.get(url=url, data=data, headers=headers)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    def run_method(self, method, url, data=None, headers=None):
        res = None
        if method == "POST" or method == "post":
            res = self.do_post(url, data, headers)
        else:
            res = self.do_get(url, data, headers)
        return res
