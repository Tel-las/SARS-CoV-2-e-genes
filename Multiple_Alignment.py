from Bio.Align.Applications import ClustalwCommandline

class Mutiple:
    def __init__(self, dir, in_file):
        self.diretoria= dir
        self.in_file = in_file
        self.name = in_file.rstrip('.fasta')

    def alignment(self):
        clustalw_cline = ClustalwCommandline(self.diretoria, infile= self.in_file)
        clustalw_cline()
        print(clustalw_cline)
        print("Ficheiros " + self.name + '.aln e '+ self.name + '.dnd gerados.')
