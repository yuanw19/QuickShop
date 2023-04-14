import itertools
from PIL import Image
import os

#take in a list of String typed items, return a list of String typed Shelves
def findShelves(items):
    Shelves = []
    for good in items:
        if good == "soap green" and "A" not in Shelves:
            Shelves.append("A")
        elif good == "soap orange" and "A" not in Shelves:
            Shelves.append("A")
        elif good == "soap red" and "A" not in Shelves:
            Shelves.append("A")
        elif good == "sphagettisauce" and "A" not in Shelves:
            Shelves.append("A")
        elif good == "strawberryjam" and "A" not in Shelves:
            Shelves.append("A")
        elif good == "BeerBottle" and "A" not in Shelves:
            Shelves.append("A")
        elif good == "lemona" and "B" not in Shelves:
            Shelves.append("B")
        elif good == "luncheoncyrcle" and "B" not in Shelves:
            Shelves.append("B")
        elif good == "baby milk" and "B" not in Shelves:
            Shelves.append("B")
        elif good == "noodle" and "B" not in Shelves:
            Shelves.append("B")
        elif good == "potatochips red" and "B" not in Shelves:
            Shelves.append("B")
        elif good == "big orange" and "C" not in Shelves:
            Shelves.append("C")
        elif good == "big soda" and "C" not in Shelves:
            Shelves.append("C")
        elif good == "Lollipop" and "C" not in Shelves:
            Shelves.append("C")
        elif good == "smart detergent" and "C" not in Shelves:
            Shelves.append("C")
        elif good == "Storage Box" and "D" not in Shelves:
            Shelves.append("D")
        elif good == "delicious cookies" and "D" not in Shelves:
            Shelves.append("D")
        elif good == "Bread" and "D" not in Shelves:
            Shelves.append("D")
        elif good == "CherryBox" and "E" not in Shelves:
            Shelves.append("E")
        elif good == "AppleBox" and "E" not in Shelves:
            Shelves.append("E")
        elif good == "Coffee" and "E" not in Shelves:
            Shelves.append("E")
        elif good == "Cheese Pizza" and "E" not in Shelves:
            Shelves.append("E")
        elif good == "Melon soda" and "F" not in Shelves:
            Shelves.append("F")
        elif good == "FrenchFries" and "F" not in Shelves:
            Shelves.append("F")
        elif good == "Butter" and "F" not in Shelves:
            Shelves.append("F")
        elif good == "Shrimp Sushi" and "G" not in Shelves:
            Shelves.append("G")
        elif good == "Tuna Sushi" and "G" not in Shelves:
            Shelves.append("G")
        elif good == "Rachel's Mustard" and "G" not in Shelves:
            Shelves.append("G")
        elif good == "Egg" and "H" not in Shelves:
            Shelves.append("H")
        elif good == "Chicken" and "H" not in Shelves:
            Shelves.append("H")
        elif good == "WaterBottle" and "I" not in Shelves:
            Shelves.append("I")
        elif good == "Fluidity Grape" and "I" not in Shelves:
            Shelves.append("I")
        elif good == "CerealBarApple" and "J" not in Shelves:
            Shelves.append("J")
        elif good == "MangoJuice" and "J" not in Shelves:
            Shelves.append("J")
        elif good == "AmericanFootball" and "K" not in Shelves:
            Shelves.append("K")
        elif good == "Skateboard" and "K" not in Shelves:
            Shelves.append("K")
        elif good == "SoccerBall" and "L" not in Shelves:
            Shelves.append("L")
        elif good == "TennisBall" and "L" not in Shelves:
            Shelves.append("L")
        elif good == "Painkillers" and "M" not in Shelves:
            Shelves.append("M")
        elif good == "Toothpaste" and "M" not in Shelves:
            Shelves.append("M")
        elif good == "Bandages" and "N" not in Shelves:
            Shelves.append("N")
        elif good == "First_aid_kit" and "N" not in Shelves:
            Shelves.append("N")
    return Shelves
