cd hashcat-6.2.6/
hashcat.exe -m 500 --username -O -a 0 -o ../cracked_test.txt ../test.txt ../wordlist_cracked.txt
pause