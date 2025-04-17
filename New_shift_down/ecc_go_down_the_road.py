P = 115792089237316195423570985008687907853269984665640564039457584007908834671663 
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx,Gy)

last = (55066263022277343669578718895168534326250603453777594175500187360389116729240,83121579216557378445487899878180864668798711284981320763518679672151497189239)
m1 = (86918276961810349294276103416548851884759982251107,28597260016173315074988046521176122746119865902901063272803125467328307387891)
m2 = (86918276961810349294276103416548851884759982251107,87194829221142880348582938487511785107150118762739500766654458540580527283772)

def oncurve(p):
  x = p[0]
  y = p[1]
  x = (x*x*x+7) % P
  y = (y*y) % P
  return x==y

def modinv(a,n):
    lm = 1
    hm = 0
    low = a%n
    high = n
    while low > 1:
        ratio = high//low
        nm = hm-lm*ratio
        new = high-low*ratio
        high = low
        low = new
        hm = lm
        lm = nm
    return lm % n

def inv(a):
    return (a[0],P-a[1])
        
def double(a):
    Lam = ((3*a[0]*a[0]) * modinv((2*a[1]),P)) % P
    x = (Lam*Lam-2*a[0]) % P
    y = (Lam*(a[0]-x)-a[1]) % P
    return (x,y)

def add_full(a,b):
    if not oncurve(a) and a != (0,0):
        raise TypeError('Point Addition Error: Point a:{} is not on the curve'.format(a))
    if not oncurve(b) and b != (0,0):
        raise TypeError('Point Addition Error: Point b:{} is not on the curve'.format(b))
    if a[0]==0 and a[1]==0:
       return b
    if b[0]==0 and b[1]==0:
        return a
    if a[0]==b[0] and a[1] != b[1]:
        return (0, 0)
    elif a[0]==b[0] and a[1]==b[1]:
        return double(a)
    else:
        LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P)) % P
        x = (LamAdd*LamAdd-a[0]-b[0]) % P
        y = (LamAdd*(a[0]-x)-a[1]) % P
        return (x,y)

def sub(a,b):
    return add_full(a,inv(b))

def mult(GenPoint, ScalarHex):
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)):
        Q=double(Q)
        if ScalarBin[i] == "1": 
            Q=add_full(Q,GenPoint)
    return Q

def div(a,b): # Point multiplication by multiplicative inverse, returns a point such that mult( div(a,b) , b ) == a
    return mult(a,modinv(b,N))

def half(a): # Inverse of point doubling, same as div(a,2)
    return mult(a,57896044618658097711785492504343953926418782139537452191302581570759080747169)

