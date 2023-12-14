ip_add=input("pls enter the ip:-")

segm1=1
segm_l=0
char =""
# ipad=int(ip_add)
# 192.168.1.1

for i in ip_add:
    if i == ".":
        print("{} and no idea {}".format(segm1,segm_l))
        segm1 +=1
        segm_l =0
    else:
        segm_l +=1

if char !=".":
    print("{} and no idea {}".format(segm1, segm_l))
