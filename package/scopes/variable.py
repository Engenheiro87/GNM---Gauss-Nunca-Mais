from package.errors import Error;
from copy import deepcopy;

class Variable:
    @staticmethod
    def all(args:str, **kwargs):
        kwargs["system"].display_variables();
    
    @staticmethod
    def delete(args:str, **kwargs):
        if not args or type(args)!=str:
            return Error("MSNG_ARGS");
        return kwargs["system"].delete_variable(args);

    @staticmethod
    def delete2(args:str, **kwargs):
        if not args or type(args)!=str:
            return Error("MSNG_ARGS");
        Variable.delete(args, **kwargs);
    
    @staticmethod
    def __copy(args:str, **kwargs):
        if not args:
            return Error("MSNG_ARGS");
        components = args.strip().split();
        if len(components)>1:
            return Error("INCRRT_ARGS", EXPECTED=1, AMOUNT=len(components));
        existing_variable = kwargs["system"].get_variable(components[0]);
        if not existing_variable:
            return Error("UNKWN_VAR", VAR=components[0]);
        return deepcopy(existing_variable);

    
    
    @staticmethod
    def show(args:str, **kwargs):
        if not args or type(args)!=str:
            return Error("MSNG_ARGS");
        for x in args.split(): kwargs["system"].display_variable(x);
    
    @staticmethod
    def __focus(args:str, **kwargs):
        #var focus matriz1
        kwargs["system"].focus_variable(args);
    
    @staticmethod
    def __reset(args:str, **kwargs):
        return kwargs["system"].focus_variable(None);
    
    ACTIONS = {
        "all":all,
        "del":delete,
        "show":show,
        "focus":__focus,
        "reset":__reset,
        "del/":delete2,
        "copy":__copy,
    };