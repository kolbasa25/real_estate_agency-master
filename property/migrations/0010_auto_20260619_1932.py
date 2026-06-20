from django.db import migrations
from phonenumbers import parse, format_number, PhoneNumberFormat, is_valid_number

def normalize_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        if flat.owners_phonenumber:
            try:
                parsed = parse(flat.owners_phonenumber, 'RU')
                if is_valid_number(parsed):
                    flat.owner_pure_phone = format_number(parsed, PhoneNumberFormat.INTERNATIONAL)
                else:
                    flat.owner_pure_phone = None
                flat.save(update_fields=['owner_pure_phone'])
            except Exception:
                flat.owner_pure_phone = None
                flat.save(update_fields=['owner_pure_phone'])

def reverse_normalize_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone=None)

class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_auto_20260619_1921'),
    ]

    operations = [
        migrations.RunPython(normalize_phones, reverse_normalize_phones),
    ]