!pip install thefuzz
!pip install fuzzywuzzy
!pip install python-Levenshtein

from fuzzywuzzy import fuzz


input_name = input("Enter the input car name and model:")

database_names = ["ford_aspire",
"ford_ecosport",
"ford_endeavour",
"ford_figo",
"honda_amaze",
"honda_city",
"honda_wr_v",
"hyundai_aura",
"hyundai_grand_i10",
"hyundai_i10",
"jeep_compass",
"jeep_meridian",
"kia_carens",
"kia_seltos",
"kia_sonet",
"land_rover_defender",
"mahindra_scorpio",
"mahindra_thar",
"mahindra_xuv300",
"mahindra_xuv400",
"mahindra_xuv700",
"maruti_celerio",
"maruti_suzuki_brezza",
"maruti_suzuki_s_presso",
"maruti_suzuki_swift",
"maruti_suzuki_wagonr",
"maruti_suzuki_xl6",
"mg_astor",
"mg_gloster",
"mg_hector",
"mg_zs_ev",
"renault_kiger",
"renault_triber",
"skoda_kushaq",
"skoda_slavia",
"tata_harrier",
"tata_punch",
"tata_tiago",
"toyota_camry",
"toyota_fortuner",
"toyota_fortuner_legender",
"toyota_glanza",
"toyota_innova_crysta"]
max_percentage=0
for names in database_names:
   # print(f" {names , fuzz.ratio(names.replace('_',' ').upper(), input_name.replace('-',' '))}")
    if(fuzz.ratio(names.replace('_',' ').upper(), input_name.replace('-',' ').upper())>max_percentage):
        max_percentage = fuzz.ratio(names.replace('_',' ').upper(), input_name.replace('-',' ').upper())
        output_name    = names
        if(max_percentage==0):
            output_name = "no match found"
print("Car Name :",output_name)
print("Matching % in database: ", max_percentage)
