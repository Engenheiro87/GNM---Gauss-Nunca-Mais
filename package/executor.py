import inspect;
from package.scopes.matrix import Matrix;
from package.scopes.variable import Variable;
from package.errors import Error;

class Executor:
    __scopes = {
        "m":Matrix,
        "var": Variable,
    };
    def __init__(self, system, scope:str|object, action:str, args:str)->any:
        self.system = system;
        self.result = None;
        scope_class = self.__get_scope(scope);
        if not scope_class:
            self.__throw_error("INVALID_SCOPE", SCOPE = scope);
            return;
        if not action in scope_class.ACTIONS:
            self.__throw_error("INVALID_COMMAND", COMMAND = action);
            return;

        self.result = scope_class.ACTIONS[action](args, system=system);
        
    def __throw_error(self, code:int, **args):
        self.result = Error(code, **args);

    def __get_scope(self, scope:str):
        return (scope in self.__scopes and self.__scopes[scope]) or self.system.get_variable(scope) or None;

    @classmethod
    def scope_exists(cls, scope:str)->bool:
        return scope in cls.__scopes;