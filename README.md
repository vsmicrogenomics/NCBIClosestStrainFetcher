# NCBIClosestStrainFetcher

NCBIClosestStrainFetcher.py: This script is a Python utility designed to query the NCBI database for closest reference strain information using genome assembly identifiers extracted from an input TSV file (gtdbtk.bac120.summary.tsv). It outputs the fetched details in a structured TSV format.

Prerequisites:

Python 3.7 or above
Biopython library
Usage:
Place the input file in a directory named input. Execute the script using the command:
python NCBIClosestStrainFetcher.py

The script will generate an output TSV file (output_strains.tsv) in the output directory, detailing the user genome, assembly ID, original strain info, and closest reference strain for each entry.

Description:
The script begins by reading the fastani_reference column from the specified input TSV file. It then leverages the Biopython library to make queries to the NCBI database, retrieving species names and strain details associated with each assembly identifier. The results are then organized and written to the output TSV file.

The core functionality revolves around the fetch_strain_info function which manages the querying and extraction process for each assembly identifier. Any identifier labeled "N/A" or empty is handled accordingly, outputting "N/A" for strain details.

Test files:
The test directory contains input and output sub-directories containing test files for the NCBIClosestStrainFetcher.py script. These files are used to verify that the script is working correctly.

Acknowledgements:
This script, NCBIClosestStrainFetcher.py, is tailored for researchers and bioinformaticians aiming to cross-reference their genome assembly data with the NCBI database, offering a clear and consolidated view of the closest reference strains.

Citation:
If you utilize the NCBIClosestStrainFetcher.py in your work, please cite it as follows:Sharma, V. (2023). NCBIClosestStrainFetcher.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/NCBIClosestStrainFetcher


