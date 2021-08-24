# coding: utf-8
import time
import random
import hashlib
import requests


def run(content):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

    s = "AUTO",
    l = "AUTO"
    u = 'fanyideskweb'
    # c = 'rY0D^0\'nM0}g5Mm1z%1G4'
    c = 'Tbh5E8=q6U3EXe+&L[4c@'
    d = content
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '205',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=178cf7f009a7b-007573c2d50af8-336a7c0e-1aeaa0-178cf7f009b461; NTES_YD_SESS=7gCAKxIvH5u3TZI5qQhbsT28bm1VacJ7kWwul8xhlsIfpvFRpWZ9_iFz8xswzqT8wTLti50eADPE6yBkUUOMYcT_MZ2NMq3pc0OcANyZTlFnSLxcDiTBKaoyFXGJ03FlXJA8Jmg_Gf4EHfhvFOxFmAek4ukYsvNKdqVLN5E83SXuNeRBz0yixGpSTPCPJfgIrJyMRGhxzXpQ01MseS7md3HAuJSIv5d8qCZB1ZVk4LgJN; S_INFO=1618388939|0|3&80##|13530552114; P_INFO=13530552114|1618388939|1|youdao_zhiyun2018|00&99|null&null&null#gud&440300#10#0|&0||13530552114; OUTFOX_SEARCH_USER_ID=-1426560297@10.169.0.83; JSESSIONID=aaaJeb0d4WdO1gO3DLpJx; OUTFOX_SEARCH_USER_ID_NCOO=585287449.5053693; ___rl__test__cookies=1618390422014',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {}
    data['i'] = content
    data['from'] = s
    data['to'] = l
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = f
    data['sign'] = sign
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLlCKBUTTON'
    data['typoResult'] = 'true'
    data['bv'] = 'ffc36c076d715bacb38ac2edc5def978'

    res = requests.post(url, data, headers=headers)
    print(res.json())
    say = res.json()['translateResult'][0][0]['tgt']
    return say
