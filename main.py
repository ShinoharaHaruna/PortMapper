import argparse


def map_to_port(string, threshold):
    total = sum(ord(c) for c in string)
    port = total % 65535
    if port <= threshold:
        port += threshold
    return port


parser = argparse.ArgumentParser(description="Map a string to a port number.")

parser.add_argument("-n", "--string", type=str, required=True, help="The input string.")
parser.add_argument(
    "-t",
    "--threshold",
    type=int,
    default=4096,
    help="The threshold value that port must be greater than.",
)

args = parser.parse_args()

port = map_to_port(args.string, args.threshold)
print('The string "%s" is mapped to port %d.' % (args.string, port))
