def get_html_head(title, columns=4, font_size="13px", padding="2px 0 2px 4px"):
    return f'''<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        @media print {{
            body {{ width: 210mm; margin: 10mm auto; }}
        }}
        body {{
            font-family: "微软雅黑", Arial, sans-serif;
            width: 210mm;
            margin: 10mm auto;
            font-size: {font_size};
            background: #fff;
        }}
        h2 {{
            text-align: center;
            margin-bottom: 10px;
        }}
        .info-row {{
            margin-bottom: 8px;
            font-size: 15px;
            display: flex;
            align-items: center;
            flex-wrap: nowrap;
            justify-content: space-between;
        }}
        .info-left {{
            display: flex;
            align-items: center;
        }}
        .info-right {{
            display: flex;
            align-items: center;
        }}
        .info-label {{
            display: inline-block;
            width: 44px;
            text-align: right;
            margin-right: 4px;
            white-space: nowrap;
        }}
        .info-input {{
            display: inline-block;
            border-bottom: 1px solid #333;
            width: 90px;
            height: 16px;
            vertical-align: middle;
            margin-right: 10px;
        }}
        .info-input.short {{
            width: 48px;
        }}
        .problems-grid {{
            display: grid;
            grid-template-columns: repeat({columns}, 1fr);
            gap: 2px 8px;
            margin-top: 8px;
            width: 100%;
        }}
        .problem-cell {{
            font-size: {font_size};
            padding: {padding};
            min-height: 22px;
            box-sizing: border-box;
            word-break: break-all;
        }}
    </style>
</head>
<body>
    <h2>{title}</h2>
    <div class="info-row">
        <div class="info-left">
            <span class="info-label">姓名：</span><span class="info-input"></span>
            <span class="info-label">日期：</span><span class="info-input"></span>
        </div>
        <div class="info-right">
            <span class="info-label">分数：</span><span class="info-input short"></span>
            <span class="info-label">时间：</span><span class="info-input short"></span>
        </div>
    </div>
    <div class="problems-grid">
'''

def get_html_tail():
    return '''
    </div>
</body>
</html>
'''