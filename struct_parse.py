import struct
record = b'\x32\x12\x08\x01raymond   \x08'
str2 = struct.unpack_from("H10sHb",record)
print(str2)

