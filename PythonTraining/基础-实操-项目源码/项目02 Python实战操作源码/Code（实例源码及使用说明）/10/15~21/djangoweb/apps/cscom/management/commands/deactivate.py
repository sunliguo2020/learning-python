from django.core.management.base import BaseCommand, CommandError
from apps.mail.models import User


class Command(BaseCommand):
    help = '更改用户激活状态为False'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for user_id in options['user_id']:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise CommandError('User "%s" does not exist' % user_id)

            # 更改用户的激活状态
            user.is_active = False
            user.save()

            self.stdout.write(self.style.SUCCESS('Successfully change user activation status to false "%s"' % user_id))
