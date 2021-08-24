import time
import math

# 定义一些时间段的常量（秒）
TimeSec_Hour = 3600
TimeSec_Day = 86400
TimeSec_Week = 604800
TimeSec_Month = 2592000
TimeSec_Year = 31536000


def timestamp_sec(timestamp):
    if timestamp_is_ms(timestamp):
        return round(timestamp / 1000)
    else:
        return timestamp


def timestamp_ms(timestamp):
    if timestamp_is_ms(timestamp):
        return timestamp
    else:
        return timestamp * 1000


def timestamp_is_ms(timestamp):
    return timestamp > 1000000000000


def format_duration(duration, ms=False):
    if ms:
        duration = round(duration / 60)
    sec = duration % 60
    minute = math.floor((duration % 3600) / 60)
    hour = math.floor((duration % 86400) / 3600)
    day = math.floor(duration / 86400)
    if day > 0:
        ret = ''.join([str(day), "天"])
        if hour > 0:
            ret = ''.join([ret, str(hour), "小时"])
    elif hour > 0:
        ret = ''.join([str(hour), "小时"])
        if minute > 0:
            ret = ''.join([ret, str(minute), "分钟"])
    elif minute > 0:
        ret = ''.join([str(minute), "分钟"])
        if sec > 0:
            ret = ''.join([ret, str(sec), "秒"])
    else:
        ret = ''.join([str(sec), '秒'])
    return ret


def datetime_format(timestamp, ms=False):
    if ms:
        timestamp = int(timestamp / 1000)
    time_array = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_array)


def dateformat(timestamp, ms=False):
    if ms:
        timestamp = int(timestamp / 1000)
    time_array = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d", time_array)


def timeformat(format_string, timestamp, ms=False):
    if ms:
        timestamp = int(timestamp / 1000)
    time_array = time.localtime(timestamp)
    return time.strftime(format_string, time_array)


def datetime_to_stamp(time_string, ms=False):
    time_array = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    ret = int(time.mktime(time_array))
    if ms:
        ret = ret * 1000
    return ret


def date_to_stamp(date_string, ms=False):
    try:
        time_array = time.strptime(date_string, "%Y-%m-%d")
        ret = int(time.mktime(time_array))
    except ValueError:
        ret = 0
    if ms:
        ret = ret * 1000
    return ret


def get_timestamp(ms=False):
    if ms:
        return int(round(time.time() * 1000))
    else:
        return int(time.time())


def get_daystart(timestamp=0, ms=False):
    if timestamp == 0:
        timestamp = int(time.time())
    elif ms:
        timestamp = int(timestamp / 1000)
    midnight = date_to_stamp(dateformat(timestamp))
    if ms:
        midnight = midnight * 1000
    return midnight


def get_dayend(timestamp=0, ms=False):
    if ms:
        timestamp = int(timestamp / 1000)
    ret = get_daystart(timestamp) + 86399
    if ms:
        ret = ret * 1000 + 999
    return ret


def datetime_format_utc(timestamp):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", timestamp)
