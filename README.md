# linearPolypeptide
Generates a linear polypeptide structure from an amino acid sequence

This set of scripts will take a protein primary sequence (i.e. the list of amino acids) and will generate a the coordinates of the equivelent perfectly linear protein. This represents the protein being flattened into 1 dimension. The process is run in two parts. First the amino acid sequence is placed into the matlab script which is then run. This will generate a csv file containing the x, y, z coordinates of each atom in the polypeptide. Then the python script is run which takes the pdb file for the protein and alters the spatial coordinates to the linear version of the protein.

In the image below the left shows the alphafold predicted structure for talin, the right shows the linearised version of talin (very zoomed in to show linearity as the whole polypeptide won't be visible on a screen).

<img width="1256" alt="image" src="https://user-images.githubusercontent.com/45679976/163256972-424e63a2-3b6c-4aeb-8f4f-669eb3dc70fe.png">
