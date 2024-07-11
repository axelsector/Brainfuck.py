a=[0]*30000
p=0
def parse(bfi):
    global a
    global p
    x=len(bfi)
    c=0
    while c < x:
        match bfi[c]:
            case "+":
                if a[p]==255:
                    a[p]=0
                else:
                    a[p]+=1
            case "-":
                if a[p]==0:
                    a[p]=255
                else:
                    a[p]-=1
            case ">":
                p+=1
            case "<":
                p-=1
            case "[":
                c+=1
                brk=1
                subbf=''
                while brk>0 and c<x:
                    if bfi[c]=="[":
                        brk+=1
                    if bfi[c]=="]":
                        brk-=1
                    subbf+=(bfi[c])
                    c+=1
                loop(subbf)
                c-=1
            case ".":
                op(a,p)
            case ",":
                inp(a,p)
        c+=1

        
def loop(subbf):
    while True:
            if a[p]!=0:
                parse(subbf)
                if a[p]==0:
                    break
            if a[p]==0:
                break

def op(a,p):
    print(chr(a[p]), end='')

def inp(a,p):
    ip=input("Enter input: ")
    if ip=="":
        a[p]=0
    else:
        a[p]=ord(ip[0])

def hlep():
    print("""Brainfuck is a language that uses 2 components. 
An array of 30,000 bytees and a pointer that can be used to manipute the memory at a single byte.
There are only 8 characters that are accepted as Brainfuck inputs. Every other character is ignored.
> = Increases memory pointer, or moves the current byte to the right by 1.
< = Decreases memory pointer, or moves the current byte to the left by 1.
+ = Increases value stored at the current byte by 1.
- = Decreases value stored at the current byte by 1.
[ = Initiates a loop till the corresponding ].
] = If currently pointed byte is not zero, jump back to [.
, = Input 1 character into the current byte of the array.
. = Prints 1 character from the current byte of the array.
The language is Turing-complete, which means these 8 characters can be used to write almost any program you can think of.
Here's the code for printing "Hello World!" to the console. 
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]
<.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.
Here's a GitHub Gist by roachhd if you want to learn more. https://gist.github.com/roachhd/dce54bec8ba55fb17d3a""")





print("""Brainfuck Compiler          
Enter Brainfuck code, or type '/help' for help.""")
bf=input("BF:")
if bf=="/help":
    hlep()
else:
    parse(bf)
