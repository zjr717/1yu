from todolist_creation import db,todolist,app
from flask import Flask,jsonify


# 增：
@app.route('/add',methods=['POST'])
def add():
    # 添加一条新的待办事项
    a = todolist(id=1,title='py第三轮作业',content='create a todolist',completion_status='no',add_time='20230112',deadline='20230112')

    db.session.add(a)
    db.session.commit()

    return jsonify(msg='已添加')

# 改
@app.route('/change',methods=['POST'])
def change():
    # 将所有待办事项设置为已完成
    b = todolist.query.filter(todolist.completion_status == 'no').update({'completion_status':'yes'})
    db.session.commit()
    print(b) # 修改条数

    return jsonify(msg='更改成功')

# 查
@app.route('/get',methods=['GET'])
def get():
    # 通过id查询事项
    c1 = todolist.query.get(1)
    print(c1.title)
    # 输入关键字查询事项
    c2 = todolist.query.filter_by(title='py第三轮作业').all()
    for i in c2:
        print(i.title)
    # 查看所有事项
    c3 = todolist.query.all()
    for i in c3:
        print(i.title)
    # 查看所有待办事项
    c4 = todolist.query.filter(todolist.completion_status == 'no').all()
    for i in c4:
        print(i.title)

    return  jsonify(msg='查询完毕')

# 删
@app.route('/delete',methods=['POST'])
def delete():
    # 删除所有已完成事项
    d = todolist.query.filter(todolist.completion_status == 'yes').delete()
    db.session.commit()
    print(d) #删除条数
    return jsonify(msg='已删除')
app.run(host='0.0.0.0')