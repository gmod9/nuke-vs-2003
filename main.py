import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Provide path to 2005 SLN file")
    
    # read sln file
    slnPath = sys.argv[1]
    with open(slnPath, "rt") as slnFile:
        sln = slnFile.readlines()
    
    # write output sln file
    slnPath = slnPath.replace("-2005", "")
    with open(slnPath, "w") as slnFile:
        slnFile.writelines(sln)