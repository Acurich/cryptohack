from Crypto.Util.number import bytes_to_long, long_to_bytes
import telnetlib
import json
import re
from pkcs1 import emsa_pkcs1_v15
from sage.all import *

HOST = "socket.cryptohack.org"
PORT = 13376

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline().decode()
    st = line[line.find('{'):]
    return json.loads(st)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

tn = telnetlib.Telnet(HOST, PORT)

ADMIN_TOKEN = b"admin=True"

print(readline())
to_send = json.loads(json.dumps({"option" : "get_pubkey"}))
json_send(to_send)

p = json_recv()
n = int(p["N"][2:],16)
e = int(p["e"][2:],16)

msg = hex(bytes_to_long(ADMIN_TOKEN) + n)
to_send = json.loads(json.dumps({"option" : "sign", "msg" : msg[2:]}))
json_send(to_send)
p = json_recv()

sig = int(p["signature"][2:],16)

to_send = json.loads(json.dumps({"option" : "verify", "signature" : hex(sig), "msg" : ADMIN_TOKEN.hex()}))
json_send(to_send)
p = json_recv()
print(p)

Flag: crypto{m4ll34b1l17y_c4n_b3_d4n63r0u5}
