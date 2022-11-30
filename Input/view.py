import sys
sys.path.append(".")

from All_Package import package
from Constant import constant

class Read_File(package.ABC):

    def read_file(self):
        self.read_file_data = package.pd.read_csv(constant.file_path)
        return self.read_file_data

    @package.abstractmethod
    def column_name(self):
        pass

    @package.abstractmethod
    def data_shape(self):
        pass