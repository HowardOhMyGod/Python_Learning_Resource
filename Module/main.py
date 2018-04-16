from arith.count import count, times
from database.db import mongoDB

def main():
    print(count.add(1,3))
    print(times(2,3))

    stock_db = mongoDB.connect('Stock')
    code_collect = stock_db['code']

    print(code_collect.find_one({}))

if __name__ == '__main__':
    main()