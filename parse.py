import pytools
import sys

class secs:
    store = {}

class process:
    def chain(chainf, addif=False, mod=False):
        i = 0
        while (i + 1) < len(chainf):
            if addif == False:
                ya = chainf[i].split("[")[1].split("]")[0]
                if chainf[i].split(":")[0] == "":
                    ba = "minecraft" + chainf[i]
                else:
                    ba = chainf[i]
                yb = chainf[i + 1].split("[")[1].split("]")[0]
                if chainf[i + 1].split(":")[0] == "":
                    bb = "minecraft" + chainf[i + 1]
                else:
                    bb = chainf[i + 1]
                if mod != False:
                    ya = mod
                    yb = mod
                    yc = mod
                pytools.IO.appendFile("script.mcfunction", "execute as @e[tag=decayPoint,type=marker] if block ~ ~" + ya + " ~ " + ba.split("[")[0] + " run fill ~ ~" + yb + " ~ ~ ~" + yb + " ~ "+ bb.split("[")[0] + " replace\n")
            else:
                ya = chainf[i].split("[")[1].split("]")[0]
                if chainf[i].split(":")[0] == "":
                    ba = "minecraft" + chainf[i]
                else:
                    ba = chainf[i]
                yb = chainf[i + 1].split("[")[1].split("]")[0]
                command = "execute as @e[tag=decayPoint,type=marker] "
                if chainf[i + 1].split(":")[0] == "":
                    bb = "minecraft" + chainf[i + 1]
                else:
                    bb = chainf[i + 1]
                if mod != False:
                    ya = mod
                    yb = mod
                    yc = mod
                for ifn in addif:
                    yc = ifn.split("[")[1].split("]")[0]
                    if ifn.split(":")[0] == "":
                        bc = "minecraft" + ifn
                    else:
                        bc = ifn
                    command = command + "if block ~ ~" + yc + " ~ " + bc.split("[")[0] + " "
                pytools.IO.appendFile("script.mcfunction", command + "if block ~ ~" + ya + " ~ " + ba.split("[")[0] + " run fill ~ ~" + yb + " ~ ~ ~" + yb + " ~ " + bb.split("[")[0] + " replace\n")
            i = i + 1

def command(line, check=False, mod=False):
    i = 0
    lf = line.split("{")
    try:
        lf.remove("")
    except:
        pass
    print(lf[0][0:4])
    if lf[0] == "chain":
        process.chain(lf[1].split("}")[0].split(">"), check, mod)
    elif lf[0][0:4] == "case":
        check = lf[0].split("case")[1].split(",")
        n = lf[1:]
        run = line.split(lf[0])[1].split("/")
        for lg in run:
            command(lg, check, mod)
    elif lf[0][0:3] == "sec":
        n = lf[1:]
        secs.store[lf[0].split("[")[1].split("]")[0]] = line.split(lf[0].split("(")[0])[1].replace("(", "").replace(")", "").split("/")
        run = line.split(lf[0])[1].split("/")
        for lg in run:
            command(lg, check, mod)
    elif lf[0][0:3] == "run":
        name = lf[0].split("<")[1].split(">")[0]
        mod = lf[0].split("[")[1].split("]")[0]
        for lg in secs.store[name]:
            command(lg, check, mod)
        
    else:
        print("Invalid. " + str(lf))
                
def file(proc):
    pytools.IO.saveFile("script.mcfunction", "")
    script = pytools.IO.getFile(proc)
    lines = script.replace("    ", "").replace(" ", "").replace("\n", "").split(";")
    for line in lines:
        command(line)