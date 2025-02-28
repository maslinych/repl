#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from HTMLParser import HTMLParser
parser = HTMLParser()
import os
import time

def addtheme(old,metatag,conditions) :
	global theme
	if old :
		conditions=re.sub(ur"ɛɛ",u"èe", conditions)
		conditions=re.sub(ur"ɛ",u"è", conditions)
		conditions=re.sub(ur"ɔ",u"ò", conditions)
		conditions=re.sub(ur"Ɛ",u"È", conditions)
		conditions=re.sub(ur"Ɔ",u"Ò", conditions)
		conditions=re.sub(ur"ɲ",u"ny", conditions)
		conditions=re.sub(ur"Ɲ",u"Ny", conditions)
	l=0
	m=re.findall(conditions,tout,re.I|re.U)
	if m!=None :
		l=len(m)
		# print metatag, l
	if l>=4 :
		if theme=="": theme=metatag
		else : 
			if metatag not in theme : theme=theme+";"+metatag

def addgenre(metatag,conditions,inwhat,nb) :
	global genre
	l=0
	m=re.findall(conditions,inwhat,re.I|re.U)
	if m!=None :
		l=len(m)
		# print metatag, l
	if l>=nb :
		if genre=="": genre=metatag
		else : 
			if metatag not in genre : genre=genre+";"+metatag
# auteurs, exemples
# prévoir tout ça, éventuellement plus d'un auteur par content
# <meta content="Kane, Sumana" name="author:name" />
# <meta content="" name="author:spelling" />
# <meta content="0" name="author:birth_year" />
# <meta content="m" name="author:sex" />
# <meta content="Bambara" name="author:native_lang" />
# <meta content="" name="author:dialect" />
# <meta content="habite Bamakɔ, Balikukalan baarada DNAFLA, EN-SUP" name="author:addon" />
# <meta content="11aefaf1-6d5b-4ffa-84c7-24a3edb32670" name="author:uuid" />
		
