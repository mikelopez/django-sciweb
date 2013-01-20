class admin_models:
    """ class wrapper for admin_models data dict """
    models = {
        'website': 'mainweb',
        'websitepage': 'mainweb'
    }
    forms = {
        'website': 'WebsiteForm', 
        'websitepage': 'WebsitePageForm'
    }

    def __init__(self):
        pass


    def get_app(self, k):
        """
        get the app name based on a model
        """
        return self.models.get(k)


    def get_app_by_model(self, k):
        """
        get the app name by the model name so that 
        we can know which app to look for forms in
        """
        if not k in self.models.keys():
            return None
        return self.models.get(k)


    def get_form_by_model(self, k):
        """
        get the form class by the model name and app name
        """
