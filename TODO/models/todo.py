import time
from models import Model


class Todo(Model):
    @classmethod
    def new(cls, form):
 
        t = cls(form)
        t.save()
        return t

    @classmethod
    def update(cls, id, form):
        t = cls.find(id)
        valid_names = [
            'title',
            'completed'
        ]
        for key in form:
            if key in valid_names:
                setattr(t, key, form[key])
        t.save()
        return t

    @classmethod
    def complete(cls, id, completed=True):
        t = cls.find(id)
        t.completed = completed
        t.save()
        return t

    def __init__(self, form):
        self.id = None
        self.title = form.get('title', '')
        # 下面的是默认的数据
        self.completed = False
        format = '%H:%M:%S'
        # 创建时间
        value = time.localtime(int(time.time()))
        self.ct = time.strftime(format, value)