# <meta content="Ture, Basiriki|Kante, Amadu Gaɲi" name="author:name" />
# <meta content="|" name="author:spelling" />
# <meta content="0|1936" name="author:birth_year" />
# <meta content="m|m" name="author:sex" />
# <meta content="Bambara|Bambara" name="author:native_lang" />
# <meta content="|Kayes" name="author:dialect" />
# <meta content="éditeur de Kibaru&#10;(ou Basidiki Ture)|né à Kita. Travaille au Point G de 1955 à 1963. Puis AMAP, L'ESSOR, L'INFORMATEUR, et enfin KIBARU." name="author:addon" />
# <meta content="60ba1311-ba33-4b5a-ab42-8fb1a6038263|797f3350-5147-480b-9ec5-4f7ccfe35139" name="author:uuid" />
dictauth={}  # devrait être chargé par authors.csv
dictauth[u"797f3350-5147-480b-9ec5-4f7ccfe35139"]=u"Kante, Amadu Gaɲi||1936|m|Bambara|Kayes|né à Kita. Travaille au Point G de 1955 à 1963. Puis AMAP, L'ESSOR, L'INFORMATEUR, et enfin KIBARU."
dictauth[u"60ba1311-ba33-4b5a-ab42-8fb1a6038263"]=u"Ture, Basiriki||0|m|Bambara||éditeur de Kibaru&#10;(ou Basidiki Ture)"
dictauth[u"11aefaf1-6d5b-4ffa-84c7-24a3edb32670"]=u"Kane, Sumana||0|m|Bambara||habite Bamakɔ, Balikukalan baarada DNAFLA, EN-SUP"
#"Jara, Dɔkala Yusufu",,,1966,Bamako,Bambara,"école à Kpoyo, lycée à Bamakɔ, dès 1994 travaille à DNAFLA, rèdacteur de Kibaru depuis 2003",b5edd814-54dd-4058-bd8c-dae51a64427d
dictauth[u"b5edd814-54dd-4058-bd8c-dae51a64427d"]=u"Jara, Dɔkala Yusufu||1966|m|Bambara|Bamako|école à Kpoyo, lycée à Bamakɔ, dès 1994 travaille à DNAFLA, rèdacteur de Kibaru depuis 2003"
#"Konta, Mahamadu",,m,,Bamako,Bambara,"né en 1957 à Bamakɔ. Diplomé ENSec-Badalabougou, a travaillé à San, Dili, Dioliba, et Baguinda et il est retourné à Bamako en 1995 pour étudier les langues nationales à l’Ecole Normale Superieure. Son premier livre a paru en 1995: Npalan, un recueil de poèmes en bamanankan. (Kɔnta)",c742b89a-fdfb-4d5c-9868-690d9935fa18
dictauth[u"c742b89a-fdfb-4d5c-9868-690d9935fa18"]=u"Konta, Mahamadu|||m|Bambara|Bamako|né en 1957 à Bamakɔ. Diplomé ENSec-Badalabougou, a travaillé à San, Dili, Dioliba, et Baguinda et il est retourné à Bamako en 1995 pour étudier les langues nationales à l’Ecole Normale Superieure. Son premier livre a paru en 1995: Npalan, un recueil de poèmes en bamanankan. (Kɔnta)"
#"Kulubali, Negeta",,,,,Bambara,"balikukalan karamɔgɔ, Banani Dunba (Kula), Kulukɔrɔ (aussi: Kulibali!)",c6563397-b2fb-465b-8c84-98ff0740b9ca
dictauth[u"c6563397-b2fb-465b-8c84-98ff0740b9ca"]=u"Kulubali, Negeta||||Bambara||balikukalan karamɔgɔ, Banani Dunba (Kula), Kulukɔrɔ (aussi: Kulibali!)"
#"Dunbuya, Amadu Tanba",,m,,,,"Bamakɔ (ou Dunbiya) - Maaya Dɔnniyada, Kanko Bolofara",587fb4ba-1385-4a2c-ab47-d60ed68d321b
dictauth[u"587fb4ba-1385-4a2c-ab47-d60ed68d321b"]=u"Dunbuya, Amadu Tanba|||m|||Bamakɔ (ou Dunbiya) - Maaya Dɔnniyada, Kanko Bolofara"
#"Dukure, Badama",,m,,,,Membre de l'équipe de Kibaru,8929d366-cfb6-4da7-a02f-1edea162b6e5
dictauth[u"8929d366-cfb6-4da7-a02f-1edea162b6e5"]=u"Dukure, Badama|||m|||Membre de l'équipe de Kibaru"
#"Sidibe, Burama",,m,,,Bambara,"Sirakɔrɔla, C.A.R. Kulukɔrɔ mara",7ef74ea3-7846-46f1-ba22-ff113b2a40e8
dictauth[u"7ef74ea3-7846-46f1-ba22-ff113b2a40e8"]=u"Sidibe, Burama|||m|Bambara||Sirakɔrɔla, C.A.R. Kulukɔrɔ mara"
#"Kantɛ, Solomani",,m,,,,"Denmisɛnw lakisi cakɛda ɲɛmɔgɔ, Kɔlɔnjɛba",dd718913-98f3-47aa-bce2-2fbffb72e317
dictauth[u"dd718913-98f3-47aa-bce2-2fbffb72e317"]=u"Kantɛ, Solomani|||m|||Denmisɛnw lakisi cakɛda ɲɛmɔgɔ, Kɔlɔnjɛba"
#"Kamisɔkɔ, Musa",,m,,,Bambara,sariyatigi,a67a4acf-6dbe-4bc1-8e20-d32c4b613128
dictauth[u"a67a4acf-6dbe-4bc1-8e20-d32c4b613128"]=u"Kamisɔkɔ, Musa|||m|Bambara||sariyatigi"
# "Sidibe, Tumani Yalam",,m,1955,Kita,Bambara,"né à Bamako, toute la vie à Bamako, Yarankabugu, sauf 1977-1989 à San, Koutiala, Kolokani (service d'alphabétisation); professeur du français par formation; éditeur de Jèkabaara",37fb14af-e1f9-4ba2-ba7c-5f67401f42fd
dictauth[u"37fb14af-e1f9-4ba2-ba7c-5f67401f42fd"]=u"Sidibe, Tumani Yalam||1955|m|Bambara|Kita|né à Bamako, toute la vie à Bamako, Yarankabugu, sauf 1977-1989 à San, Koutiala, Kolokani (service d'alphabétisation); professeur du français par formation; éditeur de Jèkabaara"
# "Si, Bubakari",,m,,,,Habite Sebekɔrɔ,297f5e59-7e14-4f9f-af0e-46a8373bcfdb
dictauth[u"297f5e59-7e14-4f9f-af0e-46a8373bcfdb"]=u"Si, Bubakari|||m|Bambara||Habite Sebekɔrɔ - 1973"
# "Tangara, Ya",,,,,Bambara,habitant Kucala,868d316d-c084-45db-921f-966fa94724ef
dictauth[u"868d316d-c084-45db-921f-966fa94724ef"]=u"Tangara, Ya||||Bambara||habitant Kucala - 1973"
#"Kulubali, Mamadu",,m,,,Bambara,habitant de Welesebugu,7389e900-8214-4516-9ba1-b8b403708d7c
dictauth[u"7389e900-8214-4516-9ba1-b8b403708d7c"]=u"Kulubali, Mamadu|||m|Bambara||habitant de Welesebugu - 1973"
# "Kulubali, Modibo",,m,,,,"Cɛcɛnbugu-Molodo, Ɲɔnɔn mara",b8c824dd-40ed-46b3-939d-0687fd3415fd
dictauth[u"b8c824dd-40ed-46b3-939d-0687fd3415fd"]=u"Kulubali, Modibo|||m|Bambara||Cɛcɛnbugu-Molodo, Ɲɔnɔn mara - 1973"
# "Ture, Seyidu",,m,,,Bambara,"habitant Ɲarela, Bamako",72559003-6529-4e84-b9c5-ef681d1b01dd
dictauth[u"72559003-6529-4e84-b9c5-ef681d1b01dd"]=u"Ture, Seyidu|||m|Bambara||habite Ɲarela, Bamakɔ - 1973 (Sedu)"
# "Berete, Nanpe",,,,,Bambara,habitant Jalafara,4627912e-d8e0-405b-a3d2-147cc73d8533
dictauth[u"4627912e-d8e0-405b-a3d2-147cc73d8533"]=u"Berete, Nanpe||||Bambara||habitant Jalafara - 1973"
# "Jara, Yaya",,m,,,Bambara,"Banantu, Buguda-Bɛlɛkɔ",fd800f25-d6ee-4b9f-b6f9-72c129183b79
dictauth[u"fd800f25-d6ee-4b9f-b6f9-72c129183b79"]=u"Jara, Yaya|||m|Bambara||Banantu, Buguda-Bɛlɛkɔ - 1973"
# "Jakite, Solomani",,m,,,Bambara,habite Masigi,33f55de3-c1d0-4365-a13f-05e6360b8ed1
dictauth[u"33f55de3-c1d0-4365-a13f-05e6360b8ed1"]=u"Jakite, Solomani|||m|Bambara||habite Masigi - 1973"
# "Banba, Namori",,m,,,Bambara,habite Nosonbugu,c4c865cb-8ccd-4ff4-9761-7186683456ef
dictauth[u"c4c865cb-8ccd-4ff4-9761-7186683456ef"]=u"Banba, Namori|||m|Bambara||habite Nosonbugu - 1973"
# "Mayiga, Bulkadèri",,m,,,,,6a1ab6fb-203c-4ef6-83a5-e020afcf9b92
dictauth[u"6a1ab6fb-203c-4ef6-83a5-e020afcf9b92"]=u"Mayiga, Bulkadɛri|||m|Bambara||1973"
# "Mariko, Yaya",,m,,,,"Kalabankɔrɔ/Senu, Kati mara",b746f073-4777-465a-8ee4-0276592cfb09
dictauth[u"b746f073-4777-465a-8ee4-0276592cfb09"]=u"Mariko, Yaya|||m|||Kalabankɔrɔ/Senu, Kati mara"
#"Kante, Ibarahima",,m,,,Bambara,"DNAFLA, Bamakɔ - Operasiyɔn Ɔtiwale",40310b23-7d3e-4f67-98ba-8e48cbae36da
dictauth[u"40310b23-7d3e-4f67-98ba-8e48cbae36da"]=u"Kante, Ibarahima|||m|Bambara||DNAFLA, Bamakɔ - Operasiyɔn Ɔtiwale"
# "Jaabi, Musa",,m,,,Bambara,"habite Bamakɔ - bamanankan karamɔgɔ, Balikukalan baarada",51652320-a88e-4b50-87f2-fc1b465a20a6
dictauth[u"51652320-a88e-4b50-87f2-fc1b465a20a6"]=u"Jaabi, Musa|||m|Bambara||habite Bamakɔ - bamanankan karamɔgɔ, Balikukalan baarada - 1987"
# "Kulubali, Negeta",,,,,Bambara,"balikukalan karamɔgɔ, Banani Dunba (Kula), Kulukɔrɔ (aussi: Kulibali!) - 1988",c6563397-b2fb-465b-8c84-98ff0740b9ca
dictauth[u"c6563397-b2fb-465b-8c84-98ff0740b9ca"]=u"Kulubali, Negeta||||Bambara||balikukalan karamɔgɔ, Banani Dunba (Kula), Kulukɔrɔ (aussi: Kulibali!) - 1988"
# "Balo, Faraban",,m,,,,"Fuladugu Kɔtuba, commune de Sebekɔrɔ, Kita - 1987, 2016",596d1365-a5b5-4aad-a3ec-937a2ec44035
dictauth[u"596d1365-a5b5-4aad-a3ec-937a2ec44035"]=u"Balo, Faraban|||m|Bambara||Fuladugu Kɔtuba, commune de Sebekɔrɔ, Kita - 1987, 2016"
# "Jalo, Isa",,m,,,,"Danbana, Kɔdugu, Dugabugu komini, Kati mara 2016",9a336ead-63bd-4bac-88a4-e63fa83c8505
dictauth[u"9a336ead-63bd-4bac-88a4-e63fa83c8505"]=u"Jalo, Isa|||m|Bambara||Danbana, Kɔdugu, Dugabugu komini, Kati mara 2016"
#"Kɔnɛ, Alu",,m,,,Bambara,"habite Zoni Ɛndisiriyɛli, Bamakɔ jagokɛla",2246823e-f72a-48b5-b593-f215a321b963
dictauth[u"2246823e-f72a-48b5-b593-f215a321b963"]=u"Kɔnɛ, Alu|||m|Bambara||habite Zoni Ɛndisiriyɛli, Bamakɔ jagokɛla"
#"Tarawele, Daramani (Daramane)",,m,,,Bambara,"chercheur à DNAFLA/ILAB, habitant de Nyaca",2da173f5-f2f0-4af0-a413-3ca3c6ee7a88
dictauth[u"2da173f5-f2f0-4af0-a413-3ca3c6ee7a88"]=u"Tarawele, Daramani (Daramane)|||m|Bambara||chercheur à DNAFLA/ILAB, habitant de Nyaca"	
# "Mɛnta, Suleyimani",,m,,,Bambara,ou Solomani,63b70297-b35e-4b1f-b5df-27fcc6dec7a5
dictauth[u"63b70297-b35e-4b1f-b5df-27fcc6dec7a5"]=u"Mɛnta, Suleyimani|||m|Bambara||ou Solomani, 1974"
# "So, Ibarahima",,m,,,Bambara,"habite Bamakɔ - kiimelikɛla, Balikukalan baarada la",8efb9f72-1f7f-45ef-88e2-63df76aa2766
dictauth[u"8efb9f72-1f7f-45ef-88e2-63df76aa2766"]=u"So, Ibarahima|||m|Bambara||habite Bamakɔ - kiimelikɛla, Balikukalansoba DNAFLA, 1989"
# "Keyita, Dawuda Moriba",,m,,,,"Bamakɔ  bp 1629, 1989, 1990 ... / BP 49 Sibi",5e81a35c-c026-408e-8680-ca4ea0d8d222
dictauth[u"5e81a35c-c026-408e-8680-ca4ea0d8d222"]=u"Keyita, Dawuda Moriba|||m|Bambara||Bamakɔ  bp 1629, 1989, 1990 ... / BP 49 Sibi"
#"Danbele, Mukutari",,,,,Bambara,"habite Sabalibugu ""A"", lakɔlikaramɔgɔ 1990",1f8ea9bb-43b3-4c4f-8e8d-7275175cfd05
dictauth[u"1f8ea9bb-43b3-4c4f-8e8d-7275175cfd05"]=u"Danbele, Mukutari||||Bambara||habite Sabalibugu A, lakɔlikaramɔgɔ 1990"
#"Sunkara, Amadu",,m,,,Bambara,"Kapala (Molobala), Kucala -  1987, 1988, 1993",f65af322-1fe8-4381-b65d-68758164036e
dictauth[u"f65af322-1fe8-4381-b65d-68758164036e"]=u"Sunkara, Amadu|||m|Bambara||Kapala (Molobala), Kucala -  1987, 1988, 1990,1993"
# "Jakite, Mamadu",,m,,,Bambara,habite Bamakɔ - «AA» - BP: 34 - TEL: 22-36-02 : 1990,0b692d2a-a0fa-4adb-869d-8249580da079
dictauth[u"0b692d2a-a0fa-4adb-869d-8249580da079"]=u"Jakite, Mamadu|||m|Bambara||habite Bamakɔ - «AA» - BP: 34 - TEL: 22-36-02 : 1990"
# "Kɔnɛ, Mohamɛdi",,m,,,,"maître d'école, Ɲɔrɔn Sahili kafo(aussi : Konɛ)",17e50ef6-e4ef-4373-a3bc-6b9fa536bfea
dictauth[u"17e50ef6-e4ef-4373-a3bc-6b9fa536bfea"]=u"Kɔnɛ, Mohamɛdi|||m|Bambara||maître d'école, Ɲɔrɔn Sahili kafo(aussi : Konɛ), 1990"
#"Komagara, Jiki",,m,,,,"Kɛɲɛlen, Kaaba, signe aussi Ji Komakara; Jigi Komakara, 1990",4b4d9826-8885-4fcd-92fc-2ff651a0b23e
dictauth[u"4b4d9826-8885-4fcd-92fc-2ff651a0b23e"]=u"Komagara, Jiki|||m|Bambara||Kɛɲɛlen, Kaaba, signe aussi Ji Komakara; Jigi Komakara, 1990"
# "Tarawele, Janginɛ",,,,,,"Animatɛri, Kɔkɛni (Sirakɔrɔla), 1990",9a7671d9-e6e2-4c86-99c2-abd6601d9ed7
dictauth[u"9a7671d9-e6e2-4c86-99c2-abd6601d9ed7"]=u"Tarawele, Janginɛ|||m|Bambara||Animatɛri, Kɔkɛni (Sirakɔrɔla), 1990"
# "Kulubali, Moriba",,m,,,Bambara,2016,8980ff6b-0155-40bc-88e3-0d5f2650e9d4
dictauth[u"8980ff6b-0155-40bc-88e3-0d5f2650e9d4"]=u"Kulubali, Moriba|||m|Bambara||2016"
# "Keyita, Burema",,m,,Bendugu,,Kucala Akademi,4dedc8fc-cc66-4982-b24b-851d31e7b315
dictauth[u"4dedc8fc-cc66-4982-b24b-851d31e7b315"]=u"Keyita, Burema|||m|Bambara|Bendugu|Kucala Akademi 2016"
# "Kulubali, Dɛnba",,,,,,2015/11 kibaru n°526,6ccb4659-2010-4a22-bff8-ef8a0786264d
dictauth[u"6ccb4659-2010-4a22-bff8-ef8a0786264d"]=u"Kulubali, Dɛnba|||m|Bambara||sports 2015 - 2016"
# "Cero, B",,,,,,"football, 2016",1f5a2623-ecc3-4dd6-81cf-ea6152562a3d
dictauth[u"1f5a2623-ecc3-4dd6-81cf-ea6152562a3d"]=u"Cero, B|||m|Bambara||football, 2016"
# "Tunkara, Solomani Bobo",,,,,,"2015/11 Kibaru n°526, 533 farikoloɲenajɛ 2016",cd5292c9-93cc-494f-abd0-0a834bb677a2
dictauth[u"cd5292c9-93cc-494f-abd0-0a834bb677a2"]=u"Tunkara, Solomani Bobo|||m|Bambara||2015/11 Kibaru n°526, 533 farikoloɲenajɛ 2016"
#"Sise, Daramani",,m,,,,"Nɔgɔlaso, commune de Sanzana, Kiɲan, Sikaso - 2016",3a8dcd18-7ff6-40d4-ad7f-67b2ee4b8537
dictauth[u"3a8dcd18-7ff6-40d4-ad7f-67b2ee4b8537"]=u"Sise, Daramani|||m|Bambara||Nɔgɔlaso, commune de Sanzana, Kiɲan, Sikaso - 2009, 2016"
#"Tarawele, Asani",,m,,,,"Kɔkuna, commune de Kapolondugu, Sikaso 2016",48347506-6757-4d20-b854-735f2c1e09cf
dictauth[u"48347506-6757-4d20-b854-735f2c1e09cf"]=u"Tarawele, Asani|||m|Bambara||Kɔkuna, commune de Kapolondugu, Sikaso 2009, 2016"
#"Nafo, Fatumata",,,,,,"2015/11 n°526, 2016 n°531 avril, 534 juil.",486d185e-79f1-492d-82e3-b48d12a2420a
dictauth[u"486d185e-79f1-492d-82e3-b48d12a2420a"]=u"Nafo, Fatumata|||f|Bambara||2015/11 n°526, 2016 n°531 avril, 534 juil."	
#"Tarawele, Alujan",,m,,,Bambara,"né environ 1955, habite Ɲɔna, 2016 ",258e2d7f-e4f4-4803-ba72-518f66f18f2d
dictauth[u"258e2d7f-e4f4-4803-ba72-518f66f18f2d"]=u"Tarawele, Alujan||1955|m|Bambara||né environ 1955, habite Ɲɔna, 2016"	
# "Fɔnba, Dirisa N°1",,m,,,Bambara,"Kula-Joyila (Doyila kafo / Joyila mara), balikukalan karamɔgɔ (Fonba) 1995",d381c752-e40c-4c6d-9cb1-60d48bc8697d
dictauth[u"d381c752-e40c-4c6d-9cb1-60d48bc8697d"]=u"Fɔnba, Dirisa N°1|||m|Bambara||Kula-Joyila (Doyila kafo / Joyila mara), balikukalan karamɔgɔ (Fonba) 1995"	
# "Jara, Dirisa Bakari",,m,,,,"Diyo-Buwatubugu - Kati, Balikukalankaramɔgɔ, 1995, 1996",266a0781-d80f-4f93-8885-fd28c4af344e
dictauth[u"266a0781-d80f-4f93-8885-fd28c4af344e"]=u"Jara, Dirisa Bakari|||m|Bambara||Diyo-Buwatubugu - Kati, Balikukalankaramɔgɔ, 1995, 1996"
# Kumarɛ, Siyaka",,m,,,,"Fiyɛna, region de Kulukɔrɔ, 1990",9d1ff4e3-f4a1-4bf4-8362-cdded032939a
dictauth[u"9d1ff4e3-f4a1-4bf4-8362-cdded032939a"]=u"Kumarɛ, Siyaka|||m|Bambara||habite Fiyɛna (Kulukɔrɔ animatɛri 1990, 1996"
# "Kulubali, Amidu",,m,,,Bambara,"(Kulibali) habite Bamakɔ, balikukalan karamɔgɔ, 1995, 1996",383c85d5-9d08-4d6f-b5e5-fd985a317d8e
dictauth[u"383c85d5-9d08-4d6f-b5e5-fd985a317d8e"]=u"Kulubali, Amidu|||m|Bambara||(Kulibali) habite Bamakɔ, balikukalan karamɔgɔ, 1995, 1996"	
# "Jara, Mamadu",,m,,,,"Npeseribugu, Masantola (Kɔlɔkani), 1993, 1996",dc81e9f8-e04a-4675-b98c-3b33b4a818ea
dictauth[u"dc81e9f8-e04a-4675-b98c-3b33b4a818ea"]=u"Jara, Mamadu|||m|Bambara||Npeseribugu, Masantola (Kɔlɔkani), 1993, 1996"
# "Tarawele, Fanta",,f,,,Bambara,"habite Lengekɔtɔ, Kita (""Fula KIBARU"") - habite Maganjanbugu (Kita) 1989",41f86179-2da0-4890-91f9-4bf687788f4b
dictauth[u"41f86179-2da0-4890-91f9-4bf687788f4b"]=u"Tarawele, Fanta|||f|Bambara||habite Tunkarala Lengekɔtɔ (Legekoto), Kita (ko Fula KIBARU) - habite Maganjanbugu (Kita) 1989, 1997"		
# "Fɔnba, Amari",,m,,,Bambara,habite Kɔnsɔfɔn (Kulukɔrɔ) animatɛri 1996,f8cab50f-1bba-4b2f-aa0e-5a4d8df8f8fe
dictauth[u"f8cab50f-1bba-4b2f-aa0e-5a4d8df8f8fe"]=u"Fɔnba, Amari|||m|Bambara|native|habite Kɔnsɔfɔn (Kulukɔrɔ) animatɛri 1996, 1998"			
# "Kulubali, Basiru","Kulibali, Basiru",m,,,Bambara,"habitant de Joro Bamana - Segu, 1996",b3d03481-2736-4a65-ae48-446097e97c31
dictauth[u"b3d03481-2736-4a65-ae48-446097e97c31"]=u"Kulubali, Basiru|||m|Bambara||habitant de Joro Bamana - Segu, 1996, 1997, 1998"	
#"So, Shɛki Madu",,m,,,,"habite Ntinɛnga (Fana) balikukalan karamɔgɔ, 1995, 1998",33bc2e39-335a-4d95-8014-2e15b52e2357
dictauth[u"33bc2e39-335a-4d95-8014-2e15b52e2357"]=u"So, Shɛki Madu|||m|||habite Ntinɛnga (Fana) balikukalan karamɔgɔ, 1995, 1998"
# "Dolo, Amagire Ogobara",,,,,,2016,70301778-a09a-4593-ade3-7586f9588d30
dictauth[u"70301778-a09a-4593-ade3-7586f9588d30"]=u"Dolo, Amagire Ogobara||||||habite Ségou? 1998, 2016"
# "Mayiga, Fatumata",,f,,Bamako,Bambara,"journaliste à l'Essor, 1998, 2009, 2016",79a71680-67a1-44be-a693-f88bb3b5dc49
dictauth[u"79a71680-67a1-44be-a693-f88bb3b5dc49"]=u"Mayiga, Fatumata|||f|Bambara|Bamako|journaliste à l'Essor, 1998, 2009, 2016"
# "Jara, Fatumata",,f,,,Bambara,"habite Diyo-Buwatubugu - Kati, Animatirisi, 1996, 1998",178d8b60-2a1f-4de8-a7dc-5a0642fccd5b
dictauth[u"178d8b60-2a1f-4de8-a7dc-5a0642fccd5b"]=u"Jara, Fatumata|||f|Bambara||habite Diyo-Buwatubugu - Kati, Animatirisi, 1996, 1998"
# "Sangare, Adama Dawuda",,m,,,Bambara,habite Jumanzana Kɔcɛbugu (Fana) 1996,65b9b944-f1a7-4973-a52d-0c30a1ce87c1
dictauth[u"65b9b944-f1a7-4973-a52d-0c30a1ce87c1"]=u"Sangare, Adama Dawuda|||m|Bambara||habite Jumanzana Kɔcɛbugu (Fana) 1996, 1998"
# "Tarawele, Sungalo",,,,,,"habitant de Nɛmabugu / Ɲamabugu, Kolokani Balikukalan Karamɔgɔ Faradala-Guni-Kulikɔrɔ 1996",db99321c-0d53-4eb3-aa86-7f14d99de21f
dictauth[u"db99321c-0d53-4eb3-aa86-7f14d99de21f"]=u"Tarawele, Sungalo|||m|Bambara||habitant de Nɛmabugu / Ɲamabugu, Kolokani Balikukalan Karamɔgɔ Faradala-Guni/Ɲuni-(Kulikɔrɔ) 1996, 1998"
# "Tarawele, Gonba",,m,,,,"Dɔribuguni, Kolokani - 1997",47d27d6a-73fd-4cfb-bb7e-acce3dd707d9
dictauth[u"47d27d6a-73fd-4cfb-bb7e-acce3dd707d9"]=u"Tarawele, Gonba|Gɔnba||m|Bambara||Dɔribugunin, Kolokani - 1997, 1998"	
# "Watara, Suleyimani",,m,,,,"1996, 1997, C.I.? 1998",4086d40b-cb3a-4b04-9688-b9e4f4a3e8c5
dictauth[u"4086d40b-cb3a-4b04-9688-b9e4f4a3e8c5"]=u"Watara, Suleyimani|||m|||1996, 1997, C.I./Burukina? 1998"
# "Jara, Shaka",,m,,,,"Kɔrɔkɔrɔ-Dɔgo - Buguni, Balikukalan karamɔgɔ, 1998",c9e74689-bedd-4331-ab78-31846fc977c1
dictauth[u"c9e74689-bedd-4331-ab78-31846fc977c1"]=u"Jara, Shaka|||m|Bambara||habite Kɔrɔkɔrɔ-Dɔgo - Buguni, Balikukalan karamɔgɔ, 1998"
# "Diko, Mohamɛdi",,m,,,Bambara,"kib 315,317,319 1998",f9d5c2b6-6699-44ea-9a2f-1bca0aeaaa28
dictauth[u"f9d5c2b6-6699-44ea-9a2f-1bca0aeaaa28"]=u"Diko, Mohamɛdi|||m|Bambara||kib 315,317,319 1998"
#"Sise, Amadu M",,m,,,Bambara,Tumutu? 2016,f38c8a39-329b-4916-8c7f-5b889e87523b
dictauth[u"f38c8a39-329b-4916-8c7f-5b889e87523b"]=u"Sise, Amadu M|||m|Bambara||Tumutu? 2016"
# "Saya, Mulayi",,m,,,,Tumutu? 2016 kib534 535,cae507d3-3764-4f88-8250-f10f65df1732
dictauth[u"cae507d3-3764-4f88-8250-f10f65df1732"]=u"Saya, Mulayi|||m|||Tumutu? 2016 kib534 535"
# #"Alimudu, L",,,,,,"2016, n°531 avril",ce4fa3c9-af99-4928-b6ab-40d91c2c1018
dictauth[u"ce4fa3c9-af99-4928-b6ab-40d91c2c1018"]=u"Alimudu, L||||Bambara||2016, n°531 535"	
## "Sidibe, M.",,,,,Bambara,2016 (kibaru n°533 passeports),d382c276-cb63-42f3-9ec8-4cc7f6e79a76
dictauth[u"d382c276-cb63-42f3-9ec8-4cc7f6e79a76"]=u"Sidibe, M.||||Bambara||2016 (kibaru n°533 passeports, 535 permis)"
#"Bagayoko, Mamadu",,m,,,Bambara,"habite Kangaba, 1987 - kibarulasela",6e83ebc8-10bf-42f7-a6f0-3ecebd79984f
dictauth[u"6e83ebc8-10bf-42f7-a6f0-3ecebd79984f"]=u"Bagayoko, Mamadu|||m|Bambara||habite Kangaba, 1987 - kibarulasela - 2016 n°535"
# "Jabi, Laji M.",,m,,,,2016,4c8159cd-a0e7-410c-85a9-ba505666abe1
dictauth[u"4c8159cd-a0e7-410c-85a9-ba505666abe1"]=u"Jabi, Laji M.|||m|Bambara||2016, kib 534, 535"
# "Jalo, Sɛki Umaru",,m,,,,,54c07225-8068-423c-bb92-ae94fea49f42
dictauth[u"54c07225-8068-423c-bb92-ae94fea49f42"]=u"Jalo, Sɛki Umaru|Shɛki||m|Bambara||1998 kib320"
#"Samake, Nanse",,,,,,"kib 316, 1998",2030b450-3a6b-49ed-83b9-5799e1c97c15
dictauth[u"2030b450-3a6b-49ed-83b9-5799e1c97c15"]=u"Samake, Nanse|Ɲanse|||Bambara||kib 316,321 (1998)"
# "Leplaideur, Marie-Agnès",,f,,,,"Kib 317, 1998",2c0367fd-a997-4609-8806-000921e35d18
dictauth[u"2c0367fd-a997-4609-8806-000921e35d18"]=u"Leplaideur, Marie-Agnès|Lepɛlidɛri||f|||Kib 317,321 (1998)"
#"Ibbo Daddy, Abdoulaye ",Ibo Dadi Abudulayi,m,,,,"habite Nizɛri, kib 317,318 1998 ",29066936-48f5-4f69-829a-dfd0c8b8f4bf
dictauth[u"29066936-48f5-4f69-829a-dfd0c8b8f4bf"]=u"Ibbo Daddy, Abdoulaye|||m|||habite Nizɛri, kib 317,318,321 (1998)"
#"Jara, Mami",,m,,,,"Npiyɛninna, commune de Cɛmɛna, Bila, Segu 1996",0d4c13df-70b8-4683-a1f3-0c248b9d4cc7
dictauth[u"0d4c13df-70b8-4683-a1f3-0c248b9d4cc7"]=u"Jara, Mami|||m|Bambara||habite Npiyɛninna/Nbiyɛnina, commune de Cɛmɛna, Bila, Segu 1996, kib 323 1998"
# "Sidibe, Isaka",,m,,,,"Sabalibugu, Bamako, balikukalan karamɔgɔ",c40b5a51-94ee-48fb-a425-1a7ac752f2f8
dictauth[u"c40b5a51-94ee-48fb-a425-1a7ac752f2f8"]=u"Sidibe, Isaka|||m|Bambara||hebite Sabalibugu, Bamako, balikukalan karamɔgɔ- kalandenjolen kib323 1998"
#"Williams, Denise",,f,,,,"kib 314,318 1998",fae54512-72ee-45fe-8b00-4dbabb6bc6d4
dictauth[u"fae54512-72ee-45fe-8b00-4dbabb6bc6d4"]=u"Williams, Denise|||f|||kib 314,318,323 (1998)"
#"Tarawele, Siyaka",,m,,,,"Diyo-Bamabugu, Kati, kib324, 1998",9885109d-3fdf-4cf2-8307-1ad88cd1d8ed
dictauth[u"9885109d-3fdf-4cf2-8307-1ad88cd1d8ed"]=u"Tarawele, Siyaka|||m|Bambara||habite Diyo-Bamabugu, Kati, kib324, 1998"
#"Tarawele, Basumana",,m,,,,"Dɛnɛnba, commune de Ɲamina, Kulukɔrɔ",e79dde7c-1739-47fa-b50d-b2addce57ae2
dictauth[u"e79dde7c-1739-47fa-b50d-b2addce57ae2"]=u"Tarawele, Basumana|||m|Bambara||habite Dɛnɛnba, commune de Ɲamina, Kulukɔrɔ, kib324 1998"
#"N'Guessan, Raphaül",,m,,,,"C.I., Kib 315,317, 1998 (Raphaul, Raphaël?)",fa8b3c83-db30-4fdf-951e-b7cb058956b7
dictauth[u"fa8b3c83-db30-4fdf-951e-b7cb058956b7"]=u"N'Guessan, Raphaül|||m|||C.I., Kib 315,317,324 (1998) (Raphaul, Raphaël?)"
# "Sise, Mahamadu B.",,m,,,Bambara,Gawo? 2016,f394dedd-9131-4b1c-8456-06b06aae98a7
dictauth[u"f394dedd-9131-4b1c-8456-06b06aae98a7"]=u"Sise, Mahamadu B.|||m|Bambara||kib331 1999, Gawo? 2016"
#"Kɔnɛ, Bakari",,m,,,,"Tiɲana, Kɔlɔnjɛba",cb16231a-ac28-474d-b82d-075d4e254e76
dictauth[u"cb16231a-ac28-474d-b82d-075d4e254e76"]=u"Kɔnɛ, Bakari|||m|Bambara||habite Tiɲana, Kɔlɔnjɛba - kib 1998"
#"Kulubali, Mamadu",,m,,,Bambara,"kibarudilala, Bamakɔ",b21d1a28-e4a2-4f91-b1d8-33cff629718e
dictauth[u"b21d1a28-e4a2-4f91-b1d8-33cff629718e"]=u"Kulubali, Mamadu|||m|Bambara||kibarudilala, Bamakɔ - 1998"
#"Ɲani, Umaru",,m,,,Bambara,"habite Batama, Kayi ? kib324,331 1999",e3f6c7e4-2f76-459c-a4e9-c4702b6bd970
dictauth[u"e3f6c7e4-2f76-459c-a4e9-c4702b6bd970"]=u"Ɲani, Umaru|||m|Bambara||habite Batama, Kayi ? kib324,331 1999"
#"Jara, Kɔnba",,f,,,,"Musokuntigi, Sanankɔ - Nɛgɛla - Kati",fc81ac64-408e-449b-85cd-8cd4ae2fab25
dictauth[u"fc81ac64-408e-449b-85cd-8cd4ae2fab25"]=u"Jara, Kɔnba|||f|Bambara||Musokuntigi, Sanankɔ - Nɛgɛla - Kati - kib334, 1999"
#"Jara, Bakari Bilen",,m,,,Bambara,"habite Diyo-Bamabugu (Kati Zafu), balikukalan karamɔgɔ 1990",a0398a7a-251b-434d-be17-91e0ee1e233e
dictauth[u"a0398a7a-251b-434d-be17-91e0ee1e233e"]=u"Jara, Bakari Bilen|||m|Bambara||habite Diyo-Bamabugu (Kati Zafu), balikukalan karamɔgɔ 1990, kib334 1999"
#"Keyita, Maman",,f,,,,"Sitantumu, Kita",33a9e28c-37f8-47ac-ae88-b8b67b4da526
dictauth[u"33a9e28c-37f8-47ac-ae88-b8b67b4da526"]=u"Keyita, Maman|Manan||f|||Sitantumu, Kita - kib334 1999"
#"Dadjo, Crépin Hilaire",,m,,,,"habite le Burukina, kib 318, 1998",4aeabf7f-35f1-4745-bf54-02a345b6f6f1
dictauth[u"4aeabf7f-35f1-4745-bf54-02a345b6f6f1"]=u"Dadjo, Crépin Hilaire|||m|||habite le Burukina, kib 318, 1998, kib334 1999"
#"Darabo, Gawusu",,m,,,Bambara,"kib 314, 1998",127f5500-c5db-4f87-8a33-d073d8430f02
dictauth[u"127f5500-c5db-4f87-8a33-d073d8430f02"]=u"Darabo, Gawusu|||m|Bambara||kib 314 1998, kib334 1999"
# "Lamu, A.",,,,,,habite Senegal? kib331 1999,ebb0c747-5e5e-41e8-baa0-c780bab4598e
dictauth[u"ebb0c747-5e5e-41e8-baa0-c780bab4598e"]=u"Lamu, Alayi||||||habite Senegal? kib331-334 1999"
#"Jabate, Fuseni",Fuseyini,m,,,Bambara,"habite Sikaso? 1998, 2016",76c495a4-7706-4487-92c1-27be5fb4e943
dictauth[u"76c495a4-7706-4487-92c1-27be5fb4e943"]=u"Jabate, Fuseni|Fuseyini||m|Bambara||habite Sikaso? 1998, 1999 2016"
# "Kaba, Mamadi",,m,,,Bambara,"kib 315, 317,319 1998",45856259-2685-4d35-b650-c8db3d5ae2d8
dictauth[u"45856259-2685-4d35-b650-c8db3d5ae2d8"]=u"Kaba, Mamadi|Mamadu||m|Bambara||kib 315, 317,319 1998-kib366 2000"
#"Dunbuya, Yusufu",,m,,,," (aussi Dunbiya!) kib 317, 1998, kib454 2009 ",da8f0ed0-5365-4dd1-93f5-3f6afc0b7643
dictauth[u"da8f0ed0-5365-4dd1-93f5-3f6afc0b7643"]=u"Dunbuya, Yusufu|Yusu||m|Bambara||(aussi Dunbiya!) kib317 1998, kib366 2000, kib454 2009 "
# "Jara, Ibarahima Baba",,m,,,Bambara,"Surukutu K18 / Ɲantansonin, commune de Dogofiri Jabali, Ɲɔnɔn -animatɛri- kib366 2000",3b24a2db-71cb-43db-bf14-59ad4a4dcde3
dictauth[u"3b24a2db-71cb-43db-bf14-59ad4a4dcde3"]=u"Jara, Ibarahima Baba|||m|Bambara||Surukutu K18 / Ɲantansonin, commune de Dogofiri Jabali, Ɲɔnɔn -animatɛri- kib366 2000"
# "Kulubali, Musa Numukɛba",,m,,,Bambara,Murugula,b2e1c18f-0369-49b0-8f51-610d492dd521
dictauth[u"b2e1c18f-0369-49b0-8f51-610d492dd521"]=u"Kulubali, Musa Numukɛba|||m|Bambara||habite Murugula puis Diwo-Kɔdiwari 2002 kib366"
# "Boli, Pate",,,,,,habite Danbana - kib324 1999,612ef758-857a-40f9-a2e3-89bff9f739cb
dictauth[u"612ef758-857a-40f9-a2e3-89bff9f739cb"]=u"Boli, Pate||||||habite Danbana/Danbanna (Kita) - kib324 1999,378 2003"
# "Jalo, Sumayila",,m,,,,"Ŋɔnɔnɔmɔn, Njila, Ɲɛna",2f7e2bf4-7d5e-43df-93a5-057d50e3c5d4
dictauth[u"2f7e2bf4-7d5e-43df-93a5-057d50e3c5d4"]=u"Jalo, Sumayila|||m|Bambara||habite Ŋɔnɔnɔmɔn, Njila, Ɲɛna (Sikaso)- peresidan AWE - kib378 2003"
# "Kamara, Usumani",,m,,,Bambara,habite Bamabugu (Kati) - kalanden jolen 1990,5bb7d097-e967-4495-ab75-b71000624bcf
dictauth[u"5bb7d097-e967-4495-ab75-b71000624bcf"]=u"Kamara, Usumani|Gigimasa||m|Bambara||habite Bamabugu (Kati) - kalanden jolen 1990 - ɲɛmɔgɔ arajo Suruku, Diyo Gari (Kati) kib 378 2003"
# "Kulubali, Mɔrikɛ",,m,,,,"Fulabugu, Kɔlɔkani mara",6c5e9b5e-6873-4141-9e5a-c829f4591aad
dictauth[u"6c5e9b5e-6873-4141-9e5a-c829f4591aad"]=u"Kulubali, Mɔrikɛ|||m|Bambara||Fulabugu/Filabugu, (Kɔlɔkani) kib378 2003"
# "Jara, Soyibajan",,m,,,,"Jɔdumadala, Wɔlɔjɛdo Nɔnkɔ, Kɔlɔkani 2016 / Kɔdumala-Nɔnsɔnbugu 1998?, kib324 1999",b225860b-9538-4504-aeca-b39750f1a1ea
dictauth[u"b225860b-9538-4504-aeca-b39750f1a1ea"]=u"Jara, Soyibajan|||m|Bambara||Jɔdumadala, Wɔlɔjɛdo Nɔnkɔ, Kɔlɔkani 2016 / Kɔdumala-Nɔnsɔnbugu 1998?, kib324 1999 kib378 2003"
#"Jara, Usumani",,m,,,,,1a596b70-23c8-45d8-b31e-517d6e44d41e
dictauth[u"1a596b70-23c8-45d8-b31e-517d6e44d41e"]=u"Jara, Usumani|||m|Bambara||habite Sikasokura km 22 la, Dɔgɔfiri komini na, kib417 2006"
# "Jara, Adama",,m,,,Bambara,Kibaru baarakɛla ? - 2016 kib534,d32c72aa-3711-46d4-a1e0-ff045f797f3e
dictauth[u"d32c72aa-3711-46d4-a1e0-ff045f797f3e"]=u"Jara, Adama|||m|Bambara||Kibaru baarakɛla ? - 2016 kib534,536"
# "Berete, Berema",Burama,m,,,,"Diyu, Kajolo mara, 2016",0c034f30-6345-4772-b9f9-981c751287e2
dictauth[u"0c034f30-6345-4772-b9f9-981c751287e2"]=u"Berete, Berema|Burama||m|Bambara|native|Diyu, Kajolo mara, kib 535,536 2016"
#"Jara, Alu Jɛnfa",,m,,,Bambara,"habite Soninkɛɲi, Kati mara la   2016",26910e4a-764c-427f-84de-721a50740b5a
dictauth[u"26910e4a-764c-427f-84de-721a50740b5a"]=u"Jara, Alu Jɛnfa|||m|Bambara||habite Soninkɛɲi, Kati mara la - kib534,536  2016"
# "Fɔnba, Basiru",,m,,,,"Jɛle, commune de Bugukura, Joyila",53ef22ce-a19a-459c-a814-84ce03706231
dictauth[u"53ef22ce-a19a-459c-a814-84ce03706231"]=u"Fɔnba, Basiru|||m|Bambara||habite Jɛle, commune de Bugukura, Joyila/Dɔyila - kib528 2016"
# "Tulema, Hamidu",,m,,,Bambara,"habite Timisa, Arajo Sigida Yiriwaso - 2016",b5864f72-0d3d-4428-a2a3-13cca538f6e1
dictauth[u"b5864f72-0d3d-4428-a2a3-13cca538f6e1"]=u"Tulema, Hamidu|||m|Bambara||habite Timisa, Arajo Sigida Yiriwaso - 2016"
# "Jire, Dusu",,,,,,2016,d2f0a2c2-d202-47a9-877e-ec52cfc694b7
dictauth[u"d2f0a2c2-d202-47a9-877e-ec52cfc694b7"]=u"Jire, Dusu||||Bambara||kib528 2016"
#"Ture, Berema",,m,,,Bambara,2016 n°531 avril,51d73647-d28e-45cb-96b1-52c86a597f72
dictauth[u"51d73647-d28e-45cb-96b1-52c86a597f72"]=u"Ture, Berema|||m|Bambara||2016 kib528,531"
# "Tarawele, Mariyamu A.",,f,,,Bambara,2009 kib454,dd14cfd3-bfc5-4b41-9827-07330f78032a
dictauth[u"dd14cfd3-bfc5-4b41-9827-07330f78032a"]=u"Tarawele, Mariyamu A.|||f|Bambara||AMAP? 2009 kib454, 2016 kib528"
# "Kulubali, Bayi",,m,,,Bambara,"kib452 2009, 2016",cb438776-e9e5-45eb-b1ae-dabe13fd783d
dictauth[u"cb438776-e9e5-45eb-b1ae-dabe13fd783d"]=u"Kulubali, Bayi|||m|Bambara||kib452 2009, 2016"
#"Ɲare, Meydi",Medi,,,,,2009 kib452,kib454,e6be7efc-34a4-4c76-a77a-d2ddcc10e56d
dictauth[u"e6be7efc-34a4-4c76-a77a-d2ddcc10e56d"]=u"Ɲare, Meydi|Medi||m|Bambara||2009 kib452,kib454"
#"Keyita, Madiba",,m,,,Bambara,"2008 kib434, 2009 kib454",66b29102-5b8c-4edd-81ec-888d2307faa2
dictauth[u"66b29102-5b8c-4edd-81ec-888d2307faa2"]=u"Keyita, Madiba|||m|Bambara||2008 kib434, 2009 kib453,454"
#"Danbɛlɛ, Bakari",,m,,,,"Sikaso Wayɛrɛma 2, kib417 2006",56f2b63c-53ac-405a-aa7f-e0ee4341f809
dictauth[u"56f2b63c-53ac-405a-aa7f-e0ee4341f809"]=u"Danbɛlɛ, Bakari|||m|Bambara||Sikaso Wayɛrɛma 2, kib417 2006, kib452,453 2009"	
#"Fɔnba, Daramani",,m,,,Bambara,village de Ncuwacɛn,ea0a1dc6-84e8-4b7c-9a6d-20749c228103
dictauth[u"ea0a1dc6-84e8-4b7c-9a6d-20749c228103"]=u"Fɔnba, Daramani|||m|Bambara||village de Ncuwacɛn - Jekabaara n°19, 1987"
# "Dukure, Mamadu",,m,,,Bambara,Jekabaara 044 1989,c697fbc1-053d-476f-a523-ea55eaf2f986
dictauth[u"c697fbc1-053d-476f-a523-ea55eaf2f986"]=u"Dukure, Mamadu|||m|Bambara||Jekabaara 044 1989 047"
# "Dunbiya, Musa",,m,,,,Kati,d12fe50b-c078-4b20-81c8-ac69948d134f
dictauth[u"d12fe50b-c078-4b20-81c8-ac69948d134f"]=u"Dunbiya, Musa|||m|Bambara||Jɛkabaara 047"
# "Jara, Bakayi",,,,,,"habite Kolodugukura, Ɲɔnɔ, 1995 - Jɛkabaara 047",34eb45e6-9e92-40c3-bf3a-90c7eb231fb6
dictauth[u"34eb45e6-9e92-40c3-bf3a-90c7eb231fb6"]=u"Jara, Bakayi|||m|Bambara||habite Kolodugukura, Ɲɔnɔ, 1995 - Jɛkabaara 054, 1990"
# "Kulubali, Usumani",,m,,,Bambara,habite Seriwala,c8c9fe81-d9e1-4d6b-a328-39b0616c19cd
dictauth[u"c8c9fe81-d9e1-4d6b-a328-39b0616c19cd"]=u"Kulubali, Usumani|||m|Bambara||habite Seriwala - Jɛkabaara 054, 1990"
# "Bari, Abdulayi","Barry, Abdoulaye",m,,,Bambara,"membre de Bɛnba kan dungew, professeur d'anglais, parlait aussi le français et le fulfuldé, Directeur de DNAFLA, décédé le 22.09.1991",02fd28a2-e96c-48d3-844f-2e35b3157bfa
dictauth[u"02fd28a2-e96c-48d3-844f-2e35b3157bfa"]=u"Bari, Abdulayi|Barry, Abdoulaye||m|Bambara||membre de Bɛnba kan dungew, professeur d'anglais, parlait aussi le français et le fulfuldé, Directeur de DNAFLA, Jɛkabaara Sɛbɛnbaakulu kuntigi, décédé le 22.09.1991"
#"Gindo, Usmani",,m,,,,"MAKOCI kalankow ɲɛmɔgɔ dankan, Jɛkabaara 053 1990 MAKOCI fɛɛrɛkalan bolofara kuntigi Jɛkabaara 056 1990",f96014e9-6a24-4735-9ffb-c9cdda74fe65
dictauth[u"f96014e9-6a24-4735-9ffb-c9cdda74fe65"]=u"Gindo, Usmani|||m|Bambara||MAKOCI kalankow ɲɛmɔgɔ dankan, Jɛkabaara 053 1990 MAKOCI fɛɛrɛkalan bolofara kuntigi Jɛkabaara 056-57 1990"
#"Jakite, Siyaka",,m,,,Bambara,"habite Boyi (Kɔlɔnjɛba) - Jɛkabaara009 1986, 21 1987",285fddae-a8f3-4d7d-b9b2-96e446ed57b2
dictauth[u"285fddae-a8f3-4d7d-b9b2-96e446ed57b2"]=u"Jakite, Siyaka|||m|Bambara||habite Boyi (Kɔlɔnjɛba) - Jɛkabaara009 1986, 21 1987, 57 1990"
# "Sise, Seku",,m,,,Bambara,"Ofisi cikɛkalanso Ɲɔnɔn - Jekabaara 054 1990",5cad8db8-f718-4d77-9b00-6b98c1ba02e3
dictauth[u"5cad8db8-f718-4d77-9b00-6b98c1ba02e3"]=u"Sise, Seku|||m|Bambara||Ofisi cikɛkalanso Ɲɔnɔn - Jekabaara 054-57 1990"
#"Kanute, Mamadu Lamini",,m,,,Bambara,membre de Bɛnba kan dungew,690f4a15-86cc-4381-9e81-f75dd9d6616d
dictauth[u"690f4a15-86cc-4381-9e81-f75dd9d6616d"]=u"Kanute, Mamadu Lamini|||m|Bambara||membre de Bɛnba kan dungew- Jɛkabaara 57 1990"
#"Kulubali, Danyɛli",,m,,,Bambara,Jekabaara022 1987 Kucala - dugukolonɔn kunbɛn baarada - Jɛkabaara 056 1990,7faf5c2d-3602-4af6-b4f5-d1b8a11e0ed6
dictauth[u"7faf5c2d-3602-4af6-b4f5-d1b8a11e0ed6"]=u"Kulubali, Danyɛli|||m|Bambara||Jekabaara022 1987 Kucala - dugukolonɔn kunbɛn baarada - Jɛkabaara 056-57 1990"
#"Kulubali, Fode",,m,,,Bambara,"dɔ̀kɔtɔrɔ, kɛnɛyako kunnafonilasela, Bamakɔ, 1987",e4ff0b2e-48d8-4b8e-82b4-f097469f2a1a
dictauth[u"e4ff0b2e-48d8-4b8e-82b4-f097469f2a1a"]=u"Kulubali, Fode|||m|Bambara||dɔ̀kɔtɔrɔ, kɛnɛyako kunnafonilasela, Bamakɔ, 1987-Jɛkabaara 063 1991"
#"Samakɛ, Sidi Lamini",,m,,,Bambara,"Jɛkabaara 054, 1990",e4cac73a-9de6-497a-b977-96a700bedf01
dictauth[u"e4cac73a-9de6-497a-b977-96a700bedf01"]=u"Samakɛ, Sidi Lamini|||m|Bambara||Jɛkabaara 054 1990- 063 1991"
#"Tarawele, Isa",,m,,,,"Kogonin K6, commune de Jabali, Ɲɔnɔn",dc8c09d1-c257-4939-a2c2-c98c494800fd
dictauth[u"dc8c09d1-c257-4939-a2c2-c98c494800fd"]=u"Tarawele, Isa|||m|Bambara||Kogonin K6, commune de Jabali, Ɲɔnɔn- Kogonin Kuruma sɛkitɛri kɔnɔ. U.P2, Ɲɔnɔ- Jɛkabaara 065-1991"
# "Kulubali, Shaka",,m,,,Bambara,village de Jijeni / Manjèla (1987),325e54ef-30c7-4710-8f60-3bed25d90df9
dictauth[u"325e54ef-30c7-4710-8f60-3bed25d90df9"]=u"Kulubali, Shaka|||m|Bambara||village de Jijeni / Manjèla (1987)"
# "Dunbiya, Siyaka",Shaka/ʃaka/Saka,m,1965,Wasolon,Bambara,"né au village de Fulagunibula (Buguni), travaille à Jamana",d969a0c7-4102-4d7a-8783-c242365f365d
dictauth[u"d969a0c7-4102-4d7a-8783-c242365f365d"]=u"Dunbiya, Siyaka|Shaka/ʃaka/Saka|1965|m|Bambara|Wasolon|né au village de Fulagunibula (Buguni), travaille à Jamana"
# "Jalo, Abdulayi",,m,,,Bambara,ka bɔ Molodo - Ofisi Nizɛri / Jɛkabaara 061 1991,c3fea918-60e2-4ad4-ac13-42f6713b1603
dictauth[u"c3fea918-60e2-4ad4-ac13-42f6713b1603"]=u"Jalo, Abdulayi|||m|Bambara||ka bɔ Molodo - Ofisi Nizɛri / Jɛkabaara 061 1991, 073 1992"
# "Sangare, Bakari",,m,,,Bambara,Ntomikɔrɔbugu Bamako - Jɛkabaara 070 1991,1cacb7c3-5fc9-4020-bffc-4f2f60bd30ef
dictauth[u"1cacb7c3-5fc9-4020-bffc-4f2f60bd30ef"]=u"Sangare, Bakari|||m|Bambara||Ntomikɔrɔbugu Bamako - Jɛkabaara 070 1991, 073 1992"
# "Berete, Salifu",,,,,,Jɛkabaara 071 1991,d6dc8fc4-170c-435a-a44d-ea4f43e998f7
dictauth[u"d6dc8fc4-170c-435a-a44d-ea4f43e998f7"]=u"Berete, Salifu|||m|Bambara||Jɛkabaara 071 1991, 073 1992"
# "Kante, Sitan",,f,,,Bambara,"Safukuntigi musoman - Operasiyɔn Ɔtiwale la Welesebugu, 1990",5ed900fb-aa35-44ea-b2dd-01c114a61b12
dictauth[u"5ed900fb-aa35-44ea-b2dd-01c114a61b12"]=u"Kante, Sitan|||f|Bambara||Safukuntigi musoman - Operasiyɔn Ɔtiwale la Welesebugu, 1990"
#"Tarawele, Kasun",,m,,,Bambara,habite Bugunina Bananba,ab30d433-20bb-4152-8885-d61c958d2517
dictauth[u"ab30d433-20bb-4152-8885-d61c958d2517"]=u"Tarawele, Kasun|||m|Bambara||habite Bugunina Bananba - Jɛkabaara 075 1992"
#"Tarawele, Duguna",,m,,,,"Samanbugu, Kati, Kulikɔrɔ - Animatɛrɛ, Zafu kuntigi",44a419e9-b797-4e3a-bbbc-cde095e486ba
dictauth[u"44a419e9-b797-4e3a-bbbc-cde095e486ba"]=u"Tarawele, Duguna|||m|Bambara||Samanbugu, Kati, Kulikɔrɔ - Animatɛrɛ, Zafu kuntigi"
#"Tarawele, Mamadu",,m,,,Bambara,"Cikɛlakɔliden kɔnperese ka bɔ M5, Kɛrɛwane, Molodo Sɛkitɛri la- Jɛkabaara072 1991, 075 1992",1f54a676-f904-4080-af0d-5b995fbf3fea
dictauth[u"1f54a676-f904-4080-af0d-5b995fbf3fea"]=u"Tarawele, Mamadu|||m|Bambara||Cikɛlakɔliden kɔnperese ka bɔ M5, Kɛrɛwane, Molodo Sɛkitɛri la- Jɛkabaara072 1991, 075 1992"
#"Samakɛ, Zan",,m,,,Bambara,"Lakɔlikaramɔgɔ «LPK» la, Bamakɔ - Jɛkabaara074 1992",5851ab7f-f669-487c-9ba8-d03577181a1d
dictauth[u"5851ab7f-f669-487c-9ba8-d03577181a1d"]=u"Samakɛ, Zan|Samake||m|Bambara||Lakɔlikaramɔgɔ «LPK» la, Bamakɔ - Jɛkabaara074 1992, 077"
#"Dunbiya, Fabu",,,,,Bambara,habite Karan,b97e7e65-dfef-4b44-b7c8-d3e0d2a7d9ac
dictauth[u"b97e7e65-dfef-4b44-b7c8-d3e0d2a7d9ac"]=u"Dunbiya, Fabu|Dunbuya|||Bambara||habite Karan, Kaaba sɛrɛkili kɔnɔ"
#"Kulubali, Siratiki",,m,,,Bambara,"habite Sirakɔrɔla, Kulikɔrɔ Animatɛri",a664260d-90d0-4271-a109-87051896c49a
dictauth[u"a664260d-90d0-4271-a109-87051896c49a"]=u"Kulubali, Siratiki|Kulubali, Siratigi||m|Bambara|m|habite Zabantukɔrɔ, Sirakɔrɔla, Kulikɔrɔ/Ɔtiwale mara - Animatɛri - Jɛkabaara 078 1992"
#"Buware, Ŋolo A.",,m,,,Bambara,karamɔgɔ Bamakɔ - Jɛkabaara075 078 1992,ad68f742-fa39-4cc8-bda6-db1f4a663e9f
dictauth[u"ad68f742-fa39-4cc8-bda6-db1f4a663e9f"]=u"Buware, Ŋolo A.|||m|Bambara||karamɔgɔ Bamakɔ - Jɛkabaara075 078 1992"
#"Sidibe, Yusufu Jime",,,,,Bambara,,c26122ec-de4d-49a9-81b8-ce5899ae0474
dictauth[u"c26122ec-de4d-49a9-81b8-ce5899ae0474"]=u"Sidibe, Yusufu Jime|||m|Bambara||Kucala MAKOCI kalanfa filanan - Jɛkabaara082 1992"
#"Sakɔ, Zan",,m,,,Bambara,"Zafukunti, Kangaba OHV kɔnɔ - Jɛkabaara076 1992",06083e70-ee05-42af-ba8e-410a3ed82a76
dictauth[u"06083e70-ee05-42af-ba8e-410a3ed82a76"]=u"Sakɔ, Zan|||m|Bambara||Zafukunti, Kangaba OHV kɔnɔ - Jɛkabaara076 082 1992"
#"Konate, Hamidu",,m,,,,Directeur de la maison d'édition Jamana,c7fa01a9-6428-4d30-bfed-426ea69618ba
dictauth[u"c7fa01a9-6428-4d30-bfed-426ea69618ba"]=u"Konate, Hamidu|||m|Bambara||Directeur de la maison d'édition Jamana"
#"Magiraga, Mahamadu",,m,,,,"balikukalan ɲɛmɔgɔ ""ODIK"", Ɲɔrɔ",71c91448-4c9e-4a70-80e6-36b4b3f8a7e3
dictauth[u"71c91448-4c9e-4a70-80e6-36b4b3f8a7e3"]=u"Magiraga, Mahamadu|||m|Bambara||balikukalan ɲɛmɔgɔ ODIK, Ɲɔrɔ"
#"Kalanbiri, Alɛkisi",,m,,,,"koperatifu Jamana baarada mɔgɔ",ccf1c399-9fa6-4ebc-8887-f99759915bab
dictauth[u"ccf1c399-9fa6-4ebc-8887-f99759915bab"]=u"Kalanbiri, Alɛkisi|||m|Bambara||koperatifu Jamana baarada mɔgɔ - Jɛkbaara 084 -1992"
#"Jalo, Daɲɛli",,,,,,Jamana baarada mɔgɔ dɔ,ee15c979-1e11-46ac-87c1-04794c3039f4
dictauth[u"ee15c979-1e11-46ac-87c1-04794c3039f4"]=u"Jalo, Daɲɛli|||m|Bambara||Jamana baarada mɔgɔ dɔ - Jɛkabaara 087 1993"
#"Jabate, Fuseni",Fuseyini,m,,,Bambara,"habite Sikaso? 1998, 2016",76c495a4-7706-4487-92c1-27be5fb4e94387"
dictauth[u"76c495a4-7706-4487-92c1-27be5fb4e943"]=u"Jabate, Fuseni|Fuseyini||m|Bambara||habite Sikaso? 1998, 2016 - kib539 2016"
#"Tarawele, C. M.",,,,,,"2015/11, 2016 - kib539 2016",c9775956-e767-411b-ac4a-aacc504aa314
dictauth[u"c9775956-e767-411b-ac4a-aacc504aa314"]=u"Tarawele, C. M.||||Bambara||2015/11, 2016 - kib539 2016"
#"Kulubali, Umaru",,m,,,Bambara,"Balikukalan kafo kuntigi, Joyila - Jɛkabaara094",f59418f3-ea40-42cb-a742-c128bcc2e4f6
dictauth[u"f59418f3-ea40-42cb-a742-c128bcc2e4f6"]=u"Kulubali, Umaru|||m|Bambara||Balikukalan kafo kuntigi, Joyila - Jɛkabaara094"
#"Ture, Madu",,,,,,"Zafukuntigi, Sirakɔrɔjɛ Marakakungo mara la Fana - Jɛkabaara091, 1993 ",eca51900-8a0c-410b-a48b-8ce752447d1a
dictauth[u"eca51900-8a0c-410b-a48b-8ce752447d1a"]=u"Ture, Madu|||m|Bambara||Zafukuntigi, Sirakɔrɔjɛ Marakakungo mara la Fana - Jɛkabaara091, 1993 "
#"Denba, Bankɔ",,,,,,"Jɛkabaara094, 1993",d2e216a8-bb57-48f9-90cc-be217d8872ef
dictauth[u"d2e216a8-bb57-48f9-90cc-be217d8872ef"]=u"Denba, Bankɔ||||Bambara||Jɛkabaara094, 1993"
#"Sidi, Tuya",,,,,Bambara,"Jɛkabaara095,99 1993",cb1c9586-e35f-48dd-9957-da1884595907
dictauth[u"cb1c9586-e35f-48dd-9957-da1884595907"]=u"Sidi, Tuya||||Bambara||Jɛkabaara095,99 1993"
#"Sako, Dotege",,m,,,Bambara,Gafe feerela kalan bolofarala Fana MAKOCI ɲɛmɔgɔsola - Jɛkabaara075 1992,b213ebbb-fcaa-48ec-9fb3-0a5cb50351da
dictauth[u"b213ebbb-fcaa-48ec-9fb3-0a5cb50351da"]=u"Sako, Dotege|||m|Bambara||Gafe feerela kalan bolofarala Fana MAKOCI ɲɛmɔgɔsola - Jɛkabaara075 1992, 103 1994"
#"Kɔnɛ, Sisela Mayimuna",,f,,,Bambara, MAKOCI formatrices - Jɛkabaara 088 1993,aa1a73cb-f9a9-497b-82a5-c33feee93bf5
dictauth[u"aa1a73cb-f9a9-497b-82a5-c33feee93bf5"]=u"Kɔnɛ, Sisela Mayimuna|||f|Bambara||MAKOCI formatrices - Jɛkabaara 088 1993, 104 1994"
#"Trawele, Umu Amar",,f,,,,"Jɛkabaara093, 1993",14e31872-e90f-48ae-b008-ff4e325fccee
dictauth[u"14e31872-e90f-48ae-b008-ff4e325fccee"]=u"Trawele, Umu Amar|||f|Bambara||Jɛkabaara093, 1993;J106 09-1994"
# "Jara, Zan Dosayi",,m,,,,MAKOCI Sɛnɛko setigi Ɲɔgɔnye sɛbɛnnikɛla - Jɛkabaara 083 1992 & 108 11-1994,8bd6f254-0f03-4822-aef7-3792ac0b07e4
dictauth[u"8bd6f254-0f03-4822-aef7-3792ac0b07e4"]=u"Jara, Zan Dosayi|||m|Bambara||MAKOCI Sɛnɛko setigi Ɲɔgɔnye sɛbɛnnikɛla - Jɛkabaara 083 1992 & 108 11-1994"
#"Dunbiya, Mamadu",,m,,,Bambara,1990 Ncɔbugu AV sekeretɛri Fana MAKOCI mara -  Jɛkabaara110 12-1994,1538e51f-7535-40c0-9bd4-e1bdafdfbec0
dictauth[u"1538e51f-7535-40c0-9bd4-e1bdafdfbec0"]=u"Dunbiya, Mamadu|||m|Bambara||1990 Ncɔbugu AV sekeretɛri Fana MAKOCI mara -  Jɛkabaara110 12-1994"
#"Jalo, Solomani",,m,,,Bambara,Jɛkabaara ka ciden - Jɛkabaara106 09-1994 n108 11-1994,be54d4e2-6f68-4e62-8802-95385ba6564b
dictauth[u"be54d4e2-6f68-4e62-8802-95385ba6564b"]=u"Jalo, Solomani|||m|Bambara||Jɛkabaara ka ciden - Jɛkabaara106 09-1994 n108 11-1994"
# "Samake, Dawuda Jinɛmusa",,m,,,Bambara,"animatɛri ɲɛmɔgɔ Seliban Jitumu Welesebugu mara - Jɛkabaara094, 1993",2a32f60e-253f-49bf-ad87-02a261f6ed52
dictauth[u"2a32f60e-253f-49bf-ad87-02a261f6ed52"]=u"Samake, Dawuda Jinɛmusa|||m|Bambara||animatɛri ɲɛmɔgɔ Seliban Jitumu Welesebugu mara - Jɛkabaara094, 1993"
#"Sise, Mamadu Yusufu",,m,,,,MAKOCI ciɲɛkuntigi dankan - Jɛkabaara120 1995,1662fdb6-5b2b-4e20-b09e-222bbc4115e6
dictauth[u"1662fdb6-5b2b-4e20-b09e-222bbc4115e6"]=u"Sise, Mamadu Yusufu|||m|Bambara||MAKOCI ciɲɛkuntigi dankan - Jɛkabaara120 1995-123 1996"
#"Mayiga, Mahamani A.",,m,,,,Jɛkabaara kanubaga ka bɔ Bamako,24d50126-b321-4288-9bca-c670c9142825
dictauth[u"24d50126-b321-4288-9bca-c670c9142825"]=u"Mayiga, Mahamani A.|||m|Bambara||Jɛkabaara kanubaga ka bɔ Bamako-jekabaara 125 1996"
#"Jara, Siyaka",,m,,,Bambara,Kucala - Jɛkabaara073 1992,0eb7d85a-bbf5-496a-9126-c7fd261621a9
dictauth[u"0eb7d85a-bbf5-496a-9126-c7fd261621a9"]=u"Jara, Siyaka|||m|Bambara||Kucala - Jɛkabaara073 1992, 129 1996"
# "Keyita, Mamadi",,m,,,,n ̊2 animatɛri don ka bɔ Karan Bilindɔ Narena - Jɛkabaara 129 1996,cef226df-486e-4d6d-a3cb-118053c436f6
dictauth[u"cef226df-486e-4d6d-a3cb-118053c436f6"]=u"Keyita, Mamadi|||m|Bambara||n ̊2 animatɛri don ka bɔ Karan Bilindɔ Narena - Jɛkabaara 129,131 1996"			
#"Senu, Idirisa",,m,,,,"Jɛkabaara 131, 132 1996",cd0ca0ae-0426-4ebc-bfd8-2390c291c98c
dictauth[u"cd0ca0ae-0426-4ebc-bfd8-2390c291c98c"]=u"Senu, Idirisa|||m|Bambara||Jɛkabaara 131, 132 1996"
#"Dawo, Dawuda Mace",,m,,,Bambara,CMDT kalanko ni fɛɛrɛko bolofara ɲɛmaa - Jekabaara 132 1996 - 136 1997,f0c85c3c-17d5-4af6-ab3e-28b8fd906fe4
dictauth[u"f0c85c3c-17d5-4af6-ab3e-28b8fd906fe4"]=u"Dawo, Dawuda Mace|||m|Bambara||CMDT kalanko ni fɛɛrɛko bolofara ɲɛmaa - Jekabaara 132 1996 - 136 1997"
#"Danbele, Yaya",,m,,Segu,Bambara,"habite Segu, balikukalan karamɔgɔ - 1987 - puis Barawul sɛrɛkɛli, Sanado mara - Bamanankan ɲinikɛla Marakala Segu: Jɛkabaara 137, 138 1997",fbfccca8-37b1-484c-a64d-9e2e81ad2832
dictauth[u"fbfccca8-37b1-484c-a64d-9e2e81ad2832"]=u"Danbele, Yaya|||m|Bambara||habite Segu, balikukalan karamɔgɔ - 1987 - puis Barawul sɛrɛkɛli, Sanado mara - Bamanankan ɲinikɛla Marakala Segu: Jɛkabaara 137, 138 1997"
#"Kulubali, Bubakari",,m,,,Bambara,"Jɛkabaara baarakɛla dɔ Bamakɔ - Jɛkabaara112 02-1995 - Jɛkabaara 114, 116, 117, 118, 119,120 1995- 122, 123, 132 1996, 138 140 1997",4c6bc903-6586-44b8-91fb-6a4764a5f20e
dictauth[u"4c6bc903-6586-44b8-91fb-6a4764a5f20e"]=u"Kulubali, Bubakari|||m|Bambara||Jɛkabaara baarakɛla dɔ Bamakɔ - Jɛkabaara112 02-1995 - Jɛkabaara 114, 116, 117, 118, 119,120 1995- 122, 123, 132 1996, 138 140 1997"
#"Kulubali, Fanta",Kulibali,f,,,Bambara,Membre de rédaction de Jèkabaara - Jɛkabaara 142 1997,6018c6bd-cad4-4354-bcb9-6327a9d28f37
dictauth[u"6018c6bd-cad4-4354-bcb9-6327a9d28f37"]=u"Kulubali, Fanta|Kulibali Kulibaly Kulubaly||f|Bambara||Membre de rédaction de Jèkabaara - Jɛkabaara 142 1997"
#"Sise, Mahamadu Lareya","Lariye, Lariya",m,,,Bambara,"ka bɔ Bamakɔ CMDT ɲɛmɔgɔsoba la. kalanfa. Jɛkabaara 136, 144, 145 1997",f3b91ae3-022a-4d2e-91f1-c18ada0000bc
dictauth[u"f3b91ae3-022a-4d2e-91f1-c18ada0000bc"]=u"Sise, Mahamadu Lareya|Lariye, Lariya||m|Bambara||ka bɔ Bamakɔ CMDT ɲɛmɔgɔsoba la. kalanfa. Jɛkabaara 136, 144, 145 1997"
#"Kɔnɛ, Musa",,m,,,Bambara,"Duguwɔlɔ, Kafoyiriwatɔn kuntigi, Bila - Jɛkabaara 148-150 1998 ",856e0687-0fb1-4469-8a46-0fa11fa9031d
dictauth[u"856e0687-0fb1-4469-8a46-0fa11fa9031d"]=u"Kɔnɛ, Musa|||m|Bambara||Duguwɔlɔ, Kafoyiriwatɔn kuntigi, Bila - Jɛkabaara 148-150 1998"
#"Fane, Mamadu",,m,,,Bambara,Bamakɔ - Jɛkabaara 156-158 1998,4168de2f-8c3a-49bf-afd1-219d1ed04a1b
dictauth[u"4168de2f-8c3a-49bf-afd1-219d1ed04a1b"]=u"Fane, Mamadu|||m|Bambara||Bamakɔ - Jɛkabaara 156-158 1998"
#"Jalo, Yusufu","Jalo, Yusuf",m,,,,Editeur en chef de Jèkabaara,04e64a0f-70c8-47e7-b887-09f1c67ce911
dictauth[u"04e64a0f-70c8-47e7-b887-09f1c67ce911"]=u"Jalo, Yusufu|||m|Bambara||Editeur en chef de Jèkabaara"
#"Fane, Yusufu F.",,m,,,,membre de la rédaction de Jèkabaara,458db881-6de5-4039-b450-9914355c0130
dictauth[u"458db881-6de5-4039-b450-9914355c0130"]=u"Fane, Yusufu F.|||m|Bambara|native|membre de la rédaction de Jèkabaara"
#"Tarawele, Usumani",,m,,,Bambara,Fana CMDT Kalanko Bolofara - Jɛkabaara 166 1999,a1396798-4b28-48a1-b16d-c9679207cb7a
dictauth[u"a1396798-4b28-48a1-b16d-c9679207cb7a"]=u"Tarawele, Usumani|||m|Bambara||Fana CMDT Kalanko Bolofara - Jɛkabaara 166 1999"
# "Sukuna, Mamayi",,,,,Bambara,Fana CMDT Kalanko Bolofara - Jɛkabaara 166 1999,5ca24c05-96f6-4332-906e-8bd1f9125015
dictauth[u"5ca24c05-96f6-4332-906e-8bd1f9125015"]=u"Sukuna, Mamayi||||Bambara||Fana CMDT Kalanko Bolofara - Jɛkabaara 166 1999"
#"Jakite, Kalifa",,m,,,Bambara,"kib537 2016, kib 541-544 2017",d28a755e-2674-4155-868e-97252d1c1b93
dictauth[u"d28a755e-2674-4155-868e-97252d1c1b93"]=u"Jakite, Kalifa|||m|Bambara||kib537 2016, kib 541-544 2017"
# "Boli, Musa",,m,,,Bambara,sports - Jɛkabaara 234-235 2005,6c349568-0bc0-44ff-92aa-6c02e99a64ef
dictauth[u"6c349568-0bc0-44ff-92aa-6c02e99a64ef"]=u"Boli, Musa|||m|Bambara||sports - Jɛkabaara 234-235 2005"
# "Balo, Modɛsi",,m,,,Bambara,"habite Kucala, 2016 - Kibaru 542-545-546 2017",db8fbfc7-30be-4c52-a536-300dacfb2943
dictauth[u"db8fbfc7-30be-4c52-a536-300dacfb2943"]=u"Balo, Modɛsi|||m|Bambara||habite Kucala, 2016 - Kibaru 542-545-546 2017"
#"Sidibe, Masa",,,,,Bambara,kibaru 542-546-547 2017,2ba135bb-49f6-4f69-bf72-d35cb7195c45
dictauth[u"2ba135bb-49f6-4f69-bf72-d35cb7195c45"]=u"Sidibe, Masa||||Bambara||kibaru 542-546-547 2017"
# "Sisoko, Mariyamumadi",,f,,,Bambara,"- Kibaru 095, 98-102 1980, ",a5c6837b-e811-400b-8df4-1bd5accbaf81
dictauth[u"a5c6837b-e811-400b-8df4-1bd5accbaf81"]=u"Sisoko, Mariyamumadi|||f|Bambara||- Kibaru 095, 98-102 1980"
# "Jara, Mamadu Nyama",,m,,,Bambara,"kibarudilala, Bamakɔ - kib090 1979, kib102 1980",618af8da-1f81-414c-b049-a6a38c9d6c80
dictauth[u"618af8da-1f81-414c-b049-a6a38c9d6c80"]=u"Jara, Mamadu Nyama|||m|Bambara||kibarudilala, Bamakɔ - kib090 1979, kib102 1980"
# "Danbele, Ibɛrɛhima",,m,,,Bambara,"habite Jatawali - kib 051 1976, kib102-103 1980",a337a319-000c-43d3-91cf-f3364c45194a
dictauth[u"a337a319-000c-43d3-91cf-f3364c45194a"]=u"Danbele, Ibɛrɛhima|||m|Bambara||habite Jatawali - kib 051 1976, kib102-103 1980"
# "Jakite, Yɔrɔ Mɛnkɔrɔ",,,,,Bambara,"habite Buguni Faraba - Kibaru 095, 98 1980 Kib107 1981",62918880-44b0-416b-a3d4-41f9e3261560
dictauth[u"62918880-44b0-416b-a3d4-41f9e3261560"]=u"Jakite, Yɔrɔ Mɛnkɔrɔ||||Bambara||habite Buguni Faraba - Kibaru 095, 98 1980 Kib107 1981"
#"Keyita, Gabukɔrɔ",,m,,Bananba,Bambara,"Village de Soso, alphabetiseur - kib102 1980 - kib 133 1983",84a8d118-b713-41a4-9ed5-16a51f4aba6f
dictauth[u"84a8d118-b713-41a4-9ed5-16a51f4aba6f"]=u"Keyita, Gabukɔrɔ|||m|Bambara||Village de Soso, alphabetiseur - kib102 1980 - kib 133 1983"
# "Kanɛ, Mari",,m,,,Bambara,habite Bugukɔrɔ - kib 132-134-135 1983,d43907f8-d08b-4474-8bb3-1d6a55b15f1a
dictauth[u"d43907f8-d08b-4474-8bb3-1d6a55b15f1a"]=u"Kanɛ, Mari|||m|Bambara||habite Bugukɔrɔ - kib 132-134-135 1983"
# "Sise, Amara",,m,,,Bambara,"habite Sabalibugu Bamakɔ, lakɔlikaramɔgɔ (Mamadu Konate lakɔliso) - Kibaru 114 1981, 120 1982 - Jɛkabaara 149, 1998 ",d1c5691b-f597-43fc-8812-de0973007697
dictauth[u"d1c5691b-f597-43fc-8812-de0973007697"]=u"Sise, Amara|||m|Bambara||habite Sabalibugu Bamakɔ, lakɔlikaramɔgɔ (Mamadu Konate lakɔliso) - Kibaru 114 1981, 120 1982 - Jɛkabaara 149, 1998"
# "Jalo, Haji",,m,,Sikaso,Bambara,"habite Yanfolila, Sikaso (OPAMU) - Kib108-114 1981-  kib122 1982",48ed0991-742d-40ae-918f-89b6a872e0a4
dictauth[u"48ed0991-742d-40ae-918f-89b6a872e0a4"]=u"Jalo, Haji|||m|Bambara|Sikaso|habite Yanfolila, Sikaso (OPAMU) - Kib108-114 1981-  kib122 1982"
# "Tarawele, Bafin",,m,,,Bambara,"habite Mɔnban - Tuguni kafo, Kulukɔrɔ - kibaru 112 1981 - 135-136 1983",0577018c-d74d-4f68-81f9-218279f2514e
dictauth[u"0577018c-d74d-4f68-81f9-218279f2514e"]=u"Tarawele, Bafin|||m|Bambara||habite Mɔnban - Tuguni kafo, Kulukɔrɔ - kibaru 112 1981 - 135-136 1983"
#"Danbɛlɛ, Banuhun",,m,,,Bambara,"habite Dɔkɔlɔ-Bamana, Yangaso  - Jekabaara n°1, 1986 - kib 132-140 1983",bede413a-a43f-4a5d-823c-cb208a12c96e
dictauth[u"bede413a-a43f-4a5d-823c-cb208a12c96e"]=u"Danbɛlɛ, Banuhun|||M|Bambara||habite Dɔkɔlɔ-Bamana, Yangaso  - Jekabaara n°1, 1986 - kib 132-140 1983"	
#"Kulubali, Kamatigi",,m,,Bananba,Bambara,"habite Sobugu (Sɔbugu), Bananba - animatɛrɛ - kib092 1979 - kib 132 1983 - kib182 1987",db7cdd2a-d0bf-4008-885a-e97338a91b83
dictauth[u"db7cdd2a-d0bf-4008-885a-e97338a91b83"]=u"Kulubali, Kamatigi|||m|Bambara||habite Sobugu (Sɔbugu), Bananba - animatɛrɛ - kib092 1979 - kib 132 1983 - kib182 1987"					
# "Sogoba, Shaka",,m,,,Bambara,(ʃaka - Siyaka) ka bɔ Kuruma - kura / Jɛkabaara 057 058 1990 - kib 267 1994,8c54b573-5ba9-4558-a828-354afef8ee5e
dictauth[u"8c54b573-5ba9-4558-a828-354afef8ee5e"]=u"Sogoba, Shaka|||m|Bambara||(ʃaka - Siyaka) ka bɔ Kuruma - kura / Jɛkabaara 057 058 1990 - kib 267 1994"
# "Jara, Mamadu",,m,,,,"Npeseribugu, Masantola (Kɔlɔkani), 1993, kib270-272 1994, 1996",dc81e9f8-e04a-4675-b98c-3b33b4a818ea
dictauth[u"dc81e9f8-e04a-4675-b98c-3b33b4a818ea"]=u"Jara, Mamadu|||m|Bambara||Npeseribugu, Masantola (Kɔlɔkani), 1993, kib270-272 1994, 1996"
# "Kanɛ, Musa",,m,,,Bambara,"habite Kɛnɛnkun, Bugukɔrɔ (Kulikɔrɔ), balikukalan karamɔgɔ, kib91 1979 - 1990 - kib269-272 1994",9f6f459c-99c5-45c9-b946-9487921c3193
dictauth[u"9f6f459c-99c5-45c9-b946-9487921c3193"]=u"Kanɛ, Musa Sayibu|||m|Bambara||habite Kɛnɛnkun, Bugukɔrɔ (Kulikɔrɔ), balikukalan karamɔgɔ, kib91 1979 - 1990 - kib269-272 1994"
# "Jara, Dirisa Bakari",,m,,,Bambara,"Diyo-Buwatubugu - Kati, Balikukalankaramɔgɔ, kib275 1994 1995, 1996",266a0781-d80f-4f93-8885-fd28c4af344e
dictauth[u"266a0781-d80f-4f93-8885-fd28c4af344e"]=u"Jara, Dirisa Bakari|||m|Bambara||Diyo-Buwatubugu - Kati, Balikukalankaramɔgɔ, kib275 1994 1995, 1996"
# "Danbele, Bakaribilen",Damele Bakari,m,,,Bambara,"habite Bɛlɛko Gegena, 1996 - Bɛlɛkɔ 1 «ZAERI» sekeretɛri don (Joyila mara la). kib275 1994 - kib276 1995",dda27c30-a372-4cdb-884b-2ac8667a1523
dictauth[u"dda27c30-a372-4cdb-884b-2ac8667a1523"]=u"Danbele, Bakaribilen|||m|Bambara||habite Bɛlɛko Gegena, 1996 - Bɛlɛkɔ 1 «ZAERI» sekeretɛri don (Joyila mara la). kib275 1994 - kib276 1995"
# "Badu, Zerɔmu Ajaku",Jerôme Adjakou Badou,m,,,,"habite le Bénin, kib276 1996, 1997, 1998",1eed21cc-1fee-477f-b51c-433c93f117b2
dictauth[u"1eed21cc-1fee-477f-b51c-433c93f117b2"]=u"Badu, Zerɔmu Ajaku|Jerôme Adjakou Badou||m|||habite le Bénin, kib276 1996, 1997, 1998"
# "Sangare, Bubakari",,m,,,Bambara,«Eko» bɔko 78 nan/Jɛkabaara  066 1991 - kib279-280 1995,6db84d53-f9ac-472a-9926-2deb1fdfe0ca
dictauth[u"6db84d53-f9ac-472a-9926-2deb1fdfe0ca"]=u"Sangare, Bubakari|||m|Bambara||«Eko» bɔko 78 nan/Jɛkabaara  066 1991 - kib279-280 1995"
# "Fɔnba, Zankɛ Ngolo",Ŋɔlɔ,m,,,Bambara,"habite Jumazana, Fana mara la - kib275 1994 kib280 1995",b4ee46bb-ec0f-417a-a5c5-397024592b62
dictauth[u"b4ee46bb-ec0f-417a-a5c5-397024592b62"]=u"Fɔnba, Zankɛ Ngolo|||m|Bambara||habite Jumazana, Fana mara la - kib275 1994 kib280 1995"
# "Samake, Fasun Idirisa",,m,,,Bambara,habite Mɔrɔjanbugu (Kati) balikukalandenjolen - kib282 1995 - 1996 ,9fec18a6-f4e7-43c0-b93e-fd6e43e90454
dictauth[u"9fec18a6-f4e7-43c0-b93e-fd6e43e90454"]=u"Samake, Fasun Idirisa|||m|Bambara||habite Mɔrɔjanbugu (Kati) balikukalandenjolen - kib282 1995 - 1996"
# "Sogoba, Bala",,m,,,Bambara,cikɛla ka bɔ Jɛda Bila kafo kɔnɔ  Segu mara la - kib277-279-282 1995,638507fe-69e0-40c2-ad36-8337730f927f
dictauth[u"638507fe-69e0-40c2-ad36-8337730f927f"]=u"Sogoba, Bala|||m|Bambara||cikɛla ka bɔ Jɛda Bila kafo kɔnɔ  Segu mara la - kib277-279-282 1995"

