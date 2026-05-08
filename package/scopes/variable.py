from package.errors import Error;

class Variable:
    @staticmethod
    def all(args:str, **kwargs):
        kwargs["system"].display_variables();
    
    @staticmethod
    def delete(args:str, **kwargs):
        if not args or type(args)!=str:
            return Error("MSNG_ARGS");
        kwargs["system"].delete_variable(args);
    
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
    };