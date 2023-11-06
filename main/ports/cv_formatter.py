from abc import ABC, abstractmethod

from main.domain.cv import CV

class CVFormatter(ABC):

    @abstractmethod
    def format(cv: CV, output_file: str):
        pass

    @abstractmethod
    def formattpl(cv: CV, output_file: str):
        pass    

    @abstractmethod
    def get_extension():
        pass
