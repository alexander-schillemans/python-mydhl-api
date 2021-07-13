import base64
import requests
import json
import time

from . import config

class MyDHLAPI:

    def __init__(self, account, username, password):

        self.account = account
        self.username = username
        self.password = password

        self.demo = demo
        self.headers = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json'
        }

        self.baseUrl = config.BASE_URL
    
    def setTokenHeader(self, token):
        basicStr = 'Basic {token}'.format(token=token)
        self.headers.update({'Authorization' : basicStr})
    
    def acquireBasicToken(self):
        credentialsString = '{username}:{password}'.format(username=self.username, password=self.password)
        encodedBytes = base64.b64encode(credentialsString.encode('utf-8'))
        encodedToken = str(encodedBytes, 'utf-8')

        self.setTokenHeader(encodedToken)
    
    def checkHeaderTokens(self):
        if 'Authorization' not in self.headers: self.acquireBasicToken()

    def doRequest(self, method, url, data=None, headers=None):

        if headers:
            mergedHeaders = self.headers
            mergedHeaders.update(headers)
            headers = mergedHeaders
        else: headers = self.headers

        reqUrl = '{base}/{url}'.format(base=self.baseUrl, url=url)

        if method == 'GET':
            response = requests.get(reqUrl, params=data, headers=headers)
        elif method == 'POST':
            response = requests.post(reqUrl, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(reqUrl, data=json.dumps(data), headers=headers)
        
        return response

    def request(self, method, url, data=None, headers=None):

        self.checkHeaderTokens()
        response = self.doRequest(method, url, data, headers)

        if 'json' in response.headers['Content-Type']:
            respContent = response.json()
        elif 'pdf' in response.headers['Content-Type']:
            respContent = response.content
        
        return response.status_code, response.headers, respContent
    
    def get(self, url, data=None, headers=None):
        status, headers, response = self.request('GET', url, data, headers)
        return status, headers, response
    
    def post(self, url, data=None, headers=None):
        status, headers, response = self.request('POST', url, data, headers)
        return status, headers, response
    
    def put(self, url, data=None, headers=None):
        status, headers, response = self.request('PUT', url, data, headers)
        return status, headers, response