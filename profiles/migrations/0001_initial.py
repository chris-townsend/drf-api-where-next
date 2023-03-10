# Generated by Django 3.2.18 on 2023-02-28 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, choices=[('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua', 'Antigua'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('The Bahamas', 'The Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia', 'Bosnia'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Central African Republic', 'Central African Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Congo, Republic of the', 'Congo, Republic of the'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Korea, North', 'Korea, North'), ('Korea, South', 'Korea, South'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Mongolia'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Nigeria', 'Nigeria'), ('North Macedonia', 'North Macedonia'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('San Marino', 'San Marino'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Tonga', 'Tonga'), ('Trinidad', 'Trinidad'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50)),
                ('favourite_location', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('profile_image', models.ImageField(default='../default_user_s9bxgj', upload_to='images/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
