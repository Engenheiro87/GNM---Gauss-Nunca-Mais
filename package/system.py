import os;
from getpass import getpass;
from package.matrix import Matrix;
from package.util import InputObject, Numbers;

class System:
    instructionsPath = "package/instrucoes.txt";
    mode = 0;
    def __init__(self):
        self.menu();
    
    def menu(self):
        print("#"*15+"\nG.N.M. (GAUSS NUNCA MAIS)");
        print("1. Solucionar sistema.");
        print("2. Instruções.");
        print("3. Selecionar modo de solução.");
        print("4. Sair.");
        action = InputObject("Digite a próxima ação: ", int, options=(1, 2, 3, 4)).result;
        match action:
            case 1:
                Matrix(System.mode);
                return self.menu();
            case 2:
                System.instrucoes();
                return self.menu();
            case 3:
                System.set_mode();
                return self.menu();
            case 4:
                print("\nBons estudos!");
    
    @classmethod
    def set_mode(cls):
        print("\nSelecione um dos modos de operação:");
        print("1. Automático.");
        print("2. Manual.");
        action = InputObject("Insira o número correspondente: ", int, options=(1, 2)).result;
        cls.mode = action-1;

    @staticmethod
    def instrucoes():
        if not os.path.exists(System.instructionsPath):
            print("Algo deu errado. O arquivo instrucoes.txt não foi carregado.");
            return;
        with open(System.instructionsPath, "r") as file:
            print("\n"+file.read()+"\n");
            getpass("Pressione enter para continuar...");

    @staticmethod
    def get_mode():
        return System.mode

