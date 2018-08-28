# coding=utf-8
# !/usr/bin/env python
"""
调用api后端方式
"""
import base64
import sys
import time
import json
import urllib
import urllib2
import datetime
import hashlib

reload(sys)
sys.setdefaultencoding('utf8')
OPENAPI_TOKEN_UID = ""
OPENAPI_TOKEN_APPID = ""
OPENAPI_TOKEN_SK = ""


class InnerToken(object):
    """
    用于生成内部token
    """
    TOKEN_TYPE = '11'
    timestamp = ''

    def sign(self, appid, uid, sk):
        """
        生成sign
        """
        md5 = hashlib.md5()
        self.timestamp = str(time.mktime(datetime.datetime.now().timetuple())).split('.')[0]
        md5.update(self.timestamp + str(uid) + str(appid) + str(sk))
        return md5.hexdigest()

    def generateToken(self, appid, uid, sk):
        """
        生成token
        """
        sign = self.sign(appid, uid, sk)
        token = self.TOKEN_TYPE + '.' + sign + '.' + self.timestamp + \
                '.' + str(uid) + "-" + str(appid)
        return token


def request_api(filename):
    """
    调用api服务
    """
    f = open(filename, 'rb')
    imagedata = base64.b64encode(f.read())
    f.close()

    innerToken = InnerToken()
    access_token = innerToken.generateToken(OPENAPI_TOKEN_APPID, \
                                            OPENAPI_TOKEN_UID, OPENAPI_TOKEN_SK)

    url = 'http://XXXXXXX'.format(access_token)
    post_data = {
        'image': imagedata,
    }
    req = urllib2.Request(url, urllib.urlencode(post_data))

    response = urllib2.urlopen(req).read()
    print json.dumps(json.loads(response), sort_keys=False, \
                     ensure_ascii=False, indent=4).encode('utf-8')


if __name__ == '__main__':
    request_api("123.png")
