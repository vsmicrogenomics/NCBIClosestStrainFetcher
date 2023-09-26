from Bio import Entrez
import csv

def fetch_strain_info(assembly_id):
    if assembly_id == "N/A" or assembly_id == "":
        return "N/A", "N/A"

    Entrez.email = "drvsbio@gmail.com"
    handle = Entrez.esearch(db="assembly", term=assembly_id)
    record = Entrez.read(handle)
    handle.close()

    if record["Count"] == "0":
        return "No record found", "No record found"

    assembly_id = record["IdList"][0]

    handle = Entrez.esummary(db="assembly", id=assembly_id)
    summary = Entrez.read(handle)
    handle.close()

    try:
        species_name = summary['DocumentSummarySet']['DocumentSummary'][0]['SpeciesName']
        strain = summary['DocumentSummarySet']['DocumentSummary'][0].get('Biosource', {}).get('InfraspeciesList', [{}])[0].get('Sub_value', 'Strain not found')
        original_strain_info = f"{species_name} (Strain: {strain})"
        
        # This is the Closest Reference Strain
        closest_reference_strain = f"{species_name} {strain}"

        return original_strain_info, closest_reference_strain
    except KeyError:
        return "Strain information not found", "Strain information not found"

# Read assembly IDs and user_genome from the new file and the new columns
with open('input/gtdbtk.bac120.summary.tsv', 'r') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    records = [(row['user_genome'], row['fastani_reference']) for row in reader]

# Fetch strain information and write to output file
with open('output/output_strains.tsv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='\t')
    writer.writerow(['User Genome', 'AssemblyID', 'OriginalStrainInfo', 'Closest Reference Strain'])  # Write header

    for user_genome, assembly_id in records:
        original_strain_info, closest_reference_strain = fetch_strain_info(assembly_id)
        writer.writerow([user_genome, assembly_id, original_strain_info, closest_reference_strain])
        print(f"For {user_genome}, fetched information for {assembly_id}: {original_strain_info} (Closest Reference: {closest_reference_strain})")
