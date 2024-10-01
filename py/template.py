import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def copy_dict(d, ignore = []):
    return {k: d[k] for k in set(list(d.keys())) - set(ignore)}

############ ---- Write below ---- ############

def main():
    pass

if __name__ == "__main__":
    main()
