class DictionaryCollection:
    def __init__(self):
        self.pos1_dict = {
            1: 'Primary Congregational Leader',
            2: 'General Congregational Leader',
            3: 'Music',
            4: 'Education',
            5: 'Youth and Young Adults',
            6: 'Adult/Family/Outreach',
            7: 'Sick/Bereaved', 
            8: 'Missions',
            9: 'blank',
            10: 'Administration',
            11: 'Lay Leader',
            12: 'Building/Grounds Caretaking',
            13: 'Other',
            14: 'Multiple Roles' 
            # Add more mappings as needed
        }
        
        self.region_dict = {
            1: 'New England or Mid-Atlantic',
            2: 'East North Central or West North Central',
            3: 'South Atlantic, East South Central, or West South Central',
            4: 'Mountain or Pacific' 
            # Add more mappings as needed
        }
        
        self.haveden_dict = {
            1: 'Yes',
            2: 'No'
            # Add more mappings as needed
        }
        
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
        
        self.dencode_dict = {
            1: 'Roman Catholic',
            2: 'Southern Baptist Convention',
            3: 'Black Baptist',
            4: 'American Black Convention',
            5: 'Other Baptist',
            6: 'United Methodist Church',
            7: 'Black Methodist', 
            8: 'Other Methodist',
            9: 'Evangelical Lutheran Church in America',
            10: 'Lutheran Church - Missouri Synod',
            11: 'Other Lutheran',
            12: 'Presbyterian Church (USA)',
            13: 'Other Presbyterian',
            14: 'Assemblies of God',
            15: 'Other Pentecostal',
            16: 'Church of God in Christ',
            17: 'Disciples of Christ',
            18: 'Episcopal Church',
            19: 'United Church of Christ',
            20: 'Reformed Church in America',
            21: 'Church of the Brethren',
            22: 'Jehovah\'s Witness',
            23: 'Mennonite',
            24: 'Church of the Nazarene',
            25: 'Seventh-day Adventist',
            26: 'Unitarian Universalist Association', 
            27: 'Eastern Orthodox',
            28: 'Church/Churches of Christ',
            29: 'Various Church of God',
            30: 'Church of Jesus Christ of Latter-day Saints',
            31: 'Jewish',
            32: 'Non-Christian/non-Jewish',
            33: 'blank',
            34: 'blank',
            35: 'blank',
            36: 'Christian and Missionary Alliance',
            37: 'Other Mainline/Liberal',
            38: 'Other Conservative/Evangelical',
            39: 'Other Christian, not elsewhere classified'
        }
        
        self.dencode3_dict = {
            1: 'Roman Catholic',
            2: 'Baptist',
            3: 'blank',
            4: 'blank',
            5: 'blank',
            6: 'Methodist',
            7: 'blank', 
            8: 'blank',
            9: 'Lutheran',
            10: 'blank',
            11: 'blank',
            12: 'Presbyterian or Reformed',
            13: 'blank',
            14: 'Pentecostal',
            15: 'blank',
            16: 'blank',
            17: 'Other mainline or liberal Protestants',
            18: 'Episcopal Church',
            19: 'blank',
            20: 'blank',
            21: 'blank',
            22: 'Other conservative, evangelical, or sectarian Protestants',
            23: 'Other Christian, not elsewhere classified',
            24: 'Non-Christian'
        } 
        
        self.trad3_dict = {
            1: 'Roman Catholic',
            2: 'White conservative, evangelical, or fundamentalist',
            3: 'Black Protestant',
            4: 'White liberal or moderate',
            5: 'blank',
            6: 'Non-Christian'
        }        
        
        self.localaff_dict = {
            1: 'Yes',
            2: 'No'
        }  
        
        self.bldgtype_dict = {
            1: 'School',
            7: 'Storefront',
            20: 'Church, Synagogue, Temple, or Mosque',
            21: 'Other'
        }

        self.viewbldg_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.ownbldg_dict = {
            1: 'Belongs to congregation or denomination',
            2: 'Belongs to another group'
        }
        
        self.remodel_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.conguse_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.congimm_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.improve_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.multisite_1_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.samebldg_18_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.multisite_2_dict = {
            1: 'Yes',
            2: 'No'
        }

    #    self.nmlocate_12_dict = {
    #        1: 'Yes',
    #        2: 'No'
    #    }

    #    self.nmlocate_18_dict = {
    #        1: 'Yes',
    #        2: 'No'
    #    }

        self.branch_12_dict = {
            1: 'Yes',
            2: 'No'
        }
        
        self.branch_18_dict = {
            1: 'Yes',
            2: 'No',
            3: 'Unknown'
        }

        self.branchmain_12_dict = {
            1: 'Satellite/Branch',
            2: 'Main Location'
        }

        self.branchmain_18_dict = {
            1: 'Satellite/Branch',
            2: 'Main Location'
        }
 
        self.sameser_12_dict = {
            1: 'Yes',
            2: 'No'
        }       

        self.sameser_18_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.samemus_12_dict = {
            1: 'Yes',
            2: 'No'
        }
        
        self.samemus_18_dict = {
            1: 'Yes',
            2: 'No',
            3: 'Unknown'
        }
        
        self.adltchg_dict = {
            1: 'Increased',
            2: 'Remained about the same',
            3: 'Decreased'
        }
        
        self.change_dict = {
            1: 'Decreased > 10%',
            2: 'Decreased < 10%',
            3: 'Remained about the same',
            4: 'Increased < 10%',
            5: 'Increased > 10%'
        }

        self.clergone_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.leadsit_dict = {
            1: 'No Leader',
            2: 'Co-Leaders',
            3: 'Other Situation'
        }
        
    #    self.leadsit_dict = {
    #        1: 'Yes',
    #        2: 'No'
    #    }

        self.ldrsrch_dict = {
            1: 'Yes',
            2: 'No'
        }
        
        self.cldrmar_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.clergsex_dict = {
            1: 'Male',
            2: 'Female'
        }
        
        self.clerrace_dict = {
            1: 'White',
            2: 'Black or African American',
            3: 'Hispanic',
            4: 'Asian or Pacific Islander',
            5: 'Other'
        }
        
        self.clerhisp_dict = {
            1: 'Yes',
            2: 'No'
        }

        self.clerrace_dict = {
            -9: 'Unknown',
            1: 'White and non-Hispanic',
            2: 'White Hispanic',
            3: 'Black and non-Hispanic',
            4: 'Black Hispanic',
            5: 'Hispanic',
            6: 'Asian and non-Hispanic',
            7: 'Asian Hispanic',
            8: 'Other'
        }
        
        self.clerorig_dict = {
            1: 'Mexican American/Chicano',
            2: 'Mexican',
            3: 'Puerto Rican',
            5: 'Cuban',
            6: 'Dominican',
            7: 'Colombian',
            9: 'Central American, Other',
            10: 'South American, Other',
            11: 'Other'
        }
        
        self.change_dict = {
            1: 'Decreased more than 10 percent',
            2: 'Decreased less than 10 percent',
            3: 'Remained about the same',
            4: 'Increased less than 10 percent',
            5: 'Increased more than 10 percent',
        }
                
        # Add more dictionaries as needed

    def get_pos1_description(self, numeric_value):
        return self.pos1_dict.get(numeric_value, 'Unknown')

    def get_denom_description(self, numeric_value):
        return self.denom_dict.get(numeric_value, 'Unknown')
    
    def get_change_description(self, numeric_value):
        return self.change_dict.get(numeric_value, 'Unknown')
    
# Example usage:
# Create an instance of the DictionaryCollection class
#dict_collection = DictionaryCollection()

# Get description for numeric value from the 'POS1' column
#numeric_value = 1  
#description = dict_collection.get_pos1_description(numeric_value)
#print(description)