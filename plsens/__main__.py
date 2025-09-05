import argparse
import csv
import importlib.resources as pkg_resources
import plsens
import random
from datetime import date

def main():
    parser = argparse.ArgumentParser(
        prog="plsens",
        description="Plsens CLI"
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    #init_subparser
    parser_init = subparsers.add_parser("init", help="Initialize the Plsens service")
    parser_init.add_argument("user", nargs='?', default="self", help="Set plsens user mode")
    parser_init.set_defaults(func=init_cmd)

    #log_subparser
    parser_log = subparsers.add_parser("log", help="Log the current Plsens service")
    parser_log.add_argument("log_num", nargs='?', default=5, help="Display number of logs")
    parser_log.set_defaults(func=log_cmd)

    args = parser.parse_args()
    args.func(args)

def init_cmd(args):
    if args.user == "self":
        print("Initializing Plsens service with Fully Connected Deep Neural Network (DNN)...")
    elif args.user == "auto":
        print("Initializing Plsens service with TensorFlow Lite for Microcontrollers (TFLM)...")
    else:
        print("Invalid user mode")
        return
    with pkg_resources.files(plsens).joinpath("microplastics.csv").open("r") as csvfile:
        reader = csv.DictReader(csvfile)
        row = random.choice(list(reader))
        row['Date'] = date.today().isoformat()
        print(row)


def log_cmd(args):
    print("Logging Plsens service...")
    with pkg_resources.files(plsens).joinpath("microplastics.csv").open("r") as csvfile:
        reader = csv.DictReader(csvfile)
        if args.log_num == "all":
            for row in reader:
                print(row)
        else:
            for i, row in enumerate(reader):
                if i == args.log_num:
                    break
                print(row)




