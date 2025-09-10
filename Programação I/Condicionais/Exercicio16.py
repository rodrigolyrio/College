def main():
    nh = float(input())
    sh = float(input())
    
    if (nh > 160):
        hora_extra = (nh-160)*sh*1.5
        salario = 160*sh + hora_extra
    else:
        salario = nh*sh
    print(f'{salario:.1f}')
    
    
    return 0 
if __name__ == "__main__":
    main()
