from package.models.parsed_command import ParsedCommand;
from package.errors import Error;

class Parser:
    @staticmethod
    def parse_command(cmd:str)->ParsedCommand:
        variable_name = None;
        if "=" in cmd:
            split = cmd.split("=", 1);
            variable_name = split[0].strip();
            cmd = len(split)>=2 and split[1].strip() or None;
            if not cmd:
                return Error("MISS_CMD");
        components = cmd.strip().split();
        if len(components)<2:
            return Error("MISS_SCP_ACTN");
        scope = components[0];
        action = components[1];
        args = len(components)>=3 and " ".join(components[2:]);
        return ParsedCommand(scope, action, args, variable=variable_name);
        
    @staticmethod
    def clean_nulls(list:list)->list:
        return [x for x in list if x!=None and x!=""];

    @staticmethod
    def convert_to_num(string:str)->float|int:
        if "/" in string:
            components = list(map(float, string.split("/")));
            return components[0]/components[1];
        else:
            try:
                return float(string);
            except:
                return 0;

if __name__ == "__main__":
    parsed_command = Parser.parse_command("matrix1 = m create 1 2 3; 4 5 6; 7 8 9");
    print(parsed_command);