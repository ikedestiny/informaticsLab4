#Задание 1
def xml_to_json(xml):
    print("File in JSON FORMAT")
    print("____________________________________________________________")
    file = open(xml, "r", encoding="utf8")
    print("{")

    for line in file:
        if "</less" in line and len(line) < 15 and "lesson4" not in line:
            line = ""
            print("              },")

        line = line.replace("<", '"')
        line = line.replace(">", '": "')
        line = line[1:-4]

        if "/" in line:
            subString = line[(line.index("/")):]
            line = line.replace(subString, ",")

        if "less" in line and len(line) < 15:
            line = line + ": {"

        if "timetable" in line:
            line = line.replace("time", '"time') + ": {"

        if len(line) == 1:
            line =""

        if (len(line) < 3):
            line = line.replace('",', "             }")

        if "lesson1" in line:
            line = line.replace(line[:],"lessons: [")

        if len(line)>1:
            print(line)

    print("           ]")
    print("         }")
    print("     }")


xml_to_json("xml.XML")






#Задание 2