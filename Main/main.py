import sys
sys.path.append(".")

from Input import view
from multipledispatch import dispatch
# null_value_list = []
class Column_Name(view.Read_File):

    def column_name(self):
        return super().read_file().columns.values
    
    def data_shape(self):
        return super().read_file().shape

class Cleaning(Column_Name):
    
    def null_value(self):
        self.null_value_find = super().read_file()
        self.null_value_list = [0 if self.null_value_find.isnull().sum()[i]==0 else 1 for i in super().column_name()]
        return all(self.null_value_list),self.null_value_find.isnull().sum()
        
class Base(Cleaning):
    pass