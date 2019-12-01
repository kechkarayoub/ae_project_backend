# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-11 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='First name')),
                ('message', models.TextField(verbose_name='Message')),
                ('object', models.CharField(max_length=30, verbose_name='Subject')),
                ('phone', models.CharField(blank=True, default='', max_length=20, verbose_name='Phone')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='ContactBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathrooms_number', models.CharField(blank=True, choices=[('', 'Select bathrooms number'), ('1', '1'), ('2', '2'), ('3_', '3 and more')], default='', max_length=10, verbose_name='Bathrooms number')),
                ('bedrooms_number', models.CharField(blank=True, choices=[('', 'Select bedrooms number'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5_', '5 and more')], default='', max_length=10, verbose_name='Bedrooms number')),
                ('building_type', models.CharField(blank=True, choices=[('', 'Select building type'), ('detached', 'Detached'), ('semi_detached', 'Semi detached'), ('attached', 'Attached'), ('attached_corner_unit', 'Attached corner unit'), ('quadrex', 'Quadrex')], default='', max_length=50, verbose_name='Building type')),
                ('city', models.CharField(choices=[('', 'Select city'), ('abbotsford', 'Abbotsford'), ('acton_vale', 'Acton Vale'), ('airdrie', 'Airdrie'), ('alma', 'Alma'), ('amos', 'Amos'), ('amqui', 'Amqui'), ('armstrong', 'Armstrong'), ('asbestos', 'Asbestos'), ('baie_comeau', 'Baie-Comeau'), ('baie_d_urfe', "Baie-D'Urfé"), ('baie_saint_paul', 'Baie-Saint-Paul'), ('barkmere', 'Barkmere'), ('barrie', 'Barrie'), ('bathurst', 'Bathurst'), ('beaconsfield', 'Beaconsfield'), ('beauceville', 'Beauceville'), ('beauharnois', 'Beauharnois'), ('beaumont', 'Beaumont'), ('beaupre', 'Beaupré'), ('becancour', 'Bécancour'), ('bedford', 'Bedford'), ('belleterre', 'Belleterre'), ('belleville', 'Belleville'), ('beloeil', 'Beloeil'), ('berthierville', 'Berthierville'), ('blainville', 'Blainville'), ('boisbriand', 'Boisbriand'), ('bois_des_filion', 'Bois-des-Filion'), ('bonaventure', 'Bonaventure'), ('boucherville', 'Boucherville'), ('brampton', 'Brampton'), ('brandon', 'Brandon'), ('brant', 'Brant'), ('brantford', 'Brantford'), ('brockville', 'Brockville'), ('brome_lake', 'Brome Lake'), ('bromont', 'Bromont'), ('brooks', 'Brooks'), ('brossard', 'Brossard'), ('brownsburg_chatham', 'Brownsburg-Chatham'), ('burlington', 'Burlington'), ('burnaby', 'Burnaby'), ('calgary', 'Calgary'), ('cambridge', 'Cambridge'), ('campbell_river', 'Campbell River'), ('campbellton', 'Campbellton'), ('camrose', 'Camrose'), ('candiac', 'Candiac'), ('cap_chat', 'Cap-Chat'), ('cap_sante', 'Cap-Santé'), ('carleton_sur_mer', 'Carleton-sur-Mer'), ('carignan', 'Carignan'), ('castlegar', 'Castlegar'), ('causapscal', 'Causapscal'), ('chambly', 'Chambly'), ('chandler', 'Chandler'), ('chapais', 'Chapais'), ('charlemagne', 'Charlemagne'), ('charlottetown', 'Charlottetown'), ('chateau_richer', 'Château-Richer'), ('chateauguay', 'Châteauguay'), ('chestermere', 'Chestermere'), ('chilliwack', 'Chilliwack'), ('chibougamau', 'Chibougamau'), ('clarence_rockland', 'Clarence-Rockland'), ('clermont', 'Clermont'), ('coaticook', 'Coaticook'), ('cold_lake', 'Cold Lake'), ('colwood', 'Colwood'), ('contrecoeur', 'Contrecoeur'), ('cookshire_eaton', 'Cookshire-Eaton'), ('coquitlam', 'Coquitlam'), ('corner_brook', 'Corner Brook'), ('cornwall', 'Cornwall'), ('cote_saint_luc', 'Côte Saint-Luc'), ('coteau_du_lac', 'Coteau-du-Lac'), ('courtenay', 'Courtenay'), ('cowansville', 'Cowansville'), ('cranbrook', 'Cranbrook'), ('danville', 'Danville'), ('dauphin', 'Dauphin'), ('daveluyville', 'Daveluyville'), ('dawson_creek', 'Dawson Creek'), ('degelis', 'Dégelis'), ('delson', 'Delson'), ('delta', 'Delta'), ('desbiens', 'Desbiens'), ('deux_montagnes', 'Deux-Montagnes'), ('dieppe', 'Dieppe'), ('disraeli', 'Disraeli'), ('dolbeau_mistassini', 'Dolbeau-Mistassini'), ('dollard_des_ormeaux', 'Dollard-des-Ormeaux'), ('donnacona', 'Donnacona'), ('dorval', 'Dorval'), ('drummondville', 'Drummondville'), ('dryden', 'Dryden'), ('duncan', 'Duncan'), ('dunham', 'Dunham'), ('duparquet', 'Duparquet'), ('east_angus', 'East Angus'), ('edmonton', 'Edmonton'), ('edmundston', 'Edmundston'), ('elliot_lake', 'Elliot Lake'), ('enderby', 'Enderby'), ('esterel', 'Estérel'), ('estevan', 'Estevan'), ('farnham', 'Farnham'), ('fermont', 'Fermont'), ('fernie', 'Fernie'), ('flin_flon', 'Flin Flon'), ('forestville', 'Forestville'), ('fort_saskatchewan', 'Fort Saskatchewan'), ('fort_st_john', 'Fort St. John'), ('fossambault_sur_le_lac', 'Fossambault-sur-le-Lac'), ('fredericton', 'Fredericton'), ('gaspe', 'Gaspé'), ('gatineau', 'Gatineau'), ('gracefield', 'Gracefield'), ('granby', 'Granby'), ('grand_forks', 'Grand Forks'), ('grande_prairie', 'Grande Prairie'), ('grande_riviere', 'Grande-Rivière'), ('greater_sudbury', 'Greater Sudbury'), ('greenwood', 'Greenwood'), ('guelph', 'Guelph'), ('haldimand_county', 'Haldimand County'), ('hamilton', 'Hamilton'), ('hampstead', 'Hampstead'), ('hudson', 'Hudson'), ('humboldt', 'Humboldt'), ('huntingdon', 'Huntingdon'), ('iqaluit', 'Iqaluit'), ('joliette', 'Joliette'), ('kamloops', 'Kamloops'), ('kawartha_lakes', 'Kawartha Lakes'), ('kelowna', 'Kelowna'), ('kenora', 'Kenora'), ('kimberley', 'Kimberley'), ('kingsey_falls', 'Kingsey Falls'), ('kingston', 'Kingston'), ('kirkland', 'Kirkland'), ('kitchener', 'Kitchener'), ('l_ancienne_lorette', "L'Ancienne-Lorette"), ('l_assomption', "L'Assomption"), ('l_epiphanie', "L'Épiphanie"), ('l_ile_cadieux', "L'Île-Cadieux"), ('l_ile_dorval', "L'Île-Dorval"), ('l_ile_perrot', "L'Île-Perrot"), ('la_malbaie', 'La Malbaie'), ('la_pocatiere', 'La Pocatière'), ('la_prairie', 'La Prairie'), ('la_sarre', 'La Sarre'), ('la_tuque', 'La Tuque'), ('lac_delage', 'Lac-Delage'), ('lac_megantic', 'Lac-Mégantic'), ('lac_saint_joseph', 'Lac-Saint-Joseph'), ('lac_sergent', 'Lac-Sergent'), ('lachute', 'Lachute'), ('lacombe', 'Lacombe'), ('langford', 'Langford'), ('langley', 'Langley'), ('laval', 'Laval'), ('lavaltrie', 'Lavaltrie'), ('lebel_sur_quevillon', 'Lebel-sur-Quévillon'), ('leduc', 'Leduc'), ('lery', 'Léry'), ('levis', 'Lévis'), ('lethbridge', 'Lethbridge'), ('lloydminster', 'Lloydminster'), ('london', 'London'), ('longueuil', 'Longueuil'), ('lorraine', 'Lorraine'), ('louiseville', 'Louiseville'), ('macamic', 'Macamic'), ('magog', 'Magog'), ('malartic', 'Malartic'), ('maniwaki', 'Maniwaki'), ('maple_ridge', 'Maple Ridge'), ('marieville', 'Marieville'), ('markham', 'Markham'), ('martensville', 'Martensville'), ('mascouche', 'Mascouche'), ('matagami', 'Matagami'), ('matane', 'Matane'), ('medicine_hat', 'Medicine Hat'), ('meadow_lake', 'Meadow Lake'), ('melfort', 'Melfort'), ('melville', 'Melville'), ('mercier', 'Mercier'), ('merritt', 'Merritt'), ('metabetchouan_lac_a_la_croix', 'Métabetchouan–Lac-à-la-Croix'), ('metis_sur_mer', 'Métis-sur-Mer'), ('mirabel', 'Mirabel'), ('miramichi', 'Miramichi'), ('mississauga', 'Mississauga'), ('moncton', 'Moncton'), ('mont_joli', 'Mont-Joli'), ('mont_laurier', 'Mont-Laurier'), ('montmagny', 'Montmagny'), ('montreal', 'Montreal'), ('montreal_west', 'Montreal West'), ('montreal_est', 'Montréal-Est'), ('mont_saint_hilaire', 'Mont-Saint-Hilaire'), ('mont_tremblant', 'Mont-Tremblant'), ('moose_jaw', 'Moose Jaw'), ('morden', 'Morden'), ('mount_royal', 'Mount Royal'), ('mount_pearl', 'Mount Pearl'), ('murdochville', 'Murdochville'), ('nanaimo', 'Nanaimo'), ('nelson', 'Nelson'), ('neuville', 'Neuville'), ('new_richmond', 'New Richmond'), ('new_westminster', 'New Westminster'), ('niagara_falls', 'Niagara Falls'), ('nicolet', 'Nicolet'), ('norfolk_county', 'Norfolk County'), ('normandin', 'Normandin'), ('north_bay', 'North Bay'), ('north_battleford', 'North Battleford'), ('north_vancouver', 'North Vancouver'), ('notre_dame_de_l_ile_perrot', "Notre-Dame-de-l'Île-Perrot"), ('notre_dame_des_prairies', 'Notre-Dame-des-Prairies'), ('orillia', 'Orillia'), ('oshawa', 'Oshawa'), ('ottawa', 'Ottawa'), ('otterburn_park', 'Otterburn Park'), ('owen_sound', 'Owen Sound'), ('parksville', 'Parksville'), ('paspebiac', 'Paspébiac'), ('pembroke', 'Pembroke'), ('penticton', 'Penticton'), ('perce', 'Percé'), ('peterborough', 'Peterborough'), ('pickering', 'Pickering'), ('pincourt', 'Pincourt'), ('pitt_meadows', 'Pitt Meadows'), ('plessisville', 'Plessisville'), ('pohenegamook', 'Pohénégamook'), ('pointe_claire', 'Pointe-Claire'), ('pont_rouge', 'Pont-Rouge'), ('port_alberni', 'Port Alberni'), ('port_cartier', 'Port-Cartier'), ('port_colborne', 'Port Colborne'), ('port_coquitlam', 'Port Coquitlam'), ('port_moody', 'Port Moody'), ('portneuf', 'Portneuf'), ('portage_la_prairie', 'Portage la Prairie'), ('powell_river', 'Powell River'), ('prevost', 'Prévost'), ('prince_albert', 'Prince Albert'), ('prince_edward_county', 'Prince Edward County'), ('prince_george', 'Prince George'), ('prince_rupert', 'Prince Rupert'), ('princeville', 'Princeville'), ('quebec', 'Québec'), ('quesnel', 'Quesnel'), ('quinte_west', 'Quinte West'), ('red_deer', 'Red Deer'), ('regina', 'Regina'), ('repentigny', 'Repentigny'), ('revelstoke', 'Revelstoke'), ('richelieu', 'Richelieu'), ('richmond', 'Richmond'), ('richmond_hill', 'Richmond Hill'), ('rimouski', 'Rimouski'), ('riviere_du_loup', 'Rivière-du-Loup'), ('riviere_rouge', 'Rivière-Rouge'), ('roberval', 'Roberval'), ('rosemere', 'Rosemère'), ('rossland', 'Rossland'), ('rouyn_noranda', 'Rouyn-Noranda'), ('saguenay', 'Saguenay'), ('saint_augustin_de_desmaures', 'Saint-Augustin-de-Desmaures'), ('saint_basile', 'Saint-Basile'), ('saint_basile_le_grand', 'Saint-Basile-le-Grand'), ('saint_bruno_de_montarville', 'Saint-Bruno-de-Montarville'), ('saint_cesaire', 'Saint-Césaire'), ('saint_colomban', 'Saint-Colomban'), ('saint_constant', 'Saint-Constant'), ('saint_eustache', 'Saint-Eustache'), ('saint_felicien', 'Saint-Félicien'), ('saint_gabriel', 'Saint-Gabriel'), ('saint_georges', 'Saint-Georges'), ('saint_hyacinthe', 'Saint-Hyacinthe'), ('saint_jean_sur_richelieu', 'Saint-Jean-sur-Richelieu'), ('saint_jerome', 'Saint-Jérôme'), ('saint_john', 'Saint John'), ('saint_joseph_de_beauce', 'Saint-Joseph-de-Beauce'), ('saint_joseph_de_sorel', 'Saint-Joseph-de-Sorel'), ('saint_lambert', 'Saint-Lambert'), ('saint_lazare', 'Saint-Lazare'), ('saint_lin_laurentides', 'Saint-Lin-Laurentides'), ('saint_marc_des_carrieres', 'Saint-Marc-des-Carrières'), ('saint_ours', 'Saint-Ours'), ('saint_pamphile', 'Saint-Pamphile'), ('saint_pascal', 'Saint-Pascal'), ('saint_pie', 'Saint-Pie'), ('saint_raymond', 'Saint-Raymond'), ('saint_remi', 'Saint-Rémi'), ('saint_sauveur', 'Saint-Sauveur'), ('saint_tite', 'Saint-Tite'), ('sainte_adele', 'Sainte-Adèle'), ('sainte_agathe_des_monts', 'Sainte-Agathe-des-Monts'), ('sainte_anne_de_beaupre', 'Sainte-Anne-de-Beaupré'), ('sainte_anne_de_bellevue', 'Sainte-Anne-de-Bellevue'), ('sainte_anne_des_monts', 'Sainte-Anne-des-Monts'), ('sainte_anne_des_plaines', 'Sainte-Anne-des-Plaines'), ('sainte_catherine', 'Sainte-Catherine'), ('sainte_catherine_de_la_jacques_cartier', 'Sainte-Catherine-de-la-Jacques-Cartier'), ('sainte_julie', 'Sainte-Julie'), ('sainte_marguerite_du_lac_masson', 'Sainte-Marguerite-du-Lac-Masson'), ('sainte_marie', 'Sainte-Marie'), ('sainte_marthe_sur_le_lac', 'Sainte-Marthe-sur-le-Lac'), ('sainte_therese', 'Sainte-Thérèse'), ('salaberry_de_valleyfield', 'Salaberry-de-Valleyfield'), ('salmon_arm', 'Salmon Arm'), ('sarnia', 'Sarnia'), ('saskatoon', 'Saskatoon'), ('sault_ste._marie', 'Sault Ste. Marie'), ('schefferville', 'Schefferville'), ('scotstown', 'Scotstown'), ('selkirk', 'Selkirk'), ('senneterre', 'Senneterre'), ('sept_iles', 'Sept-Îles'), ('shawinigan', 'Shawinigan'), ('sherbrooke', 'Sherbrooke'), ('sorel_tracy', 'Sorel-Tracy'), ('spruce_grove', 'Spruce Grove'), ('st_albert', 'St. Albert'), ('st_catharines', 'St. Catharines'), ('st_john_s', "St. John's"), ('st_thomas', 'St. Thomas'), ('stanstead', 'Stanstead'), ('stratford', 'Stratford'), ('steinbach', 'Steinbach'), ('summerside', 'Summerside'), ('surrey', 'Surrey'), ('sutton', 'Sutton'), ('swift_current', 'Swift Current'), ('temiscaming', 'Témiscaming'), ('temiscouata_sur_le_lac', 'Témiscouata-sur-le-Lac'), ('temiskaming_shores', 'Temiskaming Shores'), ('terrace', 'Terrace'), ('terrebonne', 'Terrebonne'), ('thetford_mines', 'Thetford Mines'), ('thompson', 'Thompson'), ('thorold', 'Thorold'), ('thunder_bay', 'Thunder Bay'), ('thurso', 'Thurso'), ('timmins', 'Timmins'), ('toronto', 'Toronto'), ('trail', 'Trail'), ('trois_pistoles', 'Trois-Pistoles'), ('trois_rivieres', 'Trois-Rivières'), ('val_d_or', "Val-d'Or"), ('valcourt', 'Valcourt'), ('vancouver', 'Vancouver'), ('varennes', 'Varennes'), ('vaudreuil_dorion', 'Vaudreuil-Dorion'), ('vaughan', 'Vaughan'), ('vernon', 'Vernon'), ('victoria', 'Victoria'), ('victoriaville', 'Victoriaville'), ('ville_marie', 'Ville-Marie'), ('warman', 'Warman'), ('warwick', 'Warwick'), ('waterloo', 'Waterloo'), ('waterville', 'Waterville'), ('welland', 'Welland'), ('west_kelowna', 'West Kelowna'), ('westmount', 'Westmount'), ('wetaskiwin', 'Wetaskiwin'), ('weyburn', 'Weyburn'), ('white_rock', 'White Rock'), ('whitehorse', 'Whitehorse'), ('williams_lake', 'Williams Lake'), ('windsor', 'Windsor'), ('winkler', 'Winkler'), ('winnipeg', 'Winnipeg'), ('woodstock', 'Woodstock'), ('yellowknife', 'Yellowknife'), ('yorkton', 'Yorkton')], default='', max_length=100, verbose_name='City')),
                ('construction_age', models.CharField(blank=True, choices=[('', 'Select construction age'), ('newly_built', 'Newly built'), ('10_years_and_less', '10 years and less'), ('more_than_10_years', 'More than 10 years')], default='', max_length=20, verbose_name='Construction age')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('has_dining_room', models.BooleanField(default=False, verbose_name='Dining room')),
                ('has_fireplace', models.BooleanField(default=False, verbose_name='Fireplace')),
                ('has_garage', models.BooleanField(default=False, verbose_name='Garage')),
                ('has_garden', models.BooleanField(default=False, verbose_name='Garden')),
                ('has_swimming_pool', models.BooleanField(default=False, verbose_name='Swimming pool')),
                ('last_name', models.CharField(max_length=30, verbose_name='First name')),
                ('lot_size_min', models.PositiveIntegerField(default=0, verbose_name='Lot size min(m²)')),
                ('lot_size_max', models.PositiveIntegerField(default=0, verbose_name='Lot size max(m²)')),
                ('occupation_date', models.DateField(null=True, verbose_name='Occupation date')),
                ('other_characteristics', models.TextField(blank=True, null=True, verbose_name='Other characteristics')),
                ('phone', models.CharField(blank=True, default='', max_length=20, verbose_name='Phone')),
                ('price_range', models.CharField(blank=True, choices=[('', 'Not specified'), ('0_200', 'Less than 200 000$'), ('200_300', '200 000$ - 300 000$'), ('300_400', '300 000$ - 400 000$'), ('400_500', '400 000$ - 500 000$'), ('500_1000', 'More than 500 000$')], default='', max_length=50, verbose_name='Price range')),
                ('property_type', models.CharField(blank=True, choices=[('', 'Select property type'), ('apartment', 'Apartment'), ('duplex', 'Duplex'), ('quadruplex', 'Quadruplex'), ('quintuplex', 'Quintuplex'), ('ground_floor_house', 'Ground floor house'), ('two_or_more_storey', 'Two or more storey'), ('split_level', 'Split-level'), ('one_and_a_half_storey_house', 'One-and-a-half-storey house'), ('mobile_home', 'Mobile home'), ('house', 'House'), ('loft_studio', 'Loft / Studio'), ('commercial', 'Commercial'), ('industrial', 'Industrial'), ('company', 'Company (business)'), ('bulk', 'Bulk (block sale)'), ('land', 'Land'), ('lot', 'Lot'), ('farm', 'Farm'), ('hobby_farm', 'Hobby farm'), ('other', 'Other')], default='', max_length=50, verbose_name='Property type')),
                ('status', models.CharField(blank=True, choices=[('for_sale', 'For sale'), ('for_rent', 'For rent'), ('sold', 'Sold')], default='for_sale', max_length=20, verbose_name='Status')),
            ],
            options={
                'db_table': 'contact_buy',
            },
        ),
    ]
