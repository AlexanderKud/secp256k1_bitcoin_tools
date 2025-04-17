import ec as ec
import registry as reg
'''
curve = reg.get_curve("secp256k1")
G2 = ec.Point(curve, 0xc6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5, 0x1ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a)
G3 = ec.Point(curve, 0xf9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9, 0x388f7b0f632de8140fe337e62a37f3566500a99934c2231b6cb9fd7584b8e672)
G4 = ec.Point(curve, 0xe493dbf1c10d80f3581e4904930b1404cc6c13900ee0758474fa94abe8c4cd13, 0x51ed993ea0d455b75642e2098ea51448d967ae33bfbdfe40cfe97bdc47739922)
G_point = G3 - G2
G2_point = G4 / 2
G4_point = G2 * 2
G5_point = G3 + G2
print(G_point)
print(G2_point)
print(G4_point)
print(G5_point)
print(curve.g)

rnd = ec.make_keypair(curve)
print(rnd.priv)
print(rnd.pub)
'''
subgroup = ec.SubGroup(p=349, g=(288,15), n=313, h=1)
print(subgroup)
curve = ec.Curve(a=0, b=7, field=subgroup, name='ec_curve_p349')
for i in range(1, curve.field.n+1):
    print(f'{i}: {i * curve.g}')
