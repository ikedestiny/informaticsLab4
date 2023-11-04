def xml_to_json(xmlFile):
    file = open(xmlFile,"r",encoding="utf8")

    import re

    pattern1 = r'<\w+\s*>'
    pattern2 = r'</\w+\s*>'
    pattern3 = r'{'
    pattern4 = r'}'

    input = """"""

    input+="{\n"

    front = 0
    back =0
    count =0

    for line in file:
        count+=1
        if len(re.findall(pattern1,line))>0 and len(re.findall(pattern2,line))==0:
            line = line.replace("<", '"')
            line = line.replace(">", '":  {')

        elif len(re.findall(pattern1, line)) > 0 and len(re.findall(pattern2, line)) > 0:
            line =  line.replace(re.findall(pattern2, line)[0], '",')
            line = line.replace("<", '"')
            line = line.replace(">",'": "')

        elif len(re.findall(pattern1, line)) == 0 and len(re.findall(pattern2, line)) > 0:
            line = line.replace(re.findall(pattern2,line)[0], "}")


        if len(line.strip()) == 0:
            line +="}"

        front += len(re.findall(pattern3,line))
        back +=len(re.findall(pattern4,line))

        input+=line





    print(input)

    print(front, back)


xml_to_json("xml.XML")