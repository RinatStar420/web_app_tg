from django.apps import AppConfig
# from signals import handlers

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'



# class ChannelsConfig(AppConfig):
#     default_app_config = 'core.apps.ChannelsConfig'
#     name = 'channels'
#     verbose_name = 'Channels'
#
#     def ready(self):
#         handlers.create_user_report()