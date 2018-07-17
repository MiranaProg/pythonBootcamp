def paper_doll(msg):
    msg2=" "
    for char in msg:
        msg2 += char*3
    return msg2
print(paper_doll('mississippi'))
