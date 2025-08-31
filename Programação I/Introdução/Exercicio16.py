def main():
    a = float(0.0)
    t = float(0.0)
    
    a = float(input(""))
    t = float(input(""))
    
    v0 = 0
    s0 = 0
    
    v = v0 + a * t
    
    s = s0+v0*t+0.5*a*t**2
    
    print(f"{v} m/s e {s} m")
    
    return 0
if __name__ == "__main__":
    main()
