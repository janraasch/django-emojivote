from django.db import migrations


def seed_emojis(apps, schema_editor):
    Emoji = apps.get_model("vote", "Emoji")
    emojis = [
        ("🐍", "Snake"),
        ("🦄", "Unicorn"),
        ("🚀", "Rocket"),
        ("🎸", "Guitar"),
        ("🌮", "Taco"),
        ("🐶", "Dog"),
    ]
    for character, name in emojis:
        Emoji.objects.create(character=character, name=name)


class Migration(migrations.Migration):
    dependencies = [
        ("vote", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_emojis, migrations.RunPython.noop),
    ]
