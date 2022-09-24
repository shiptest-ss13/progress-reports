import mistletoe
import os

with open("output/index.html", "x") as out:
    filelist = os.listdir("reports")
    filelist.reverse()
    for file in filelist:
        out.write(f"<div id='{file}'>")
        with open(f"reports/{file}") as input:
            out.write(mistletoe.markdown(input))
        out.write("</div>\n<br><hr><br>\n")
