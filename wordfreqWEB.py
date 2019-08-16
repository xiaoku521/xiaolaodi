# 先安装 flask -- 用这个命令 pip install flask
from flask import Flask, request
from WordFreq import WordFreq
from wordfreqCMD import youdao_link

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':  # 按下Get word frequency按钮，提交表格后
        content = request.form['content']
        f = WordFreq(content)
        lst = f.get_freq()
        # 把lst里面的内容用html格式显示出来
        page = ''
        count = 1 # 用来数一共有多少个独特的单词
        for x in lst:
            page += '<p><font color="grey">%d</font>: <a href="%s">%s</a> (%d)</p>\n' % (count, youdao_link(x[0]), x[0], x[1])
            count += 1
        return page
    else: # 访问http://127.0.0.1:5000/时候回执行以下的代码
        page = '<p><b>Word Frequence Counter</b></p>'
        page += '<form method="post" action="/">'
        page += ' <textarea name="content" rows="30" cols="60"></textarea><br/>'
        page += ' <input type="submit" value="Get word frequency"/>'
        page += '</form>'
        return page


if __name__ == '__main__':
    app.run(debug=True)
