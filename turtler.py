from lzma import compress, decompress

f = open('177.txt','rb').read()
h = compress(f)
open('177c.txt','wb').write(h)