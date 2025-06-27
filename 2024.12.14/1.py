from pathlib import Path

def list_files(directory_path: str) -> tuple[str] | None:
    path = Path(directory_path)
    return tuple(f.name for f in path.iterdir() if f.is_file()) if path.is_dir() else None
    
    
#C:\Git\Sajgakova\2024.12.14>tree /f
#Структура папок тома Windows
#Серийный номер тома: 1224-819E
#C:.
#│   # HW 2024.12.14.txt
#│   1.py
#│
#└───data
#    │   7MD9i.chm
#    │   conf.py
#    │   E3ln1.txt
#    │   F1jws.jpg
#    │   le1UO.txt
#    │   q40Kv.docx
#    │   questions.quiz
#    │   r62Bf.txt
#    │   vars.py
#    │   xcD1a.zip
#    │
#    ├───c14KE
#    │       5vsIh.dat
#    │       P2a91.dat
#    │
#    ├───mXbd9
#    │       RoBjg.pt
#    │       z03EN.pt
#    │
#    └───names
#            женские_имена.txt
#            мужские_имена_отчества.txt
#            фамилии.txt
#

#>>> list_files(r'C:\Git\Sajgakova\2024.12.14\data')
#('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 
#'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')