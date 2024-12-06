# Prepair:---------------------------------------------------------
import os

os.makedirs('templates', exist_ok=True)
sss = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Đoạn này không cần thuộc, hiểu là được -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.1/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    
    <title>Bai 2</title>
</head>
<body>    
    <div class="container">        
        <p>Chọn một file excel để upload lên server, server sẽ hiển thị nội dung file đó.</p>
        <form action="/" method="post" enctype="multipart/form-data"> <!-- tất cả thông tin muốn đẩy lên sever đều phải để trong form -->
            <div class="row">
                <div class="col-md-9">
                    <input class="form-control w80" type="file" name="file1" id="file1" accept=".xlsx"><!--đặc biệt muốn upload được file cần có enctype="multipart/form-data"-->
                </div>
                <div class="col-md-3">
                    <input class="btn btn-info" type="submit" value="Submit">
                </div>
            </div>
        </form>
    </div>
    
    <div>
        {%if tables%} <!-- đây là jinja 2. giúp đẩy dữ liệu từ server qua -->
            <p>Đây là nội dung của file bạn đã tải lên:</p>
            {{ tables[0]|safe }}  
        {%endif%}
    </div>
    
</body>
</html>
"""
open("templates/index2.html", "w", encoding='utf-8').write(sss)
# End Prepair:-----------------------------------------------------

from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)  # Khai báo khởi tạo hệ thống


@app.route('/', methods=['GET', 'POST'])  # định danh url cho hệ thống
def upload():  # khai báo hàm cho url vừa định danh

    if request.method == 'POST':
        file = request.files['file1']  # hàm này lấy tất cả thông tin từ tag input:file theo 'name'
        # ngoài ra để lấy tất cả thông tin từ tag khác thì dùng request.form['<name>']. <name>: name của tag cần lấy dữ liệu
        upload_dir = f"data/ProjectName/{request.environ['REMOTE_ADDR']}"
        os.makedirs(upload_dir, exist_ok=True)
        objects = os.listdir(upload_dir)
        files_file = [f for f in objects if os.path.isfile(os.path.join(upload_dir, f))]
        for f in files_file:
            os.remove(os.path.join(upload_dir, f))
        file.save(os.path.join(upload_dir, file.filename))
        df = pd.read_excel(file)  # hàm này đọc excel theo dữ liệu lấy trực tiếp. ngoài ra có thể thay bằng đường dẫn tuyệt đối.
        # đây là hàm return khi nhận được request POST từ client
        return render_template('index2.html', tables=[df.to_html(classes='table table-hover', index=False, table_id='tb-resuly')])

    return render_template('index2.html')  # render ra file html trong thư mục templates


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
