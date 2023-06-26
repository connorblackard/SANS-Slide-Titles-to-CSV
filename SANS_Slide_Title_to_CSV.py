import json

with open('course.json') as course_json:
  parsed_json = json.load(course_json)

output = open('course_output.csv', 'w')

for section in parsed_json["data"]["course"]["sections"]:
  for subsection in section["modules"]:
    for slide in subsection["slides"]:
        output.write(section["name"] + "|" + subsection["name"] + "|" + str(subsection["fullNumber"]) + "." +str(slide["number"])+ "|" + slide["name"] + "|" + slide["duration"][0:8]+'\n')

output.close()
