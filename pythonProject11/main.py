from struct import *
print(pack(">llle", 7, 34, 56, 0.0007))
print(unpack(">le", b'\x00\x00\x00\x07\x11\xbc'))