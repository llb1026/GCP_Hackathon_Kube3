from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    # templates/index.html 파일이 view입니다
    # 아래 render_template에 추가 인자로 데이터값을 넘겨줄 수 있습니다

    # 예를 들어서, test.py 파일에서 이미지 처리한 결과 리스트를 변수 predictions에 저장했다면
    # render_template("index.html", result = predictions)로 값을 넘겨줄 수 있습니다

    # 이렇게 넘겨준 result값을 index.html에 나타나게 하려면
    # 적절한 위치에 {{result}} 를 넣어주면 됩니다
    
    return render_template("index.html")

if __name__ =='__main__':
    app.run(debug=True)