import json

fname = '/Users/dstatz/Documents/pgit/video-streaming-analytics/data-process/flumenz/src/test/resources/cdn_log.json'

with open(fname, 'r') as f:
    res = f.readlines()
    print(json.dumps(res))