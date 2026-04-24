from package.util import Numbers;

class CommandSolver:
    def __init__(self, matrix):
        self.matrix = matrix;
        self.commands = {
            "swap":self.command_swap,
            "scale":self.command_scale,
            "add":self.command_add,
        };
        self.get_command();

    def get_command(self):
        command_input = input("\nRun command | ");
        result = self.interpret_command(command_input);
        if result == False:
            return;
        self.matrix.displayMatrix();
        self.get_command();

    def interpret_command(self, command_input:str):
        if command_input.lower() == "exit" or command_input.lower() == "exit()":
            return False;
        arguments = list(map(CommandSolver.process_input, command_input.split(" ")));
        self.commands.get(arguments[0], self.failed_command)(attempt=arguments[0], arguments=arguments);

    def failed_command(self, attempt:str, **kwargs):
        return print(f"\"{attempt}\" não é um comando válido!");

    def command_add(self, arguments, **kwargs):
        if not CommandSolver.countArguments(arguments, 3):
            return;
        m = self.matrix.matrix;
        line1 = CommandSolver.getArgument(arguments, 1)-1;
        line2 = CommandSolver.getArgument(arguments, 3)-1;
        scalar = CommandSolver.getArgument(arguments, 2, float);
        for lineNum in (line1, line2):
            if not self.matrix.lineExists(lineNum):
                return print(f"Não existe linha \"{lineNum+1}\"!");
        self.matrix.linha_escalar_linha(
            m[line1],
            scalar,
            m[line2]
        );

    def command_scale(self, arguments, **kwargs):
        if not CommandSolver.countArguments(arguments, 2):
            return;
        lineNum = CommandSolver.getArgument(arguments, 1)-1;
        scalar = CommandSolver.getArgument(arguments, 2, float);
        if not self.matrix.lineExists(lineNum):
            return print(f"Não existe linha \"{lineNum+1}\"");
        self.matrix.linha_escalar(
            self.matrix.matrix[lineNum],
            scalar
        );

    def command_swap(self, arguments, **kwargs):
        if not CommandSolver.countArguments(arguments, 2):
            return;
        arg1 = CommandSolver.getArgument(arguments, 1)-1;
        arg2 = CommandSolver.getArgument(arguments, 2)-1;
        for x in (arg1, arg2):
            if not self.matrix.lineExists(x):
                return print(f"Não existe linha \"{x+1}\"!");
        self.matrix.permutar(arg1, arg2);

    @staticmethod
    def countArguments(argList:list, expected:int)->bool:
        if len(argList)-1!= expected:
            print(f"Invalid amount of arguments. Expected {expected}, got {len(argList)-1}");
            return False;
        return True;

    @staticmethod
    def getArgument(args:list, num:int, formatExpected=int)->any:
        try:
            return formatExpected(args[num]);
        except:
            while True:
                print(f"Invalid format for argument \"{args[num]}\". Expected {formatExpected!=str and "num" or "str"}");
                try:
                    return formatExpected(input("Try again: "));
                except:
                    continue;

    @staticmethod
    def process_input(x:any)->any:
        for function in (int, float, Numbers.getFraction, str):
            try:
                if "/" in x:
                    components = list(map(int, x.split('/')));
                    return components[0]/components[1];
                return function(x);
            except:
                continue;