def decrypt(q, h, f, g, e):
    a = (f * e) % q
    m = (a * inverse_mod(f, g)) % g
    return m

q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

f, g = matrix([[1,h], [0,q]]).LLL()[0]
m = decrypt(q,h,f,g,e)
print(bytes.fromhex(hex(m)[2:]).decode())

Flag: crypto{Gauss_lattice_attack!}