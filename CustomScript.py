from antlr4 import *
from CustomScriptLexer import CustomScriptLexer
from CustomScriptListener import CustomScriptListener
from CustomScriptParser import CustomScriptParser
import sys

forloopcounter = 0
ifcounter = 0
finalString = ""

def createArg(arg):
    out = ""
    if arg.ARG1() is not None:
        out += "%1"
    if arg.ARG2() is not None:
        out += "%2"
    if arg.ARG3() is not None:
        out += "%3"
    if arg.ARG4() is not None:
        out += "%4"
    if arg.ARG5() is not None:
        out += "%5"
    if arg.ARG6() is not None:
        out += "%6"
    if arg.ARG7() is not None:
        out += "%7"
    if arg.ARG8() is not None:
        out += "%8"
    if arg.ARG9() is not None:
        out += "%9"
    if arg.LARG1() is not None:
        out += "%~1"
    if arg.LARG2() is not None:
        out += "%~2"
    if arg.LARG3() is not None:
        out += "%~3"
    if arg.LARG4() is not None:
        out += "%~4"
    if arg.LARG5() is not None:
        out += "%~5"
    if arg.LARG6() is not None:
        out += "%~6"
    if arg.LARG7() is not None:
        out += "%~7"
    if arg.LARG8() is not None:
        out += "%~8"
    if arg.LARG9() is not None:
        out += "%~9"
    return out

def createOperator(operator):
    out = ""
    if operator.NUMBER() is not None:
        out += str(operator.NUMBER())
    if operator.IDENTIFIER() is not None:
        out += "%" + str(operator.IDENTIFIER()) + "%"
    if operator.arg() is not None:
        out += createArg(operator.arg())
    return out

def createOperation(operation):
    out = createOperator(operation.operator()[0])
    out += " " + str(operation.OPERAND()) + " "
    out += createOperator(operation.operator()[1])
    return out

def createVar(var):
    out = "set "
    if var.NUMBERVAR() is not None:
        out += "/a "
    if var.IDENTIFIER() is not None:
        out += str(var.IDENTIFIER()) + "="
    if var.arg() is not None:
        out += createArg(var.arg()) + " "
    if var.NUMBER() is not None:
        out += str(var.NUMBER())
    if var.TEXT() is not None:
        out += str(var.TEXT())
    if var.operation() is not None:
        out += createOperation(var.operation())
    return out

def createCommand(text):
    formatted = str(text.TEXT()).strip()
    formatted = formatted[1:len(formatted)-1]
    formatted = formatted.replace("\\\"", "\"")
    if text.IDENTIFIER() is not None:
        formatted += " %" + str(text.IDENTIFIER()) + "%"
    if text.arg() is not None:
        formatted += " " + createArg(text.arg())
    return formatted


def createFunctionInput(funInput):
    out = ""
    l = []
    if funInput.functioninputpart() is not None:
        for i in funInput.functioninputpart():
            if i.NUMBER() is not None:
                l.append(str(i.NUMBER()))
            if i.TEXT() is not None:
                formatted = str(i.TEXT()).strip()
                formatted = formatted[1:len(formatted)-1]
                formatted = formatted.replace("\\\"", "\"")
                l.append(formatted)
            if i.IDENTIFIER() is not None:
                l.append("%" + str(i.IDENTIFIER()) + "%")
            if i.arg() is not None:
                l.append(createArg(i.arg()))

        out = ",".join(str(x) for x in l)
    return out

def createFunctionCall(call):
    out = "call :"
    out += str(call.IDENTIFIER())
    if call.functioninput() is not None:
        out += " " + createFunctionInput(call.functioninput())
    return out

def createOp(op):
    out = createCommand(op.command())
    if len(op.addon()) > 0:
        for index in range(0, len(op.addon())):
            addon = op.addon()[index]
            if addon.redirect().customin() is not None:
                out += " < "
            if addon.redirect().out() is not None:
                out += " > "
            if addon.redirect().to() is not None:
                out += " | "
            if addon.command() is not None:
                out += createCommand(addon.command())
    return out

def createLine(line):
    out = ""
    if line.op() is not None:
        out += createOp(line.op())
    if line.var() is not None:
        out += createVar(line.var())
    if line.functioncall() is not None:
        out += createFunctionCall(line.functioncall())
    out += "\n"
    return out

def createConditionPart(part):
    out = ""
    if part.NUMBER() is not None:
        out += str(part.NUMBER())
    if part.TEXT() is not None:
        out += str(part.TEXT())
    if part.IDENTIFIER() is not None:
        out += "%" + str(part.IDENTIFIER()) + "%"
    if part.arg() is not None:
        out += createArg(part.arg())
    return out

def createConditional(conditional):
    out = ""
    out += createConditionPart(conditional.conditionpart()[0])
    if str(conditional.CONDITION()) == "==":
        out += " EQU "
    if str(conditional.CONDITION()) == "!=":
        out += " NEQ "
    if str(conditional.CONDITION()) == "<":
        out += " LSS "
    if str(conditional.CONDITION()) == ">":
        out += " GTR "
    if str(conditional.CONDITION()) == "<=":
        out += " LEQ "
    if str(conditional.CONDITION()) == ">=":
        out += " GEQ "
    out += createConditionPart(conditional.conditionpart()[1])
    return out

def createFor(f):
    out = ""
    iterator = str(f.var().IDENTIFIER())
    out += createVar(f.var()) + "\n"
    out += ":FORLOOP" + str(forloopcounter) + "\n"
    out += "if /I NOT " + createConditional(f.conditional()) + " GOTO FOREND" + str(forloopcounter) + "\n"
    for line in  f.line():
        out+= createLine(line)
    out += "set /a " + iterator + "=" + createOperation(f.operation()) + "\n"
    out += "GOTO :FORLOOP" + str(forloopcounter) + "\n"
    out += ":FOREND" +  str(forloopcounter) + "\n"
    return out

def createIf(f):
    out = "if /I NOT "
    out += createConditional(f.conditional()) + " GOTO IFEND" + str(ifcounter) + "\n"
    for line in f.line():
        out+= createLine(line)
    out += ":IFEND" +  str(ifcounter) + "\n"
    return out

def createFunction(f):
    out = ":" + str(f.IDENTIFIER()) + "\n"
    for line in f.line():
        out+= createLine(line)
    out += "EXIT /B 0\n"
    return out

class CustomPrintListener(CustomScriptListener):


    def enterScript(self, ctx):
        for element in ctx.scriptelement():
            global forloopcounter, ifcounter, file
            if element.line() is not None:
                file.write(createLine(element.line()))
            if element.forstatement() is not None:
                file.write(createFor(element.forstatement()))
                forloopcounter+=1
            if element.ifstatement() is not None:
                file.write(createIf(element.ifstatement()))
                ifcounter+=1
        file.write("@EXIT /B 0\n")
        for fun in ctx.functionstatement():
            if fun is not None:
                file.write(createFunction(fun))



def main(argv):
    global file
    input_stream = FileStream(argv[1])
    file = open(argv[2], "w")
    file.write(":: Name:\t" + argv[2]+"\n")
    file.write("@echo off\n")
    file.write("SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION\n")

    lexer = CustomScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CustomScriptParser(stream)
    tree = parser.script()
    printer = CustomPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