def findShortestDistance(shelf1,shelf2):
    if (shelf1 == "A" and shelf2 == "B") or (shelf1 == "B" and shelf2 == "A"):
        return 1
    elif (shelf1 == "A" and shelf2 == "C") or (shelf1 == "C" and shelf2 == "A"):
        return 5
    elif (shelf1 == "A" and shelf2 == "D") or (shelf1 == "D" and shelf2 == "A"):
        return 6
    elif (shelf1 == "A" and shelf2 == "E") or (shelf1 == "E" and shelf2 == "A"):
        return 10
    elif (shelf1 == "A" and shelf2 == "F") or (shelf1 == "F" and shelf2 == "A"):
        return 11
    elif (shelf1 == "A" and shelf2 == "G") or (shelf1 == "G" and shelf2 == "A"):
        return 15
    elif (shelf1 == "A" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "A"):
        return 16
    elif (shelf1 == "A" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "A"):
        return 8
    elif (shelf1 == "A" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "A"):
        return 9
    elif (shelf1 == "A" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "A"):
        return 10
    elif (shelf1 == "A" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "A"):
        return 11
    elif (shelf1 == "A" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "A"):
        return 16
    elif (shelf1 == "A" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "A"):
        return 17

    elif (shelf1 == "B" and shelf2 == "C") or (shelf1 == "C" and shelf2 == "B"):
        return 4
    elif (shelf1 == "B" and shelf2 == "D") or (shelf1 == "D" and shelf2 == "B"):
        return 5
    elif (shelf1 == "B" and shelf2 == "E") or (shelf1 == "E" and shelf2 == "B"):
        return 9
    elif (shelf1 == "B" and shelf2 == "F") or (shelf1 == "F" and shelf2 == "B"):
        return 10
    elif (shelf1 == "B" and shelf2 == "G") or (shelf1 == "G" and shelf2 == "B"):
        return 14
    elif (shelf1 == "B" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "B"):
        return 15
    elif (shelf1 == "B" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "B"):
        return 9
    elif (shelf1 == "B" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "B"):
        return 8
    elif (shelf1 == "B" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "B"):
        return 9
    elif (shelf1 == "B" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "B"):
        return 10
    elif (shelf1 == "B" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "B"):
        return 15
    elif (shelf1 == "B" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "B"):
        return 16

    elif (shelf1 == "C" and shelf2 == "D") or (shelf1 == "D" and shelf2 == "C"):
        return 1
    elif (shelf1 == "C" and shelf2 == "E") or (shelf1 == "E" and shelf2 == "C"):
        return 5
    elif (shelf1 == "C" and shelf2 == "F") or (shelf1 == "F" and shelf2 == "C"):
        return 6
    elif (shelf1 == "C" and shelf2 == "G") or (shelf1 == "G" and shelf2 == "C"):
        return 10
    elif (shelf1 == "C" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "C"):
        return 11
    elif (shelf1 == "C" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "C"):
        return 12
    elif (shelf1 == "C" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "C"):
        return 11
    elif (shelf1 == "C" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "C"):
        return 8
    elif (shelf1 == "C" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "C"):
        return 9
    elif (shelf1 == "C" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "C"):
        return 14
    elif (shelf1 == "C" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "C"):
        return 15

    elif (shelf1 == "D" and shelf2 == "E") or (shelf1 == "E" and shelf2 == "D"):
        return 4
    elif (shelf1 == "D" and shelf2 == "F") or (shelf1 == "F" and shelf2 == "D"):
        return 5
    elif (shelf1 == "D" and shelf2 == "G") or (shelf1 == "G" and shelf2 == "D"):
        return 9
    elif (shelf1 == "D" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "D"):
        return 10
    elif (shelf1 == "D" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "D"):
        return 13
    elif (shelf1 == "D" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "D"):
        return 12
    elif (shelf1 == "D" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "D"):
        return 9
    elif (shelf1 == "D" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "D"):
        return 9
    elif (shelf1 == "D" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "D"):
        return 14
    elif (shelf1 == "D" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "D"):
        return 14

    elif (shelf1 == "E" and shelf2 == "F") or (shelf1 == "F" and shelf2 == "E"):
        return 1
    elif (shelf1 == "E" and shelf2 == "G") or (shelf1 == "G" and shelf2 == "E"):
        return 5
    elif (shelf1 == "E" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "E"):
        return 6
    elif (shelf1 == "E" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "E"):
        return 17
    elif (shelf1 == "E" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "E"):
        return 16
    elif (shelf1 == "E" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "E"):
        return 13
    elif (shelf1 == "E" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "E"):
        return 14
    elif (shelf1 == "E" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "E"):
        return 8
    elif (shelf1 == "E" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "E"):
        return 7

    elif (shelf1 == "F" and shelf2 == "G") or (shelf1 == "G" and shelf2 == "F"):
        return 4
    elif (shelf1 == "F" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "F"):
        return 5
    elif (shelf1 == "F" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "F"):
        return 18
    elif (shelf1 == "F" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "F"):
        return 17
    elif (shelf1 == "F" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "F"):
        return 14
    elif (shelf1 == "F" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "F"):
        return 15
    elif (shelf1 == "F" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "F"):
        return 7
    elif (shelf1 == "F" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "F"):
        return 6

    elif (shelf1 == "G" and shelf2 == "H") or (shelf1 == "H" and shelf2 == "G"):
        return 1
    elif (shelf1 == "G" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "G"):
        return 23
    elif (shelf1 == "G" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "G"):
        return 22
    elif (shelf1 == "G" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "G"):
        return 18
    elif (shelf1 == "G" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "G"):
        return 18
    elif (shelf1 == "G" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "G"):
        return 6
    elif (shelf1 == "G" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "G"):
        return 5

    elif (shelf1 == "H" and shelf2 == "I") or (shelf1 == "I" and shelf2 == "H"):
        return 24
    elif (shelf1 == "H" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "H"):
        return 23
    elif (shelf1 == "H" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "H"):
        return 19
    elif (shelf1 == "H" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "H"):
        return 19
    elif (shelf1 == "H" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "H"):
        return 7
    elif (shelf1 == "H" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "H"):
        return 6

    elif (shelf1 == "I" and shelf2 == "J") or (shelf1 == "J" and shelf2 == "I"):
        return 1
    elif (shelf1 == "I" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "I"):
        return 5
    elif (shelf1 == "I" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "I"):
        return 6
    elif (shelf1 == "I" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "I"):
        return 10
    elif (shelf1 == "I" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "I"):
        return 11

    elif (shelf1 == "J" and shelf2 == "K") or (shelf1 == "K" and shelf2 == "J"):
        return 4
    elif (shelf1 == "J" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "J"):
        return 5
    elif (shelf1 == "J" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "J"):
        return 9
    elif (shelf1 == "J" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "J"):
        return 10

    elif (shelf1 == "K" and shelf2 == "L") or (shelf1 == "L" and shelf2 == "K"):
        return 1
    elif (shelf1 == "K" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "K"):
        return 5
    elif (shelf1 == "K" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "K"):
        return 6

    elif (shelf1 == "L" and shelf2 == "M") or (shelf1 == "M" and shelf2 == "L"):
        return 4
    elif (shelf1 == "L" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "L"):
        return 5

    elif (shelf1 == "M" and shelf2 == "N") or (shelf1 == "N" and shelf2 == "M"):
        return 1
#take in a list of String typed items, and return shortest path
def shortestPath(items):
    Shelves = findShelves(items)
    Permutation = list(itertools.permutations(Shelves))
    ShortestDis = 10000
    BestPermu = ()
    for i in range(len(Permutation)):
        dis = 0
        for first,second in zip(Permutation[i],Permutation[i][1:]):
            dis += findShortestDistance(first, second)
        if dis < ShortestDis:
            ShortestDis = dis
            BestPermu = Permutation[i]
    return BestPermu

def iterate3DPicHelper(folderPath):
    for file in os.listdir(folderPath):
        image = Image.open(folderPath+"/"+file)
        image.show()
    img = Image.open("stop.PNG")
    img.show()


