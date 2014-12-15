# coding: utf-8
from string import Template


class HtmlInput:
    def __init__(self, show_name, ids, name):
        self.show_name = show_name  # ids if ids else name
        self.ids = ids
        self.name = name
        pass

    def __repr__(self):
        ret = 'show_name:', self.show_name
        return str(ret)

    def get_private_property(self):
        private_property = """
    private string ${show_name} = ${condition_exp}"""
        show_name = ''
        condition_exp = ''
        if self.ids:
            show_name = 'id_' + self.show_name
            condition_exp = '"id=' + self.ids + '"'
        elif self.name:
            show_name = 'name_' + self.show_name
            condition_exp = '"name=' + self.name + '"'
            # 利用Template替换掉原来占位符
        return Template(private_property).substitute({'show_name': show_name, 'condition_exp': condition_exp})

    def get_public_property(self):
        public_property = """
    public HtmlInputText ${show_name}
    {
        get
        {
            return Get<HtmlInputText>(TagInput,${condition_exp});
        }
    }
    """
        condition_exp = ''
        # 若有id属性，直接用id属性，否则若有text属性，就用text属性，否则利用href属性
        if self.ids:
            condition_exp = 'id_' + self.show_name
            pass
        elif self.name:
            condition_exp = 'name_' + self.show_name

        #利用Template替换掉原来占位符
        return Template(public_property).substitute({'show_name': self.show_name, 'condition_exp': condition_exp})

