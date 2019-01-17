from bluepy import btle

scanner = btle.Scanner(0)
devices = scanner.scan(30.0)

for device in devices:
	print('---------------------------------------------------')
	print('MACアドレス：'+device.addr)
	print('アドレスタイプ：'+device.addrType)
	print('RSSI：'+str(device.rssi))
	print()
	for (adTypeCode, description, valueText) in device.getScanData():
		print('アドバタイシングデータ：'+description+'/'+valueText)