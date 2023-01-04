# Ionical_conductivity_database 🔋
  **Ionical_conductivity_database** is tools for extracting ionical conductivity from scientific documents and generating a database using [ChemDataExtractor](https://github.com/CambridgeMolecularEngineering/chemdataextractor2).
  
## Introduction
  We extract ionical conductivity from scientific documents using this program.
  And we reconstruct the battery database by adding the extracted information (ionical conductivity property, structural type).
  
## Preparation
  - Clone [battery database](https://github.com/ShuHuang/batterydatabase) repository here.
  
  - Check if they are Organized as following:
    ```
    Ionical_conductivity_database/
      ├── batterydatabase/
      |         ├── ...
      |         └── chemdataextractor_batteries/
      |                  ├── ...
      |                  └── chemdataextractor/
      |                           ├── ...
      |                           └── parse/
      ├── exp/
      └── database/
    ```
    
  - Replace batterydatabase/database.py with the database.py provided in this repository.
  - Replace batterydatabase/chemdataextractor_batteries/chemdataextractor/parse/battery_conductivity.py with the battery_conductivity.py provided in this repository.


## Usage
 1. How to extract relation: run batterydatabase/extract.py
     ```
     python extract.py [input directory] [output directory] [start index] [end index] [output file name]
     ```

 2. How to acquire an ionical conductivity database: download database/IonicalConductivityDatabase.json


 3. How to acquire an reconstructed battery database: download [ion.xlsx](https://docs.google.com/spreadsheets/d/1-PSomuy72Uuq60BRBLPKHGbQ0gNBosEz/edit?usp=sharing&ouid=100763551141257878367&rtpof=true&sd=true)


 4. How to visualize the distribution of data: 
   - download [battery.json](https://drive.google.com/file/d/1uGynZkAmpc1oD6DebRfXC0EKX3VFIDEB/view?usp=sharing) and put it in exp/ directory
   - run exp/experiment.py
