import xmltodict
import json

xml_string = """
"""
input = open("xml2.XML", "r", encoding="utf8")
for line in input:
    xml_string+=line

#print(xml_string)


data_dict = xmltodict.parse(xml_string)

#print(data_dict)

json_data = json.dumps(data_dict, indent=4).encode().decode('unicode_escape')
print(json_data)