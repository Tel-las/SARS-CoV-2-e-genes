from Bio import SeqIO
from Bio.Blast import NCBIWWW

class Blast:
    def __init__(self, name, ficheiro , blast, format):
        '''
        VARIAVEIS:
            Self = Acession number
            ficheiro = ficheiro <genbank ou fasta>
            format = formato do ficheiro <'gb' ou fasta>
            blast = tipo de blast a fazer

        '''
        self.ficheiro = ficheiro
        self.format = format
        self.blast = blast
        self.name = name
        if self.blast == 'blastn':
            self.database = 'nt'
        elif self.blast == 'blastp' or 'blastx':
            self.database = 'nr'
        else: raise Exception('Blast not supported')

    def blast(self):
        '''
            VARIAVEIS:
                Self = Acession number
                ficheiro = ficheiro <genbank ou fasta>
                format = formato do ficheiro <'gb' ou fasta>
            RETURNS:
                Gera um ficheiro .xml com o resultado do blastn contra   a database dos nucleotidos .
            '''
        print('Iniciar blast...')
        record = SeqIO.read(self.ficheiro, format= self.format)
        result_handle = NCBIWWW.qblast(self.blast, self.database, record.seq)
        name = self.name + "_" + str(self.blast) + ".xml"
        print('A guardar ficheiro com blast...')
        with open(name, "w") as out_handle:
            out_handle.write(result_handle.read())
        result_handle.close()
        print('Blast guardado no ficheiro ' + name)
