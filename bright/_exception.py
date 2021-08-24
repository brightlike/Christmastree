import json


def _exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return _ret(ex.code, ex.msg)

    return inner


def _ret(ret, msg, data={}):
    return {
        "isBase64Encoded": not isinstance({}, dict),
        "statusCode": 200,
        "headers": {
            "Content-Type": 'application/json'
        },
        "body": json.dumps({
            'code': ret,
            'msg': msg,
            'data': data
        })
    }

