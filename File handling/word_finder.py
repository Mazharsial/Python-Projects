with open("log.txt") as f:
    content=f.readlines()

line_no=1
for line in content:
    if("python" in line):
        print(f"Yes python is present. on line no: {line_no}")
        break
    line_no +=1

else:
    print("python is not present")