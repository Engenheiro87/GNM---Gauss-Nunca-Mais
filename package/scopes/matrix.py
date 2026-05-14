from package.utils.value_parser import ValueParser;
from package.errors import Error;
from copy import deepcopy;

class Matrix:
    def __init__(self, lines:list):
        self.lines = lines;
        self.ACTIONS = {
            "scale":self.__scale,
            "swap":self.__swap,
            "add": self.__add,
        }
    
    def get_order(self)->str:
        return str.format("%dx%d" % (len(self.lines), len(self.lines[0].form)))

    def __scale(self, args:str, **kwargs):
        if not args:
            return Error("MSNG_ARGS");
        parsed = list(map(ValueParser.convert_to_num, args.strip().split()))
        if len(parsed)!=2:
            return Error("INCRRT_ARGS", AMOUNT=len(parsed), EXPECTED = 2);
        lineNum = parsed[0];
        scalar:float = parsed[1];
        if type(lineNum)!=int:
            return Error("INCRRT_TYPE", VAR=lineNum, EXPECTED="int", GOT=type(lineNum).__name__);
        if type(scalar)!=float and type(scalar)!=int:
            return Error("INCRRT_TYPE", VAR=scalar, EXPECTED="int", GOT=type(scalar).__name__);
        if lineNum<=0 or lineNum>len(self.lines):
            return Error("NO_LINE", LINE=lineNum, MAX=len(self.lines));
        self.lines[lineNum-1].scale(scalar);
        print(self);
        print(f"L{lineNum} -> L{lineNum} * {ValueParser.turn_to_string(scalar)}");

    def __swap(self, args:str, **kwargs):
        #matrix swap 1 2
        if not args:
            return Error("MSNG_ARGS");
        parsed = list(map(ValueParser.convert_to_num, args.strip().split()));
        if len(parsed)!=2:
            return Error("INCRRT_ARGS", AMOUNT=len(parsed), EXPECTED = 2);
        for arg in parsed:
            type_ = type(arg);
            if type_!=int:# argument isn't an integer
                return Error("INCRRT_TYPE", VAR=arg, EXPECTED="int", GOT=type_.__name__);
            if arg<=0 or arg>len(self.lines):# line doesn't exist
                return Error("NO_LINE", LINE=arg, MAX=len(self.lines));
        l1, l2 = self.lines[parsed[0]-1], self.lines[parsed[1]-1];
        l1.position, l2.position = l2.position, l1.position;
        for line in (l1, l2):
            self.lines[line.position] = line;
        print(self);
        print(f"L{parsed[0]} -> L{parsed[1]}");
    
    def __add(self, args:str, **kwargs):
        # matrix add 2 -2 1
        if not args:
            return Error("MSNG_ARGS");
        parsed = list(map(ValueParser.convert_to_num, args.strip().split()));
        if len(parsed)!=3:
            return Error("INCRRT_ARGS", AMOUNT=len(parsed), EXPECTED = 3);
        l1, l2 = parsed[0], parsed[2];
        scalar = parsed[1];
        for l_arg in (l1, l2):
            type_ = type(l_arg);
            if type_!=int:
                return Error("INCRRT_TYPE", VAR=l_arg, EXPECTED="int", GOT=type_.__name__);
        if type(scalar)!=int and type(scalar)!=float:
            return Error("INCRRT_TYPE", VAR=scalar, EXPECTED="float/int", GOT=type(scalar).__name__);
        for x in (l1, l2):
            if x<=0 or x>len(self.lines):
                return Error("NO_LINE", LINE=x, MAX=len(self.lines));
        line1, line2 = self.lines[l1-1], self.lines[l2-1];
        for column in range(len(line1.form)):
            line1.form[column]+=scalar*line2.form[column];
        print(self);
        print(f"L{l1} -> L{l1} {"- " if scalar<0 else "+ "+ValueParser.turn_to_string(scalar)} * L{l2}");

    def __str__(self):
        columns_lengths = [1 for x in self.lines[0].form];
        horizontalLength = len(self.lines[0].form)
        for line in self.lines:
            for column in range(len(line.form)):
                item = line.form[column];
                item_len = len(ValueParser.turn_to_string(item));
                if columns_lengths[column]<item_len:
                    columns_lengths[column] = item_len;
        hspace = sum(columns_lengths)+horizontalLength-1;
        print("┌"+" "*hspace+"  ┐");
        for line in self.lines:
            print("|", end="");
            for column in range(horizontalLength):
                item = line.form[column];
                str_item = ValueParser.turn_to_string(item);
                spaces = " "*(columns_lengths[column]-len(str_item)+1);
                print(spaces+str_item, end="");
            print(" |");
        print("└"+" "*hspace+"  ┘"+f"{len(self.lines)}x{horizontalLength}");
        return "";

    def __add__(self:Matrix, other:Matrix)->Matrix:
        if type(other)!=Matrix:
            raise TypeError(f"Attempt to add \"Matrix\" type to \"{type(other).__name__}\" type");
        if self.get_order()!=other.get_order():
            raise Error(f"Incompatibility error - Attempt to add {self.get_order()} matrix to {other.get_order()} matrix.");
        return Matrix([
            self.lines[i]+other.lines[i] for i in range(len(self.lines))
        ]);
        
    @staticmethod
    def __create_matrix(args:str, **kwargs)->Error|Matrix:
        if not args:
            return Error("MSNG_ARGS");
        lines = Matrix.__get_lines(args);
        if type(lines)==Error:
            return lines;
        return Matrix(lines);

    @staticmethod
    def __get_lines(args:str)->list:
        str_rows = args.split(";");#["1 2 3", " 4 1/2 6", " 7 8 9"];
        lines = [];
        for i in range(len(str_rows)):
            x:str = str_rows[i];
            lines.append(Line(list(map(ValueParser.convert_to_num, x.strip().split())), i));
        error = None;
        size = len(lines[0].form);
        for i in range(len(lines)):
            item = lines[i];
            if item==None or None in item.form or len(item.form)<=0:
                error = Error("MFRMD_MTRX", LINE=i+1);
                break;
            elif len(item.form)!=size:
                error = Error("INCSTNT_LNGTH");
                break;
        
        return error or lines;

    @staticmethod
    def __sum(args:str, **kwargs)->Matrix|Error:
        # PARSING
        #matrix3 = m sum matrix1 matrix2 ... matrixn
        if not args:
            return Error("MSNG_ARGS");
        components = args.split();
        if len(components)<2:
            return Error("INCRRT_ARGS", EXPECTED=2, AMOUNT=len(components));
        parsed = [];
        for x in components:
            memory_var:Matrix = kwargs["system"].get_variable(x);
            if not memory_var:# variable isn't registed in memory
                return Error("UNKWN_VAR", VAR=x);
            elif type(memory_var)!=Matrix: # provided variable isn't from MATRIX type.
                return Error("TYPE_ERR2", ARG=x, TYPE="MATRIX");
            elif len(parsed)>0 and memory_var.get_order()!=parsed[0].get_order():# provided variable isn't from the same order as the first variable
                return Error("INCMPTBLTY_M1");
            parsed.append(memory_var);
        s = parsed[0];
        for matrix in parsed[1:]:
            s+=matrix;
        return s;

    @staticmethod
    def __m_scale(args:str, **kwargs):
        #m scale matrix1 3
        if not args:
            return Error("MSNG_ARGS");
        components = args.split();
        if len(components)!=2:
            return Error("INCRRT_ARGS", EXPECTED=2, AMOUNT=len(components));
        existing_variable = kwargs["system"].get_variable(components[0]);
        scalar = ValueParser.convert_to_num(components[1]);
        if not existing_variable:
            return Error("UNKWN_VAR", VAR=components[0]);
        elif not scalar:
            return Error("INCRRT_TYPE", VAR=components[1], EXPECTED="float|int", GOT=type(scalar).__name__);
        elif type(existing_variable)!=Matrix:
            return Error("INCRRT_TYPE", VAR=components[0], EXPECTED="MATRIX", GOT=type(existing_variable).__name__);
    
        copy = Matrix(deepcopy(existing_variable.lines));
        for i in range(len(copy.lines)):
            current_line = copy.lines[i];
            copy.lines[i] = current_line*scalar;
        return copy;
        
    ACTIONS = {
        "create" : __create_matrix,
        "sum":__sum,
        "scale":__m_scale,
    } 

