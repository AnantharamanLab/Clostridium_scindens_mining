import sys

input_gff_file = sys.argv[1]
output_fasta_file = input_gff_file.replace(".gff", ".fasta")
test = False

with open(input_gff_file, "r") as input, open(output_fasta_file, "w") as output:
    for line in input:
        if "##FASTA" not in line and test == False:
            continue
        elif "##FASTA" in line:
            test = True
            continue
        
        if test == True:
            output.write(line)

        
