# Generated by Django 3.2.7 on 2021-09-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataretrievalapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stepmaterialmapper',
            name='material',
        ),
        migrations.RemoveField(
            model_name='stepmaterialmapper',
            name='step',
        ),
        migrations.RemoveField(
            model_name='steprecipemapper',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='steprecipemapper',
            name='step',
        ),
        migrations.AddField(
            model_name='material',
            name='steps',
            field=models.ManyToManyField(to='dataretrievalapi.Step'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='projects',
            field=models.ManyToManyField(to='dataretrievalapi.Project'),
        ),
        migrations.AddField(
            model_name='step',
            name='recipes',
            field=models.ManyToManyField(to='dataretrievalapi.Recipe'),
        ),
        migrations.DeleteModel(
            name='RecipeProjectMapper',
        ),
        migrations.DeleteModel(
            name='StepMaterialMapper',
        ),
        migrations.DeleteModel(
            name='StepRecipeMapper',
        ),
    ]
