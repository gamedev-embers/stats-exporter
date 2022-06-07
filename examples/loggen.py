import json
import argparse
from datetime import datetime
import random
from uuid import uuid4

parser = argparse.ArgumentParser(description='generate logs for test')
parser.add_argument('--count',  default=10, help='the count of logs')
parser.add_argument('--output',  default="./output.log", help='the file path of logs')

now = lambda: int(datetime.now().timestamp() * 1000)

def gen_row_account(lineNum: int) -> dict:
    return {
        "type": "account",
        "subtype": "login",
        "args": json.dumps({
            "first": True,
        })
    }


def gen_row_payment(lineNum: int) -> dict:
    return {
        "type": "payment",
        "subtype": "normal",
        "args": json.dumps({
            "amount": random.randint(1, 1000),
        })
    }


def gen_row_system(lineNum: int) -> dict:
    n = random.randint(1000, 20000)
    return {
        "type": "system",
        "subtype": "info",
        "args": json.dumps({
            "onlines": n,
            "servers": int(n/1000),
        })
    }


def gen_row(lineNum: int, type:str, interv=10*000) -> dict:
    row = {
        "ts": now() + interv*lineNum,
        "playerId": str(uuid4()),
    }
    if type == "account":
        row.update(gen_row_account(lineNum))
    elif type == "payment":
        row.update(gen_row_payment(lineNum))
    elif type == "system":
        row.update(gen_row_system(lineNum))
    else:
        raise Exception(f"invalid type {type}")
    return row

if __name__ == "__main__":
    args = parser.parse_args()
    if not args.output:
        print("missing --output")
        exit(1)
        pass

    fp = open(args.output, "w", encoding="utf-8")
    for type in ["account", "payment", "system"]:
        print(f"generating: {args.count} rows of {type}")
        for i in range(args.count):
            row = gen_row(i, type=type)
            json.dump(row, fp)
            fp.write("\n")
            pass
    print(f"writed: {args.output}")
    fp.close()
    pass