if __name__ == '__main__':
    goods = []
    while True:
        inputItem = input("Enter item name: ")
        if inputItem == "OK":
            break
        goods.append(inputItem)
    version = input("2D or 3D?")
    shortPath = shortestPath(goods)
    if version == "2D":
        for i in range(len(shortPath)):
            if i == len(shortPath) - 1:
                if shortPath[i] == "A":
                    img = Image.open("A2.PNG")
                    img.show()
                elif shortPath[i] == "B":
                    img = Image.open("B2.PNG")
                    img.show()
                elif shortPath[i] == "C":
                    img = Image.open("C2.PNG")
                    img.show()
                elif shortPath[i] == "D":
                    img = Image.open("D2.PNG")
                    img.show()
                elif shortPath[i] == "E":
                    img = Image.open("E2.PNG")
                    img.show()
                elif shortPath[i] == "F":
                    img = Image.open("F2.PNG")
                    img.show()
                elif shortPath[i] == "G":
                    img = Image.open("G2.PNG")
                    img.show()
                elif shortPath[i] == "H":
                    img = Image.open("H2.PNG")
                    img.show()
                elif shortPath[i] == "I":
                    img = Image.open("I2.PNG")
                    img.show()
                elif shortPath[i] == "J":
                    img = Image.open("J2.PNG")
                    img.show()
                elif shortPath[i] == "K":
                    img = Image.open("K2.PNG")
                    img.show()
                elif shortPath[i] == "L":
                    img = Image.open("L2.PNG")
                    img.show()
                elif shortPath[i] == "M":
                    img = Image.open("M2.PNG")
                    img.show()
                elif shortPath[i] == "N":
                    img = Image.open("N2.PNG")
                    img.show()
                break
            if i == 0:
                if shortPath[i] == "A":
                    img = Image.open("A1.PNG")
                    img.show()
                elif shortPath[i] == "B":
                    img = Image.open("B1.PNG")
                    img.show()
                elif shortPath[i] == "C":
                    img = Image.open("C1.PNG")
                    img.show()
                elif shortPath[i] == "D":
                    img = Image.open("D1.PNG")
                    img.show()
                elif shortPath[i] == "E":
                    img = Image.open("E1.PNG")
                    img.show()
                elif shortPath[i] == "F":
                    img = Image.open("F1.PNG")
                    img.show()
                elif shortPath[i] == "G":
                    img = Image.open("G1.PNG")
                    img.show()
                elif shortPath[i] == "H":
                    img = Image.open("H1.PNG")
                    img.show()
                elif shortPath[i] == "I":
                    img = Image.open("I1.PNG")
                    img.show()
                elif shortPath[i] == "J":
                    img = Image.open("J1.PNG")
                    img.show()
                elif shortPath[i] == "K":
                    img = Image.open("K1.PNG")
                    img.show()
                elif shortPath[i] == "L":
                    img = Image.open("L1.PNG")
                    img.show()
                elif shortPath[i] == "M":
                    img = Image.open("M1.PNG")
                    img.show()
                elif shortPath[i] == "N":
                    img = Image.open("N1.PNG")
                    img.show()
            if shortPath[i] + shortPath[i+1] == "AB" or shortPath[i] + shortPath[i+1] == "BA":
                image = Image.open("AB.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AC" or shortPath[i] + shortPath[i+1] == "CA":
                image = Image.open("AC.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AD" or shortPath[i] + shortPath[i+1] == "DA":
                image = Image.open("AD.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AE" or shortPath[i] + shortPath[i+1] == "EA":
                image = Image.open("AE.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AF" or shortPath[i] + shortPath[i+1] == "FA":
                image = Image.open("AF.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AG" or shortPath[i] + shortPath[i+1] == "GA":
                image = Image.open("AG.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AH" or shortPath[i] + shortPath[i+1] == "HA":
                image = Image.open("AH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AI" or shortPath[i] + shortPath[i+1] == "IA":
                image = Image.open("AI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AJ" or shortPath[i] + shortPath[i+1] == "JA":
                image = Image.open("AJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AK" or shortPath[i] + shortPath[i+1] == "KA":
                image = Image.open("AK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AL" or shortPath[i] + shortPath[i+1] == "LA":
                image = Image.open("AL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AM" or shortPath[i] + shortPath[i+1] == "MA":
                image = Image.open("AM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "AN" or shortPath[i] + shortPath[i+1] == "NA":
                image = Image.open("AN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BC" or shortPath[i] + shortPath[i+1] == "CB":
                image = Image.open("BC.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BD" or shortPath[i] + shortPath[i+1] == "DB":
                image = Image.open("BD.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BE" or shortPath[i] + shortPath[i+1] == "EB":
                image = Image.open("BE.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BF" or shortPath[i] + shortPath[i+1] == "FB":
                image = Image.open("BF.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BG" or shortPath[i] + shortPath[i+1] == "GB":
                image = Image.open("BG.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BH" or shortPath[i] + shortPath[i+1] == "HB":
                image = Image.open("BH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BI" or shortPath[i] + shortPath[i+1] == "IB":
                image = Image.open("BI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BJ" or shortPath[i] + shortPath[i+1] == "JB":
                image = Image.open("BJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BK" or shortPath[i] + shortPath[i+1] == "KB":
                image = Image.open("BK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BL" or shortPath[i] + shortPath[i+1] == "LB":
                image = Image.open("BL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BM" or shortPath[i] + shortPath[i+1] == "MB":
                image = Image.open("BM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "BN" or shortPath[i] + shortPath[i+1] == "NB":
                image = Image.open("BN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CD" or shortPath[i] + shortPath[i+1] == "DC":
                image = Image.open("CD.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CE" or shortPath[i] + shortPath[i+1] == "EC":
                image = Image.open("CE.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CF" or shortPath[i] + shortPath[i+1] == "FC":
                image = Image.open("CF.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CG" or shortPath[i] + shortPath[i+1] == "GC":
                image = Image.open("CG.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CH" or shortPath[i] + shortPath[i+1] == "HC":
                image = Image.open("CH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CI" or shortPath[i] + shortPath[i+1] == "IC":
                image = Image.open("CI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CJ" or shortPath[i] + shortPath[i+1] == "JC":
                image = Image.open("CJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CK" or shortPath[i] + shortPath[i+1] == "KC":
                image = Image.open("CK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CL" or shortPath[i] + shortPath[i+1] == "LC":
                image = Image.open("CL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CM" or shortPath[i] + shortPath[i+1] == "MC":
                image = Image.open("CM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "CN" or shortPath[i] + shortPath[i+1] == "NC":
                image = Image.open("CN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DE" or shortPath[i] + shortPath[i+1] == "ED":
                image = Image.open("DE.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DF" or shortPath[i] + shortPath[i+1] == "FD":
                image = Image.open("DF.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DG" or shortPath[i] + shortPath[i+1] == "GD":
                image = Image.open("DG.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DH" or shortPath[i] + shortPath[i+1] == "HD":
                image = Image.open("DH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DI" or shortPath[i] + shortPath[i+1] == "ID":
                image = Image.open("DI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DJ" or shortPath[i] + shortPath[i+1] == "JD":
                image = Image.open("DJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DK" or shortPath[i] + shortPath[i+1] == "KD":
                image = Image.open("DK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DL" or shortPath[i] + shortPath[i+1] == "LD":
                image = Image.open("DL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DM" or shortPath[i] + shortPath[i+1] == "MD":
                image = Image.open("DM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "DN" or shortPath[i] + shortPath[i+1] == "ND":
                image = Image.open("DN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EF" or shortPath[i] + shortPath[i+1] == "FE":
                image = Image.open("EF.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EG" or shortPath[i] + shortPath[i+1] == "GE":
                image = Image.open("EG.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EH" or shortPath[i] + shortPath[i+1] == "HE":
                image = Image.open("EH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EI" or shortPath[i] + shortPath[i+1] == "IE":
                image = Image.open("EI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EJ" or shortPath[i] + shortPath[i+1] == "JE":
                image = Image.open("EF.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EK" or shortPath[i] + shortPath[i+1] == "KE":
                image = Image.open("EK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EL" or shortPath[i] + shortPath[i+1] == "LE":
                image = Image.open("EL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EM" or shortPath[i] + shortPath[i+1] == "ME":
                image = Image.open("EM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "EN" or shortPath[i] + shortPath[i+1] == "NE":
                image = Image.open("EN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FG" or shortPath[i] + shortPath[i+1] == "GF":
                image = Image.open("FG.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FH" or shortPath[i] + shortPath[i+1] == "HF":
                image = Image.open("FH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FI" or shortPath[i] + shortPath[i+1] == "IF":
                image = Image.open("FI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FJ" or shortPath[i] + shortPath[i+1] == "JF":
                image = Image.open("FJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FK" or shortPath[i] + shortPath[i+1] == "KF":
                image = Image.open("FK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FL" or shortPath[i] + shortPath[i+1] == "LF":
                image = Image.open("FL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FM" or shortPath[i] + shortPath[i+1] == "MF":
                image = Image.open("FM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "FN" or shortPath[i] + shortPath[i+1] == "NF":
                image = Image.open("FN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GH" or shortPath[i] + shortPath[i+1] == "HG":
                image = Image.open("GH.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GI" or shortPath[i] + shortPath[i+1] == "IG":
                image = Image.open("GI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GJ" or shortPath[i] + shortPath[i+1] == "JG":
                image = Image.open("GJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GK" or shortPath[i] + shortPath[i+1] == "KG":
                image = Image.open("GK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GL" or shortPath[i] + shortPath[i+1] == "LG":
                image = Image.open("GL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GM" or shortPath[i] + shortPath[i+1] == "MG":
                image = Image.open("GM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "GN" or shortPath[i] + shortPath[i+1] == "NG":
                image = Image.open("GN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "HI" or shortPath[i] + shortPath[i+1] == "IH":
                image = Image.open("HI.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "HJ" or shortPath[i] + shortPath[i+1] == "JH":
                image = Image.open("HJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "HK" or shortPath[i] + shortPath[i+1] == "KH":
                image = Image.open("HK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "HL" or shortPath[i] + shortPath[i+1] == "LH":
                image = Image.open("HL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "HM" or shortPath[i] + shortPath[i+1] == "MH":
                image = Image.open("HM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "HN" or shortPath[i] + shortPath[i+1] == "NH":
                image = Image.open("HN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "IJ" or shortPath[i] + shortPath[i+1] == "JI":
                image = Image.open("IJ.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "IK" or shortPath[i] + shortPath[i+1] == "KI":
                image = Image.open("IK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "IL" or shortPath[i] + shortPath[i+1] == "LI":
                image = Image.open("IL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "IM" or shortPath[i] + shortPath[i+1] == "MI":
                image = Image.open("IM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "IN" or shortPath[i] + shortPath[i+1] == "NI":
                image = Image.open("IN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "JK" or shortPath[i] + shortPath[i+1] == "KJ":
                image = Image.open("JK.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "JL" or shortPath[i] + shortPath[i+1] == "LJ":
                image = Image.open("JL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "JM" or shortPath[i] + shortPath[i+1] == "MJ":
                image = Image.open("JM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "JN" or shortPath[i] + shortPath[i+1] == "NJ":
                image = Image.open("JN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "KL" or shortPath[i] + shortPath[i+1] == "LK":
                image = Image.open("KL.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "KM" or shortPath[i] + shortPath[i+1] == "MK":
                image = Image.open("KM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "KN" or shortPath[i] + shortPath[i+1] == "NK":
                image = Image.open("KN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "LM" or shortPath[i] + shortPath[i+1] == "ML":
                image = Image.open("LM.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "LN" or shortPath[i] + shortPath[i+1] == "NL":
                image = Image.open("LN.JPG")
                image.show()
            elif shortPath[i] + shortPath[i+1] == "MN" or shortPath[i] + shortPath[i+1] == "NM":
                image = Image.open("MN.JPG")
                image.show()
    else:
        for i in range(len(shortPath)):
            if i == len(shortPath) - 1:
                if shortPath[i] == "A":
                    iterate3DPicHelper("3DPic/Exit/A")
                elif shortPath[i] == "B":
                    iterate3DPicHelper("3DPic/Exit/B")
                elif shortPath[i] == "C":
                    iterate3DPicHelper("3DPic/Exit/C")
                elif shortPath[i] == "D":
                    iterate3DPicHelper("3DPic/Exit/D")
                elif shortPath[i] == "E":
                    iterate3DPicHelper("3DPic/Exit/E")
                elif shortPath[i] == "F":
                    iterate3DPicHelper("3DPic/Exit/F")
                elif shortPath[i] == "G":
                    iterate3DPicHelper("3DPic/Exit/G")
                elif shortPath[i] == "H":
                    iterate3DPicHelper("3DPic/Exit/H")
                elif shortPath[i] == "I":
                    iterate3DPicHelper("3DPic/Exit/I")
                elif shortPath[i] == "J":
                    iterate3DPicHelper("3DPic/Exit/J")
                elif shortPath[i] == "K":
                    iterate3DPicHelper("3DPic/Exit/K")
                elif shortPath[i] == "L":
                    iterate3DPicHelper("3DPic/Exit/L")
                elif shortPath[i] == "M":
                    iterate3DPicHelper("3DPic/Exit/M")
                elif shortPath[i] == "N":
                    iterate3DPicHelper("3DPic/Exit/N")
                break
            if i == 0:
                if shortPath[i] == "A":
                    iterate3DPicHelper("3DPic/Entrance/A")
                elif shortPath[i] == "B":
                    iterate3DPicHelper("3DPic/Entrance/B")
                elif shortPath[i] == "C":
                    iterate3DPicHelper("3DPic/Entrance/C")
                elif shortPath[i] == "D":
                    iterate3DPicHelper("3DPic/Entrance/D")
                elif shortPath[i] == "E":
                    iterate3DPicHelper("3DPic/Entrance/E")
                elif shortPath[i] == "F":
                    iterate3DPicHelper("3DPic/Entrance/F")
                elif shortPath[i] == "G":
                    iterate3DPicHelper("3DPic/Entrance/G")
                elif shortPath[i] == "H":
                    iterate3DPicHelper("3DPic/Entrance/H")
                elif shortPath[i] == "I":
                    iterate3DPicHelper("3DPic/Entrance/I")
                elif shortPath[i] == "J":
                    iterate3DPicHelper("3DPic/Entrance/J")
                elif shortPath[i] == "K":
                    iterate3DPicHelper("3DPic/Entrance/K")
                elif shortPath[i] == "L":
                    iterate3DPicHelper("3DPic/Entrance/L")
                elif shortPath[i] == "M":
                    iterate3DPicHelper("3DPic/Entrance/M")
                elif shortPath[i] == "N":
                    iterate3DPicHelper("3DPic/Entrance/N")
            if shortPath[i] + shortPath[i+1] == "AB":
                iterate3DPicHelper("3DPic/AB")
            elif shortPath[i] + shortPath[i+1] == "AC":
                iterate3DPicHelper("3DPic/AC")
            elif shortPath[i] + shortPath[i+1] == "AD":
                iterate3DPicHelper("3DPic/AD")
            elif shortPath[i] + shortPath[i+1] == "AE":
                iterate3DPicHelper("3DPic/AE")
            elif shortPath[i] + shortPath[i+1] == "AF":
                iterate3DPicHelper("3DPic/AF")
            elif shortPath[i] + shortPath[i+1] == "AG":
                iterate3DPicHelper("3DPic/AG")
            elif shortPath[i] + shortPath[i+1] == "AH":
                iterate3DPicHelper("3DPic/AH")
            elif shortPath[i] + shortPath[i+1] == "AI":
                iterate3DPicHelper("3DPic/AI")
            elif shortPath[i] + shortPath[i+1] == "AJ":
                iterate3DPicHelper("3DPic/AJ")
            elif shortPath[i] + shortPath[i+1] == "AK":
                iterate3DPicHelper("3DPic/AK")
            elif shortPath[i] + shortPath[i+1] == "AL":
                iterate3DPicHelper("3DPic/AL")
            elif shortPath[i] + shortPath[i+1] == "AM":
                iterate3DPicHelper("3DPic/AM")
            elif shortPath[i] + shortPath[i+1] == "AN":
                iterate3DPicHelper("3DPic/AN")
            elif shortPath[i] + shortPath[i+1] == "BA":
                iterate3DPicHelper("3DPic/BA")
            elif shortPath[i] + shortPath[i+1] == "BC":
                iterate3DPicHelper("3DPic/BC")
            elif shortPath[i] + shortPath[i+1] == "BD":
                iterate3DPicHelper("3DPic/BD")
            elif shortPath[i] + shortPath[i+1] == "BE":
                iterate3DPicHelper("3DPic/BE")
            elif shortPath[i] + shortPath[i+1] == "BF":
                iterate3DPicHelper("3DPic/BF")
            elif shortPath[i] + shortPath[i+1] == "BG":
                iterate3DPicHelper("3DPic/BG")
            elif shortPath[i] + shortPath[i+1] == "BH":
                iterate3DPicHelper("3DPic/BH")
            elif shortPath[i] + shortPath[i+1] == "BI":
                iterate3DPicHelper("3DPic/BI")
            elif shortPath[i] + shortPath[i+1] == "BJ":
                iterate3DPicHelper("3DPic/BJ")
            elif shortPath[i] + shortPath[i+1] == "BK":
                iterate3DPicHelper("3DPic/BK")
            elif shortPath[i] + shortPath[i+1] == "BL":
                iterate3DPicHelper("3DPic/BL")
            elif shortPath[i] + shortPath[i+1] == "BM":
                iterate3DPicHelper("3DPic/BM")
            elif shortPath[i] + shortPath[i+1] == "BN":
                iterate3DPicHelper("3DPic/BN")
            elif shortPath[i] + shortPath[i+1] == "CA":
                iterate3DPicHelper("3DPic/CA")
            elif shortPath[i] + shortPath[i+1] == "CB":
                iterate3DPicHelper("3DPic/CB")
            elif shortPath[i] + shortPath[i+1] == "CD":
                iterate3DPicHelper("3DPic/CD")
            elif shortPath[i] + shortPath[i+1] == "CE":
                iterate3DPicHelper("3DPic/CE")
            elif shortPath[i] + shortPath[i+1] == "CF":
                iterate3DPicHelper("3DPic/CF")
            elif shortPath[i] + shortPath[i+1] == "CG":
                iterate3DPicHelper("3DPic/CG")
            elif shortPath[i] + shortPath[i+1] == "CH":
                iterate3DPicHelper("3DPic/CH")
            elif shortPath[i] + shortPath[i+1] == "CI":
                iterate3DPicHelper("3DPic/CI")
            elif shortPath[i] + shortPath[i+1] == "CJ":
                iterate3DPicHelper("3DPic/CJ")
            elif shortPath[i] + shortPath[i+1] == "CK":
                iterate3DPicHelper("3DPic/CK")
            elif shortPath[i] + shortPath[i+1] == "CL":
                iterate3DPicHelper("3DPic/CL")
            elif shortPath[i] + shortPath[i+1] == "CM":
                iterate3DPicHelper("3DPic/CM")
            elif shortPath[i] + shortPath[i+1] == "CN":
                iterate3DPicHelper("3DPic/CN")
            elif shortPath[i] + shortPath[i+1] == "DA":
                iterate3DPicHelper("3DPic/DA")
            elif shortPath[i] + shortPath[i+1] == "DB":
                iterate3DPicHelper("3DPic/DB")
            elif shortPath[i] + shortPath[i+1] == "DC":
                iterate3DPicHelper("3DPic/DC")
            elif shortPath[i] + shortPath[i+1] == "DE":
                iterate3DPicHelper("3DPic/DE")
            elif shortPath[i] + shortPath[i+1] == "DF":
                iterate3DPicHelper("3DPic/DF")
            elif shortPath[i] + shortPath[i+1] == "DG":
                iterate3DPicHelper("3DPic/DG")
            elif shortPath[i] + shortPath[i+1] == "DH":
                iterate3DPicHelper("3DPic/DH")
            elif shortPath[i] + shortPath[i+1] == "DI":
                iterate3DPicHelper("3DPic/DI")
            elif shortPath[i] + shortPath[i+1] == "DJ":
                iterate3DPicHelper("3DPic/DJ")
            elif shortPath[i] + shortPath[i+1] == "DK":
                iterate3DPicHelper("3DPic/DK")
            elif shortPath[i] + shortPath[i+1] == "DL":
                iterate3DPicHelper("3DPic/DL")
            elif shortPath[i] + shortPath[i+1] == "DM":
                iterate3DPicHelper("3DPic/DM")
            elif shortPath[i] + shortPath[i+1] == "DN":
                iterate3DPicHelper("3DPic/DN")
            elif shortPath[i] + shortPath[i+1] == "EA":
                iterate3DPicHelper("3DPic/EA")
            elif shortPath[i] + shortPath[i+1] == "EB":
                iterate3DPicHelper("3DPic/EB")
            elif shortPath[i] + shortPath[i+1] == "EC":
                iterate3DPicHelper("3DPic/EC")
            elif shortPath[i] + shortPath[i+1] == "ED":
                iterate3DPicHelper("3DPic/ED")
            elif shortPath[i] + shortPath[i+1] == "EF":
                iterate3DPicHelper("3DPic/EF")
            elif shortPath[i] + shortPath[i+1] == "EG":
                iterate3DPicHelper("3DPic/EG")
            elif shortPath[i] + shortPath[i+1] == "EH":
                iterate3DPicHelper("3DPic/EH")
            elif shortPath[i] + shortPath[i+1] == "EI":
                iterate3DPicHelper("3DPic/EI")
            elif shortPath[i] + shortPath[i+1] == "EJ":
                iterate3DPicHelper("3DPic/EJ")
            elif shortPath[i] + shortPath[i+1] == "EK":
                iterate3DPicHelper("3DPic/EK")
            elif shortPath[i] + shortPath[i+1] == "EL":
                iterate3DPicHelper("3DPic/EL")
            elif shortPath[i] + shortPath[i+1] == "EM":
                iterate3DPicHelper("3DPic/EM")
            elif shortPath[i] + shortPath[i+1] == "EN":
                iterate3DPicHelper("3DPic/EN")
            elif shortPath[i] + shortPath[i+1] == "FA":
                iterate3DPicHelper("3DPic/FA")
            elif shortPath[i] + shortPath[i+1] == "FB":
                iterate3DPicHelper("3DPic/FB")
            elif shortPath[i] + shortPath[i+1] == "FC":
                iterate3DPicHelper("3DPic/FC")
            elif shortPath[i] + shortPath[i+1] == "FD":
                iterate3DPicHelper("3DPic/FD")
            elif shortPath[i] + shortPath[i+1] == "FE":
                iterate3DPicHelper("3DPic/FE")
            elif shortPath[i] + shortPath[i+1] == "FG":
                iterate3DPicHelper("3DPic/FG")
            elif shortPath[i] + shortPath[i+1] == "FH":
                iterate3DPicHelper("3DPic/FH")
            elif shortPath[i] + shortPath[i+1] == "FI":
                iterate3DPicHelper("3DPic/FI")
            elif shortPath[i] + shortPath[i+1] == "FJ":
                iterate3DPicHelper("3DPic/FJ")
            elif shortPath[i] + shortPath[i+1] == "FK":
                iterate3DPicHelper("3DPic/FK")
            elif shortPath[i] + shortPath[i+1] == "FL":
                iterate3DPicHelper("3DPic/FL")
            elif shortPath[i] + shortPath[i+1] == "FM":
                iterate3DPicHelper("3DPic/FM")
            elif shortPath[i] + shortPath[i+1] == "FN":
                iterate3DPicHelper("3DPic/FN")
            elif shortPath[i] + shortPath[i+1] == "GA":
                iterate3DPicHelper("3DPic/GA")
            elif shortPath[i] + shortPath[i+1] == "GB":
                iterate3DPicHelper("3DPic/GB")
            elif shortPath[i] + shortPath[i+1] == "GC":
                iterate3DPicHelper("3DPic/GC")
            elif shortPath[i] + shortPath[i+1] == "GD":
                iterate3DPicHelper("3DPic/GD")
            elif shortPath[i] + shortPath[i+1] == "GE":
                iterate3DPicHelper("3DPic/GE")
            elif shortPath[i] + shortPath[i+1] == "GF":
                iterate3DPicHelper("3DPic/GF")
            elif shortPath[i] + shortPath[i+1] == "GH":
                iterate3DPicHelper("3DPic/GH")
            elif shortPath[i] + shortPath[i+1] == "GI":
                iterate3DPicHelper("3DPic/GI")
            elif shortPath[i] + shortPath[i+1] == "GJ":
                iterate3DPicHelper("3DPic/GJ")
            elif shortPath[i] + shortPath[i+1] == "GK":
                iterate3DPicHelper("3DPic/GK")
            elif shortPath[i] + shortPath[i+1] == "GL":
                iterate3DPicHelper("3DPic/GL")
            elif shortPath[i] + shortPath[i+1] == "GM":
                iterate3DPicHelper("3DPic/GM")
            elif shortPath[i] + shortPath[i+1] == "GN":
                iterate3DPicHelper("3DPic/GN")
            elif shortPath[i] + shortPath[i+1] == "HA":
                iterate3DPicHelper("3DPic/HA")
            elif shortPath[i] + shortPath[i+1] == "HB":
                iterate3DPicHelper("3DPic/HB")
            elif shortPath[i] + shortPath[i+1] == "HC":
                iterate3DPicHelper("3DPic/HC")
            elif shortPath[i] + shortPath[i+1] == "HD":
                iterate3DPicHelper("3DPic/HD")
            elif shortPath[i] + shortPath[i+1] == "HE":
                iterate3DPicHelper("3DPic/HE")
            elif shortPath[i] + shortPath[i+1] == "HF":
                iterate3DPicHelper("3DPic/HF")
            elif shortPath[i] + shortPath[i+1] == "HG":
                iterate3DPicHelper("3DPic/HG")
            elif shortPath[i] + shortPath[i+1] == "HI":
                iterate3DPicHelper("3DPic/HI")
            elif shortPath[i] + shortPath[i+1] == "HJ":
                iterate3DPicHelper("3DPic/HJ")
            elif shortPath[i] + shortPath[i+1] == "HK":
                iterate3DPicHelper("3DPic/HK")
            elif shortPath[i] + shortPath[i+1] == "HL":
                iterate3DPicHelper("3DPic/HL")
            elif shortPath[i] + shortPath[i+1] == "HM":
                iterate3DPicHelper("3DPic/HM")
            elif shortPath[i] + shortPath[i+1] == "HN":
                iterate3DPicHelper("3DPic/HN")
            elif shortPath[i] + shortPath[i+1] == "IA":
                iterate3DPicHelper("3DPic/IA")
            elif shortPath[i] + shortPath[i+1] == "IB":
                iterate3DPicHelper("3DPic/IB")
            elif shortPath[i] + shortPath[i+1] == "IC":
                iterate3DPicHelper("3DPic/IC")
            elif shortPath[i] + shortPath[i+1] == "ID":
                iterate3DPicHelper("3DPic/ID")
            elif shortPath[i] + shortPath[i+1] == "IE":
                iterate3DPicHelper("3DPic/IE")
            elif shortPath[i] + shortPath[i+1] == "IF":
                iterate3DPicHelper("3DPic/IF")
            elif shortPath[i] + shortPath[i+1] == "IG":
                iterate3DPicHelper("3DPic/IG")
            elif shortPath[i] + shortPath[i+1] == "IH":
                iterate3DPicHelper("3DPic/IH")
            elif shortPath[i] + shortPath[i+1] == "IJ":
                iterate3DPicHelper("3DPic/IJ")
            elif shortPath[i] + shortPath[i+1] == "IK":
                iterate3DPicHelper("3DPic/IK")
            elif shortPath[i] + shortPath[i+1] == "IL":
                iterate3DPicHelper("3DPic/IL")
            elif shortPath[i] + shortPath[i+1] == "IM":
                iterate3DPicHelper("3DPic/IM")
            elif shortPath[i] + shortPath[i+1] == "IN":
                iterate3DPicHelper("3DPic/IN")
            elif shortPath[i] + shortPath[i+1] == "JA":
                iterate3DPicHelper("3DPic/JA")
            elif shortPath[i] + shortPath[i+1] == "JB":
                iterate3DPicHelper("3DPic/JB")
            elif shortPath[i] + shortPath[i+1] == "JC":
                iterate3DPicHelper("3DPic/JC")
            elif shortPath[i] + shortPath[i+1] == "JD":
                iterate3DPicHelper("3DPic/JD")
            elif shortPath[i] + shortPath[i+1] == "JD":
                iterate3DPicHelper("3DPic/JD")
            elif shortPath[i] + shortPath[i+1] == "JE":
                iterate3DPicHelper("3DPic/JE")
            elif shortPath[i] + shortPath[i+1] == "JF":
                iterate3DPicHelper("3DPic/JF")
            elif shortPath[i] + shortPath[i+1] == "JG":
                iterate3DPicHelper("3DPic/JG")
            elif shortPath[i] + shortPath[i+1] == "JH":
                iterate3DPicHelper("3DPic/JH")
            elif shortPath[i] + shortPath[i+1] == "JI":
                iterate3DPicHelper("3DPic/JI")
            elif shortPath[i] + shortPath[i+1] == "JK":
                iterate3DPicHelper("3DPic/JK")
            elif shortPath[i] + shortPath[i+1] == "JL":
                iterate3DPicHelper("3DPic/JL")
            elif shortPath[i] + shortPath[i+1] == "JM":
                iterate3DPicHelper("3DPic/JM")
            elif shortPath[i] + shortPath[i+1] == "JN":
                iterate3DPicHelper("3DPic/JN")
            elif shortPath[i] + shortPath[i+1] == "KA":
                iterate3DPicHelper("3DPic/KA")
            elif shortPath[i] + shortPath[i+1] == "KB":
                iterate3DPicHelper("3DPic/KB")
            elif shortPath[i] + shortPath[i+1] == "KC":
                iterate3DPicHelper("3DPic/KC")
            elif shortPath[i] + shortPath[i+1] == "KD":
                iterate3DPicHelper("3DPic/KD")
            elif shortPath[i] + shortPath[i+1] == "KE":
                iterate3DPicHelper("3DPic/KE")
            elif shortPath[i] + shortPath[i+1] == "KF":
                iterate3DPicHelper("3DPic/KF")
            elif shortPath[i] + shortPath[i+1] == "KG":
                iterate3DPicHelper("3DPic/KG")
            elif shortPath[i] + shortPath[i+1] == "KH":
                iterate3DPicHelper("3DPic/KH")
            elif shortPath[i] + shortPath[i+1] == "KI":
                iterate3DPicHelper("3DPic/KI")
            elif shortPath[i] + shortPath[i+1] == "KJ":
                iterate3DPicHelper("3DPic/KJ")
            elif shortPath[i] + shortPath[i+1] == "KL":
                iterate3DPicHelper("3DPic/KL")
            elif shortPath[i] + shortPath[i+1] == "KM":
                iterate3DPicHelper("3DPic/KM")
            elif shortPath[i] + shortPath[i+1] == "KN":
                iterate3DPicHelper("3DPic/KN")
            elif shortPath[i] + shortPath[i+1] == "LA":
                iterate3DPicHelper("3DPic/LA")
            elif shortPath[i] + shortPath[i+1] == "LB":
                iterate3DPicHelper("3DPic/LB")
            elif shortPath[i] + shortPath[i+1] == "LC":
                iterate3DPicHelper("3DPic/LC")
            elif shortPath[i] + shortPath[i+1] == "LD":
                iterate3DPicHelper("3DPic/LD")
            elif shortPath[i] + shortPath[i+1] == "LE":
                iterate3DPicHelper("3DPic/LE")
            elif shortPath[i] + shortPath[i+1] == "LF":
                iterate3DPicHelper("3DPic/LF")
            elif shortPath[i] + shortPath[i+1] == "LG":
                iterate3DPicHelper("3DPic/LG")
            elif shortPath[i] + shortPath[i+1] == "LH":
                iterate3DPicHelper("3DPic/LH")
            elif shortPath[i] + shortPath[i+1] == "LI":
                iterate3DPicHelper("3DPic/LI")
            elif shortPath[i] + shortPath[i+1] == "LJ":
                iterate3DPicHelper("3DPic/LJ")
            elif shortPath[i] + shortPath[i+1] == "LK":
                iterate3DPicHelper("3DPic/LK")
            elif shortPath[i] + shortPath[i+1] == "LM":
                iterate3DPicHelper("3DPic/LM")
            elif shortPath[i] + shortPath[i+1] == "LN":
                iterate3DPicHelper("3DPic/LN")
            elif shortPath[i] + shortPath[i+1] == "MA":
                iterate3DPicHelper("3DPic/MA")
            elif shortPath[i] + shortPath[i+1] == "MB":
                iterate3DPicHelper("3DPic/MB")
            elif shortPath[i] + shortPath[i+1] == "MC":
                iterate3DPicHelper("3DPic/MC")
            elif shortPath[i] + shortPath[i+1] == "MD":
                iterate3DPicHelper("3DPic/MD")
            elif shortPath[i] + shortPath[i+1] == "ME":
                iterate3DPicHelper("3DPic/ME")
            elif shortPath[i] + shortPath[i+1] == "MF":
                iterate3DPicHelper("3DPic/MF")
            elif shortPath[i] + shortPath[i+1] == "MG":
                iterate3DPicHelper("3DPic/MG")
            elif shortPath[i] + shortPath[i+1] == "MH":
                iterate3DPicHelper("3DPic/MH")
            elif shortPath[i] + shortPath[i+1] == "MI":
                iterate3DPicHelper("3DPic/MI")
            elif shortPath[i] + shortPath[i+1] == "MJ":
                iterate3DPicHelper("3DPic/MJ")
            elif shortPath[i] + shortPath[i+1] == "MK":
                iterate3DPicHelper("3DPic/MK")
            elif shortPath[i] + shortPath[i+1] == "ML":
                iterate3DPicHelper("3DPic/ML")
            elif shortPath[i] + shortPath[i+1] == "MN":
                iterate3DPicHelper("3DPic/MN")
            elif shortPath[i] + shortPath[i+1] == "NA":
                iterate3DPicHelper("3DPic/NA")
            elif shortPath[i] + shortPath[i+1] == "NB":
                iterate3DPicHelper("3DPic/NB")
            elif shortPath[i] + shortPath[i+1] == "NC":
                iterate3DPicHelper("3DPic/NC")
            elif shortPath[i] + shortPath[i+1] == "ND":
                iterate3DPicHelper("3DPic/ND")
            elif shortPath[i] + shortPath[i+1] == "NE":
                iterate3DPicHelper("3DPic/NE")
            elif shortPath[i] + shortPath[i+1] == "NF":
                iterate3DPicHelper("3DPic/NF")
            elif shortPath[i] + shortPath[i+1] == "NG":
                iterate3DPicHelper("3DPic/NG")
            elif shortPath[i] + shortPath[i+1] == "NH":
                iterate3DPicHelper("3DPic/NH")
            elif shortPath[i] + shortPath[i+1] == "NI":
                iterate3DPicHelper("3DPic/NI")
            elif shortPath[i] + shortPath[i+1] == "NJ":
                iterate3DPicHelper("3DPic/NJ")
            elif shortPath[i] + shortPath[i+1] == "NK":
                iterate3DPicHelper("3DPic/NK")
            elif shortPath[i] + shortPath[i+1] == "NL":
                iterate3DPicHelper("3DPic/NL")
            elif shortPath[i] + shortPath[i+1] == "NM":
                iterate3DPicHelper("3DPic/NM")
