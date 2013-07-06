import struct, socket, os, sys


def sendMagicPacket():
	dst_mac_addr = 'YOUR-MAC-ADDRESS' #for example '00:00:00:00:00:00'
	self = "YOUR-TARGET-IP-ADDRESS" #for example '127.0.0.1'
		
	addr_byte = dst_mac_addr.split(':')
	hw_addr = struct.pack('BBBBBB', int(addr_byte[0], 16), int(addr_byte[1], 16), int(addr_byte[2], 16), int(addr_byte[3], 16), int(addr_byte[4], 16), int(addr_byte[5], 16))
	macpck = '\xff' * 6 + hw_addr * 16
	scks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	scks.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	scks.sendto(macpck, ('<broadcast>', 9))
	scks.close()
    


sendMagicPacket()