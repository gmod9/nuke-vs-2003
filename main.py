import os
import sys

def process(slnPath, project, new):
    projectPath = os.path.join(slnPath, project)
    newPath = os.path.join(slnPath, new)
    oldPath = projectPath.replace("-2005", "-2003")
    
    if not os.path.exists(projectPath):
        print("{0} project not found!".format(projectPath))
        return

    try:
        # delete vs 2003 project
        if os.path.exists(oldPath):
            os.remove(oldPath)

        # rename vs 2005 project to normal name
        os.rename(projectPath, newPath)

        print(projectPath, " -> ", newPath)
    except Exception as e:
        print("{0}: {1}".format(projectPath, str(e)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Provide path to 2005 SLN file")
    
    # read sln file
    slnDir = os.path.dirname(sys.argv[1])
    slnPath = os.path.join(slnDir, sys.argv[1])
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

        process(slnDir, projectPath, newPath)

        sln[i] = " ".join(tokens)

    # write output sln file
    slnPath = slnPath.replace("-2005", "")
    with open(slnPath, "w") as slnFile:
        slnFile.writelines(sln)