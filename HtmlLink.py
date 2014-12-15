# coding: utf-8
from string import  Template
class HtmlLink:
    def __init__(self, show_name, ids, text, href):
        self.show_name = show_name
        self.ids = ids
        self.text = text
        self.href = href
        pass

    def __repr__(self):
        ret = 'show_name:', self.show_name
        return str(ret)

    def get_private_property(self):
        private_property = """
    private string ${show_name} = ${condition_exp}"""
        show_name = ''
        condition_exp=''
        if self.ids:
            show_name = 'id_' + self.show_name
            condition_exp = '"id=' + self.ids + '"'
        elif self.text:
            show_name = 'text_' + self.show_name
            condition_exp ='"TextContent=' + self.text + '"'
        elif self.href:
            show_name = 'href_' + self.show_name
            condition_exp ='"href=' + self.href + '"'
         #利用Template替换掉原来占位符
        return Template(private_property).substitute({'show_name': show_name, 'condition_exp': condition_exp})


    def get_public_property(self):
        public_property = """
    public HtmlAnchor ${show_name}
    {
        get
        {
            return Get<HtmlAnchor>(TagA,${condition_exp});
        }
    }
    """
        condition_exp = ''
        #若有id属性，直接用id属性，否则若有text属性，就用text属性，否则利用href属性
        if self.ids:
            condition_exp = 'id_' + self.show_name
            pass
        elif self.text:
            condition_exp = 'text_' + self.show_name
            pass
        elif self.href:
            condition_exp = 'href_' + self.show_name
            pass

        #利用Template替换掉原来占位符
        return Template(public_property).substitute({'show_name': self.show_name, 'condition_exp': condition_exp})

