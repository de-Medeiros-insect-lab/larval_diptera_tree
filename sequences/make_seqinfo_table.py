import os
import csv

# Define the output CSV file
with open("sequence_info.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # Initialize the header
    header = ["folder", "filename", "genus", "genus_ncbi_id", "tip_name"]

    # Create a list to store the data
    data = []

    # Traverse directory recursively
    for dirpath, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".fasta"):
                # Read the first line of the file
                with open(os.path.join(dirpath, filename)) as fasta_file:
                    for line in fasta_file:
                        if line.startswith('>'):  # Only process sequence header lines
                            # Remove ">" at the start of the line
                            line = line[1:].strip()

                            # Split the line into fields
                            tip_name, *other_fields = line.split('|')

                            # Split the name field into genus and ncbi_id
                            genus_ncbi_id_split = tip_name.split('_')

                            # Check if there are enough parts to unpack
                            if len(genus_ncbi_id_split) < 2:
                                print(line)
                                genus = ""
                                genus_ncbi_id = ""
                            else:
                                genus, genus_ncbi_id = genus_ncbi_id_split[0:2]

                            # Initialize the record dictionary
                            record = {"folder": dirpath, "filename": filename, "genus": genus, "genus_ncbi_id": genus_ncbi_id, "tip_name": tip_name}

                            # Parse the other fields
                            for field in other_fields:
                                if ':' in field:
                                    key, value = field.split(':', 1)
                                    record[key] = value

                                    # Add the key to the header if it's not already there
                                    if key not in header:
                                        header.append(key)

                            # Add the record to the data
                            data.append(record)

    # Write the header
    writer.writerow(header)

    # Write the data
    for record in data:
        writer.writerow([record.get(key, "") for key in header])

