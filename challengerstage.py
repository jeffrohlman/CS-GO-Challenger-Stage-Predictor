import random

class Team:
    record = "xxxxx"
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def updateRecord(self, r, w):
        if(w):
            self.record = self.record[0:r-1] + "W" + self.record[r:]
        else:
            self.record = self.record[0:r-1] + "L" + self.record[r:]
        

astralis = Team("Astralis",1.15 * 93) #106.85
liquid = Team("Team Liquid",1.05 * 99) #103.95
rng = Team("Renegades", .99 * 56) #55.44
north = Team("North",1.03 * 47) #48.41
nip = Team("Ninjas in Pyjamas",1.03 * 44) #45.32
gambit = Team("Gambit",.97 * 46) #44.62
tyloo = Team("TyLoo", 37 * 1.05) #38.85
big = Team("BIG",29 * 1.04) #30.16
hr = Team("HellRaisers", 26 * 1.07) #27.82
vp = Team("Virtus Pro", 25 * 1.04) #26
optic = Team("Optic",21 * 1.07) #22.47
rogue = Team("Rogue", 37 * 1.05 / 2) #19.43
spirit = Team("Team Spirit",1.03 * 48 / 3) #16.48
ss = Team("Space Soldiers", 14 * 1.07) #14.98
col = Team("Complexity",27 * 1.05 / 2) #14.18
vega = Team("Vega Squadron", 17 * 1.05 / 2) #8.93

teams = [astralis,liquid,rng,north,nip,gambit,tyloo,big,hr,vp,spirit,optic,rogue,ss,col,vega]
t30 = []
t31 = []
t32 = []
t23 = []
t13 = []
t03 = []

def pickwinner(t1, t2 , r):
    w = random.random() * (t1.rating+t2.rating)
    if(w > t1.rating):
        t1.updateRecord(r, False)
        t2.updateRecord(r, True)
        print(t2.name +" beats " + t1.name)
    else:
        t1.updateRecord(r, True)
        t2.updateRecord(r, False)
        print(t1.name + " beats " + t2.name)
    return (t1,t2)

#round1
print("Round 1:")

(ss, rogue) = pickwinner(ss, rogue, 1)
(vp, nip) = pickwinner(vp, nip, 1)
(gambit, tyloo) = pickwinner(gambit, tyloo, 1)
(big, rng) = pickwinner(big, rng, 1)
(vega, spirit) = pickwinner(vega, spirit, 1)
(north, hr) = pickwinner(north, hr, 1)
(liquid, optic) = pickwinner(liquid, optic, 1)
(astralis, col) = pickwinner(astralis, col, 1)

round1winners = []
round1losers = []
for t in teams:
    if(t.record[0] == "W"):
       round1winners.append(t)
    else:
       round1losers.append(t)
       
#round2
print("\nRound 2:")
random.shuffle(round1winners)
random.shuffle(round1losers)

(round1winners[0], round1winners[1]) = pickwinner(round1winners[0], round1winners[1], 2)
(round1winners[2], round1winners[3]) = pickwinner(round1winners[2], round1winners[3], 2)
(round1winners[4], round1winners[5]) = pickwinner(round1winners[4], round1winners[5], 2)
(round1winners[6], round1winners[7]) = pickwinner(round1winners[6], round1winners[7], 2)
(round1losers[0], round1losers[1]) = pickwinner(round1losers[0], round1losers[1], 2)
(round1losers[2], round1losers[3]) = pickwinner(round1losers[2], round1losers[3], 2)
(round1losers[4], round1losers[5]) = pickwinner(round1losers[4], round1losers[5], 2)
(round1losers[6], round1losers[7]) = pickwinner(round1losers[6], round1losers[7], 2)

round2WW = []
round2WL = []
round2LL = []
for t in teams:
    if(t.record[0:2] == "WW"):
        round2WW.append(t)
    elif(t.record[0:2] == "WL"):
        round2WL.append(t)
    elif(t.record[0:2] == "LW"):
        round2WL.append(t)
    else:
        round2LL.append(t)

#round3
print("\nRound 3:")
random.shuffle(round2WW)
random.shuffle(round2WL)
random.shuffle(round2LL)

(round2WW[0], round2WW[1]) = pickwinner(round2WW[0], round2WW[1], 3)
(round2WW[2], round2WW[3]) = pickwinner(round2WW[2], round2WW[3], 3)
(round2WL[0], round2WL[1]) = pickwinner(round2WL[0], round2WL[1], 3)
(round2WL[2], round2WL[3]) = pickwinner(round2WL[2], round2WL[3], 3)
(round2WL[4], round2WL[5]) = pickwinner(round2WL[4], round2WL[5], 3)
(round2WL[6], round2WL[7]) = pickwinner(round2WL[6], round2WL[7], 3)
(round2LL[0], round2LL[1]) = pickwinner(round2LL[0], round2LL[1], 3)
(round2LL[2], round2LL[3]) = pickwinner(round2LL[2], round2LL[3], 3)

round3WWL = []
round3WLL = []
for t in teams:
    if(t.record[0:3] == "WWW"):
        t30.append(t)
    elif(t.record[0:3] == "WLW"):
        round3WWL.append(t)
    elif(t.record[0:3] == "LWW"):
        round3WWL.append(t)
    elif(t.record[0:3] == "WWL"):
        round3WWL.append(t)
    elif(t.record[0:3] == "LLL"):
        t03.append(t)
    else:
        round3WLL.append(t)

#round4
print("\nRound 4:")
random.shuffle(round3WWL)
random.shuffle(round3WLL)

(round3WWL[0], round3WWL[1]) = pickwinner(round3WWL[0], round3WWL[1], 4)
(round3WWL[2], round3WWL[3]) = pickwinner(round3WWL[2], round3WWL[3], 4)
(round3WWL[4], round3WWL[5]) = pickwinner(round3WWL[4], round3WWL[5], 4)
(round3WLL[0], round3WLL[1]) = pickwinner(round3WLL[0], round3WLL[1], 4)
(round3WLL[2], round3WLL[3]) = pickwinner(round3WLL[2], round3WLL[3], 4)
(round3WLL[4], round3WLL[5]) = pickwinner(round3WLL[4], round3WLL[5], 4)

round4 = []
for t in teams:
    if(t.record[0:4] == "LWWW"):
        t31.append(t)
    elif(t.record[0:4] == "WLWW"):
        t31.append(t)
    elif(t.record[0:4] == "WWLW"):
        t31.append(t)
    elif(t.record[0:4] == "WLLL"):
        t13.append(t)
    elif(t.record[0:4] == "LWLL"):
        t13.append(t)
    elif(t.record[0:4] == "LLWL"):
        t13.append(t)
    elif(t.record[3] != "x"):
        round4.append(t)

#round5
print("\nRound 5:")
random.shuffle(round4)

(round4[0], round4[1]) = pickwinner(round4[0], round4[1], 5)
(round4[2], round4[3]) = pickwinner(round4[2], round4[3], 5)
(round4[4], round4[5]) = pickwinner(round4[4], round4[5], 5)

for t in round4:
    if(t.record[4] == "L"):
        t23.append(t)
    else:
        t32.append(t)

#Results
print("\n3-0:")
for t in t30:
    print(t.name)
print("\n3-1:")
for t in t31:
    print(t.name)
print("\n3-2:")
for t in t32:
    print(t.name)
print("\n2-3:")
for t in t23:
    print(t.name)
print("\n1-3:")
for t in t13:
    print(t.name)
print("\n0-3:")
for t in t03:
    print(t.name)
