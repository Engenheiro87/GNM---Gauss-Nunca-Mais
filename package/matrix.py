from package.util import InputObject, Numbers;
from package.command import CommandSolver;

class Matrix:
    def __init__(self, mode):
        self.matrix = [];
        self.focus = 0;
        self.mode = mode;
        self.linhas = InputObject("Quantas linhas?: ", int).result;
        self.colunas = InputObject("Quantas colunas?: ", int).result;
        for i in range(self.linhas):
            self.matrix.append(self.get_new_row(i));
        self.displayMatrix();
        if self.mode==0:
            self.operar();
        else:
            CommandSolver(self);
    
    def lineExists(self, lineNum:int)->bool:
        m = self.matrix;
        return not (lineNum<0 or lineNum+1>len(m));
    
    def get_new_row(self, iteration:int)->list:
        newRow = list(map(Numbers.processNumber, input("Linha %d: " % (iteration+1)).split(" ")));
        if len(newRow) != self.colunas:
            print("Número incorreto de colunas inserido. Tente novamente.");
            return self.get_new_row(iteration);
        return newRow;
    
    def displayMatrix(self):
        length = len(self.matrix);
        for i in range(length):
            print(self.get_row_as_string(i));
        print("-"*15+"\n");

    def get_row_as_string(self, rowIndex:int):
        length = len(self.matrix);
        corners = Matrix.getCorner(rowIndex, length);
        row = self.matrix[rowIndex];
        converted = [Numbers.getFraction(x) for x in row];
        return f"{corners[0]}{str(converted).replace(",", "").replace("'", "")[1:-1]}{corners[1]}";

    def permutar(self, l1:int, l2:int):
        m = self.matrix;
        m[l1], m[l2] = m[l2], m[l1];
        print(f"Permutando L{l1+1} -> L{l2+1}" if l1!=l2 else "Sem permutações.");
        return self;
    
    def linha_escalar(self, row, scalar):
        rowIndex = self.get_row_index(row);
        print(f"L{rowIndex+1} -> L{rowIndex+1}*{Numbers.getFraction(scalar)}");
    
        new_row = [x*scalar for x in row];
        self.matrix[self.get_row_index(row)] = new_row;
        return self;

    def linha_escalar_linha(self, row1:list, scalar:int|float, row2:list):
        new_row = row1.copy();
        for i in range(len(row1)):
            new_row[i] = row1[i]+scalar*row2[i];

        row1_index = self.get_row_index(row1);
        row2_index = self.get_row_index(row2);
        print(f"L{row1_index+1} -> L{row1_index+1} {"+" if scalar>0 else ""}{Numbers.getFraction(scalar)} * L{row2_index+1}");

        self.matrix[self.get_row_index(row1)] = new_row;
        return self;

    def operar(self):
        for focus in range(self.linhas):
            self.focus = focus;
            response = self.action1()
            if response == -1:
                print("Interrupção: Linha nula. \nVerifique este resultado: ");
                self.displayMatrix();
                break;
            self.action2().action3();
    
    def action1(self):
        """
        Permuta a linha correspondente ao foco atual para cima.
        """
        focus = self.focus;
        next_row = self.get_next_row();
        if not next_row:
            return -1;
        next_index = self.get_row_index(next_row);
        self.permutar(focus, next_index);
        self.displayMatrix();
        return self;
    
    def action2(self):
        """
        Transforma o pivô da linha-foco em 1.
        """
        focus = self.focus;
        row = self.matrix[focus];
        ratio = 1/row[focus];
        self.linha_escalar(row, ratio)
        self.displayMatrix();
        return self;

    def action3(self):
        focus = self.focus;
        for row in self.matrix:
            row_index = self.get_row_index(row);
            if row_index<=self.focus:
                continue;
            self.linha_escalar_linha(row, -row[focus], self.matrix[focus]);
        self.displayMatrix();
            
    def get_next_row(self):
        focus = self.focus;
        for row in self.matrix:
            if not Matrix.is_row_null(row, focus) and self.get_row_index(row)>=focus:
                return row;

    def get_row_index(self, row:list)->int:
        return self.matrix.index(row);

    @staticmethod
    def is_row_null(row:list, focus:int):
        return row[focus]==0;
        
    @staticmethod
    def getCorner(rowIndex:int, matrixLen:int)->tuple:
        if rowIndex==0:
            return ("┌ ", " ┐");
        elif rowIndex == matrixLen-1:
            return ("└ ", " ┘");
        return ("| ", " |");

if __name__ == "__main__":
    Matrix();