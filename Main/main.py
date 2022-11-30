import sys
sys.path.append(".")

from Input import view

class Column_Name(view.Read_File):

    def column_name(self):
        return super().read_file().columns.values
    
    def data_shape(self):
        return super().read_file().shape

class Cleaning(Column_Name):
    
    def null_value(self):
        null_value_find = super().read_file()
        self.column_name = super().column_name()
        return null_value_find.isnull().mean()[self.column_name]
class Base(Cleaning):
    pass