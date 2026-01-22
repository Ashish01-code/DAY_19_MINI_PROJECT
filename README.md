# DAY_19_MINI_PROJECT
# PRODUCT MANAGEMENT SYSTEM (PYTHON + CSV)

This is a menu-driven Product Management System built using Python, OOPS, dictionaries, and CSV file handling.  
The program stores product data permanently in a CSV file and allows full CRUD operations along with sorting and filtering.

FEATURES:
- Add Product
- View Products
- Search Product by ID
- Update Product
- Delete Product
- Count Products
- Open CSV file directly in Excel
- Sort Products by Price
- Filter Products by Price Range
- Filter Products by Quality (GOOD / BAD)

CSV FILE:
Data is stored in a CSV (Comma Separated Values) file.
CSV is a text file that opens in Excel automatically.
Format:
product_id,product_name,price,quality

TECH USED:
- Python 3
- csv module
- os module
- OOPS
- Dictionary

HOW IT WORKS:
- Product data is loaded from CSV into a dictionary at program start
- All operations are performed on the dictionary
- After every change, data is saved back to CSV
- Sorting and filtering are done using temporary lists
- CSV file can be opened directly in Excel using os.startfile()

LEARNING OUTCOME:
- Strong understanding of file handling
- CSV mechanics without pandas
- Real-world menu-based application logic
- Foundation for Data Analysis & Machine Learning

STATUS:
Completed ✔
Tested ✔
GitHub Ready ✔
