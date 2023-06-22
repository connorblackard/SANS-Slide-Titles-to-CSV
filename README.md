# SANS Slide Titles to CSV

# Project Description
This script is a tool used to extract the SANS On Demand slide titles and durations and output to a CSV file.

# Why
I made this script because I am in the SANS MSISE program. Working full time and doing a masters program requires strong time management skills. Part of my orgnaizational process was entering each module name and module length to a spreadsheet so I can project milestones in the course I would need to reach to remain on track. This process was usually 20-30 minutes of copy and pasting for each course. I have 7 more On Demand courses in the program so it made sense to spend a half hour to make a tool to do this and maybe save others some time.

# How to Use
1. Login to the SANS website and navigate to your On Demand course
2. Open Chrome and press F12 to open Developer Tools
3. Select the "Network" tab at the top bar
4. Type "graphql" in the filter bar
5. Select an entry and select the "Payload" tab
6. Look through all the entries until you find one that has the key value pair `OperationName: CourseQuery`
7. Once you find that entry, select the "Payload" tab
8. Copy the entire contents of this field (note: this will be a lot of content and you will have to scroll down quite a ways)
9. Create a text file on your computer called "course.json" in the same directory as the script
10. Run the script with Python
11. Open a blank excel sheet
12. Click the "Data" tab
13. Click "From Text/CSV"
14. Navigate to your course_output.csv file and select "Import"
15. Make sure the delimeter is set to "|" and Data Type Detection is set to "Do not detect data types"
16. Select Load

Now you should have a nicely organized list of the Section, Module, Slide Number, Slide Name, and Duration to use for planning purposes. You'll likely need to adjust the column names and data types to make this work for your purposes.


# FAQ

1. Can I use firefox?
   
   Probably, just lookup the key for developer tools and it should be similar.

2. I am getting errors about "UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position ..."
   
   That is likely an odd character. Open the json file in your favorite text editor and replace or escape the character as needed.
