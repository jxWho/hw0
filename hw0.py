def main():
    f = open("iowa-liquor-sample.csv", "r")
    cnt = 0
    for line in f:
        index = line.upper().find('SINGLE MALT SCOTCH')
        if index != -1:
            cnt += 1
    return cnt

if __name__ == "__main__":
    number = main()
    print number
