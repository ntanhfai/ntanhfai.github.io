# Prepair:---------------------------------------------------------
import os 
os.makedirs('templates', exist_ok=True)
sss="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bai 1</title>
</head>
<body>
    <input type="text" name="txt_1" id="txt_1">
    <input type="submit" value="Submit">    
</body>
</html>
"""
open("templates/index.html", "w", encoding='utf-8').write(sss)
# End Prepair:-----------------------------------------------------

from flask import Flask, render_template,request
app = Flask(__name__) #Khai báo khởi tạo hệ thống
@app.route('/') #định danh url cho hệ thống
def index(): #khai báo hàm cho url vừa định danh
    return render_template('index.html') #render ra file html trong thư mục templates

if __name__ == '__main__': #khai báo hàm main
    app.run(debug=True, port=5000, host='0.0.0.0') #khởi chạy hệ thống. ở đây thì cổng port là 1221 (mặc định là 5000)