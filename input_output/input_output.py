# ! write opertion
with open('file.txt','w') as f:
    f.write('laptop:Dell\nmouse:pentium\nkeyboard:Doc\nmonitor:LG')
# ! read operation
with open('file.txt','r') as f:
    content=f.read()
    print("############Read Starts############")
    for line in content.split('\n'):
        print(line)
    print("##############Read Ends############")
print("\n")
# ! append operation
with open('file.txt','a') as f:
    f.write('\nprinter:HP\nspeaker:JBL')

# ! Delete operation
with open('file.txt','r+') as f:
    lines=f.read()
    f.seek(0)
    f.truncate()
    for line in range(len(lines)):
        if line%2==0:
            f.write(lines[line])

# ! Final read to verify
with open('file.txt','r') as f:     
    content=f.read()
    print("############Final Read Starts############")
    for line in content.split('\n'):
        print(line)
    print("##############Final Read Ends############")
    
# ! Remove file
import os
os.remove('file.txt')


