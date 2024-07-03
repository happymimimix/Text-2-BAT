import time
from tkinter import filedialog, Tk
Tk().withdraw()
while True:
    print('\033[2J\033[HOutput mode selection: ')
    print('\n  1. Output using the ECHO command (Line split: ^\\n)')
    print('\n  2. Output using the ECHO command (Line split: \\n@ECHO)')
    print('\n  3. Pass to cmd.exe and run as commands (No multi-line support!)')
    print('\n  4. Pass to powershell.exe and run as commands (No multi-line support!)')
    print('\n  5. Pass to powershell.exe and output using ECHO')
    print('\n  6. Show a messagebox with vbscript')
    print('\n  7. Pass to mshta.exe and run as vbscript code (No multi-line support!)')
    print('\n  8. Pass to other programs as parameters')
    OutputMode = input('\n>')
    if OutputMode == '1' or OutputMode == '2' or OutputMode == '3' or OutputMode == '4' or OutputMode == '5' or OutputMode == '6' or OutputMode == '7' or OutputMode == '8':
        break
print('\033[2J\033[HPlease select a file...')
filepath = filedialog.askopenfilename(filetypes=[('Text Document', '*.txt'),('All Files', '*.*')])
file = open(filepath, mode = 'r')
output = open(filepath+'.bat', mode = 'w')
if OutputMode == '1':
    output.write("setlocal disabledelayedexpansion&@ECHO.")
if OutputMode == '2':
    output.write("setlocal disabledelayedexpansion\n@ECHO.")
if OutputMode == '3':
    output.write("setlocal disabledelayedexpansion&CMD /C ")
if OutputMode == '4':
    output.write("setlocal disabledelayedexpansion&POWERSHELL -Command \"")
if OutputMode == '5':
    output.write("setlocal disabledelayedexpansion&POWERSHELL -Command \"ECHO \"^\"\"")
if OutputMode == '6':
    output.write("setlocal disabledelayedexpansion&mshta vbscript:msgbox(\"")
if OutputMode == '7':
    output.write("setlocal disabledelayedexpansion&mshta vbscript:execute(\"")
if OutputMode == '8':
    output.write("setlocal disabledelayedexpansion&YourProgram.exe \"")
FirstLine = True
for Line in file.readlines():
    if OutputMode == '1':
        output.write(("" if FirstLine else "^\n\n") + Line.rstrip('\n').replace("^", "^^").replace("\"", "^\"").replace("!", "^!").replace("%", "^%%").replace("&", "^&").replace("<", "^<").replace(">", "^>").replace("|", "^|"))
    if OutputMode == '2':
        output.write(("" if FirstLine else "\n@ECHO.") + Line.rstrip('\n').replace("^", "^^").replace("\"", "^\"").replace("!", "^!").replace("%", "^%%").replace("&", "^&").replace("<", "^<").replace(">", "^>").replace("|", "^|"))
    if OutputMode == '3':
        output.write(("" if (FirstLine or Line.rstrip('\n').strip() == "") else "^&") + Line.rstrip('\n').replace("%%", "%").replace("^", "^^").replace("\"", "^\"").replace("!", "^!").replace("%", "^%%").replace("&", "^&").replace("<", "^<").replace(">", "^>").replace("|", "^|"))
    if OutputMode == '4':
        output.write(("" if (FirstLine or Line.rstrip('\n').strip() == "") else ";") + Line.rstrip('\n').replace("%", "%%").replace("\"", "\"^\"\""))
    if OutputMode == '5':
        output.write(("" if FirstLine else "\"^\"\" \"^\"\"") + Line.rstrip('\n').replace("`", "``").replace("$", "`$").replace("%", "%%").replace("\"", "`\"^\"\""))
    if OutputMode == '6':
        output.write(("" if FirstLine else "\"+vbCrLf+\"") + Line.rstrip('\n').replace("%", "%%").replace("\"", "\"\""))
    if OutputMode == '7':
        output.write(("" if FirstLine else ":") + Line.rstrip('\n').replace("%", "%%").replace("\"", "\"\""))
    if OutputMode == '8':
        output.write(("" if FirstLine else "\" \"") + Line.rstrip('\n').replace("%", "%%").replace("\"", "\"\""))
    FirstLine = False
if OutputMode == '1':
    output.write("&endlocal")
if OutputMode == '2':
    output.write("\nendlocal")
if OutputMode == '3':
    output.write("&endlocal")
if OutputMode == '4':
    output.write("\"&endlocal")
if OutputMode == '5':
    output.write("\"^\"\"\"&endlocal")
if OutputMode == '6':
    output.write("\",48,\"Title\")(window.close)&endlocal")
if OutputMode == '7':
    output.write("\")(window.close)&endlocal")
if OutputMode == '8':
    output.write("\"&endlocal")
output.close()
print('\033[2J\033[HTask completed! ')
time.sleep(3)
