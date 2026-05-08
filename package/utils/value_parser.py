from fractions import Fraction;
class ValueParser:
    @staticmethod
    def convert_to_num(x:str)->float:
        x = x.strip();
        if "/" in x:
            numerator, denominator = x.split("/", 1);
            try:
                return float(numerator)/float(denominator);
            except:
                return None;
        else:
            for f in (int, float):
                try:
                    return f(x);
                except:
                    continue;
            return None;

    @staticmethod
    def turn_to_string(x:float|int)->str|None:
        if type(x)==float:
            return str(Fraction(x).limit_denominator(50));
        elif type(x)==int:
            return str(x);
        return None;

if __name__ == "__main__":
    print(ValueParser.turn_to_string(2/4));