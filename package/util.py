from fractions import Fraction;

class InputObject:
    def __init__(self, message:str, acceptedFormat=str, **kwargs)-> any:
        while True:
            try:
                result = acceptedFormat(input(message));
                if kwargs:
                    if "options" in kwargs and (not result in kwargs.get("options")):
                        print(f"\"{result}\" não é uma opção válida! Por favor tente novamente!");
                        continue;
                self.result = result;
                break;
            except:
                print("Invalid format. Please try again.");
                continue;

class Numbers:
    @staticmethod
    def getFraction(x:float|int)->str:
        if not Numbers.isDecimal(x):
            return str(x) if x!=0 else "0.0";
        return str(Fraction(str(x)).limit_denominator());

    @staticmethod
    def isDecimal(x)->bool:
        return int(x)!=x
    
    @staticmethod
    def processNumber(x:str)->float:
        if "/" in x:
            numbs = list(map(int, x.split("/")));
            return numbs[0]/numbs[1];
        else:
            try:
                return float(x);
            except:
                return 0;