def f_argumento(x):
    if(x > 0):
        return('P')
    elif(x < 0):
        return('N')
    else:
        return('Z')

def main():
    a = int(0)
    
    a = int(input (''))
    
    print(f_argumento(a))
    
    return 0
if __name__ == "__main__":
    main()
