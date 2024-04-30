from Bio import SeqIO

original_file = r"/scratch/gent/472/vsc47291/MA1_CompPlantDev/data/Proteomes/Lotus_japonica.fa"
corrected_file = r"scratch/gent/472/vsc47291/MA1_CompPlantDev/data/Proteomes/Lotus_japonica_corr.fa"

with open(original_file) as original, open(corrected_file, 'w') as corrected:
    records = SeqIO.parse(original_file, 'fasta')
    for record in records:           
        gene_name = record.id.split()[0]
        record.description += f" gene:{gene_name}"        
        SeqIO.write(record, corrected, 'fasta')