input = input().split()
width = int(input[0])
height = int(input[1])
width += 8
height *= 3
print(width,height,width*height,sep='\n')