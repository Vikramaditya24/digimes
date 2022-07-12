# Generated by Django 3.1.1 on 2021-10-14 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_model',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('staff', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Phone Number')),
                ('faculty', models.CharField(max_length=100, null=True, verbose_name='Faculty')),
                ('dept', models.CharField(max_length=100, null=True, verbose_name='Department')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='profile_model',
            fields=[
                ('dept', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=10, verbose_name='Department')),
                ('name', models.CharField(max_length=100, verbose_name='Name of the Staff')),
                ('qualification', models.CharField(max_length=100, verbose_name='Qualification of the Staff ')),
                ('designation', models.CharField(choices=[('HOD', 'HOD'), ('Lecturer', 'Lecturer')], max_length=100, verbose_name='Designation')),
                ('num', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('doj', models.DateField(verbose_name='Date of joining MESACS')),
                ('pan', models.CharField(max_length=100, verbose_name='PAN number')),
                ('aadhar', models.CharField(max_length=100, verbose_name='AAdhar Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email ID')),
                ('address', models.TextField(verbose_name='Address')),
                ('photo', models.ImageField(upload_to='images', verbose_name='Photos')),
                ('tenth_markscard', models.FileField(blank='True', null='True', upload_to='files', verbose_name='Tenth Marks Card')),
                ('pu_markscard', models.FileField(blank='True', null='True', upload_to='files', verbose_name='PU Marks Card')),
                ('degree_markscard', models.FileField(blank='True', null='True', upload_to='files', verbose_name='Degree Marks Card')),
                ('master_markscard', models.FileField(blank='True', null='True', upload_to='files', verbose_name="Master's Marks Card")),
                ('mphill_markscard', models.FileField(blank='True', null='True', upload_to='files', verbose_name="MPhill's Marks Card")),
                ('phd_markscard', models.FileField(blank='True', null='True', upload_to='files', verbose_name='Phd Marks Card')),
                ('apppointment_letter', models.FileField(blank='True', null='True', upload_to='files', verbose_name='Appointment Letter')),
                ('resume', models.FileField(null='True', upload_to='files', verbose_name='Resume')),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='univ_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('BOS', 'BOS'), ('BOE', 'BOE'), ('Valuation', 'Valuation'), ('Others if any', 'Others if any')], max_length=100, verbose_name='Activities')),
                ('date', models.DateField(verbose_name='Date')),
                ('document', models.FileField(null='True', upload_to='files', verbose_name='Document')),
                ('staff', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='staff.profile_model')),
            ],
        ),
        migrations.CreateModel(
            name='pub_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('Publication of staff in the Journals notified on UGC Website', 'Publication of staff in the Journals notified on UGC Website'), ('Publication of staff in National/International Conference Prooceedings', 'Publication of staff in National/International Conference Prooceedings'), ('Publication of staff in the Books and Book Chapters in Edited Volume', 'Publication of staff in the Books and Book Chapters in Edited Volume'), ('Others if any', 'Others if any')], max_length=100, verbose_name='Publication in')),
                ('dept', models.CharField(max_length=10, verbose_name='Department')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('name', models.CharField(max_length=100, verbose_name='Name of the author/s')),
                ('num', models.CharField(max_length=100, verbose_name='Number of the Journal/Chapter')),
                ('year', models.CharField(max_length=100, verbose_name='Year of publication')),
                ('issn', models.CharField(max_length=100, verbose_name='ISSN/ISBN Number')),
                ('pubname', models.CharField(blank=True, max_length=100, verbose_name='Name of the Publisher')),
                ('document', models.FileField(upload_to='files', verbose_name='Upload UGC enlistment of the Journal')),
                ('staff', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='staff.profile_model')),
            ],
        ),
        migrations.CreateModel(
            name='port_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Portfolio Name')),
                ('year', models.CharField(max_length=10, verbose_name='Year')),
                ('desc', models.TextField(verbose_name='Descprition in 500 words')),
                ('staff', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='staff.profile_model')),
            ],
        ),
        migrations.CreateModel(
            name='misc_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('Guest of Honours', 'Guest of Honours'), ('Awards', 'Awards'), ('Apreciation', 'Appreciation'), ('Lectures Given', 'Lectures Given'), ('Faculty Development conducted', 'Faculty Development conducted'), ('Any Other Relevant', 'Any Other Relevant')], max_length=100, verbose_name='Achievement')),
                ('date', models.DateField(verbose_name='Date')),
                ('document', models.FileField(null='True', upload_to='files', verbose_name='Document')),
                ('staff', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='staff.profile_model')),
            ],
        ),
        migrations.CreateModel(
            name='aad_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('Seminar', 'Seminar'), ('Workshop', 'Workshop'), ('Conference attendance', 'Conference attendance'), ('Paper Presentation attendance', 'Paper Presentation attendance'), ('Faculty Development Program', 'Faculty Development Program'), ('Referesher', 'Referesher'), ('Orientation Prg Attended', 'Orientation Prg Attended'), ('Others if any', 'Others if any')], max_length=100, verbose_name='Event')),
                ('date', models.DateField(verbose_name='Date')),
                ('document', models.FileField(null='True', upload_to='files', verbose_name='Document')),
                ('staff', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='staff.profile_model')),
            ],
        ),
    ]
