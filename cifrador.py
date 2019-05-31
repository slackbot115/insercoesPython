def main():
    wordlist = open("wordlist.txt", "r")
    listWord = wordlist.readlines()
    for word in listWord:
        print("INSERT INTO `diaZer0Test`.`tb_disciplina` (`cd_disciplina`, `nm_disciplina`) VALUES (NULL, '",word,"');")

main()
