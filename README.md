# KeyLogger/Password Cracker

!!!!!!!!!IMPORTANT PLEASE READ!!!!!!!!

  I initially stated working on this program because I got interested in cybersecurity and was trying to think of a way to collect unique words for a wordlist that can be used to bruteforce passwords.
  
  So far the program is able to record the keystrokes of a user and writes them into a text file. Originally it included special keys such as "Key.space" "Key.enter", but I recently changed it to only include "Key.shift". Each line in the text file contains characters that add up to a single word before keys such as space or enter are hit. Additionally it is important to note that, so far, the program does not take into account special characters or combination inputs.
  
  Once the text is recorded to the file, it is "cleaned" so that it becomes easier to manipulate and use the words in the text file. The cleaned data is then added to a different text file which is the word list that can be used for brute force attacks.


***I would like to make sure that it is clear, THIS PROGRAM IS FOR EDUCATIONAL PURPOSES ONLY! Using scripts like these against real people could lead to trouble, so please be careful.
