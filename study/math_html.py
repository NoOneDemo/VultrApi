from paper_type import PaperType
from html_template import get_html_head, get_html_tail
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseMath:
    def __init__(self):
        if not hasattr(self, "paper_type"):
            raise ValueError("必须在子类中指定 paper_type")

    def problem(self):
        raise NotImplementedError

    def render_problems(self, problems):
        html = ""
        for prob in problems:
            if len(prob) == 3:
                a, op, b = prob
                content = f'{a} {op} {b} = '
            else:
                expr, _ = prob
                content = f'{expr} = '
            html += f'<div class="problem-cell">{content}</div>\n'
        return html

    def gen_html(self, n=None, saveFile=False):
        if n is None:
            n = self.paper_type.count
        problems = [self.problem() for _ in range(n)]
        html = get_html_head(
            self.paper_type.title,
            columns=self.paper_type.columns,
            font_size=self.paper_type.font_size,
            padding=self.paper_type.padding
        ) + self.render_problems(problems) + get_html_tail()
        if saveFile:
            output_file = os.path.join(BASE_DIR, f"{self.paper_type.title}.html")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"试卷已保存到：{output_file}")
        return html

class SimpleMath(BaseMath):
    paper_type = PaperType.SIMPLE

    def __init__(self):
        super().__init__()

    def problem(self):
        import random
        op = random.choice(['+', '-'])
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if op == '-' and a < b:
            a, b = b, a
        return a, op, b

class MixedMath(BaseMath):
    paper_type = PaperType.MIXED

    def __init__(self):
        super().__init__()

    def problem(self):
        import random
        while True:
            nums = [random.randint(1, 999) for _ in range(3)]
            ops = [random.choice(['+', '-']) for _ in range(2)]
            expr = f"{nums[0]} {ops[0]} {nums[1]} {ops[1]} {nums[2]}"
            result = nums[0]
            for i in range(2):
                if ops[i] == '+':
                    result += nums[i+1]
                else:
                    result -= nums[i+1]
            if result > 0:
                return expr, result

def load_all_math_classes():
    # 只需扫描当前文件中的 BaseMath 子类，无需动态导入其它模块
    pass

def get_math_class(paper_type):
    load_all_math_classes()
    for cls in BaseMath.__subclasses__():
        if getattr(cls, "paper_type", None) == paper_type:
            return cls
    raise ValueError(f"未知的试卷类型: {paper_type}")

def gen_math_html_text(paper_type=PaperType.SIMPLE, saveFile=False):
    math_cls = get_math_class(paper_type)
    math_obj = math_cls()
    return math_obj.gen_html(saveFile=saveFile)

if __name__ == "__main__":
    gen_math_html_text(PaperType.SIMPLE, True)
    gen_math_html_text(PaperType.MIXED, True)