n = input("IPv4 network prefix length:")
if n.isdigit() and 32>=int(n)>=0:
    n = int(n)
    binary_code = "1"*n + "0"*(32-n)
    print(f"binary:{binary_code}")
    binary_code = int(binary_code)
    ip = [0,0,0,0]
    for i in range(4):
        ip[i] = binary_code//(10**(8*(3-i)))
        binary_code = binary_code - ip[i]*(10**(8*(3-i)))
        total = 0
        x = ip[i]
        for j in range(8):
            total += (x%10)*(2**j)
            x = x//10
        ip[i] = total
    print(f"subnet mask:{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}")
else:
    print("please input number between 0~32")
