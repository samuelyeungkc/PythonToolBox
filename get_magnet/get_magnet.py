import bencode, hashlib, base64, urllib
import os

def get_magnet(file_name):
        torrent = open(file_name, 'rb').read()
        metadata = bencode.bdecode(torrent)
        hash_info = metadata['info']
        hash_info = hashlib.sha1(bencode.bencode(hash_info)).hexdigest()
        magnet = "magnet:?xt=urn:btih:" + hash_info
        return magnet

if __name__ == "__main__":
	output = ""
	list = os.listdir(".")
	for f in list:
		if f.startswith("."):
			continue
		elif f == __file__:
			continue
		elif f.endswith(".torrent"):
			output += get_magnet(f) + "\n"
	print output
