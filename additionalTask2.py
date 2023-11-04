import re


def xml_to_json(xml):
    file = open(xml, "r", encoding="utf8")

    theFileInTextForm = file.read().split('\n')
    input = """
    """

    pattern1 = r'<\w+\s*>'
    pattern2 = r'</\w+\s*>'

    print("{")
    for line in theFileInTextForm:
        if len(re.findall(pattern1,line))>0 and len(line)<15:
            line = line.replace("<", '"')
            line = line.replace(">", '" {')

        if len(re.findall(pattern2,line))>0:
            if "lesson4" in  line or "timetable" in line:
                line = "     }"
            else:
                line = line.replace(">", '": "')
                line = line[1:-4]
                line = line.replace("<",'"')
                ind = line.index("/")
                line = line.replace(line[ind:],",")

        if line.startswith('"d'):
            line = line.replace('"d','    "d')

        if len(line)< 5:
            line = "           },"
        input += line + "\n"


#for line in input:


    startTags = re.findall(pattern1,input)

    print(input)
    print("}")

xml_to_json("xml.XML")