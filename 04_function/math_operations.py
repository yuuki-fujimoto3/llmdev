def add(a, b):
    """2つの数を加算する"""
    return a + b

def substruct(a, b):
    """2つの数を減算する"""
    return a - b

if __name__ == "__main__":
    # モジュールが直接実行された場合にだけ実行される
    print( "5 + 3 =",       add( 5, 3))
    print("10 - 4 =", substruct(10, 4))