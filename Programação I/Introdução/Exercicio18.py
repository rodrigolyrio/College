def main():
    a = int(input(''))
    b = int(input(''))
    
    a = a + b
    b = a - b
    a = a - b
    
    print(f' {a} e {b}')
    
    return 0 
if __name__ == "__main__":
    main()
