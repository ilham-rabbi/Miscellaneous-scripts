# Miscellaneous-scripts
A storage box for scripts i've written that don't quite need their own repository

-------------------------------
### Script 1: PAW_Accessions_Modifier

This is a short script which removes extraneous information from protein accessions output by the PAW pipeline (see Phil Wilmarth's GitHub). Accession in PAW output files presently have the database (SP or TR) appended at the front and a short name appended at the end.

![image](https://user-images.githubusercontent.com/103604756/185961980-0890d3f7-74ca-46dd-a585-bfad089938dd.png)

this script takes in a list of accessions in this format and returns a textfile containing just the main accessions.