p255,p254,p253,p252,p251,p250,p249,p248 = mult(G,2**255),mult(G,2**254),mult(G,2**253),mult(G,2**252),mult(G,2**251),mult(G,2**250),mult(G,2**249),mult(G,2**248)
p247,p246,p245,p244,p243,p242,p241,p240 = mult(G,2**247),mult(G,2**246),mult(G,2**245),mult(G,2**244),mult(G,2**243),mult(G,2**242),mult(G,2**241),mult(G,2**240)
p239,p238,p237,p236,p235,p234,p233,p232 = mult(G,2**239),mult(G,2**238),mult(G,2**237),mult(G,2**236),mult(G,2**235),mult(G,2**234),mult(G,2**233),mult(G,2**232)
p231,p230,p229,p228,p227,p226,p225,p224 = mult(G,2**231),mult(G,2**230),mult(G,2**229),mult(G,2**228),mult(G,2**227),mult(G,2**226),mult(G,2**225),mult(G,2**224)
p223,p222,p221,p220,p219,p218,p217,p216 = mult(G,2**223),mult(G,2**222),mult(G,2**221),mult(G,2**220),mult(G,2**219),mult(G,2**218),mult(G,2**217),mult(G,2**216)
p215,p214,p213,p212,p211,p210,p209,p208 = mult(G,2**215),mult(G,2**214),mult(G,2**213),mult(G,2**212),mult(G,2**211),mult(G,2**210),mult(G,2**209),mult(G,2**208)
p207,p206,p205,p204,p203,p202,p201,p200 = mult(G,2**207),mult(G,2**206),mult(G,2**205),mult(G,2**204),mult(G,2**203),mult(G,2**202),mult(G,2**201),mult(G,2**200)
p199,p198,p197,p196,p195,p194,p193,p192 = mult(G,2**199),mult(G,2**198),mult(G,2**197),mult(G,2**196),mult(G,2**195),mult(G,2**194),mult(G,2**193),mult(G,2**192)
p191,p190,p189,p188,p187,p186,p185,p184 = mult(G,2**191),mult(G,2**190),mult(G,2**189),mult(G,2**188),mult(G,2**187),mult(G,2**186),mult(G,2**185),mult(G,2**184)
p183,p182,p181,p180,p179,p178,p177,p176 = mult(G,2**183),mult(G,2**182),mult(G,2**181),mult(G,2**180),mult(G,2**179),mult(G,2**178),mult(G,2**177),mult(G,2**176)
p175,p174,p173,p172,p171,p170,p169,p168 = mult(G,2**175),mult(G,2**174),mult(G,2**173),mult(G,2**172),mult(G,2**171),mult(G,2**170),mult(G,2**169),mult(G,2**168)
p167,p166,p165,p164,p163,p162,p161,p160 = mult(G,2**167),mult(G,2**166),mult(G,2**165),mult(G,2**164),mult(G,2**163),mult(G,2**162),mult(G,2**161),mult(G,2**160)
p159,p158,p157,p156,p155,p154,p153,p152 = mult(G,2**159),mult(G,2**158),mult(G,2**157),mult(G,2**156),mult(G,2**155),mult(G,2**154),mult(G,2**153),mult(G,2**152)
p151,p150,p149,p148,p147,p146,p145,p144 = mult(G,2**151),mult(G,2**150),mult(G,2**149),mult(G,2**148),mult(G,2**147),mult(G,2**146),mult(G,2**145),mult(G,2**144)
p143,p142,p141,p140,p139,p138,p137,p136 = mult(G,2**143),mult(G,2**142),mult(G,2**141),mult(G,2**140),mult(G,2**139),mult(G,2**138),mult(G,2**137),mult(G,2**136)
p135,p134,p133,p132,p131,p130,p129,p128 = mult(G,2**135),mult(G,2**134),mult(G,2**133),mult(G,2**132),mult(G,2**131),mult(G,2**130),mult(G,2**129),mult(G,2**128)
p127,p126,p125,p124,p123,p122,p121 = mult(G,2**127),mult(G,2**126),mult(G,2**125),mult(G,2**124),mult(G,2**123),mult(G,2**122),mult(G,2**121)
p120,p119,p118,p117,p116,p115,p114,p113 = mult(G,2**120),mult(G,2**119),mult(G,2**118),mult(G,2**117),mult(G,2**116),mult(G,2**115),mult(G,2**114),mult(G,2**113)
p112,p111,p110,p109,p108,p107,p106,p105 = mult(G,2**112),mult(G,2**111),mult(G,2**110),mult(G,2**109),mult(G,2**108),mult(G,2**107),mult(G,2**106),mult(G,2**105)
p104,p103,p102,p101,p100,p99,p98,p97,p96 = mult(G,2**104),mult(G,2**103),mult(G,2**102),mult(G,2**101),mult(G,2**100),mult(G,2**99),mult(G,2**98),mult(G,2**97),mult(G,2**96)
p95,p94,p93,p92,p91,p90,p89,p88,p87 = mult(G,2**95),mult(G,2**94),mult(G,2**93),mult(G,2**92),mult(G,2**91),mult(G,2**90),mult(G,2**89),mult(G,2**88),mult(G,2**87)
p86,p85,p84,p83,p82,p81,p80,p79,p78 = mult(G,2**86),mult(G,2**85),mult(G,2**84),mult(G,2**83),mult(G,2**82),mult(G,2**81),mult(G,2**80),mult(G,2**79),mult(G,2**78)
p77,p76,p75,p74,p73,p72,p71,p70,p69,p68 = mult(G,2**77),mult(G,2**76),mult(G,2**75),mult(G,2**74),mult(G,2**73),mult(G,2**72),mult(G,2**71),mult(G,2**70),mult(G,2**69),mult(G,2**68)
p67,p66,p65,p64,p63,p62,p61,p60,p59 = mult(G,2**67),mult(G,2**66),mult(G,2**65),mult(G,2**64),mult(G,2**63),mult(G,2**62),mult(G,2**61),mult(G,2**60),mult(G,2**59)
p58,p57,p56,p55,p54,p53,p52,p51,p50 = mult(G,2**58),mult(G,2**57),mult(G,2**56),mult(G,2**55),mult(G,2**54),mult(G,2**53),mult(G,2**52),mult(G,2**51),mult(G,2**50)
p49,p48,p47,p46,p45,p44,p43,p42,p41 = mult(G,2**49),mult(G,2**48),mult(G,2**47),mult(G,2**46),mult(G,2**45),mult(G,2**44),mult(G,2**43),mult(G,2**42),mult(G,2**41)
p40,p39,p38,p37,p36,p35,p34,p33,p32 = mult(G,2**40),mult(G,2**39),mult(G,2**38),mult(G,2**37),mult(G,2**36),mult(G,2**35),mult(G,2**34),mult(G,2**33),mult(G,2**32)
p31,p30,p29,p28,p27,p26,p25,p24,p23 = mult(G,2**31),mult(G,2**30),mult(G,2**29),mult(G,2**28),mult(G,2**27),mult(G,2**26),mult(G,2**25),mult(G,2**24),mult(G,2**23)
p22,p21,p20,p19,p18,p17,p16,p15,p14 = mult(G,2**22),mult(G,2**21),mult(G,2**20),mult(G,2**19),mult(G,2**18),mult(G,2**17),mult(G,2**16),mult(G,2**15),mult(G,2**14)
p13,p12,p11,p10,p9,p8,p7,p6,p5 = mult(G,2**13),mult(G,2**12),mult(G,2**11),mult(G,2**10),mult(G,2**9),mult(G,2**8),mult(G,2**7),mult(G,2**6),mult(G,2**5)
p4,p3,p2,p1 = mult(G,2**4),mult(G,2**3),mult(G,2**2),mult(G,2**1)

