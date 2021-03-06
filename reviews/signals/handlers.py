from django.conf import settings


def create_notice_types():
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from pinax.notifications.models import NoticeType
        print("Creating notices for review")
        NoticeType.create('new_review', ' Review added ', 'Check out this review')
    else:
        print("Notification app not found")