#modèle dictauth[u"uuid"]=u"Nom, Prénom|spelling|datebirth|sex|Bambara|native|comment"
#modèle dictauth[u"uuid"]=u"Nom, Prénom|spelling|datebirth|sex|language|native|comment"
#fileauth=open("C:\Documents and Settings\Jean-Jacques.Meric.PARLXP10059\My Documents\Bambara-INALCO\GIT\corbama\\authors.csv","r")
# two problems : variable file location + reading a csv file with headers


def addauthor(authcond,uuid) :
	global auuid,aname,aspelling,abirth,asex,anative,adialect,aaddon
	l=0
	m=re.findall(authcond,tout,re.U)
	if m!=None :
		l=len(m)
		adata=dictauth[uuid].split("|")	
	if l>=1 :
		print "  author : ",m
		if auuid==u"": 
			auuid=uuid
			aname=adata[0]
			aspelling=adata[1]
			abirth=adata[2]
			asex=adata[3]
			anative=adata[4]
			adialect=adata[5]
			aaddon=adata[6]
		else : 
			if uuid not in auuid : 
				auuid=auuid+"|"+uuid
				aname=aname+"|"+adata[0]
				aspelling=aspelling+"|"+adata[1]
				abirth=abirth+"|"+adata[2]
				asex=asex+"|"+adata[3]
				anative=anative+"|"+adata[4]
				adialect=adialect+"|"+adata[5]
				aaddon=aaddon+"|"+adata[6]


