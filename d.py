import os


d = os.popen('"C:/Program Files (x86)/ZBar/bin/zbarimg.exe" --raw D:/qr.jpg').read()
print(d)