from package.parser import Parser;
from package.executor import Executor;
from package.errors import Error;
from colorama import init, Fore, Back, Style;
init(autoreset=True);
class System:
    def __init__(self, block=False):
        self.__memory = {};
        self.__focused_var = None;
        print("[G_NM] - Gauss Nunca Mais (v2.0.0)\n");
        if not block:
            self.start_prompt();
    
    @property
    def memory(self):
        return self.__memory;

    def start_prompt(self):
        try:
            raw_input = input("Run Command | ");
            if raw_input.lower() == "exit":
                return self.__exit();
            if raw_input.lower()=="help":
                self.__show_instructions()
                return self.start_prompt();
            self.run_command(self.__add_focused_variable(raw_input)+raw_input);
        except KeyboardInterrupt:
            self.__exit();
    
    def __exit(self):
        print(". . .");

    def __show_instructions(self):
        file_path = "package/instructions.txt";
        try:
            with open(file_path, encoding="utf-8") as file:
                print(file.read());
        except:
            return Error("NO_INSTRCTNS");

    def run_command(self, command:str):
        parsed_command = Parser.parse_command(command);
        if type(parsed_command)==Error:
            return self.start_prompt();
        result = Executor(self, parsed_command.scope, parsed_command.action, parsed_command.args).result;
        if type(result)!=Error and result!=None:
            if parsed_command.variable_name:
                self.__set_variable(parsed_command.variable_name, result);
            else:
                print(result);
        self.start_prompt();
    
    def get_variable(self, var_name:str)->any|None:
        return var_name in self.memory and self.memory[var_name] or None;
    
    def display_variables(self):
        for name, item in self.__memory.items():
            print(f"\"{name}\" =");
            print(item);
    
    def delete_variable(self, vars:str):
        cached_variable = None;
        for var_name in vars.split():
            if not var_name in self.__memory:
                return Error("UNKWN_VAR", VAR=var_name);
            if self.__focused_var == var_name:
                self.focus_variable(None);
            cached_variable = self.__memory.pop(var_name);
        return cached_variable;
    
    def display_variable(self, var_name:str):
        if not var_name in self.__memory:
            return Error("UNKWN_VAR", VAR=var_name);
        print(f"\"{var_name}\" =");
        print(self.__memory[var_name]);
    
    def focus_variable(self, var_name:str|None):
        if var_name!=None:
            if not var_name in self.memory:
                return Error("UNKWN_VAR", VAR=var_name);
            print(Fore.BLUE+f"(@) Focused on variable \"{var_name}\"");
        self.__focused_var = var_name;

    def __add_focused_variable(self, raw_cmd:str)->str:
        if not self.__focused_var or "var " in raw_cmd:
            return "";
        return self.__focused_var+" ";
    
    def __set_variable(self, var_name:str, value:any):
        if Executor.scope_exists(var_name):
            return Error("FRBDDN_VAR", NAME=var_name);
        elif self.__focused_var:
            return Error("VAR_CRTN1");
        elif " " in var_name:
            return Error("VAR_CRTN2", VARNAME=var_name, MESSAGE="Cannot contain spaces");
        self.__memory[var_name] = value;
