import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "百位数加减法试卷.html")

def gen_problem():
    op = random.choice(['+', '-'])
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    # 保证减法结果为正数
    if op == '-' and a < b:
        a, b = b, a
    return a, op, b

problems = [gen_problem() for _ in range(50)]

html_head = '''<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>百位数加减法试卷</title>
    <style>
        @media print {
            body { width: 210mm; margin: 10mm auto; }
        }
        body {
            font-family: "微软雅黑", Arial, sans-serif;
            width: 210mm;
            margin: 10mm auto;
            font-size: 18px;
            background: #fff;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .info-row {
            margin-bottom: 18px;
            font-size: 17px;
            display: flex;
            align-items: center;
            flex-wrap: nowrap;
        }
        .info-label {
            display: inline-block;
            width: 44px;
            text-align: right;
            margin-right: 4px;
            white-space: nowrap;
        }
        .info-input {
            display: inline-block;
            border-bottom: 1px solid #333;
            width: 90px;
            height: 22px;
            vertical-align: middle;
            margin-right: 16px;
        }
        .info-input.short {
            width: 48px;
        }
        .problems {
            display: flex;
            flex-wrap: wrap;
            width: 100%;
        }
        .problem {
            width: 32%;
            margin-bottom: 18px;
            box-sizing: border-box;
            padding-left: 5px;
        }
        .problem-num {
            font-weight: bold;
            margin-right: 4px;
        }
    </style>
</head>
<body>
    <h2>百位数加减法试卷</h2>
    <div class="info-row">
        <span class="info-label">姓名：</span><span class="info-input"></span>
        <span class="info-label">日期：</span><span class="info-input"></span>
        <span class="info-label">分数：</span><span class="info-input short"></span>
        <span class="info-label">时间：</span><span class="info-input short"></span>
    </div>
    <div class="problems">
'''

html_tail = '''
    </div>
</body>
</html>
'''

problem_html = ""
for idx, (a, op, b) in enumerate(problems, 1):
    problem_html += f'        <div class="problem"><span class="problem-num">{idx}.</span> {a} {op} {b} = </div>\n'

html = html_head + problem_html + html_tail

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("试卷已生成：百位数加减法试卷.html")