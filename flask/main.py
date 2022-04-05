import flask
from flask import *
import json
from datetime import timedelta
import pymysql

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates'
            )
@app.route('/chuli',methods=['POST'])
def chuli():
    if request.method=="POST":
        username = request.form.get("uname")
        password = request.form.get("passwd")
        print("用户名提交了"+username+"密码提交了"+password)

        # 打开数据库
    db = pymysql.connect(host="localhost", user="root", password="root", db="haha")
    # 创建游标对象
    cursor = db.cursor()
    # sql语句
    sql = "select * from table1"
    # 执行sql
    cursor.execute(sql)
    # 确认
    db.commit()
    list1=[]
    for i in range(4):
        data = cursor.fetchone()
        li=list(data)
        list+=li
    print(list1)


    return render_template('chuli.html')
    pass

@app.route('/test1')
def text1():
    return render_template('text1.html')

    pass


@app.route('/abcd',methods=['GET','POST'])
def abcd_page():
    user_name = request.form.get('uname')
    user_pass = request.form.get('upass')
    return "this is a %s hahahaha"%(request.user_agent.platform)
    pass

@app.route('/b')
def b_page():
    flask.abort(404)
    return '你来了啊'

    pass


@app.route('/redirect')#重定向
def abcde_page():
    #站外
    #return flask.redirect("http://baidu.com")
    #站内
    return flask.redirect(flask.url_for('b_page',user_id=123)) #用b的函数名定位地址
    pass

@app.route('/woshihenchangdeluyou',endpoint='b1')
def bc_page():
    return '您来了哈'
    pass

@app.route('/bcd')
def bcd_page():
    return flask.redirect(flask.url_for('b1'))
    pass

@app.route('/c') #支持html返回
def c_page():

    return Response('<h1>haha nihao</h1>'
                     '<br>'
                     '<h2>hahawoshi</h2>'
                    )
    pass

@app.route('/d/<id>') #模板
def d_page(id):
    m_int = int(id)+20
    m_str = "nihao haha"
    m_list = ["xiaoming","xiaohong","xiaoli"]
    vip = 0
    return flask.render_template("tempa.html",mint = m_int,mstr = m_str,mlist = m_list,vip=vip)

    pass

#cookie交互
#@app.route('/e')  #设置cookie
#def e_page():
#    response = flask.make_response('success')
#    response.set_cookie('user_id',max_age=150)
#  response.set_cookie('vip','0',max_age=150)
#   return response
#    pass

#@app.route('/ea')
#def ea_page():      #读取cookie
#    user_id = request.cookies.get('user_id')
#    vip = request.cookies.get('vip')
#    return flask.render_template("tempa.html",user_id=user_id,vip=vip)

#配置加密字符串
app.config['SECRET_KEY'] = 'key123'
#设置7天有效
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)

@app.route('/f')
def f_page():
    response = flask.make_response('success')
    #设置session
    session['user_id']="20"
    session['vip']='0'
    return 'success'
    pass

@app.route('/fa')
def fa_page():
    #读取session
    user_id = session['user_id']
    vip = session['vip']
    return flask.render_template("tempa.html",user_id=user_id,vip=vip)

@app.route('/logout')
def logout():
    #response = flask.make_response('退出')
    #response.delete_cookie('user_id')
    #response.delete_cookie('vip')

    #session.pop('user_id',None)
    #session.pop('vip',None)

    #session['user_id']=False

    session.clear()

    return 'logout'
    pass






@app.route('/abc')
def abc_page():
    #定义一个字典
    json_dict = {
        "name":"xiaoli",
        "age":"19",
        "score":"89",
    }
    result = json.dumps(json_dict)

    dict1 = json.loads('{"name": "xiaoli", "age": "19", "score": "89"}')
    print(dict1)
    return 'x'
    pass

@app.errorhandler(404)  #404重定向
def page_not_found(e):
    return '你出错了',404

    pass

@app.template_filter('dore')  #过滤器
def do_reserver(li):
    temp = list(li)
    temp.reverse()
    return temp


#装饰器，关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)