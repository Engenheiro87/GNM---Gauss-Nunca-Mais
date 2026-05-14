class ParsedCommand:
    def __init__(self, scope:str, action:str, args:list, variable=None):
        self.variable_name = variable;
        self.scope = scope;
        self.action = action;
        self.args = args;
        pass;
    
    def __str__(self):
        return f"""
Parsed command:
variable_name = {self.variable_name};
scope = {self.scope};
action = {self.action};
args = {self.args}.
"""