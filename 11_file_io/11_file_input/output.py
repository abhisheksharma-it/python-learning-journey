#file input and output in python

#reading from a file

import PyPDF2

# 1. File ko 'rb' (read binary) mode me open karein
file_path = r"C:\Users\mex3y\Downloads\DEMGN101 (2).pdf"
f = open(file_path, "rb")

# 2. PyPDF2 ka 'PdfReader' banayein jo is binary ko samjhega
reader = PyPDF2.PdfReader(f)

# 3. PDF me total kitne pages hain, wo check karein
print("Total Pages:", len(reader.pages))

# 4. Kisi specific page ko select karein (index 0 ka matlab Page 1)
page_one = reader.pages[0]

# 5. Us page ka text extract karein aur print karein
text = page_one.extract_text()
print(text)

# 6. File close karna na bhoolein
f.close()