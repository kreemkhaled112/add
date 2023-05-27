from random import *


file1_path = 'Frist_name.txt'  # Replace with the actual file path for the first file
file2_path = 'Last_name.txt'  # Replace with the actual file path for the second file

with open('Frist_name.txt', 'r', encoding='utf-8') as f:
        first = f.read().splitlines()
        first = choice(first)

        if any('\u0600' <= char <= '\u06FF' for char in first):
                
                while True:
                    with open('Last_name.txt', 'r', encoding='utf-8') as f:
                        last = f.read().splitlines()
                        last = choice(last)
                        
                        if any('\u0600' <= char <= '\u06FF' for char in last):
                            print(f"Arabic Line from the second file: {last}")
                            break
                         
        else:
            while True:
                    with open('Last_name.txt', 'r', encoding='utf-8') as f:
                        last = f.read().splitlines()
                        last = choice(last)
                        
                        if not any('\u0600' <= char <= '\u06FF' for char in last):
                            print(f"English Line from the second file: {last}")
                            break
                        
            print(f"English Line from the first file: {first}")
            
        
