import sys

default_in = "input"
default_out = "output"

# use cmd arg as input file instead of default input file
args = len(sys.argv)
input = default_in
output = default_out
if (args == 2):
	input = sys.argv[1]
elif (args == 3):
	input = sys.argv[1]
	output = sys.argv[2]

f = open(input, 'r')
out = open (output, 'w')

line = f.readline()
processed = line.replace("\n","")

while line != "":
	if processed != "":
		out.write(processed + "\n")
	line = f.readline()
	processed = line.replace("\n","")

print "Completed removing empty line(s) in output file : " + out.name
