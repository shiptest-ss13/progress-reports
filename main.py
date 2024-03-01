import mistletoe
import bs4
import os

#Write report from markdown file `input_filename` to file stream `target`
def WriteReport(target, input_filename):
	target.write(f"<details id='{input_filename}'>")
	with open(f"reports/{input_filename}", "r") as input:
		#Parse the markdown file and convert it to HTML
		content = mistletoe.markdown(input)
		soup = bs4.BeautifulSoup(content, "html.parser")

		#Find the first header in the report and use it as the summary
		title = soup.h1 or soup.h2 or soup.h3
		target.write(f"<summary>{title.text}</summary>\n")
		
		#Write the report content
		target.write(content)
	target.write("</details>\n<br><hr>\n")

with open("output/index.html", "w") as out:
	with open("output/all.html", "w") as out_all:
		filelist = os.listdir("reports")
		filelist.sort(reverse=True)

		with open("templates/header.html") as header:
			out_all.write(header.read())

		for index, file in enumerate(filelist):
			#Only write the first three reports to the index file
			if index < 3:
				WriteReport(out, file)
				
			#Always write to the out_all file
			WriteReport(out_all, file)
		
		with open("templates/footer.html") as footer:
			out_all.write(footer.read())
