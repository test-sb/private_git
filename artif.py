import argparse


parser = argparse.ArgumentParser(description='Running MNIST Algorithm')
parser.add_argument('--epochs', help='name of file to create')
args = parser.parse_args()
epochs = int(args.epochs)


print('file_name ', epochs)

f = open(f"demofile{epochs}.txt", "w")
f.close()