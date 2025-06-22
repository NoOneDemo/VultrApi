def main():
    import gradio as gr
    import importlib.util
    import os
    import sys

    # 1. 获取 study 目录
    math_html_dir = "/home/ubuntu/codersun/VultrApi/study"
    sys.path.insert(0, math_html_dir)
    

    # 3. 动态导入 math_html.py
    spec = importlib.util.spec_from_file_location("math_html", os.path.join(math_html_dir, "math_html.py"))
    math_html = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(math_html)
    
    PaperType = math_html.PaperType
    # 枚举类型和按钮名称映射
    PAPER_TYPE_MAP = {
        "百位数加减法练习": PaperType.SIMPLE,
        "百位数加减法混合运算": PaperType.MIXED,
    }

    def gen_math_html_btn(paper_type):
        html_content = math_html.gen_math_html_text(paper_type, False)
        import html as html_lib
        safe_html = html_lib.escape(html_content).replace('\n', '\\n').replace("'", "\\'")
        print_btn_html = f"""
        <button style="background:#ff9800;color:#fff;font-size:20px;font-weight:bold;padding:12px 32px;border:none;border-radius:6px;cursor:pointer;box-shadow:0 2px 8px #ccc;margin-bottom:20px;" 
            onclick="let win=window.open('about:blank','_blank');win.document.write('{safe_html}');win.document.close();win.print();">
            🖨️ 打印本页考题
        </button>
        <br>
        """
        html_content = print_btn_html + html_content
        return html_content

    with gr.Blocks() as demo:
        with gr.Row():
            gr.Markdown("# CoderSun Apps", elem_id="title", elem_classes="title-class")
            gr.HTML(
                """
                <div style="text-align:right;">
                    <button onclick="location.reload()" style="background:#2196f3;color:#fff;font-size:16px;font-weight:bold;padding:8px 24px;border:none;border-radius:6px;cursor:pointer;box-shadow:0 2px 8px #ccc;">
                        🔄 刷新页面
                    </button>
                </div>
                """,
                elem_id="refresh_btn"
            )

        # 枚举按钮区
        with gr.Row():
            btns = []
            for btn_name in PAPER_TYPE_MAP.keys():
                btns.append(gr.Button(btn_name))
        math_html_output = gr.HTML(visible=True, elem_id="math_html_output")

        # 按钮事件绑定
        for btn, (btn_name, paper_type) in zip(btns, PAPER_TYPE_MAP.items()):
            btn.click(
                fn=lambda _=None, pt=paper_type: gen_math_html_btn(pt),
                inputs=None,
                outputs=math_html_output
            )

    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()