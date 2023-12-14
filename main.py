import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Provide path to 2005 SLN file")
    
    # read sln file
    slnPath = sys.argv[1]
    with open(slnPath, "rt") as slnFile:
        sln = slnFile.readlines()
    
    # find and parse projects
    for (i, line) in enumerate(sln):
        if not line.startswith("Project"):
            continue

        tokens = line.split(" ")
        projectName = tokens[2][1:-2]
        projectPath = tokens[3][1:-2]

        newPath = projectPath.replace("-2005", "")
        tokens[3] = "\"{0}\",".format(newPath)

        sln[i] = " ".join(tokens)

    # write output sln file
    slnPath = slnPath.replace("-2005", "")
    with open(slnPath, "w") as slnFile:
        slnFile.writelines(sln)