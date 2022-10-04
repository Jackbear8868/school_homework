n = int(input(""))

def castle_builder(n):
    if n >=1: #for 1
        print(" "*(4*n+1),"|>",sep="")
        print(" "*(4*n+1),"|",sep="")
        print(" "*(4*n+1),"|",sep="")

        for i in range(1,n+1):


            if i %2 ==1:
                print(" "*(4*(n-i)+1),"_   "*(2*i+1),sep="")
                print(" "*(4*(n-i)),"|X| "*(2*i+1),sep="")
                for j in range(i):
                    print(" "*(4*(n-i)),"|","X"*((2*i+1)*3+2*i-2),"|",sep="")
                print(" "*(4*(n-i)),"\\","X"*((2*i+1)*3+2*i-2),"/",sep="")
                print(" "*(4*(n-i))," ","\\","X"*((2*i+1)*3+2*i-4),"/",sep="")

                if i == n:
                    for j in range(i-1):
                        print(" "*(4*(n-i))," ","|","X"*(8*i-1),"|",sep="")
                    print(" "*(4*(n-i))," ","|","X"*(4*i-1),"_","X"*(4*i-1),"|",sep="")
                    print(" "*(4*(n-i))," ","|","X"*(4*i-2),"| |","X"*(4*i-2),"|",sep="")
                    print(" "*(4*(n-i)),"/","X"*(4*i-1),"| |","X"*(4*i-1),"\\",sep="")
                else:
                    for j in range(i+1):
                        print(" "*(4*(n-i))," ","|","X"*(8*i-1),"|",sep="")
            else:
                print(" "*(4*(n-i)+1),"_   "*(2*i+1),sep="")
                print(" "*(4*(n-i)),"| | "*(2*i+1),sep="")
                for j in range(i):
                    print(" "*(4*(n-i)),"|"," "*((2*i+1)*3+2*i-2),"|",sep="")
                print(" "*(4*(n-i)),"\\"," "*((2*i+1)*3+2*i-2),"/",sep="")
                print(" "*(4*(n-i))," ","\\"," "*((2*i+1)*3+2*i-4),"/",sep="")

                if i == n:
                    for j in range(i-1):
                        print(" "*(4*(n-i))," ","|"," "*(8*i-1),"|",sep="")
                    print(" "*(4*(n-i))," ","|"," "*(4*i-1),"_"," "*(4*i-1),"|",sep="")
                    print(" "*(4*(n-i))," ","|"," "*(4*i-2),"| |"," "*(4*i-2),"|",sep="")
                    print(" "*(4*(n-i)),"/"," "*(4*i-1),"| |"," "*(4*i-1),"\\",sep="")
                else:
                    for j in range(i+1):
                        print(" "*(4*(n-i))," ","|"," "*(8*i-1),"|",sep="")
    else:
        print("|>")
        print("|")
        print("|")


castle_builder(n)
