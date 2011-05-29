import badges
from CoffeeGrid.userprofiles.models import UserProfile

class Autobiographer(badges.MetaBadge):
    id = "autobiographer"
    model = UserProfile
    one_time_only = True

    title = "Autobiographer"
    description = "Completed the User Profile"
    level = "1"

    progress_start = 0
    progress_finish = 2

    def get_user(self, instance):
        return instance.user

    def get_progress(self, user):
        has_email = 1 if user.email else 0
        has_bio = 1 if user.get_profile().intro else 0
        return has_email + has_bio

    def check_email(self, instance):
        return instance.user.email

    def check_bio(self, instance):
        return instance.intro
