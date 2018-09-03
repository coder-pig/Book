from app import db
import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import Required


class ToDo(db.Model):
    __tablename__ = 'note'
    __table_args__ = {"useexisting": True}
    _id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    content = db.Column(db.TEXT)
    time = db.Column(db.DATETIME)
    status = db.Column(db.INT, default=0)

    @property
    def id(self):
        return self._id


class ToDoForm(FlaskForm):
    todo = StringField(r'内容', validators=[Required()])
    add = SubmitField(r'添加')


if __name__ == '__main__':
    db.create_all()  # 创建表
