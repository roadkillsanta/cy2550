cd hashcat-6.2.6/
hashcat.exe -m 500 --username -O -a 0 -r rules/dive.rule -o ../cracked.txt ../nie.e@northeastern.edu.shadow example.dict
pause