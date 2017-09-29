import os
import subprocess

def file(*path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *path)

TEMPLATE = """
### %d. %s
\\newpage
"""

with open(file("statements.md"), "w") as target:
    target.write("---\ngeometry: margin=2cm\nfontsize: 14pt\ndocumentclass: extreport\n---\n\\pagenumbering{gobble}\n")
    with open(file("order.txt")) as order:
        for index, directory in enumerate(order, 1):
            with open(file(directory[:-1], "description.md")) as source:
                target.write(TEMPLATE % (index, source.read()[3:]))

subprocess.run(["pandoc", "statements.md", "-o", "statements.pdf"], cwd=file())
subprocess.run(["pdfjam", "--nup", "2x2", "-o", "statements-small.pdf", "--no-landscape", "statements.pdf"], cwd=file())
