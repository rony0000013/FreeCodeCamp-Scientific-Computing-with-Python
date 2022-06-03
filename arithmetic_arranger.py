import re

def arithmetic_arranger(problems,value = False):

    if len(problems) > 5:
        return "Error: Too many problems."
    
    line1 , line2 ,line3 ,line4 = [] , [] , [] , []
    for problem in problems:
        
        operator = re.findall("\s([+|-])\s",problem)
        if (len(operator) == 0):
            return "Error: Operator must be '+' or '-'."

        num1 = problem.split(" ")[0]
        num2 = problem.split(" ")[2]
        try:
            num3 = int(num1) + int(num2) if (operator[0] == "+") else int(num1) - int(num2)
        except:
            return "Error: Numbers must only contain digits."
        
        str(num1),str(num2)
        if (len(num1) > 4) or (len(num2) > 4):
            return "Error: Numbers cannot be more than four digits."

        length = max(len(num1),len(num2)) + 2

        temp = ""
        for i in range(length - len(num1)):
            temp += " "
        temp += num1
        line1.append(temp)

        temp = "" + operator[0]
        for i in range(length - len(num2) -1):
            temp += " "
        temp += num2
        line2.append(temp)

        temp = ""
        for i in range(length):
            temp += "-"
        line3.append(temp)

        temp = ""
        num3 = str(num3)
        for i in range(length - len(num3)):
            temp += " "
        temp += num3
        line4.append(temp)

    line1str = "    ".join(line1)
    line2str = "    ".join(line2)
    line3str = "    ".join(line3)
    line4str = "    ".join(line4)

    if value == True:
        return line1str + "\n" + line2str + "\n" + line3str + "\n" + line4str
    return line1str + "\n" + line2str + "\n" + line3str 


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))