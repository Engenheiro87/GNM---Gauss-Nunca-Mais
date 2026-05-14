from colorama import init, Fore, Back, Style
init(autoreset=True);
class Error:    
    def __init__(self, code:str, **args):
        er_info = ERRORS.get(code);
        print(Fore.RED+Style.BRIGHT+f"(!) Error ({code})");
        print(
            Fore.RED+Style.NORMAL+
            self.replace_args(er_info.get("content"), args)
        );
    
    def replace_args(self, message:str, args:dict)->str:
        for key, value in args.items():
            message = message.replace("{%s}"% key, str(value));
        return message;

ERRORS = {
    "INVALID_SCOPE": {
        "content":"Unknown scope \"{SCOPE}\".",
    },
    "INVALID_COMMAND":{
        "content":"Unknown command \"{COMMAND}\"."
    },
    "MISS_CMD":{
        "content":"Syntax Error: Missing command.",
    },
    "MISS_SCP_ACTN":{
        "content":"Syntax Error: Missing scope or function.",
    },
    "UNKWN_VAR":{
        "content":"Unknown variable \"{VAR}\"",
    },
    "MSNG_ARGS":{
        "content":"Syntax Error: Missing arguments (this function demands arguments)",
    },
    "INCRRT_ARGS":{
        "content":"Syntax Error: Wrong argument count. Expected {EXPECTED}, got {AMOUNT}."
    },
    "INCRRT_TYPE":{
        "content":"Syntax Error: Incorrect type for variable \"{VAR}\", expected \"{EXPECTED}\" got \"{GOT}\""
    },
    "NO_LINE":{
        "content":"Index Error: Line \"{LINE}\" does not exist. Max = \"{MAX}\".",
    },
    "MFRMD_MTRX":{
        "content":"Syntax Error: Malformed Matrix (Line {LINE})",
    },
    "INCSTNT_LNGTH":{
        "content":"Syntax Error: Inconsistent row length. All rows must have the same length.",
    },
    "FRBDDN_VAR":{
        "content":"Forbidden: Name \"{NAME}\" is reserved.",
    },
    "NO_INSTRCTNS":{
        "content":"Could not find the instructions file.",
    },
    "INCMPTBLTY_M1":{
        "content":"Compatibility Error: Not all matrices are from the same order."
    },
    "TYPE_ERR1":{
        "content":"Type Error: Not all arguments are from type \"{TYPE}\"."
    },
    "TYPE_ERR2":{
        "content":"Type Error: Argument \"{ARG}\" is not from required type \"{TYPE}\"."
    },
    "VAR_CRTN1":{
        "content":"Forbidden: Cannot create variable while in \"focus\" mode."
    },
    "VAR_CRTN2":{
        "content":"Invalid variable name \"{VARNAME}\" ({MESSAGE})"
    }
}

if __name__ == "__main__":
    Error("INVALID_SCOPE", SCOPE="banana");