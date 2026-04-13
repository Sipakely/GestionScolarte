from django.db import migrations, models


def populate_school_username(apps, schema_editor):
    School = apps.get_model('utilisateur', 'School')
    UserAccount = apps.get_model('utilisateur', 'UserAccount')

    used_usernames = set(
        School.objects.exclude(username__isnull=True).exclude(username='').values_list('username', flat=True)
    )

    for school in School.objects.all().order_by('id'):
        if school.username:
            used_usernames.add(school.username)
            continue

        related_user = UserAccount.objects.filter(school_id=school.id).order_by('id').first()
        base_username = ''
        if related_user and related_user.username:
            base_username = related_user.username.strip()

        if not base_username:
            base_username = school.email.split('@')[0].strip() if school.email else f'school{school.id}'

        if not base_username:
            base_username = f'school{school.id}'

        candidate = base_username
        suffix = 1
        while candidate in used_usernames:
            candidate = f'{base_username}{suffix}'
            suffix += 1

        school.username = candidate
        school.save(update_fields=['username'])
        used_usernames.add(candidate)


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0003_school_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.RunPython(populate_school_username, noop_reverse),
    ]
