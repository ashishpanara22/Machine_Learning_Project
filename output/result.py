import sys
sys.path.append(".")

from Input import view
from Main import main

# read_file = view.Read_File()
base = main.Base()

print("column name")
print(base.column_name(),"\n")

print("data shape")
print(base.data_shape(),"\n")

print("null value")
print(base.null_value())