point = mult(G,115792089237316195423570985008687907852837564279074904382605163141518161493762)
point = sub(point, p255)
pattern = [p254,p253,p252,p251,p250,p249,p248,p247,p246,p245,p244,p243,p242,p241,p240,p239,p238,p237,p236,p235,p234,p233,p232,p231,p230,p229,p228,p227,p226,p225,p224,p223,p222,p221,p220,p219,p218,p217,p216,p215,p214,p213,p212,p211,p210,p209,p208,p207,p206,p205,p204,p203,p202,p201,p200,p199,p198,p197,p196,p195,p194,p193,p192,p191,p190,p189,p188,p187,p186,p185,p184,p183,p182,p181,p180,p179,p178,p177,p176,p175,p174,p173,p172,p171,p170,p169,p168,p167,p166,p165,p164,p163,p162,p161,p160,p159,p158,p157,p156,p155,p154,p153,p152,p151,p150,p149,p148,p147,p146,p145,p144,p143,p142,p141,p140,p139,p138,p137,p136,p135,p134,p133,p132,p131,p130,p129,p127,p125,p124,p123,p121,p119,p117,p115,p114,p113,p111,p110,p108,p107,p106,p103,p102,p101,p98,p97,p95,p93,p91,p90,p89,p88,p86,p83,p79,p77,p69,p68,p67,p65,p64,p63,p61,p60,p59,p58,p57,p56,p55,p54,p52,p49,p46,p44,p43,p42,p41,p39,p35,p34,p31,p30,p28,p21,p20,p18,p17,p13,p12,p11,p10,p9,p8,p1]
for i in range(0,len(pattern)):
    point = sub(point,pattern[i])
    for name, value in list(globals().items()):
        if value is pattern[i]:
            p_name = name
    print(f'{p_name}: {point}')

