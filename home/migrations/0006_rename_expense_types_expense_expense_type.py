# Generated by Django 4.1.6 on 2023-02-09 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_amounts_expense_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense_types',
            new_name='expense_type',
        ),
    ]
