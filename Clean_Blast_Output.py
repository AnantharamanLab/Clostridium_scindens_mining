import sys

concatenated_input_file = sys.argv[1]
concatenated_output_file = concatenated_input_file.split(".tsv")[0] + "_cleaned.tsv"

first_output_line = "Query Sequence id\tSubject Sequence id\tQuery Sequence Length\tSubject Sequence Length\tStart of Alignment in Query\tEnd of Alignment in Query\tStart of Alignment in Subject\tEnd of Alignment in Subject\tAlignment Length\tNumber of Mismatches\tE-value\tBit Score\t Percent Identity"


with open(concatenated_input_file, "r") as input, open(concatenated_output_file, "w") as output:
    output.write(first_output_line + "\n")
    for line in input:
        if "#" in line:
            continue
        else:
            output.write(line)