class Line:
    def __init__(self, num_list:list, position:int):
        self.__form = num_list;
        self.__position = position;
    
    @property
    def length(self):
        return len(self.__form);

    @property
    def form(self):
        return self.__form;

    @property
    def position(self):
        return self.__position;

    @position.setter
    def position(self, new_position:int):
        self.__position = new_position;
    
    def scale(self, alpha:float):
        self.__form = [x*alpha for x in self.__form];

    def __str__(self):
        return " ".join([ValueParser.turn_to_string(x) for x in self.__form]);

    def __add__(self:Line, other:Line)->Line:
        if type(other)!=Line:
            raise TypeError(f"Attempt to add Line object to \"{type(other).__name__}\" object");
        if len(other.form)!=len(self.form):
            raise Error("Incompatibility Error: Attempt to add lines with different lengths.");
        return Line([self.form[i]+other.form[i] for i in range(len(self.form))], self.position);

    def __mul__(self, other)->Line:
        other_type = type(other);
        if other_type == int or other_type==float:
            return Line([x*other for x in self.form], self.position);
        else:
            raise TypeError(f"Attempt to perform arithmetic (mul) with LINE and {other_type.__name__}");

if __name__ == "__main__":
    ln1 = Line([1, 2, 3],0);
    ln1*=2;
    print(ln1);