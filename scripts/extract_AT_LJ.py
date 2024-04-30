import os
import pandas as pd
from Bio import SeqIO

# Directory containing the original FASTA files
input_dir = "/scratch/gent/472/vsc47291/MA1_CompPlantDev/data/Proteomes/primary_transcripts/OrthoFinder/Results_Mar05/Single_Copy_Orthologue_Sequences"

# Output directory for the new FASTA-like file
output_dir = "/scratch/gent/472/vsc47291/MA1_CompPlantDev/results"

# DataFrame to store sequences
AT_LJ = pd.DataFrame(columns=["Arabidopsis_thaliana", "Lotus_japonicus"])

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".fa"):
        AT_id = "NA"
        LJ_id = "NA"
        file_path = os.path.join(input_dir, filename)

        # Read sequences from the current file
        records = SeqIO.parse(file_path, "fasta")

        # Extract sequences starting with ">AT" or ">Lot" and add to DataFrame
        for record in records:
            if record.id.startswith("AT"):
                AT_id = str(record.id)

            elif record.id.startswith("Lot"):
                LJ_id = str(record.id)
        
        AT_LJ = AT_LJ.append({"Arabidopsis_thaliana": AT_id, "Lotus_japonicus": LJ_id}, ignore_index=True)

# Save DataFrame to a CSV file
output_file_path = os.path.join(output_dir, "AT_LJ_Orthogroups.csv")
AT_LJ.to_csv(output_file_path, index=False)

print("Data organized and saved to:", output_file_path)
