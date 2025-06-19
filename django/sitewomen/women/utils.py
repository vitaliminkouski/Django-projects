menu=[
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Add Page', 'url_name': 'add_page'},
    {'title': 'Log in', 'url_name': 'login'},
    {'title': 'About', 'url_name': 'about'},
]

class DataMixin():
    page_title=None
    extra_context={}
    cat_selected=None
    action_to_do=None
    paginate_by = 1

    def __init__(self):
        if self.page_title:
            self.extra_context['title']=self.page_title
        if self.cat_selected is not None:
            self.extra_context['cat_selected']=self.cat_selected
        if self.action_to_do is not None:
            self.extra_context['action_to_do']=self.action_to_do

        if 'menu' not in self.extra_context:
            self.extra_context['menu']=menu

    def get_mixin_content(self, context, **kwargs):
        context['menu']=menu
        context['cat_selected']=None
        context.update(kwargs)
        return context