print("\033c")

# nongenlog.py
#
# Sum up the number of bytes transferred in an Apache log file
# using a simple for-loop.   We're not using generators here.

# 140.180.132.213 - - [24/Feb/2008:00:08:59 -0600] "GET /ply/ply.html HTTP/1.1" 200 97238
with open("access-log") as wwwlog:
    total = 0
    for line in wwwlog:
        bytes_sent = line.rsplit(None,1)[1]
        if bytes_sent != '-':
            total += int(bytes_sent)
    print("Total", total)



with open("access-log") as wwwlog:
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
    bytes_sent = (int(x) for x in bytecolumn if x != '-')
    print("Total", sum(bytes_sent))

