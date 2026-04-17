from package.util import Numbers;

class CommandSolver:
    def __init__(self, matrix):
        self.matrix = matrix;
        self.get_command();

    def get_command(self):
        command_input = input("\nRun Command | ");
        self.interpret_command(command_input);

    def interpret_command(self, command_input:str):
        if command_input.lower() == "exit" or command_input.lower() == "exit()":
            return;
        arguments = list(map(CommandSolver.process_input, command_input.split(" ")));
        if arguments[0] == "swap":
            self.matrix.permutar(arguments[1]-1, arguments[2]-1);
        elif arguments[0] == "scale":
            self.matrix.linha_escalar(
                self.matrix.matrix[arguments[1]-1],
                arguments[2]
            );
        elif arguments[0] == "add":
            m = self.matrix.matrix;
            self.matrix.linha_escalar_linha(
                m[arguments[1]-1],
                arguments[2],
                m[arguments[3]-1]
            );
        else:
            print(f"\"{command_input}\" não é um comando válido!");
        
        self.matrix.displayMatrix();
        self.get_command();
    
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