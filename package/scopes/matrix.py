from package.utils.value_parser import ValueParser;
from package.errors import Error;

class Matrix:
    def __init__(self, lines:list):
        self.lines = lines;
        self.ACTIONS = {
            "scale":self.__scale,
            "swap":self.__swap,
            "add": self.__add,
        }

    def __scale(self, args:str, **kwargs):
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
        print(f"L{l1} -> L{l1} {scalar:+} * L{l2}");

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

    ACTIONS = {
        "create" : __create_matrix,
        "scale": __scale,
    }

class Line:
    def __init__(self, num_list:list, position:int):
        # self.__form = [x for x in num_list if x!=None];
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
    
    
if __name__ == "__main__":
    print(Matrix.ACTIONS["create"]("1 1/2 3; 4 5 6;; 7 8 9;   "));