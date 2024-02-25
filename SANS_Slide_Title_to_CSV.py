import json, argparse

parser = argparse.ArgumentParser(prog='SANS_Slide_Title_to_CSV.py',
                    description='This program will take the a JSON output from the SANS OnDemand player and convert it to CSV format (delimited by pipes |)')
parser.add_argument("-f", "--filename", type=str, default='course.json')
parser.add_argument("-o", "--output", type=str, default="course_output.csv")

args = parser.parse_args()
filename = args.filename
output_file = args.output


with open(filename, encoding='utf-8') as course_json:
  parsed_json = json.load(course_json)

output = open(output_file, 'w',encoding='utf-16')

for section in parsed_json["data"]["course"]["sections"]:
  for subsection in section["modules"]:
    for slide in subsection["slides"]:
        output.write(section["name"] + "|" + subsection["name"] + "|" + str(subsection["fullNumber"]) + "." +str(slide["number"])+ "|" + slide["name"] + "|" + slide["duration"][0:8]+'\n')

output.close()
