from sympy import cbrt
c = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
print(bytes.fromhex(hex(cbrt(c))[2:]).decode())

Flag: crypto{N33d_m04R_p4dd1ng}