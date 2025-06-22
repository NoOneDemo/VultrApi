from enum import Enum

class PaperType(Enum):
    SIMPLE = {
        "title": "两位数加减法",
        "columns": 4,
        "font_size": "15px",
        "padding": "4px 0 4px 4px",
        "count": 100
    }
    MIXED = {
        "title": "三位数加减法混合运算",
        "columns": 3,
        "font_size": "16px",
        "padding": "4px 0 4px 8px",
        "count": 99
    }

    @property
    def title(self):
        return self.value["title"]

    @property
    def columns(self):
        return self.value["columns"]

    @property
    def font_size(self):
        return self.value["font_size"]

    @property
    def padding(self):
        return self.value["padding"]

    @property
    def count(self):
        return self.value["count"]