import pandas as pd
import numpy as np

class dictionaryCollection:
    def __init__(self):
        self.denom_dict = {
            1: 'Jewish Orthodox',
            2: 'Jewish Reform (Union)',
            3: 'Jewish Conservative (United)',
            4: 'Jewish, other/unspecified',
            5: 'Hindu',
            6: 'Buddhist',
            7: 'Muslim', 
            8: 'Other Non-Christian',
            9: 'Catholic',
            10: 'Episcopal Church',
            11: 'ELCA',
            12: 'Lutheran, Missouri Synod',
            13: 'Wisconsin Evangelical Lutheran Synod',
            14: 'Other Lutheran',
            15: 'PCUSA',
            16: 'PCA',
            17: 'Other Presbyterian',
            18: 'RCA',
            19: 'Christian Reformed',
            20: 'Other Reformed',
            21: 'UU',
            22: 'UMC',
            23: 'Nazarene',
            24: 'Wesleyan',
            25: 'Free Methodist',
            26: 'Other Methodist', 
            27: 'UCC',
            28: 'SBC',
            29: 'National Baptist Convention, USA, Inc',
            30: 'American Baptist Churches in the USA (Northern)',
            31: 'National Baptist',
            32: 'Baptist General Conference (Converge)',
            33: 'Baptist Churches Association of America',
            34: 'Missionary Baptist',
            35: 'Freewill Baptist',
            36: 'National Baptist Convention of America',
            37: 'Progressive National Baptist Convention',
            38: 'Primitive Baptist',
            39: 'Conservative Baptist Association of America',
            40: 'General Association of Regular Baptist Churches',
            41: 'Other Baptist',
            42: 'Disciples of Christ',
            43: 'Church/Churches of Christ',
            44: 'Brethren Churches',
            45: 'Mennonite',
            46: 'Quaker',
            47: 'Greek Orthodox',
            48: 'Eastern and Other Orthodox',
            49: 'AME',
            50: 'AME Zion',
            51: 'COGIC',
            52: 'Vineyard',
            53: 'Calvary Chapel',
            54: 'Christian Missionary Alliance',
            55: 'Evangelical Free Church',
            56: 'Evangelical Covenant',
            57: 'blank',
            58: 'Assemblies of God',
            59: 'Foursquare Gospel',
            60: 'Church of God (Cleveland, TN)',
            61: 'Church of God (Anderson, IN)',
            62: 'Other Church/Churches of God',
            63: 'Pentecostal Holiness',
            64: 'Full Gospel',
            65: 'Other Pentecostal',
            66: 'Mormon',
            67: 'Jehovah\'s Witnesses',
            68: 'Seventh Day Adventist',
            69: 'Unity Church',
            70: 'Other Christian',
            99: 'No Official Denomination'
            # Add more mappings as needed
        }
        
        self.change_dict = {
            1: 'Decreased more than 10 percent',
            2: 'Decreased less than 10 percent',
            3: 'Remained about the same',
            4: 'Increased less than 10 percent',
            5: 'Increased more than 10 percent'
        }
        
        # Facilities
        
        self.bldgtype_dict = {
            1: 'School',
            7: 'Storefront',
            20: 'Church, Synagogue, Temple, or Mosque',
            21: 'Other'
        }
        
        self.viewbldg_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.remodel_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.homeschl_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.haveschl_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.usebldg_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.permpurp_dict = {
            1: 'Kitchen',
            2: 'Buliding/Remodeling',
            3: 'Liquor License',
            4: 'Day Care License',
            5: 'Bingo/Gabling/Raffle License',
            6: 'Signage/Statue',
            7: 'Burning',
            8: 'Festival/Bazaar',
            9: 'Parade/March',
            10: 'Boiler',
            11: 'Mailing',
            12: 'Zoning',
            13: 'Tax Exemption',
            15: 'Food License',
            16: 'Worker\'s Compensation',
            17: 'Soup Kitchen',
            18: 'Fire Department',
            19: 'Rezoning',
            20: 'Expand Cemetery',
            21: 'Vehicle License',
            22: 'School Registration',
            23: 'Build Houses',
            24: 'Handicapped License',
            25: 'Health Permit',
            26: 'Visa',
            27: 'Elevator',
            28: 'Resale Permit',
            29: 'Historic Site Status',
            30: 'Radio Station'
            # Add more mappings as needed
        }
        
        # Music
        
        self.singing_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.choir_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.piano_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.organ_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.drums_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.elecgtr_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.guitar_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        # Staffing - no dictionaries needed
        
        # Worship
        
        self.sermon_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.spkrdwn_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.greet_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.kidtime_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.teenpart_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.robe_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.applause_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.laugh_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.program_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.overhead_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.streamed_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.smtphone_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.congread_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.offering_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        # Programs
        
        self.clsyacs_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.clsadlt_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.ythgrp_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.teenchor_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.teencamp_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.teenvol_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.politics_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.disbible_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.books_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.parents_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.voterreg_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.science_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.environ_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.orgvols_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.workprob_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.newmems_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.train_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.racerel_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.othtrad_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.ownmony_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.congmony_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.assess_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.marriage_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.womengrp_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.mengrp_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.exercise_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
        
        self.lgbt_dict = {
            1: True,
            2: False
            # Add more mappings as needed
        }
                        
        # Add more dictionaries as needed


    def get_denom_description(self, numeric_value):
        return self.denom_dict.get(numeric_value, np.nan)
    
    def get_change_description(self, numeric_value):
        return self.change_dict.get(numeric_value, np.nan)
    
    def get_bldgtype_description(self, numeric_value):
        return self.bldgtype_dict.get(numeric_value, np.nan)
    
    def get_viewbldg_description(self, numeric_value):
        return self.viewbldg_dict.get(numeric_value, np.nan)
 
    def get_remodel_description(self, numeric_value):
        return self.remodel_dict.get(numeric_value, np.nan)

    def get_homeschl_description(self, numeric_value):
        return self.homeschl_dict.get(numeric_value, np.nan) 
 
    def get_haveschl_description(self, numeric_value):
        return self.haveschl_dict.get(numeric_value, np.nan)  
 
    def get_usebldg_description(self, numeric_value):
        return self.usebldg_dict.get(numeric_value, np.nan)  
 
    def get_permpurp_description(self, numeric_value):
        return self.permpurp_dict.get(numeric_value, np.nan)  
 
    def get_singing_description(self, numeric_value):
        return self.singing_dict.get(numeric_value, np.nan)  
 
    def get_choir_description(self, numeric_value):
        return self.choir_dict.get(numeric_value, np.nan) 
 
    def get_piano_description(self, numeric_value):
        return self.piano_dict.get(numeric_value, np.nan) 

    def get_organ_description(self, numeric_value):
        return self.organ_dict.get(numeric_value, np.nan) 

    def get_drums_description(self, numeric_value):
        return self.drums_dict.get(numeric_value, np.nan) 

    def get_elecgtr_description(self, numeric_value):
        return self.elecgtr_dict.get(numeric_value, np.nan) 

    def get_guitar_description(self, numeric_value):
        return self.guitar_dict.get(numeric_value, np.nan) 

    def get_sermon_description(self, numeric_value):
        return self.sermon_dict.get(numeric_value, np.nan) 

    def get_spkrdwn_description(self, numeric_value):
        return self.spkrdwn_dict.get(numeric_value, np.nan) 

    def get_greet_description(self, numeric_value):
        return self.greet_dict.get(numeric_value, np.nan) 

    def get_kidtime_description(self, numeric_value):
        return self.kidtime_dict.get(numeric_value, np.nan) 

    def get_teenpart_description(self, numeric_value):
        return self.teenpart_dict.get(numeric_value, np.nan) 

    def get_robe_description(self, numeric_value):
        return self.robe_dict.get(numeric_value, np.nan) 

    def get_applause_description(self, numeric_value):
        return self.applause_dict.get(numeric_value, np.nan) 

    def get_laugh_description(self, numeric_value):
        return self.laugh_dict.get(numeric_value, np.nan) 

    def get_program_description(self, numeric_value):
        return self.program_dict.get(numeric_value, np.nan) 

    def get_overhead_description(self, numeric_value):
        return self.overhead_dict.get(numeric_value, np.nan) 

    def get_streamed_description(self, numeric_value):
        return self.streamed_dict.get(numeric_value, np.nan)

    def get_smtphone_description(self, numeric_value):
        return self.smtphone_dict.get(numeric_value, np.nan)

    def get_congread_description(self, numeric_value):
        return self.congread_dict.get(numeric_value, np.nan)

    def get_offering_description(self, numeric_value):
        return self.offering_dict.get(numeric_value, np.nan)

    def get_clsyacs_description(self, numeric_value):
        return self.clsyacs_dict.get(numeric_value, np.nan)

    def get_clsadlt_description(self, numeric_value):
        return self.clsadlt_dict.get(numeric_value, np.nan)

    def get_ythgrp_description(self, numeric_value):
        return self.ythgrp_dict.get(numeric_value, np.nan)

    def get_teenchor_description(self, numeric_value):
        return self.teenchor_dict.get(numeric_value, np.nan)

    def get_teencamp_description(self, numeric_value):
        return self.teencamp_dict.get(numeric_value, np.nan)

    def get_teenvol_description(self, numeric_value):
        return self.teenvol_dict.get(numeric_value, np.nan)
    
    def get_politics_description(self, numeric_value):
        return self.politics_dict.get(numeric_value, np.nan)    
    
    def get_disbible_description(self, numeric_value):
        return self.disbible_dict.get(numeric_value, np.nan)     
    
    def get_books_description(self, numeric_value):
        return self.books_dict.get(numeric_value, np.nan)    
    
    def get_parents_description(self, numeric_value):
        return self.parents_dict.get(numeric_value, np.nan)    
    
    def get_voterreg_description(self, numeric_value):
        return self.voterreg_dict.get(numeric_value, np.nan)    
    
    def get_science_description(self, numeric_value):
        return self.science_dict.get(numeric_value, np.nan)

    def get_environ_description(self, numeric_value):
        return self.environ_dict.get(numeric_value, np.nan)

    def get_orgvols_description(self, numeric_value):
        return self.orgvols_dict.get(numeric_value, np.nan)

    def get_workprob_description(self, numeric_value):
        return self.workprob_dict.get(numeric_value, np.nan)

    def get_newmems_description(self, numeric_value):
        return self.newmems_dict.get(numeric_value, np.nan)  

    def get_train_description(self, numeric_value):
        return self.train_dict.get(numeric_value, np.nan)   
 
    def get_racerel_description(self, numeric_value):
        return self.racerel_dict.get(numeric_value, np.nan)
 
    def get_othtrad_description(self, numeric_value):
        return self.othtrad_dict.get(numeric_value, np.nan) 
 
    def get_ownmony_description(self, numeric_value):
        return self.ownmony_dict.get(numeric_value, np.nan) 
 
    def get_congmony_description(self, numeric_value):
        return self.congmony_dict.get(numeric_value, np.nan) 
 
    def get_assess_description(self, numeric_value):
        return self.assess_dict.get(numeric_value, np.nan) 

    def get_marriage_description(self, numeric_value):
        return self.marriage_dict.get(numeric_value, np.nan) 

    def get_womengrp_description(self, numeric_value):
        return self.womengrp_dict.get(numeric_value, np.nan) 

    def get_mengrp_description(self, numeric_value):
        return self.mengrp_dict.get(numeric_value, np.nan) 

    def get_exercise_description(self, numeric_value):
        return self.exercise_dict.get(numeric_value, np.nan)  

    def get_lgbt_description(self, numeric_value):
        return self.lgbt_dict.get(numeric_value, np.nan) 
    
    
    # Replace Numeric Values
    
    def replace_numeric_values(self, df):
        df['DENOM'] = df['DENOM'].apply(self.get_denom_description)
        df['CHANGE'] = df['CHANGE'].apply(self.get_change_description)
        df['BLDGTYPE'] = df['BLDGTYPE'].apply(self.get_bldgtype_description)
        df['VIEWBLDG'] = df['VIEWBLDG'].apply(self.get_viewbldg_description)
        df['REMODEL'] = df['REMODEL'].apply(self.get_remodel_description)
        df['HOMESCHL'] = df['HOMESCHL'].apply(self.get_homeschl_description)
        df['HAVESCHL'] = df['HAVESCHL'].apply(self.get_haveschl_description)
        df['USEBLDG'] = df['USEBLDG'].apply(self.get_usebldg_description)
        df['PERMPURP'] = df['PERMPURP'].apply(self.get_permpurp_description)
        df['SINGING'] = df['SINGING'].apply(self.get_singing_description)
        df['CHOIR'] = df['CHOIR'].apply(self.get_choir_description)
        df['PIANO'] = df['PIANO'].apply(self.get_piano_description)
        df['ORGAN'] = df['ORGAN'].apply(self.get_organ_description)
        df['DRUMS'] = df['DRUMS'].apply(self.get_drums_description)
        df['ELECGTR'] = df['ELECGTR'].apply(self.get_elecgtr_description)
        df['GUITAR'] = df['GUITAR'].apply(self.get_guitar_description)
        df['SERMON'] = df['SERMON'].apply(self.get_sermon_description)
        df['SPKRDWN'] = df['SPKRDWN'].apply(self.get_spkrdwn_description)
        df['GREET'] = df['GREET'].apply(self.get_greet_description)
        df['KIDTIME'] = df['KIDTIME'].apply(self.get_kidtime_description)
        df['TEENPART'] = df['TEENPART'].apply(self.get_teenpart_description)
        df['ROBE'] = df['ROBE'].apply(self.get_robe_description)
        df['LAUGH'] = df['LAUGH'].apply(self.get_laugh_description)
        df['PROGRAM'] = df['PROGRAM'].apply(self.get_program_description)
        df['OVERHEAD'] = df['OVERHEAD'].apply(self.get_overhead_description)
        df['STREAMED'] = df['STREAMED'].apply(self.get_streamed_description)
        df['SMTPHONE'] = df['SMTPHONE'].apply(self.get_smtphone_description)
        df['CONGREAD'] = df['CONGREAD'].apply(self.get_congread_description)
        df['OFFERING'] = df['OFFERING'].apply(self.get_offering_description)
        df['CLSYACS'] = df['CLSYACS'].apply(self.get_clsyacs_description)
        df['CLSADLT'] = df['CLSADLT'].apply(self.get_clsadlt_description)
        df['YTHGRP'] = df['YTHGRP'].apply(self.get_ythgrp_description)
        df['TEENCHOR'] = df['TEENCHOR'].apply(self.get_teenchor_description)
        df['TEENCAMP'] = df['TEENCAMP'].apply(self.get_teencamp_description)
        df['TEENVOL'] = df['TEENVOL'].apply(self.get_teenvol_description)
        df['POLITICS'] = df['POLITICS'].apply(self.get_politics_description)
        df['DISBIBLE'] = df['DISBIBLE'].apply(self.get_disbible_description)
        df['BOOKS'] = df['BOOKS'].apply(self.get_books_description)
        df['PARENTS'] = df['PARENTS'].apply(self.get_parents_description)
        df['VOTERREG'] = df['VOTERREG'].apply(self.get_voterreg_description)
        df['SCIENCE'] = df['SCIENCE'].apply(self.get_science_description)
        df['ENVIRON'] = df['ENVIRON'].apply(self.get_environ_description)
        df['ORGVOLS'] = df['ORGVOLS'].apply(self.get_orgvols_description)
        df['WORKPROB'] = df['WORKPROB'].apply(self.get_workprob_description)
        df['NEWMEMS'] = df['NEWMEMS'].apply(self.get_newmems_description)
        df['TRAIN'] = df['TRAIN'].apply(self.get_train_description)
        df['RACEREL'] = df['RACEREL'].apply(self.get_racerel_description)
        df['OTHTRAD'] = df['OTHTRAD'].apply(self.get_othtrad_description)
        df['OWNMONY'] = df['OWNMONY'].apply(self.get_ownmony_description)
        df['CONGMONY'] = df['CONGMONY'].apply(self.get_congmony_description)
        df['ASSESS'] = df['ASSESS'].apply(self.get_assess_description)
        df['MARRIAGE'] = df['MARRIAGE'].apply(self.get_marriage_description)
        df['WOMENGRP'] = df['WOMENGRP'].apply(self.get_womengrp_description)
        df['MENGRP'] = df['MENGRP'].apply(self.get_mengrp_description)
        df['EXERCISE'] = df['EXERCISE'].apply(self.get_exercise_description)
        df['LGBT'] = df['LGBT'].apply(self.get_lgbt_description)
        
        return df
        
# Example usage:
# Create an instance of the DictionaryCollection class
#dict_collection = DictionaryCollection()

# Get description for numeric value from the 'POS1' column
#numeric_value = 1  
#description = dict_collection.get_pos1_description(numeric_value)
#print(description)