title=re.compile(ur'\<h\>(.*)\<\/h\>',re.U)
searchwords=re.compile(ur'([a-zɛɔɲŋA-ZƐƆƝŊ\-́̀̌̂]+)',re.U)
newalphabet=re.compile(ur"(ɛ|ɔ|ɲ|Ɛ|Ɔ|Ɲ)",re.U|re.MULTILINE)
oldalphabet=re.compile(ur"(è|ò|è|ò|È|Ò)",re.U|re.MULTILINE)

metasstub=u"""<html><head><meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="" name="corpus:sponsor" />
<meta content="MM/JJ/AAAA" name="corpus:adddate" />
<meta content="Kibaru" name="source:title" />
<meta content="XXXX" name="source:year" />
<meta content="XXX" name="source:number" />
<meta content="XX" name="source:pagetotal" />
<meta content="AMAP" name="source:editor" />
<meta content="Kibarudiso" name="source:publisher" />
<meta content="Bamako" name="source:address" />
<meta content="Périodiques" name="source:type" />
<meta content="  .  .    " name="source:date" />
<meta content="" name="source:misc" />
<meta content="" name="source:url" />
<meta content="Jean Jacques Meric" name="corpus:operator" />
<meta content="XXX" name="text:title" />
<meta content="XX.XX.XXXX" name="text:date" />
<meta content="XX" name="text:pages" />
<meta content="XXX" name="text:script" />
<meta content="XXX" name="text:genre" />
<meta content="XXX" name="text:theme" />
<meta content="" name="text:rubric" />
<meta content="" name="text:transcription" />
<meta content="" name="text:transldata" />
<meta content="" name="text:original_lang" />
<meta content="écrit" name="text:medium" />
<meta content="inconnu" name="text:translation" />
<meta content="XX" name="_auto:words" />
</head>
"""

