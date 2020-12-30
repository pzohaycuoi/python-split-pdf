import split
import merge
import checkMissingFile

print("=" * 100)
print(
        "1. Merge the file\
        2. Split the file\
        3. Check missing file\
        4. Merge then Split"
    )
print("=" * 100)
print("Choosing option: ", end=" ")
a = int(input())

if a == 1:
    print("=== Merge the file ===")
    
    print("Input folder contains files need to be merged: ", end=" ")
    input1 = str(input())
    print("Input destination for merged file: ", end=" ")
    input2 = str(input())
elif a == 2:
    print("=== Split the file ===")

    print("Input absolute path to the file need to be splitted: ", end=" ")
    input3 = str(input())
    print("Input page range: ", end=" ")
    input3 = int(input())
    print("Input start file number: ", end=" ")
    input3 = int(input())
elif a == 3:
    sudo        ok ok ok