import mistletoe
import os

with open("output/index.html", "x") as out:
    filelist = []
    filelist.extend(os.listdir("reports"))
    filelist.reverse()
    for file in filelist:
        with open(f"reports/{file}") as f:
            out.write(mistletoe.markdown(f))
        out.write("<br>\n<hr>\n<br>\n")
