def main():
    import gradio as gr
    import importlib.util

    def greet(name):
        return f"Hello, {name}!"

    # 动态导入 math_html.py
    spec = importlib.util.spec_from_file_location("math_html", "/home/ubuntu/codersun/VultrApi/study/math_html.py")
    math_html = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(math_html)

    def gen_math_html():
        html_content = math_html.gen_math_html_text(False)
        import html as html_lib
        safe_html = html_lib.escape(html_content).replace('\n', '\\n').replace("'", "\\'")
        # 更醒目的打印按钮，插入到内容最上方
        print_btn_html = f"""
        <button style="background:#ff9800;color:#fff;font-size:20px;font-weight:bold;padding:12px 32px;border:none;border-radius:6px;cursor:pointer;box-shadow:0 2px 8px #ccc;margin-bottom:20px;" 
            onclick="let win=window.open('about:blank','_blank');win.document.write('{safe_html}');win.document.close();win.print();">
            🖨️ 打印本业考题
        </button>
        <br>
        """
        # 将按钮加在最前面
        html_content = print_btn_html + html_content
        return html_content

    def print_math_html():
        # 返回一段JS，打印 math_html_output 的内容
        return """
        <script>
        let html = document.querySelector('[data-testid="math_html_output"]').innerHTML;
        let win = window.open('', '_blank');
        win.document.write(html);
        win.document.close();
        win.print();
        </script>
        <span>正在打开打印窗口...</span>
        """

    with gr.Blocks() as demo:
        with gr.Row():
            gr.Markdown("# CoderSun Apps", elem_id="title", elem_classes="title-class")
            # 用 HTML 实现右上角刷新按钮
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

        # 其余内容
        math_btn = gr.Button("生成百位数加减法试卷")
        math_html_output = gr.HTML(visible=True, elem_id="math_html_output")
        math_btn.click(fn=gen_math_html, inputs=None, outputs=math_html_output)

    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()