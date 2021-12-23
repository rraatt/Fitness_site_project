menu = [{'title': 'Make an appointment', 'url_name': 'new_training'},
        {'title': 'Group trainings', 'url_name': 'group_schedule'},
        {'title': 'Examinations', 'url_name': 'examination'},
        {'title': 'About us', 'url_name': 'about'},
        {'title': 'Profile', 'url_name': 'profile'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(4)
        context['menu'] = user_menu
        return context
