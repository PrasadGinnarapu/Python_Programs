import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--user_input",help="how many command prompts you need",default=3)
args = parser.parse_args()
print("==================",args)
args.user_input=int(args.user_input)
print(args.user_input)
print(type(args.user_input))
while args.user_input>1:
    parser.add_argument("user_input",help="how many command prompts you need",default=3)
    break
