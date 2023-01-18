import mistletoe
import os

#Write report from markdown file `input_filename` to file stream `target`
def WriteReport(target, input_filename):
	target.write(f"<div id='{input_filename}'>")
	with open(f"reports/{input_filename}") as input:
		target.write(mistletoe.markdown(input))
	target.write("</div>\n<br><hr><br>\n")

with open("output/index.html", "x") as out:
	with open("output/index.html", "x") as out_all:
		filelist = os.listdir("reports")
		#We want the latest first, so it'll be the last alphabetically if numbered ascendingly
		filelist.reverse()

		for index, file in enumerate(filelist):
			#Only write the first three reports to the index file
			if index < 3:
					WriteReport(out, file)
				
				#Always write to the out_all file
				WriteReport(out_all, file)
