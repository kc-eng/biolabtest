"""
A simple package to print program texts exactly as they are.
"""

PROGRAM1 = '''
1
from Bio.Seq import Seq

dna_seq=Seq("ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC")
print("DNA Sequence: ", dna_seq)

sliced_seq=dna_seq[3:11]
print("Sliced Sequence: ", sliced_seq)

another_seq=Seq("TGCA")
concatenated_seq=sliced_seq+another_seq

print("Concatenated: ",concatenated_seq)

rna_seq=concatenated_seq.transcribe()
print("RNA: ",rna_seq)

protein_seq=rna_seq.translate()
print("Protein: ",protein_seq)
********************************************************'''

PROGRAM2 = '''2

from Bio import SeqIO

def read_fasta(file_name):
    for record in SeqIO.parse(file_name,"fasta"):
        print("Header: ",record.description)
        print("Sequence: ",record.seq)
        print()
   


fasta_file="eg.fasta"

read_fasta(fasta_file)

*********************************************************'''

PROGRAM3 = '''3

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dna_seq = Seq("AGTCTACGTACCCTAGGCCAAA")

record = SeqRecord(
    dna_seq,
    id="seq1",
    name="Example_gene",
    description="Example gene sequence",
    annotations={
        "molecule_type": "DNA",  # Required for GenBank format
        "gene": "Example gene",
        "function": "hypothetical protein"
    }
)

# Define output file path
output_file = "example.gb"

# Open file for writing (without 'with')
ofile = open(output_file, "w")
SeqIO.write(record, ofile, "genbank")
ofile.close()  # Must manually close the file

print("Written successfully")

# Open file for reading (without 'with')
ifile = open(output_file, "r")
record_read = SeqIO.read(ifile, "genbank")
ifile.close()  # Must manually close the file

print(record_read)

*************************************************************
'''

PROGRAM4 = '''4

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

records=[]

for record in SeqIO.parse("eg.fasta","fasta"):
    new=SeqRecord(
        record.seq,
        id=record.id,
        name="gene",
        description=record.description,
        annotations={
            "molecule_type":"DNA"
        }
    )
    records.append(new)
   
file=open("4th_genbank.gb","w")
SeqIO.write(records,file,"genbank")
file.close()

file=open("4th_genbank.gb","r")
for content in SeqIO.parse(file,"genbank"):
    print(content)
file.close()

********************************************************************'''

PROGRAM5 = '''from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

record = SeqRecord(Seq("ATGCGTACGTAGCTAGCTAG"), id="seq1", name="random ass name", description="some description")
record.annotations["gene"] = "ExampleGene"
record.annotations["organism"]="New species"
record.annotations["function"]="Hypothetical protein"
record.features.append(SeqFeature(FeatureLocation(0, 21), type="gene"))
print(record.name)
print(record.id)
print(record.description)
print(record.annotations)
print(record.features)
'''

PROGRAM6 = '''6

from Bio import Entrez, SeqIO

Entrez.email = "nikhilsingh.is22@bmsce.ac.in"
handle = Entrez.efetch(db="nucleotide", id="NM_001301717", rettype="gb", retmode="text")

record = SeqIO.read(handle, "genbank")
print(record)
print(record.id)
print(record.description)
# print(record.features)
print(record.seq[:30])



**************************************************************************************'''

PROGRAM7 = '''7
from Bio.Align import PairwiseAligner
aligner = PairwiseAligner()
alignment = aligner.align("AGTACACTGGT", "AGTACGCTGGT")
print(alignment)
print(alignment[0])
print(alignment[2])
print(alignment[0].score)



************************************************************************'''

PROGRAM8 = '''8

import subprocess
from Bio import AlignIO

subprocess.run(["muscle", "-in", "eg.fasta", "-out", "aligned.fasta"])
alignment = AlignIO.read("aligned.fasta", "fasta")

print(alignment)


************************************************************************************
'''

PROGRAM9 = '''from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

alignment = AlignIO.read("aligned.fasta", "fasta")
dm = DistanceCalculator("identity").get_distance(alignment)
tree = DistanceTreeConstructor().upgma(dm)

Phylo.draw(tree)
# Print ASCII tree
Phylo.draw_ascii(tree)

# Save to file
Phylo.write(tree, "tree.newick", "newick")


*********************************************************************************************'''

PROGRAM10 = '''10

from Bio.PDB import *
import matplotlib.pyplot as plt
import numpy as np

# 1. Download and parse PDB file (using mmCif format)
pdb_id = "1A3N"  # Example: Hemoglobin
pdbl = PDBList()
cif_file = pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="mmCif")
structure = MMCIFParser().get_structure(pdb_id, cif_file)

# 2. Get all atom coordinates
atoms = np.array([atom.coord for atom in structure.get_atoms()])

# 3. Simple 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*atoms.T, s=5, alpha=0.5)
ax.set_title(f"{pdb_id} Structure")
plt.tight_layout()
plt.show()'''

def print_program1():
    """Print the exact text of Program 1."""
    print(PROGRAM1)

def print_program2():
    """Print the exact text of Program 2."""
    print(PROGRAM2)

def print_program3():
    """Print the exact text of Program 3."""
    print(PROGRAM3)

def print_program4():
    """Print the exact text of Program 4."""
    print(PROGRAM4)

def print_program5():
    """Print the exact text of Program 5."""
    print(PROGRAM5)

def print_program6():
    """Print the exact text of Program 6."""
    print(PROGRAM6)

def print_program7():
    """Print the exact text of Program 7."""
    print(PROGRAM7)

def print_program8():
    """Print the exact text of Program 8."""
    print(PROGRAM8)

def print_program9():
    """Print the exact text of Program 9."""
    print(PROGRAM9)

def print_program10():
    """Print the exact text of Program 10."""
    print(PROGRAM10) 
