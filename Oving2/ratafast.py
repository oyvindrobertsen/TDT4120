from sys import stdin
def main():
    stdin.readline()
    stdin.readline()
    rot = stdin.readline().strip()
    rata = stdin.readline().strip()
    dybde = 0
    dicti = dict()
    for linje in stdin:
        barn = linje.split()
        far = barn.pop(0)
        for b in barn:
            dicti[b] = far
        while rata in dicti:
            rata = dicti[rata]
            dybde += 1
        if rata == rot:
            print dybde
            return
main()
