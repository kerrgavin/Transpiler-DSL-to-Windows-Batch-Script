# Generated from CustomScript.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CustomScriptParser import CustomScriptParser
else:
    from CustomScriptParser import CustomScriptParser

# This class defines a complete listener for a parse tree produced by CustomScriptParser.
class CustomScriptListener(ParseTreeListener):

    # Enter a parse tree produced by CustomScriptParser#script.
    def enterScript(self, ctx:CustomScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#script.
    def exitScript(self, ctx:CustomScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#scriptelement.
    def enterScriptelement(self, ctx:CustomScriptParser.ScriptelementContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#scriptelement.
    def exitScriptelement(self, ctx:CustomScriptParser.ScriptelementContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#line.
    def enterLine(self, ctx:CustomScriptParser.LineContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#line.
    def exitLine(self, ctx:CustomScriptParser.LineContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#op.
    def enterOp(self, ctx:CustomScriptParser.OpContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#op.
    def exitOp(self, ctx:CustomScriptParser.OpContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#addon.
    def enterAddon(self, ctx:CustomScriptParser.AddonContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#addon.
    def exitAddon(self, ctx:CustomScriptParser.AddonContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#redirect.
    def enterRedirect(self, ctx:CustomScriptParser.RedirectContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#redirect.
    def exitRedirect(self, ctx:CustomScriptParser.RedirectContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#var.
    def enterVar(self, ctx:CustomScriptParser.VarContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#var.
    def exitVar(self, ctx:CustomScriptParser.VarContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#command.
    def enterCommand(self, ctx:CustomScriptParser.CommandContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#command.
    def exitCommand(self, ctx:CustomScriptParser.CommandContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#customin.
    def enterCustomin(self, ctx:CustomScriptParser.CustominContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#customin.
    def exitCustomin(self, ctx:CustomScriptParser.CustominContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#out.
    def enterOut(self, ctx:CustomScriptParser.OutContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#out.
    def exitOut(self, ctx:CustomScriptParser.OutContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#to.
    def enterTo(self, ctx:CustomScriptParser.ToContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#to.
    def exitTo(self, ctx:CustomScriptParser.ToContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#ifstatement.
    def enterIfstatement(self, ctx:CustomScriptParser.IfstatementContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#ifstatement.
    def exitIfstatement(self, ctx:CustomScriptParser.IfstatementContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#forstatement.
    def enterForstatement(self, ctx:CustomScriptParser.ForstatementContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#forstatement.
    def exitForstatement(self, ctx:CustomScriptParser.ForstatementContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#functionstatement.
    def enterFunctionstatement(self, ctx:CustomScriptParser.FunctionstatementContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#functionstatement.
    def exitFunctionstatement(self, ctx:CustomScriptParser.FunctionstatementContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#functioncall.
    def enterFunctioncall(self, ctx:CustomScriptParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#functioncall.
    def exitFunctioncall(self, ctx:CustomScriptParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#functioninput.
    def enterFunctioninput(self, ctx:CustomScriptParser.FunctioninputContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#functioninput.
    def exitFunctioninput(self, ctx:CustomScriptParser.FunctioninputContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#functioninputpart.
    def enterFunctioninputpart(self, ctx:CustomScriptParser.FunctioninputpartContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#functioninputpart.
    def exitFunctioninputpart(self, ctx:CustomScriptParser.FunctioninputpartContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#operation.
    def enterOperation(self, ctx:CustomScriptParser.OperationContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#operation.
    def exitOperation(self, ctx:CustomScriptParser.OperationContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#operator.
    def enterOperator(self, ctx:CustomScriptParser.OperatorContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#operator.
    def exitOperator(self, ctx:CustomScriptParser.OperatorContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#conditional.
    def enterConditional(self, ctx:CustomScriptParser.ConditionalContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#conditional.
    def exitConditional(self, ctx:CustomScriptParser.ConditionalContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#conditionpart.
    def enterConditionpart(self, ctx:CustomScriptParser.ConditionpartContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#conditionpart.
    def exitConditionpart(self, ctx:CustomScriptParser.ConditionpartContext):
        pass


    # Enter a parse tree produced by CustomScriptParser#arg.
    def enterArg(self, ctx:CustomScriptParser.ArgContext):
        pass

    # Exit a parse tree produced by CustomScriptParser#arg.
    def exitArg(self, ctx:CustomScriptParser.ArgContext):
        pass


