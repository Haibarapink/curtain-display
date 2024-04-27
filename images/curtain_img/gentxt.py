import os

def generate_html():
    html_code = ''
    directory = 'images/curtain_img'  # 图片文件夹路径
    
    # 遍历图片文件夹中的所有文件
    count = 0
    for i, filename in enumerate(os.listdir('.'), start=1):
        if filename.endswith('.jpg'):  # 只处理 jpg 格式的图片
            img_path = os.path.join(directory, filename)
            # 如果是一组中的第一张图片，则生成新的 curtain-march div
            if count % 3 == 0:
                if count != 0:
                    html_code += '</div>\n'  # 结束上一组的 curtain-march div
                html_code += '<div class="curtain-march">\n'  # 开始新的 curtain-march div
            # 每个照片包裹在一个 curtain-product div 中
            html_code += f'''
    <div class="curtain-product">
        <img src="{img_path}">
    </div>
'''
            count += 1
    
    # 结束最后一组的 curtain-march div
    html_code += '</div>\n'

    return html_code

# 生成 HTML 代码
html_content = generate_html()

# 输出生成的 HTML 代码
print(html_content)