bi=time.strftime("%m/%d/%Y")
metasstub=re.sub(r"\"(MM\/JJ\/AAAA)\" name\=\"corpus\:adddate\"","\""+bi+"\" name=\"corpus:adddate\"",metasstub)

nargv=len(sys.argv)
if nargv==2 : 
  sys.exit("entrer la date et le nombre de pages du numéro de Kibaru/Jekabaara: metakin.py 01.MM.AAAA N ")
else : 
	datenum= str(sys.argv[1])
	pagestotal= str(sys.argv[2])

aaaa=re.search(r"[0-9]*\.[0-9]*\.([0-9]*)",datenum).group(1)

metasstub=re.sub(r"\"(XXXX)\" name=\"source\:year\"","\""+aaaa+"\" name=\"source:year\"",metasstub)
metasstub=re.sub(r"\"(XX)\" name=\"source\:pagetotal\"","\""+pagestotal+"\" name=\"source:pagetotal\"",metasstub)
metasstub=re.sub(r"\"(XX.XX.XXXX)\" name=\"text\:date\"","\""+datenum+"\" name=\"text:date\"",metasstub)

# possibilité de récupérer ici le n° de Kibaru via os.dirname (?)
filenames=os.listdir(".")
filenames=sorted(filenames)
for filename in filenames:
	if ".txt" in filename :
		print  filename
		find_in_name=re.search(r"(kibaru|jekabaara)([0-9\-]*)\_",filename)
		periodique=find_in_name.group(1)
		if periodique=="jekabaara" :
			metasstub=re.sub('<meta content="Kibaru" name="source:title" />','<meta content="Jɛkabaara" name="source:title" />',metasstub)
			metasstub=re.sub('<meta content="AMAP" name="source:editor" />','<meta content="Jamana" name="source:editor" />',metasstub)
			metasstub=re.sub('<meta content="Kibarudiso" name="source:publisher" />','<meta content="ODIPAC / CMDT / ODIMO" name="source:publisher" />',metasstub)
		numero=find_in_name.group(2)
		numerosource=numero
		if "-" in numero :
			numeros=numero.split("-")
			numerosource=numeros[0]  # meta.py n'accepte pas les - dans les numéros, on en choisi un seul, le premier...
		page=re.search(r"[0-9\-]*\_([0-9]*)",filename).group(1)
		metas=metasstub
		metas=re.sub(r"\"(XXX)\" name=\"source\:number\"","\""+numerosource+"\" name=\"source:number\"",metas)
		metas=re.sub(r"\"(XX)\" name=\"text\:pages\"","\""+page+"\" name=\"text:pages\"",metas)
		
		fileIN = open(filename, "r")
		#tout=fileIN.readlines()
		line = fileIN.readline()
		tout=u""
		while line:
			tout=tout+line.decode("utf-8")
			line = fileIN.readline()
		fileIN.close()

		# is it "old"
		old=False
		if ".old.txt" in filename : old=True # no question asked, we trust it's old, and output file WILL be .old.html
		else:
			m=newalphabet.findall(tout)  # check if there are any of new alphabet (start here because sometime there are a few possible French è )
			if m!=None:
				l=len(m)
				if l==0 :
					m2=oldalphabet.findall(tout) # check if there are any of old alphabet (this is positive check !!!)
					if m2!=None :
						l2=len(m2)
						if l2==0 :
							print "new or old alphabet unidentifiable, assumed new <- please CHECK content"
						else: 
							old=True
							prevfilename=filename
							filename=re.sub(ur".txt",u".old.txt",filename)
							os.rename(prevfilename, filename)

		if old :   # replaced and by or, twas too restrictive maybe !
			metas=re.sub(r"\"(XXX)\" name=\"text\:script\"","\"Ancien orthographe malien\" name=\"text:script\"",metas)
			tout=re.sub(u"è",u"è",tout,0,re.U|re.MULTILINE)
			tout=re.sub(u"ò",u"ò",tout,0,re.U|re.MULTILINE)
			
		else :
			metas=re.sub(r"\"(XXX)\" name=\"text\:script\"","\"Nouvel orthographe malien\" name=\"text:script\"",metas)
		

		titl=title.search(tout).group(1)
		titl=re.sub(u"\"","&quot;",titl)
		# print "titl="+titl
		metas=re.sub(r"\"(XXX)\" name=\"text\:title\"","\""+titl+"\" name=\"text:title\"",metas)
		

		tout=re.sub(ur"\<",u"&lt;",tout,0,re.U|re.MULTILINE)  
		tout=re.sub(ur"\>",u"&gt;",tout,0,re.U|re.MULTILINE)
		
		#bis ?
		#tout=re.sub(ur"\<",u"&lt;",tout,re.U|re.MULTILINE)  
		#tout=re.sub(ur"\>",u"&gt;",tout,re.U|re.MULTILINE)

		touttxt=tout
		touttxt=re.sub(ur"&lt;c&gt;.*&lt;/c&gt;",u" ",touttxt,re.U|re.MULTILINE)  # enlever les séquences <c>...</c>
		touttxt=re.sub(ur"&lt;n&gt;.*&lt;/n&gt;",u" ",touttxt,re.U|re.MULTILINE)  # enlever les séquences <n>...</n>
		touttxt=re.sub(ur"&lt;h&gt;|&lt;/h&gt;",u" ",touttxt,re.U|re.MULTILINE)  # enlever les tags <h> ou </h>
		touttxt=re.sub(ur"&lt;ill&gt;|&lt;/ill&gt;",u" ",touttxt,re.U|re.MULTILINE)  # enlever les tags <ill> ou </ill>
		touttxt=re.sub(ur"&lt;ls&gt;|&lt;/ls&gt;",u" ",touttxt,re.U|re.MULTILINE)  # enlever les tags <ls> ou </ls>
		touttxt=re.sub(ur"&lt;br/&gt;",u" ",touttxt,re.U|re.MULTILINE)  # enlever les tags <br/>
			
		swords=searchwords.findall(touttxt)
		if swords :
			words=len(swords)
			word=str(words)
		
		# print word,"mots"
		metas=re.sub(r"\"(XX)\" name=\"_auto\:words\"","\""+word+"\" name=\"_auto:words\"",metas)

		# rubriques et thèmes
		# <meta content="XXX" name="text:genre" />
		genre=""
		if old :
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nsiirin|Nsiirin)",titl,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nin kèra cè dò ye|nin kèra cè fila ye|nin kèra cè saba ye|nin kèra muso dò ye|nin kèra muso ye|Nin kèra cè dò ye|Nin kèra cè fila ye|Nin kèra cè saba ye|Nin kèra muso dò ye|Nin kèra muso ye)",tout,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nin kèra muso dò ye|nin kèra muso fila ye|nin kèra muso saba ye)",tout,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nin kèra [^\s]* dò ye|nin kèra [^\s]* fila ye|nin kèra [^\s]* saba ye)",tout,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(suruku|nsonsanin|waraba|waraninkalan|warabilen|ntura|sama|kami|ntori)",tout,3)
			addgenre("Litt&#233;rature orale : Proverbes",ur"(nsana|Nsana)",titl,1)
			addgenre("Litt&#233;rature orale : &#201;pop&#233;es",ur"(maana|Maana)",titl,1)
			addgenre("Litt&#233;rature orale : Devinettes",ur"(Kuma kòròma|kuma kòròma|Ntèntèn|ntèntèn)",titl,1)
			addgenre("Belles-Lettres : Po&#233;sie moderne",ur"(Poyi|N ka kalimu|poyi|n ka kalimu)",titl,1)
			addgenre("Belles-Lettres : Po&#233;sie moderne",ur"(&lt;po&gt;)",tout,1)
			## trop dangereux (autres longue listes de noms) : addgenre("Belles-Lettres : Po&#233;sie moderne",ur"(&lt;br/&gt;)",tout,12)
		else :
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nsiirin|Nsiirin)",titl,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nin kɛra cɛ dɔ ye|nin kɛra cɛ fila ye|nin kɛra cɛ saba ye|nin kɛra muso dɔ ye|nin kɛra muso ye|Nin kɛra cɛ dɔ ye|Nin kɛra cɛ fila ye|Nin kɛra cɛ saba ye|Nin kɛra muso dɔ ye|Nin kɛra muso ye)",tout,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nin kɛra muso dɔ ye|nin kɛra muso fila ye|nin kɛra muso saba ye)",tout,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(nin kɛra [^\s]* dɔ ye|nin kɛra [^\s]* fila ye|nin kɛra [^\s]* saba ye)",tout,1)
			addgenre("Litt&#233;rature orale : Contes populaires",ur"(suruku|nsonsanin|waraba|waraninkalan|warabilen|bilisi)",tout,3)
			addgenre("Litt&#233;rature orale : Proverbes",ur"(nsana|Nsana|laadilikan)",titl,1)
			addgenre("Litt&#233;rature orale : &#201;pop&#233;es",ur"(maana|Maana)",titl,1)
			addgenre("Litt&#233;rature orale : Devinettes",ur"(Kuma kɔrɔma|Ntɛntɛn|kuma kɔrɔma|ntɛntɛn)",titl,1)
			addgenre("Litt&#233;rature orale : Devinettes",ur"(Kuma kɔrɔma|Ntɛntɛn|kuma kɔrɔma|ntɛntɛn)",tout,1)
			addgenre("Belles-Lettres : Po&#233;sie moderne",ur"(Poyi|N ka kalimu|poyi|n ka kalimu)",titl,1)
			addgenre("Belles-Lettres : Po&#233;sie moderne",ur"(&lt;po&gt;)",tout,1)
			## trop dangereux (autres longue listes de noms) : addgenre("Belles-Lettres : Po&#233;sie moderne",ur"(&lt;br/&gt;)",tout,12)
			
		if genre!="" :
			metas=re.sub(r"\"(XXX)\" name=\"text\:genre\"","\""+genre+"\" name=\"text:genre\"",metas)
			print "  "+genre
		else:
			if page=="01" :
				metas=re.sub(r"\"(XXX)\" name=\"text\:genre\"","\"Information : Editorial\" name=\"text:genre\"",metas)
			else :
				metas=re.sub(r"\"(XXX)\" name=\"text\:genre\"","\"Information : Nouvelles\" name=\"text:genre\"",metas)

		# <meta content="XXX" name="text:theme" />
		theme=""

		addtheme(old,"&#201;ducation",ur"(balikukalan|kalanso|kalanden|kalanbaliya|karamɔgɔ|lakɔli|Lakɔli|unesco|lɛkɔliden|lɛkɔlikaramɔgɔ)")
		addtheme(old,"Administration",ur"(ciyakɛda|mɛri|komini|minisiri|Minisiri|forobakɛsu|nisɔngɔ|lɛnpo|takisi sarali|takisiw sarali|gɔfɛrɛnɛri|gɔfɛrɛnora|gɔfɛrɛnɛrɛ| kɔnsɛyi|arɔndisiman|erezɔn|sɛriwusida|baarada)")
		addtheme(old,"Agriculture",ur"(fantɔrɔmansin|malokisɛ|maloforo|hɛkitari|sayijirinin|Sayijirinin|jirituru|jiriden|jiribulu|jiridili|sɛnɛkɛ|Sɛnɛkɛ|cikɛko|cikɛla|Cikɛla|bagan|mɔnni|nakɔ|sanji|bulukuli|shyɛnni|turuli|saribilennin|dabakurunin|danni|jiri turu|ɲɔforo|kɔɔri|kabaforo|malosɛnɛ|keninge|suman|jiginɛ|misi|shɛmara|syɛmara|sagagɛn|jɛgɛ|taari|kɔrɔshiyɛn|nɔgɔdon|Ofisidinizɛri|pɔmutɛri|tigasɛnɛ)")
		addtheme(old,"Arm&#233;e et Guerre",ur"(burudamɛkɛlɛ|binkanni|burudamɛ murutilenw|kɛlɛbansɛbɛn|sɔrɔdasi|marifatigi|binnkannikɛla|binkannikɛla|binnkanikɛla|Minusima|kojugubakɛla|dagayɔrɔ|basigibaliya|maramafɛn)")
		addtheme(old,"Chasse",ur"(donsokɛ|donsoya|kungo sogo)")
		addtheme(old,"Christianisme", ur"(kereciyɛn|Kereciyɛn|mɔnsɛɲɛri|Mɔnsɛɲɛri|tubabumori|egilizi|Mishɔn|mishɔn)")
		addtheme(old,"Communication",ur"(kunnafonidila|kibaru|amap|jɛkabaara|arajo|tele|jabaranin|ORTM|nɛgɛjurusira|SOTƐLIMA|KABAARU|kabaaru)")
		addtheme(old,"Economie et Finances",ur"(dewaliyasɔn|Dewaliyasɔnkɔlɔnsen|SUKALA|CMDT|KOMATƐKISI|SOTELMA|SEPAMA|OTER|OPAM|F.M.I|FARANSEFA|FARANSƐFA|FARANFARANSƐ|Faran Sefa|SEFAKO|forobakɛsu|foroba kɛsu|foroba wariko|dɔrɔmɛ|dugujukɔrɔfɛn|babili|izini|taji sɔngɔ|tajijago|tajifeere|sanbaga|nafolo|musaka|lɛnpo|wusuru|sefawari|warikodɛmɛ|sanubɔ|BNDA|banki|warimaraso|BDI)")
		addtheme(old,"Environnement",ur"(kungodaw yiriwali ni sigiyɔrɔw lakanali|Kɔlɔnsen|pɔnpu|pɔnpekɔlɔn|Pɔnpekɔlɔn|jikodɛsɛ|jikomako|sanjiba|tasuma don kungo|sigiyɔrɔ lakana|sigida lakana|sigidaw lakana|sanjiko|jakɔngɔ|sanji hakɛ|sanji mumɛ|sigida|lamini|sanya|ɲamanton)")
		addtheme(old,"G&#233;ographie",ur"(sigi cogo|sigicogo|SIGICOGO|sigi cogo|ye dugu ye a bɛ)")
		addtheme(old,"Histoire",ur"(tubabu-bilen|tubabubilen|Fɔlɔ-fɔlɔ|Fɔlɔfɔlɔ|tariki|TARIKI|sigi cogo|sigicogo|tariku|Tariku|jɔnfeere|Jɔnfeere|Eziputi|farawona|farawuna|lawale|Lawale|tubabutile|Samori|Bakarijan|Bakari Jan|Kanku Musa|Sunjata Keyita)")
		addtheme(old,"Islam", ur"(silamɛ|Silamɛ|hijitaa|silamɛ|makantaa|misiri|sunkalo|sunbagatɔ|morikɛ|kuranɛ|garibu)")
		addtheme(old,"Linguistique",ur"(wolokan|bamanankan|sinminkan|kanw sɛbɛnni|mabɛn|fasokan|mabɛnnidaɲɛ|kawaleyalan|kamankutulan|dɛmɛnan|kɔbila|sinsinnan|sɛbɛncogo|Mandenkan|kanbolofara|daɲɛgafe|siginiden|kumasen)")
		addtheme(old,"Loi",ur"(OMAFES|yɛrɛwolodenyasɛbɛn|sariya|Sariya|sariyasen|Sariyasen|ɲangilisariya|sariyatigi|kiiri|kiri|kiritigɛla|kaso)")
		addtheme(old,"Loisirs", ur"(cd kasɛti|«O.R.T.M» sigidoolo|gintan|filimu|FESPACO|Shɛki Umaru SISOKO|Sulɛyimani SISE|Etalɔn Yenɛnga|folisen|jeli|dɔnkilidala|tarikitigi|siniman|Siniman|Eliwisi Pɛrɛsili|Mayikɔli Jakison|Salifu Keyita|Umu Sangare|Ali Farika Ture)")
		addtheme(old,"M&#233;decine et sant&#233;",ur"(kɔnɔboli|dɔlɔmin|farigan|tɔgɔtɔgɔnin|O.M.S|kunfilatu|kunfilanitu|kunfilanintu|sida|kɛnɛya|bana|fura|dɔgɔtɔrɔ|dɔkɔtɔrɔ|ɲɛdimi|kɔnɔdimi|dusukundimi|boloci|sumaya|furakisɛ|pilili|fugula nafama|ɲɔnin|ɲɔnisan|muso kɔnɔma|bolokolo|senkolo|bolotuguda)")
		addtheme(old,"Philosophie", ur"(saya|limaniya|mɔnɛbɔ|miiri|faamuya)")
		addtheme(old,"Politique",ur"(fangaso|jɛkakuma kunbɛn|Amadu Tumani TURE|Musa Tarawele|Musa TARAWELE|UDPM|UNFM|politiki|pariti|sɛkisɔn|kalata|yɛrɛta|wote|peresidan|gɔfɛrɛnaman|bɛɛya|bɛɛjɛfanga|demokarasi|forobaya|depitew|mɛriw|yɛrɛmahɔrɔnya|Musa TARAWELE)")
		addtheme(old,"Soci&#233;t&#233;",ur"(dutigi|duden|polisi|kaso|fatɔ|Fatɔ|duguba|musocamanfuru|tungafɛtaala|Tungafɛtaala|yɛrɛwolodenya|binkanni|tungalataa|UNFM|dɔrɔgu|furujoona|furusa|furusiri|boloko|karadante|dennadon|tɔgɔladon|jɔyɔrɔ|musotɔn|jɛkulu|jɛkafɔ|jɛkabaara|jɛkakɛ|senenkunya|sinankunya|dɛsɛbagatɔ|baloko|kɔngɔ kunbɛnniko|musofuru|sigiɲɔgɔnya|denmisɛnw ka donba|denmisɛnw ka seliba|denmisɛnw tɔgɔladon|musow ka donba|musow ka seliba|musow tɔgɔladon|Musocamanfuru|musocamanfuru|furuko|denko|denladon|furu kɔnɔ|garibu|warikogɛlɛya|balokogɛlɛya|jɔnya)")
		addtheme(old,"Sport",ur"(kupu tanko|bi kelen don|kurunboli|Kurunboli|balontan|ntolatan|Ntolatan|ladegebaga|farikoloɲɛnajɛ|bidonna|ziɲɔri|kade|ɲɛfɛmɔgɔ|bololantola|basikɛti|kupu|kupudafiriki|Kupudafiriki|kupudimɔndi|Kupudimɔndi|KUPUDIMƆNDI|KUPU DI MALI|kupu di Mali|baarita|bolokuru|soboli|balɔntan|samatasɛgɛ|Samatasɛgɛ)")
		addtheme(old,"Technologie", ur"(mansin|ɔridinatɛri)")
		addtheme(old,"Transport",ur"(sira dilanni|siraba|sirantanya|Siraba|bolifɛnko|pɔn jɔra|mobilibolila|mobilitigi|kamyɔn|kamyon|Dugumabolifɛnkow|dugumabolifɛnkow|jikanta|awiyɔn|pankurun|Pankurun)")
		
		if theme!="" :
			metas=re.sub(r"\"(XXX)\" name=\"text\:theme\"","\""+theme+"\" name=\"text:theme\"",metas)
			print "  "+theme
		else :
			metas=re.sub(r"\"(XXX)\" name=\"text\:theme\"","\"\" name=\"text:theme\"",metas)
		
		
		authstub=u"""<meta content="XXX" name="author:name" />
		<meta content="XXX" name="author:spelling" />
		<meta content="XXX" name="author:birth_year" />
		<meta content="XXX" name="author:sex" />
		<meta content="XXX" name="author:native_lang" />
		<meta content="XXX" name="author:dialect" />
		<meta content="XXX" name="author:addon" />
		<meta content="XXX" name="author:uuid" />
		"""

		aname=u""
		aspelling=u""
		abirth=u""
		asex=u""
		anative=u""
		adialect=u""
		aaddon=u""
		auuid=u""

		authshort=u""
		fileauth=re.search(r"[0-9\-]*\_[0-9]*([a-z\_]*)\-",filename)
		if fileauth : authshort="_"+fileauth.group(1)+"_"
		# pas de elif : il peut y avoir plusieurs auteurs !!!
		# LECTURE :
		# si le premier nom est dans le nom de fichier, 
		# chercher la signature dans le fichier, càd l'un des noms entre (),
		# si elle y est, ajouter l'auteur trouvé (par son uuid).

		if "_abdoulaye_" in authshort or "_abudululayi_" in authshort : 
			addauthor(ur"(Ibbo Daddy Abdoulaye|Ibo Daddy Abdoulaye|Ibo Dadi Abudulayi|Ibɔ Dadi Abudulayi)",u"29066936-48f5-4f69-829a-dfd0c8b8f4bf")
		if "_alimuludu_" in authshort : addauthor(ur"(L. Alimudu|L. ALIMULUDU|Lugayi Alimuludu|Migayi Alimuludu)",u"ce4fa3c9-af99-4928-b6ab-40d91c2c1018")
		if "_badou_" in authshort : addauthor(ur"(Zerɔmu Ajaku Badou|Jerome Badou|Zerɔmu Badou|Jerome Adjakou Badou)",u"1eed21cc-1fee-477f-b51c-433c93f117b2")
		if "_badu_" in authshort : addauthor(ur"(Zerɔmu Ajaku Badu|Jerome Badu|Zerɔmu Badu|Jerome Adjaku Badu)",u"1eed21cc-1fee-477f-b51c-433c93f117b2")
		if "_bagayogo_" in authshort : addauthor(ur"(M. Bagayogo|M. BAGAYOGO|Mamadu Bagayogo|Mamadu BAGAYOGO)",u"6e83ebc8-10bf-42f7-a6f0-3ecebd79984f")
		if "_balo_" in authshort : 
			addauthor(ur"(faraban balo|Faraban Balo)",u"596d1365-a5b5-4aad-a3ec-937a2ec44035")
			addauthor(ur"(Modɛsi Balo|Modɛsi BALO)",u"db8fbfc7-30be-4c52-a536-300dacfb2943")
		if "_banba_" in authshort : addauthor(ur"(namori banba|Namori Banba)",u"c4c865cb-8ccd-4ff4-9761-7186683456ef")
		if "_banyumanke_" in authshort:
			addauthor(ur"(Baɲumankɛ|baɲumankɛ)",u"37fb14af-e1f9-4ba2-ba7c-5f67401f42fd")   # = TYS encore!!!
		if "_bari_" in authshort : addauthor(ur"(Abdulayi Bari|Abdulayi BARI|Abdoulaye Barry|Abdoulaye BARRY)",u"02fd28a2-e96c-48d3-844f-2e35b3157bfa")
		if "_berete_" in authshort or "_berte_" in authshort : 
			addauthor(ur"(nanpe berete|Nanpe Berete)",u"4627912e-d8e0-405b-a3d2-147cc73d8533")
			addauthor(ur"(Berema Berete|Burama Berete|Berema BERETE|Burama BERETE)",u"0c034f30-6345-4772-b9f9-981c751287e2")
			addauthor(ur"(Salifu Berete|Salifu BERETE|Salifu Bɛrte|Salif Bɛrte)",u"d6dc8fc4-170c-435a-a44d-ea4f43e998f7")
		if "_boli_" in authshort : 
			addauthor(ur"(Pate Boli|Pate BOLI)",u"612ef758-857a-40f9-a2e3-89bff9f739cb")
			addauthor(ur"(Musa Boli|Musa BOLI)",u"6c349568-0bc0-44ff-92aa-6c02e99a64ef")
		if "_buware_" in authshort : addauthor(ur"(Ŋolo A. Buware|Ŋolo Buware|Ɲolo A. Buware|Ɲolo Buware|ŋolo Buware|Ŋɔlɔ A. Buware|Ŋɔlɔ Buware|Ɲɔlɔ A. Buware|Ɲɔlɔ Buware|ŋɔlɔ Buware)",u"ad68f742-fa39-4cc8-bda6-db1f4a663e9f")
		if "_cero_" in authshort : addauthor(ur"(b. cero|B. Cero|B. Cɛro|B. CERO|B. CƐRO)",u"1f5a2623-ecc3-4dd6-81cf-ea6152562a3d")
		if "_dadjo_" in authshort : addauthor(ur"(Crépin Hilaire Dadjo|Crépin Hilaire DADJO)",u"4aeabf7f-35f1-4745-bf54-02a345b6f6f1")
		if "_damele_" in authshort : addauthor(ur"(Bakaribilen Danbele|Bakari Danbele|Bakari Damele|Bakaribilen Damele)",u"dda27c30-a372-4cdb-884b-2ac8667a1523")
		if "_danbele_" in authshort :
			addauthor(ur"(Mukutari DANBELE|Mukutari Danbele)",u"1f8ea9bb-43b3-4c4f-8e8d-7275175cfd05")
			addauthor(ur"(Bakari Danbɛlɛ|Bakari DANBƐLƐ)",u"56f2b63c-53ac-405a-aa7f-e0ee4341f809")
			addauthor(ur"(Yaya Danbele|Yaya DANBELE)",u"fbfccca8-37b1-484c-a64d-9e2e81ad2832")
			addauthor(ur"(ibɛrɛhima danbele|Ibɛrɛhima Danbele|Ibèrèhima Danbele)",u"a337a319-000c-43d3-91cf-f3364c45194a")
			addauthor(ur"(Banuhun Danbɛlɛ|Banuhun DANBƐLƐ)",u"bede413a-a43f-4a5d-823c-cb208a12c96e")
			addauthor(ur"(Bakaribilen Danbele|Bakari Danbele|Bakari DANBELE|Bakari Damele|Bakaribilen Damele)",u"dda27c30-a372-4cdb-884b-2ac8667a1523")

		if "_darabo_" in authshort : addauthor(ur"(Gawusu Darabo|Gawusu DARABO)",u"127f5500-c5db-4f87-8a33-d073d8430f02")
		if "_dawo_" in authshort : addauthor(ur"(Dawuda Mace Dawo|Dawuda M\.Dawo|Dawuda M\. Dawo|Dawudi Mace Dawo)",u"f0c85c3c-17d5-4af6-ab3e-28b8fd906fe4")
		if "_denba_" in authshort : addauthor(ur"(Bankɔ Denba|Bankɔ DENBA)",u"d2e216a8-bb57-48f9-90cc-be217d8872ef")
		if "_drabo_" in authshort : addauthor(ur"(Gawusu Drabo|Gawusu DRABO)",u"127f5500-c5db-4f87-8a33-d073d8430f02")
		if "_diko_" in authshort : addauthor(ur"(Mohamɛdi Diko|Mohamɛdi DIKO)",u"f9d5c2b6-6699-44ea-9a2f-1bca0aeaaa28")
		if "_dolo_" in authshort : addauthor(ur"(Amagire Ogobara Dolo|Amagire Ogobara DOLO|Amagire O. Dolo|Amagire O. DOLO|A. O. Dolo|A. O. DOLO|Amagirɛyi O. DOLO)",u"70301778-a09a-4593-ade3-7586f9588d30")
		if "_dukure_" in authshort :
			addauthor(ur"(badama dukure|Badama Dukure|Badama DUKURE|Dadama Dukure)",u"8929d366-cfb6-4da7-a02f-1edea162b6e5")
			addauthor(ur"(Mamadu Dukure|Mamadu DUKURE)",u"c697fbc1-053d-476f-a523-ea55eaf2f986")
		if "_dunbiya_" in authshort:
			addauthor(ur"(Amadu Tanba DUNBIYA|Amadu Tanba Dunbiya)",u"587fb4ba-1385-4a2c-ab47-d60ed68d321b")
			addauthor(ur"(Yusufu Dunbiya|Yusu Dunbiya|Yusufu DUNBIYA|Yusu DUNBIYA)",ur"da8f0ed0-5365-4dd1-93f5-3f6afc0b7643")
			addauthor(ur"(Musa Dunbiya|Musa DUNBIYA)",u"d12fe50b-c078-4b20-81c8-ac69948d134f")
			addauthor(ur"(Siyaka Dunbiya|Shaka Dunbiya|ʃaka Dunbiya|Saka Dunbiya|Siyaka DUNBIYA)",u"d969a0c7-4102-4d7a-8783-c242365f365d")
			addauthor(ur"(Fabu Dunbiya)",u"b97e7e65-dfef-4b44-b7c8-d3e0d2a7d9ac")
			addauthor(ur"(Mamadu Dunbiya)",u"1538e51f-7535-40c0-9bd4-e1bdafdfbec0")
		if "_dunbuya_" in authshort:
			addauthor(ur"(Amadu Tanba DUNBUYA|Amadu Tanba Dunbuya)",u"587fb4ba-1385-4a2c-ab47-d60ed68d321b")
			addauthor(ur"(Yusufu Dunbuya|Yusu Dunbuya|Yusufu DUNBUYA|Yusu DUNBUYA)",ur"da8f0ed0-5365-4dd1-93f5-3f6afc0b7643")			
			addauthor(ur"(Fabu Dunbuya)",u"b97e7e65-dfef-4b44-b7c8-d3e0d2a7d9ac")
		if "_fane_" in authshort: 
			addauthor(ur"(Mamadu Fane|Mamadu FANE|Mamadu Fanɛ)",u"4168de2f-8c3a-49bf-afd1-219d1ed04a1b")
			addauthor(ur"(Yusufu F. Fanɛ|Yusufu Famori Fanɛ|Yusuf F. Fanɛ|Yusuf Famori Fanɛ|Yusufu Fanɛ|Yusufu F. Fane|Yusufu Famori Fane|Yusufu - Famori Fane|Yusufu Fane|Yusuf F. Fane|Yusuf Famori Fane)",u"458db881-6de5-4039-b450-9914355c0130")
		if "_fonba_" in authshort: 
			addauthor(ur"(Dirisa Fɔnba|Dirisa FƆNBA|Dirisa Fonba)",u"d381c752-e40c-4c6d-9cb1-60d48bc8697d")
			addauthor(ur"(Amari Fɔnba|Amari FƆNBA|Amari Fonba)",u"f8cab50f-1bba-4b2f-aa0e-5a4d8df8f8fe")
			addauthor(ur"(Basiru Fɔnba|Basiru FƆNBA)",u"53ef22ce-a19a-459c-a814-84ce03706231")
			addauthor(ur"(Daramani Fɔnba|Daramani FƆNBA)",u"ea0a1dc6-84e8-4b7c-9a6d-20749c228103")
			addauthor(ur"(Zankɛ Ngolo Fɔnba|Zankɛ Ngolo FƆNBA|Zankɛ Ŋɔlɔ Fɔnba|)",u"b4ee46bb-ec0f-417a-a5c5-397024592b62")

		if "_gindo_" in authshort : addauthor(ur"(Usmani Gindo|usumani Gindo|Usumani Gindo|Usumani Guido)",u"f96014e9-6a24-4735-9ffb-c9cdda74fe65")
		if "_jabate_" in authshort : addauthor(ur"(Fuseni Jabate|Fuseni JABATE|Fuseyini Jabate|Fuseyini JABATE)",u"76c495a4-7706-4487-92c1-27be5fb4e943")
		if "_jaabi_" in authshort : addauthor(ur"(Musa Jaabi|Musa JAABI)",u"51652320-a88e-4b50-87f2-fc1b465a20a6")
		if "_jabate_" in authshort : addauthor(ur"(Fuseni Jabate|Fuseni Jabatɛ)",u"76c495a4-7706-4487-92c1-27be5fb4e943")
		if "_jabi_" in authshort : addauthor(ur"(Laji M. Jabi|Laji M. JABI)",u"4c8159cd-a0e7-410c-85a9-ba505666abe1")
		if "_jakite_" in authshort : 
			addauthor(ur"(solomani jakite|Solomani Jakite)",u"33f55de3-c1d0-4365-a13f-05e6360b8ed1")
			addauthor(ur"(mamadu jakite|Mamadu Jakite|Mamadu JAKITE)",u"0b692d2a-a0fa-4adb-869d-8249580da079")
			addauthor(ur"(Siyaka Jakite|Siyaka JAKITE|Saka Jakite)",u"285fddae-a8f3-4d7d-b9b2-96e446ed57b2")
			addauthor(ur"(Kalifa Jakite|Kalifa JAKITE)",u"d28a755e-2674-4155-868e-97252d1c1b93")
			# "Jakite, Yɔrɔ Mɛnkɔrɔ",,,,,Bambara,"habite Buguni Faraba - Kibaru 095, 98 1980 Kib107 1981",62918880-44b0-416b-a3d4-41f9e3261560
			addauthor(ur"(yɔrɔ mɛnkɔrɔ jakite|Yɔrɔ Mɛnkɔrɔ Jakite|Yòrò Mènkòrò Jakite)",u"62918880-44b0-416b-a3d4-41f9e3261560")
		if "_jalo_" in authshort : 
			addauthor(ur"(Isa Jalo|Isa JALO|ISA JALO|isa jalo)",u"9a336ead-63bd-4bac-88a4-e63fa83c8505")
			addauthor(ur"(Shɛki U. Jalo|Shɛki U. JALO|Shɛki Umaru Jalo|Sɛki U. Jalo|Sɛki U. JALO|Sɛki Umaru Jalo)",u"54c07225-8068-423c-bb92-ae94fea49f42")
			addauthor(ur"(Sumayila Jalo|Sumɛyila Jalo|Sumayila JALO)",u"2f7e2bf4-7d5e-43df-93a5-057d50e3c5d4")
			addauthor(ur"(Abdulayi Jalo|Abdulayi JALO)",u"c3fea918-60e2-4ad4-ac13-42f6713b1603")
			addauthor(ur"(Daɲɛli Jalo|Danyɛli Jalo|Daɲɛli JALO)",u"ee15c979-1e11-46ac-87c1-04794c3039f4")
			addauthor(ur"(Solomani Jalo|Solomani JALO|Solomani jalo)",u"be54d4e2-6f68-4e62-8802-95385ba6564b")
			addauthor(ur"(Yusufu Jalo|Yusufu JALO|Yusuf Jalo)",u"04e64a0f-70c8-47e7-b887-09f1c67ce911")
			addauthor(ur"(Haji Jalo|Haji JALO)",u"48ed0991-742d-40ae-918f-89b6a872e0a4")

		if "_jara_" in authshort : 
			addauthor(ur"(Dɔkala Yusufu Jara|Dɔkala Yusuf Jara|Dɔkala Yusufu JARA|Dɔkala Y. Jara|Dɔkala Y. JARA)",u"b5edd814-54dd-4058-bd8c-dae51a64427d")
			addauthor(ur"(yaya jara|Yaya Jara|Yaya JARA)",u"fd800f25-d6ee-4b9f-b6f9-72c129183b79")
			addauthor(ur"(Dirisa Bakari Jara|Dirisa Bakari JARA)",u"266a0781-d80f-4f93-8885-fd28c4af344e")
			addauthor(ur"(Mamadu Nyama Jara|mamadu nyama jara|Mamadu Ɲama Jara)",u"618af8da-1f81-414c-b049-a6a38c9d6c80")
			addauthor(ur"(Fatumata Jara|Fatumata JARA)",u"178d8b60-2a1f-4de8-a7dc-5a0642fccd5b")
			addauthor(ur"(Shaka Jara|Shaka JARA)",u"c9e74689-bedd-4331-ab78-31846fc977c1")
			addauthor(ur"(Mami Jara|Mami JARA)",u"0d4c13df-70b8-4683-a1f3-0c248b9d4cc7")
			addauthor(ur"(Kɔnba Jara|Kɔnba JARA)",u"fc81ac64-408e-449b-85cd-8cd4ae2fab25")
			addauthor(ur"(Bakari Bilen Jara|Bakari Bilen JARA)",u"a0398a7a-251b-434d-be17-91e0ee1e233e")
			addauthor(ur"(Ibarahima Baba Jara|Ibarahima Jara|Ibarahima JARA|Ibarayima Jara|Ibarayima JARA)",u"3b24a2db-71cb-43db-bf14-59ad4a4dcde3")
			addauthor(ur"(Soyibajan Jara|Soyibajan JARA)",u"b225860b-9538-4504-aeca-b39750f1a1ea")
			addauthor(ur"(Usumani Jara|Usumani JARA)",u"1a596b70-23c8-45d8-b31e-517d6e44d41e")
			addauthor(ur"(Adama Jara|Adama JARA)",u"d32c72aa-3711-46d4-a1e0-ff045f797f3e")
			addauthor(ur"(Alu Jɛnfa Jara|Alu Jɛnfa JARA)",u"26910e4a-764c-427f-84de-721a50740b5a")
			addauthor(ur"(Bakayi Jara|Bakayi jara|Bakayi JARA)",u"34eb45e6-9e92-40c3-bf3a-90c7eb231fb6")
			addauthor(ur"(Zan Dosayi Jara|Zan Dosaye Jara)",u"8bd6f254-0f03-4822-aef7-3792ac0b07e4")
			addauthor(ur"(Siyaka Jara|Siyaka JARA)",u"0eb7d85a-bbf5-496a-9126-c7fd261621a9")
			addauthor(ur"(Dirisa Bakari Jara|Dirisa Bakari JARA)",u"266a0781-d80f-4f93-8885-fd28c4af344e")
			if "Nperesibugu" in tout or "NPeresibugu" in tout or "Npeseribugu" in tout or "NPeseribugu" in tout:
				addauthor(ur"(Mamadu Jara|Mamadu JARA)",u"dc81e9f8-e04a-4675-b98c-3b33b4a818ea")

		if "_jire_" in authshort : addauthor(ur"(Dusu Jire|Dusu JIRE)",u"d2f0a2c2-d202-47a9-877e-ec52cfc694b7")
		if "_kaba_" in authshort : addauthor(ur"(Mamadi Kaba|Mamadu Kaba|Mamadu KABA)",u"45856259-2685-4d35-b650-c8db3d5ae2d8")
		if "_kalanbiri_" in authshort : addauthor(ur"(Alɛkisi Kalanbiri|Alex Kalanbiri)",u"ccf1c399-9fa6-4ebc-8887-f99759915bab")
		if "_kamara_" in authshort : addauthor(ur"(Usumani Kamara|Usumani KAMARA|Gigimasa)",u"5bb7d097-e967-4495-ab75-b71000624bcf")
		if "_kamisoko_" in authshort : addauthor(ur"(Musa Kamisɔkɔ|Musa KAMISƆKƆ)",u"a67a4acf-6dbe-4bc1-8e20-d32c4b613128")
		if "_kane_" in authshort : 
			addauthor(ur"(Sumana Kane|Sumana KANE|Sumana Kanɛ)",u"11aefaf1-6d5b-4ffa-84c7-24a3edb32670")
			addauthor(ur"(mari kanɛ|mari kanè|Mari Kanɛ|Mari Kanè)",u"d43907f8-d08b-4474-8bb3-1d6a55b15f1a")
			addauthor(ur"(Musa Kanɛ|Musa Sayibu Kanɛ|Musa KANƐ)",u"9f6f459c-99c5-45c9-b946-9487921c3193")
		if "_kante_" in authshort : 
			addauthor(ur"(amadu ganyi kante|amadu ganyi kantè|A.G. Kante|A. G. Kante|A.G. KANTE|A.G.KANTE|A. G. KANTE|Amadu GANI Kante|Amadu GAƝI Kante|Amadu GAƝi Kante|Amadu Gaɲi Kante|Amadou Gaɲi Kante|Amadu G. Kante|Amadu G. KANTE|Amadu GANYI Kante|Amadu GAGNY Kante|Amadu Gagny Kante|Amadu Ganyi Kante|Amadu Gagny Kante|Amadu Gaɲi KANTE)",u"797f3350-5147-480b-9ec5-4f7ccfe35139")
			addauthor(ur"(Solomani Kantɛ|Solomani kantɛ|Solomani KANTƐ|solomani kantè)",u"dd718913-98f3-47aa-bce2-2fbffb72e317")
			addauthor(ur"(Ibarahima Kante|Ibarahima KANTE)",u"40310b23-7d3e-4f67-98ba-8e48cbae36da")
			addauthor(ur"(Mamadu Kanute|Mamadu Lamini Kanute|Mamadu KANUTE)",u"690f4a15-86cc-4381-9e81-f75dd9d6616d")
			addauthor(ur"(Sitan Kante|Sitan KANTE)",ur"5ed900fb-aa35-44ea-b2dd-01c114a61b12")
		if "_keyita_" in authshort : 
			addauthor(ur"(Dawuda Moriba Keyita|Dawuda Moriba keyita|Dawuda Moriba KEYITA|Dawuda Keyita|Dawuda KEYITA)",u"5e81a35c-c026-408e-8680-ca4ea0d8d222")
			addauthor(ur"(Burema Keyita|Burema KEYITA|Burama Keyita|Burama KEYITA)",u"4dedc8fc-cc66-4982-b24b-851d31e7b315")
			addauthor(ur"(Maman Keyita|Maman KEYITA|Manan Keyita)",u"33a9e28c-37f8-47ac-ae88-b8b67b4da526")
			addauthor(ur"(Madiba Keyita|Madiba KEYITA)",u"66b29102-5b8c-4edd-81ec-888d2307faa2")
			addauthor(ur"(Mamadi Keyita|Mamadi KEYITA)",u"cef226df-486e-4d6d-a3cb-118053c436f6")
			addauthor(ur"(Gabukɔrɔ Keyita|Gabukòrò Keyita)",u"84a8d118-b713-41a4-9ed5-16a51f4aba6f")
		if "_komagara_" in authshort : addauthor(ur"(Jiki Komagara|Jiki KOMAGARA|Jigi Komagara|Jigi KOMAGARA)",u"4b4d9826-8885-4fcd-92fc-2ff651a0b23e")
		if "_komakara_" in authshort : addauthor(ur"(Jiki Komakara|Jiki KOMAKARA|Jigi Komakara|Jigi KOMAKARA)",u"4b4d9826-8885-4fcd-92fc-2ff651a0b23e")
		if "_konate_" in authshort : addauthor(ur"(Hamidu Konate|Hamidu KONATE)",u"c7fa01a9-6428-4d30-bfed-426ea69618ba")
		if "_kone_" in authshort : 
			addauthor(ur"(Alu Kɔnɛ|Alu KƆNƐ|alu kɔnɛ|alu kònè)",u"2246823e-f72a-48b5-b593-f215a321b963")
			addauthor(ur"(Mohamɛdi Kɔnɛ|Mohamɛdi KƆNƐ|Mohamɛdi KONƐ|Mohamɛdi KONE|M ohamɛdi kɔnɛ|mohamɛdi kɔnɛ|mohamèdi kònè)",u"17e50ef6-e4ef-4373-a3bc-6b9fa536bfea")
			addauthor(ur"(Bakari Kɔnɛ|Bakari KƆNƐ)",u"cb16231a-ac28-474d-b82d-075d4e254e76")
			addauthor(ur"(Sisela Mayimuna Kɔnɛ|Sisela Mayimuna KƆNƐ)",u"aa1a73cb-f9a9-497b-82a5-c33feee93bf5")
			addauthor(ur"(Musa Kɔnɛ|Musa KƆNƐ)",u"856e0687-0fb1-4469-8a46-0fa11fa9031d")
		if "_konta_" in authshort : addauthor(ur"(Mahamadu Konta|Mahamadu Kɔnta|Mahamadu kɔnta|Mahamaddu Kɔnta|Mahamadu KONTA|Mahamadu KƆNTA)",u"c742b89a-fdfb-4d5c-9868-690d9935fa18")
		if "_kulibali_" in authshort:
			addauthor(ur"(Nɛgɛta Kulibali|Nɛgɛta KULIBALI|Negeta Kulibali|nègèta kulibali|Negeta KULIBALI)",u"c6563397-b2fb-465b-8c84-98ff0740b9ca")
			addauthor(ur"(basiru kulibali|Basiru Kulibali|Basiru KULIBALI)",u"b3d03481-2736-4a65-ae48-446097e97c31")
			addauthor(ur"(Daniyɛli Kulibali|Daniyɛli KULIBALI)",u"7faf5c2d-3602-4af6-b4f5-d1b8a11e0ed6")
			addauthor(ur"(Fanta Kulibali|Fanta KULIBALI)",u"6018c6bd-cad4-4354-bcb9-6327a9d28f37")
			addauthor(ur"(Kamatigi Kulibali|Kamatigi KULIBALI)",u"db7cdd2a-d0bf-4008-885a-e97338a91b83")
		if "_kulibaly_" in authshort:
			addauthor(ur"(Fanta Kulibaly|Fanta KULIBALY)",u"6018c6bd-cad4-4354-bcb9-6327a9d28f37")
		if periodique=="jekabaara" and "_kulubali_" in authshort:
			addauthor(ur"(Bubakari Kulubali|Bubakari kulubali|Babakari Kulubali|B. Kulubali|B.Kulubali)",u"4c6bc903-6586-44b8-91fb-6a4764a5f20e")
		if periodique=="jekabaara" and "_kulibali_" in authshort:
			addauthor(ur"(Bubakari Kulibali|Bubakari kulibali|B. Kulibali|B.Kulibali)",u"4c6bc903-6586-44b8-91fb-6a4764a5f20e")		
		if "_kulubali_" in authshort:
			# Bubakari : il y en a trop !
			addauthor(ur"(nɛgɛta kulubali|Nɛgɛta Kulubali|Nɛgɛta KULUBALI|Negeta Kulubali|nègèta kulubali|Negeta KULUBALI)",u"c6563397-b2fb-465b-8c84-98ff0740b9ca")
			#addauthor(ur"(mamadu kulubali|Mamadu Kulubali)",u"7389e900-8214-4516-9ba1-b8b403708d7c")
			addauthor(ur"(mamadu kulubali|Mamadu Kulubali|M. KULUBALI|M. Kulubali)",u"b21d1a28-e4a2-4f91-b1d8-33cff629718e")
			addauthor(ur"(modibo kulubali|Modibo Kulubali)",u"b8c824dd-40ed-46b3-939d-0687fd3415fd")
			addauthor(ur"(moriba kulubali|Moriba Kulubali|Moriba KULUBALI|Mɔriba KULUBALI)",u"8980ff6b-0155-40bc-88e3-0d5f2650e9d4")
			addauthor(ur"(dɛnba kulubali|Dɛnba Kulubali|Dɛnba KULUBALI)",u"6ccb4659-2010-4a22-bff8-ef8a0786264d")
			addauthor(ur"(amidu kulubali|Amidu Kulubali|Amidu KULUBALI)",u"383c85d5-9d08-4d6f-b5e5-fd985a317d8e")
			addauthor(ur"(basiru kulubali|Basiru Kulubali|Basiru KULUBALI)",u"b3d03481-2736-4a65-ae48-446097e97c31")
			addauthor(ur"(Musa Numukɛba Kulubali|Musa Numukɛba KULUBALI)",u"b2e1c18f-0369-49b0-8f51-610d492dd521")
			addauthor(ur"(Mɔrikɛ Kulubali|Mɔrikɛ KULUBALI)",u"6c5e9b5e-6873-4141-9e5a-c829f4591aad")
			addauthor(ur"(Bayi Kulubali|Bayi KULUBALI)",u"cb438776-e9e5-45eb-b1ae-dabe13fd783d")
			addauthor(ur"(Usumani Kulubali|Usumani kulubali|Usumani KULUBALI)",u"c8c9fe81-d9e1-4d6b-a328-39b0616c19cd")
			addauthor(ur"(Daniyɛli Kulubali|Daniyɛli KULUBALI|Daniyɛli kulubali)",u"7faf5c2d-3602-4af6-b4f5-d1b8a11e0ed6")
			addauthor(ur"(Fode Kulubali|Fode KULUBALI)",u"e4ff0b2e-48d8-4b8e-82b4-f097469f2a1a")
			addauthor(ur"(Shaka Kulubali|Shaka KULUBALI|Ishaka Kulubali)",u"325e54ef-30c7-4710-8f60-3bed25d90df9")
			addauthor(ur"(Siratiki Kulubali|Siratigi Kulubali)",u"a664260d-90d0-4271-a109-87051896c49a")
			addauthor(ur"(Umaru Kulubali|Umaru KULUBALI)",u"f59418f3-ea40-42cb-a742-c128bcc2e4f6")
			addauthor(ur"(Fanta Kulubali|Fanta KULUBALI)",u"6018c6bd-cad4-4354-bcb9-6327a9d28f37")
			addauthor(ur"(Kamatigi Kulubali|Kamatigi KULUBALI)",u"db7cdd2a-d0bf-4008-885a-e97338a91b83")

		if "_kulubaly_" in authshort:
			addauthor(ur"(Fanta Kulubaly|Fanta KULUBALY)",u"6018c6bd-cad4-4354-bcb9-6327a9d28f37")
		if "_kumare_" in authshort : addauthor(ur"Siyaka Kumarɛ|Siyaka Kumare|Siyaka kumare|Siyaka KUMARƐ",u"9d1ff4e3-f4a1-4bf4-8362-cdded032939a")
		if "_lamu_" in authshort : addauthor(ur"(A. Lamu|Alayi Lamu|Alayi LAMU)",u"ebb0c747-5e5e-41e8-baa0-c780bab4598e")
		if "_leplaideur_" in authshort : addauthor(ur"(Marie-Agnès Leplaideur|Marie Agnès Leplaideur|Marie Agnès Leplaideur)",u"2c0367fd-a997-4609-8806-000921e35d18")
		
		if "_magiraga_" in authshort : addauthor(ur"(Mahamadu Magiraga)",u"71c91448-4c9e-4a70-80e6-36b4b3f8a7e3")
		if "_mariko_" in authshort : addauthor(ur"(yaya mariko|Yaya Mariko)",u"b746f073-4777-465a-8ee4-0276592cfb09")
		if "_mayiga_" in authshort : 
			addauthor(ur"(bulkadèri mayiga|Bulkadèri Mayiga|Bulkadɛri Mayiga)",u"6a1ab6fb-203c-4ef6-83a5-e020afcf9b92")
			addauthor(ur"(fatumata mayiga|Fatumata Mayiga|Fatumata MAYIGA)",u"79a71680-67a1-44be-a693-f88bb3b5dc49")
			addauthor(ur"(Mahamani A. Mayiga|Mahamane Mayiga)",u"24d50126-b321-4288-9bca-c670c9142825")
		if "_menta_" in authshort : addauthor(ur"(Suleyimani Mɛnta|Solomani Mɛnta|solomani mɛnta|solomani mènta)",u"63b70297-b35e-4b1f-b5df-27fcc6dec7a5")
		if "_nafo_" in authshort : addauthor(ur"(F. Nafo|Fatumata Nafo|Fatumata NAFO)",u"486d185e-79f1-492d-82e3-b48d12a2420a")
		if "_ndawo_" in authshort : addauthor(ur"(Dawuda Mace Ndawo|Dawuda M\.Ndawo|Dawuda M\. Ndawo)",u"f0c85c3c-17d5-4af6-ab3e-28b8fd906fe4")
		if "_nguessan_" in authshort : addauthor(ur"(Raphaül N'Guessan|Raphaül N'Guessan|Raphaul N'Guessan|Raphaül N'GUESSAN|Raphaül N'GUESSAN|Raphaul N'GUESSAN)",u"fa8b3c83-db30-4fdf-951e-b7cb058956b7")
		if "_nyani_" in authshort or "_nani_" in authshort : addauthor(ur"(Umaru Nani|Umaru Ɲani|Umaru ƝANI)",u"e3f6c7e4-2f76-459c-a4e9-c4702b6bd970")
		if "_nyare_" in authshort : addauthor(ur"(Meydi Ɲare|Medi Ɲare|Meydi ƝARE|Medi ƝARE)",u"e6be7efc-34a4-4c76-a77a-d2ddcc10e56d")
		if "_sako_" in authshort : 
			addauthor(ur"(Zan Sakɔ)",u"06083e70-ee05-42af-ba8e-410a3ed82a76")
			addauthor(ur"(Dotege Sako|Dotigi Sako|Dotege SAKO)",u"b213ebbb-fcaa-48ec-9fb3-0a5cb50351da")
		if "_samake_" in authshort : 
			addauthor(ur"(Nanse Samake|Nanse SAMAKE|Ɲanse SAMAKE)",u"2030b450-3a6b-49ed-83b9-5799e1c97c15")
			addauthor(ur"(Sidi Lamini Samake|Sidi Lamini Samakɛ)",u"e4cac73a-9de6-497a-b977-96a700bedf01")
			addauthor(ur"(Zan Samake|Zan Samakɛ)",u"5851ab7f-f669-487c-9ba8-d03577181a1d")
			addauthor(ur"(Dawuda Jinɛmusa Samake|Dawuda jinɛmusa Samake|Dawuda, ko jinɛmusa Samake)",u"2a32f60e-253f-49bf-ad87-02a261f6ed52")
			addauthor(ur"(Bubakari Sangare|Bubakari SANGARE)",u"6db84d53-f9ac-472a-9926-2deb1fdfe0ca")
			addauthor(ur"(Fasun Idirisa Samake|Fasun Samake|Fasun Idirisa SAMAKE)",u"9fec18a6-f4e7-43c0-b93e-fd6e43e90454")
		if "_sangare_" in authshort : 
			addauthor(ur"(Adama Dawuda Sangare|Adama Dawuda SANGARE)",u"65b9b944-f1a7-4973-a52d-0c30a1ce87c1")
			addauthor(ur"(Bakari Sangare|Bakari sangare|Bakari SANGARE|Bakary Sangare)",u"1cacb7c3-5fc9-4020-bffc-4f2f60bd30ef")
		if "_saya_" in authshort : addauthor(ur"(Mulayi Saya|Mulayi SAYA)",u"cae507d3-3764-4f88-8250-f10f65df1732")
		if "_senu_" in authshort : addauthor(ur"(Idirisa Senu|Idirisa SENU|Idrisa SENU|Drisa Senu|Drisa SENU)",u"cd0ca0ae-0426-4ebc-bfd8-2390c291c98c")
		if "_si_" in authshort : 
			addauthor(ur"(bubakari si|Bubakari Si|Bubakari SI)",u"297f5e59-7e14-4f9f-af0e-46a8373bcfdb")
			addauthor(ur"(Ti Yalam Si|Ti Yalam SI)",u"37fb14af-e1f9-4ba2-ba7c-5f67401f42fd")  # = TYS			
		if "_sidi_" in authshort : addauthor(ur"(Tuya Sidi|Tu Ya Sidi|Tuya SIDI)",u"37fb14af-e1f9-4ba2-ba7c-5f67401f42fd")  # = TYS
		if "_sidibe_" in authshort : 
			addauthor(ur"(M. Sidibe|M. SIDIBE)",u"d382c276-cb63-42f3-9ec8-4cc7f6e79a76")
			addauthor(ur"(Masa Sidibe|Masa SIDIBE)",u"2ba135bb-49f6-4f69-bf72-d35cb7195c45")
			addauthor(ur"(tumani yalamu sidibe|tumani yalame sidibe|Tumani Sidibe|Tuya Sidibe|Ti Yalam Si|Tumani Yalam Sidibe|Tumani Y Sidibe|Tumani yalam Sidibe|Tumani Yalam SIDIBE|Tumani Yalamu Sidibe|Tumani Yalamu SIDIBE|Tumani Y. Sidibe|Tumani Y. SIDIBE|T. Y. Sidibe|T. Y. SIDIBE|Toumani Yalam Sidibe|Toumani Yalam SIDIBE)",u"37fb14af-e1f9-4ba2-ba7c-5f67401f42fd")
			addauthor(ur"(Burama Sidibe|Burama SIDIBE)",u"7ef74ea3-7846-46f1-ba22-ff113b2a40e8")
			addauthor(ur"(Isaka Sidibe|Isaka SIDIBE|Isiyaka Sidibe|Isiyaka SIDIBE)",u"c40b5a51-94ee-48fb-a425-1a7ac752f2f8")
			addauthor(ur"(Yusufu Jime Sidibe|Yusufu Jime SIDIBE|Yusuf Jime Sidibe|Yusufu Jimɛ Sidibe|Yusufu Jimɛ SIDIBE|Yusuf Jimɛ Sidibe)",u"c26122ec-de4d-49a9-81b8-ce5899ae0474")
		if "_sise_" in authshort : 
			addauthor(ur"(Daramani Sise|Daramani SISE)",u"3a8dcd18-7ff6-40d4-ad7f-67b2ee4b8537")
			addauthor(ur"(Amadu M. Sise|Amadu M. SISE)",u"f38c8a39-329b-4916-8c7f-5b889e87523b")
			addauthor(ur"(Mahamadu B. Sise|Mahamadu B. SISE|M. B. SISE)", u"f394dedd-9131-4b1c-8456-06b06aae98a7")
			addauthor(ur"(Seku Sise|Seku SISE)",u"5cad8db8-f718-4d77-9b00-6b98c1ba02e3")
			addauthor(ur"(mamadu yusufu sise|Mamadu Yusufu Sise|Mamadu Yusuf Sise|Mamadu Yusufu SISE)",u"1662fdb6-5b2b-4e20-b09e-222bbc4115e6")
			addauthor(ur"(Mahamadu Lareya Sise|Mamadu Lareya Sise|Mahamadu Lariya Sise|Mamadu Lariya Sise)",u"f3b91ae3-022a-4d2e-91f1-c18ada0000bc")
			addauthor(ur"(Amara Sise|Amara SISE)",u"d1c5691b-f597-43fc-8812-de0973007697")
		if "_sisoko_" in authshort :
			addauthor(ur"(mariyamumadi misoko|mariyamadi sisoko|mariyanmadi sisoko|Mariyanmadi sisoko|Mariyanmadi Sisoko|Mariyamumadi Sisoko|Mariyamadi Sisoko)",u"a5c6837b-e811-400b-8df4-1bd5accbaf81")
		if "_so_" in authshort : 
			addauthor(ur"(Ibarahima SO|Ibarahima SƆ|Ibarahima So|Ibarahima Sɔ|ibarahima so)",u"8efb9f72-1f7f-45ef-88e2-63df76aa2766")
			addauthor(ur"(Shɛki Madu SO|Shɛki Madu SƆ|Shɛki Madu So|Shɛki Madu Sɔ|shɛki madu so)",u"33bc2e39-335a-4d95-8014-2e15b52e2357")
		if "_sogoba_" in authshort : 
			addauthor(ur"(Shaka Sogoba|ʃaka Sogoba|Siyaka Sogoba)",u"8c54b573-5ba9-4558-a828-354afef8ee5e")
			addauthor(ur"(Bala Sogoba|Bala SOGOBA)",u"638507fe-69e0-40c2-ad36-8337730f927f")
			
		if "_sukuna_" in authshort: addauthor(ur"(Mamayi Sukuna|Mamayi SUKUNA)",u"5ca24c05-96f6-4332-906e-8bd1f9125015")
		if "_sunkara_" in authshort :addauthor(ur"(Amadu SUNKARA|Amadu Sunkara|amadu sunkara)",u"f65af322-1fe8-4381-b65d-68758164036e")
		if "_tangara_" in authshort : addauthor(ur"(ya tangara|Ya Tangara)",u"868d316d-c084-45db-921f-966fa94724ef")
		if "_trawele_" in authshort: 
			addauthor(ur"(Umu Amar Trawele)",u"14e31872-e90f-48ae-b008-ff4e325fccee")
			addauthor(ur"(Daramani Trawele|Daramane Trawele|Daraman Trawele|Daramani TRAWELE|Daramane TRAWELE|Daraman TRAWELE)",u"2da173f5-f2f0-4af0-a413-3ca3c6ee7a88")
		if "_tarawele_" in authshort : 
			addauthor(ur"(Daramani Tarawele|Daramane Tarawele|Daraman Tarawele|Daramani TARAWELE|Daramane TARAWELE|Daraman TARAWELE)",u"2da173f5-f2f0-4af0-a413-3ca3c6ee7a88")
			addauthor(ur"(Janginɛ Tarawele|Janginɛ TARAWELE)",u"9a7671d9-e6e2-4c86-99c2-abd6601d9ed7")
			addauthor(ur"(Asani Tarawele|Asani TARAWELE|Alasani Tarawele|Alasani TARAWELE)",u"48347506-6757-4d20-b854-735f2c1e09cf")
			addauthor(ur"(Alujan Tarawele|Alujan TARAWELE)",u"258e2d7f-e4f4-4803-ba72-518f66f18f2d")
			addauthor(ur"(Fanta Tarawele|Fanta TARAWELE|Fanta Fula Tarawele)",u"41f86179-2da0-4890-91f9-4bf687788f4b")
			addauthor(ur"(Sungalo Tarawele|Sungalo TARAWELE|Sunkalo Tarawele)",u"db99321c-0d53-4eb3-aa86-7f14d99de21f")
			addauthor(ur"(Gɔnba Tarawele|Gɔnba TARAWELE|Gonba Tarawele|Gonba TARAWELE)",u"47d27d6a-73fd-4cfb-bb7e-acce3dd707d9")
			addauthor(ur"(Siyaka Tarawele|Siyaka TARAWELE)",u"9885109d-3fdf-4cf2-8307-1ad88cd1d8ed")
			addauthor(ur"(Basumana Tarawele|Basumana TARAWELE)",u"e79dde7c-1739-47fa-b50d-b2addce57ae2")
			addauthor(ur"(Mariyamu A Tarawele|Mariyamu A. Tarawele|Mariyamu A TARAWELE|Mariyamu A. TARAWELE)",u"dd14cfd3-bfc5-4b41-9827-07330f78032a")
			addauthor(ur"(Isa Tarawele|Isa Trawele|Isa TARAWELE)",u"dc8c09d1-c257-4939-a2c2-c98c494800fd")
			addauthor(ur"(Kasun Tarawele|Kasun TARAWELE)",u"ab30d433-20bb-4152-8885-d61c958d2517")
			addauthor(ur"(Duguna Tarawele|Duguna TARAWELE)",u"44a419e9-b797-4e3a-bbbc-cde095e486ba")
			addauthor(ur"(Mamadu Tarawele|Mamadu TARAWELE)",u"1f54a676-f904-4080-af0d-5b995fbf3fea")
			addauthor(ur"(C.M. Tarawele|C. M. Tarawele)",u"c9775956-e767-411b-ac4a-aacc504aa314")
			addauthor(ur"(Usumani Tarawele|Usumani TARAWELE)",u"a1396798-4b28-48a1-b16d-c9679207cb7a")
			addauthor(ur"(Bafin Tarawele|Bafin TARAWELE)",u"0577018c-d74d-4f68-81f9-218279f2514e")

		if "_tulema_" in authshort : addauthor(ur"(Hamidu Tulema|Hamidu TULEMA)",u"b5864f72-0d3d-4428-a2a3-13cca538f6e1")
		if "_tunkara_" in authshort : addauthor(ur"(S. B. Tunkara|Solomani Bobo Tunkara|Solomani Bobo TUNKARA|Solomani B. Tunkara)",u"cd5292c9-93cc-494f-abd0-0a834bb677a2")
		if "_ture_" in authshort : 
			addauthor(ur"(B. Ture|B. TURE|Basiriki Ture|Basiriki TURE|Basidiki Ture|Basidiki TURE)",u"60ba1311-ba33-4b5a-ab42-8fb1a6038263")
			addauthor(ur"(sedu ture|sedu turè|seyidu ture|Seyidu Ture)",u"72559003-6529-4e84-b9c5-ef681d1b01dd")
			addauthor(ur"(Berema Ture|Berema TURE)",u"51d73647-d28e-45cb-96b1-52c86a597f72")
			addauthor(ur"(Madu Ture|Madu TURE)",u"eca51900-8a0c-410b-a48b-8ce752447d1a")
		if "_watara_" in authshort or "_ouattara_" in authshort :
			addauthor(ur"(Suleyimani Watara|Suleyimani WATARA|Sulɛyimani WATARA|Suleyimani Ouattara|Suleymane Watara)",u"4086d40b-cb3a-4b04-9688-b9e4f4a3e8c5")
		if "_williams_" in authshort : addauthor(ur"(Denise Williams|Denise WILLIAMS)",u"fae54512-72ee-45fe-8b00-4dbabb6bc6d4")


		authmetas=u""
		if auuid!=u"" :
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:uuid\"","\""+auuid+"\" name=\"author:uuid\"",authstub)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:name\"","\""+aname+"\" name=\"author:name\"",authmetas)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:spelling\"","\""+aspelling+"\" name=\"author:spelling\"",authmetas)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:birth_year\"","\""+abirth+"\" name=\"author:birth_year\"",authmetas)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:sex\"","\""+asex+"\" name=\"author:sex\"",authmetas)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:native_lang\"","\""+anative+"\" name=\"author:native_lang\"",authmetas)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:dialect\"","\""+adialect+"\" name=\"author:dialect\"",authmetas)
			authmetas=re.sub(r"\"(XXX)\" name=\"author\:addon\"","\""+aaddon+"\" name=\"author:addon\"",authmetas)
		# print metas
		# sys.exit("---stop tests---")
		filenameout=re.sub("\.txt",".html",filename)   # filename can be *.txt or *.old.txt -> *.html, *.old.html
		outf=open(filenameout,"w")
		if authmetas!=u"" :
			metas=re.sub("</head>",authmetas+"\n</head>",metas)
		outf.write(metas+u"\n<body><p>"+tout+u"</p></body>\n</html>\n")
		outf.close()
		fileIN.close()