import timeit
import array

TIMES = 1000000

SETUP = """
str_cafe   = 'café'
bytes_cafe = bytes(str_cafe, encoding='utf-8')
bytesarray_cafe = bytearray(bytes_cafe)
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


print("\033c")
print("\t\033[35;1;6;4;5mLet's Time Some Stuff!!\033[0m\n")

clock("upper on bytes     :", "x = bytes_cafe.upper().decode('utf-8')")
clock("upper on bytesarray:", "x = bytesarray_cafe.upper().decode('utf-8')")
clock("upper on a string  :", "x = str_cafe.upper()")



