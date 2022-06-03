def make_repeater_of(n):
    assert type(n) == int, "n must be an integer"
    def repeater(s):
        assert type(s) == str, "The input must be a string"
        return s * n
    return repeater

def make_division_by(n):
    n = float(n)
    def division(x):
        x = float(x)
        assert x != 0, "x cannot be zero"
        return x / n
    return division

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hello"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Jose"))
    
    print("+++++++++ DIVISION +++++++++")
    
    divison_by_3 = make_division_by(3)
    print(divison_by_3(18))
    divison_by_5 = make_division_by(5)
    print(divison_by_5(100))
    divison_by_18 = make_division_by(18)
    print(divison_by_18(54))

if __name__=="__main__":
    run()