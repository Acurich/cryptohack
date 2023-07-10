from pwn import remote
from json import dumps

io = remote("socket.cryptohack.org", 13385)
io.readline()
io.sendline(dumps({"prime": 2836331989097579758718892236976489043728710231836254290417342418003626284171153973270931498095415940742232485272768848664552542346387268063933743435138381539118667646531665378922141212157811699494418765721358442421568750370199598923649757845299767409845572673526062374763, "base": 72728440703025898243229908787433884538071481867621613352800346068965950623818635078553163}).encode())
print(io.readline().decode())

Flag: crypto{Forging_Primes_with_Francois_Arnault}
