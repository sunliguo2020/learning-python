from wtforms import Form,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class SuggetionForm(Form):
    """
    意见建议
    """
    content = TextAreaField(
        id = 'ckeditor_content', # 这里新增了id属性
        label="意见或建议",
        validators=[
            DataRequired("内容不能为空！")
        ],
        description="意见或建议",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入内容！",
            "rows" : 7
        }
    )
    submit = SubmitField(
        '发送消息',
        render_kw={
            "class": "btn btn-primary",
        }
    )