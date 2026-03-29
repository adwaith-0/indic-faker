"""Cities, districts, and villages for Indian states."""

# State abbreviation → {cities: [...], districts: [...], villages: [...]}
PLACES = {
    "DL": {
        "cities": ["New Delhi", "Delhi", "Dwarka", "Rohini", "Saket", "Lajpat Nagar", "Karol Bagh", "Connaught Place"],
        "districts": ["Central Delhi", "East Delhi", "New Delhi", "North Delhi", "South Delhi", "West Delhi", "North East Delhi", "North West Delhi", "South East Delhi", "South West Delhi", "Shahdara"],
        "villages": ["Alipur", "Bakhtawarpur", "Nangli Poona", "Pooth Khurd", "Qutabgarh", "Tikri Khurd"],
        "landmarks": ["Near India Gate", "Opposite Red Fort", "Behind Qutub Minar", "Near Lotus Temple", "Beside Metro Station"],
        "building_formats": ["{} Block, {}", "Plot No. {}", "House No. {}", "Flat No. {}, {} Apartments"],
    },
    "UP": {
        "cities": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Allahabad", "Meerut", "Noida", "Ghaziabad", "Bareilly", "Aligarh", "Gorakhpur", "Moradabad"],
        "districts": ["Lucknow", "Kanpur Nagar", "Agra", "Varanasi", "Prayagraj", "Meerut", "Gautam Buddha Nagar", "Ghaziabad", "Bareilly", "Aligarh", "Gorakhpur", "Moradabad", "Mathura", "Jhansi"],
        "villages": ["Bithoor", "Sarnath", "Chunar", "Fatehpur Sikri", "Mahoba", "Dalmau", "Lakhimpur", "Misrikh", "Barabanki", "Mohanlalganj"],
        "landmarks": ["Near Charbagh Station", "Opposite GPO", "Behind Collectorate", "Near Bus Stand", "Beside Tahsil Office"],
        "building_formats": ["{}/{}", "House No. {}", "Mohalla {}, H.No. {}", "Gali No. {}, House {}"],
    },
    "KL": {
        "cities": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kollam", "Palakkad", "Alappuzha", "Kannur", "Kottayam", "Malappuram"],
        "districts": ["Thiruvananthapuram", "Kollam", "Pathanamthitta", "Alappuzha", "Kottayam", "Idukki", "Ernakulam", "Thrissur", "Palakkad", "Malappuram", "Kozhikode", "Wayanad", "Kannur", "Kasaragod"],
        "villages": ["Punalur", "Adoor", "Thodupuzha", "Muvattupuzha", "Perumbavoor", "Chalakudy", "Ottapalam", "Tirur", "Thalassery", "Payyanur", "Nedumangad", "Attingal", "Varkala", "Kayamkulam"],
        "landmarks": ["Near Temple", "Near Church", "Near Mosque", "Opposite Panchayat Office", "Near Junction", "Behind Bus Stand", "Near KSRTC Bus Station"],
        "building_formats": ["TC {}/{}", "{}/{}, Ward {}", "House No. {}", "Door No. {}"],
    },
    "TN": {
        "cities": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Erode", "Vellore", "Thoothukudi", "Thanjavur", "Dindigul", "Karur"],
        "districts": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Erode", "Vellore", "Thoothukudi", "Thanjavur", "Dindigul", "Karur", "Kanchipuram", "Cuddalore", "Nagapattinam"],
        "villages": ["Mamallapuram", "Kumbakonam", "Srirangam", "Pollachi", "Palani", "Nagercoil", "Rajapalayam", "Sivakasi", "Karaikudi", "Arakkonam", "Tiruvannamalai", "Chidambaram"],
        "landmarks": ["Near Bus Stand", "Opposite Temple", "Near Railway Station", "Behind Collectorate", "Near Market"],
        "building_formats": ["No. {}", "Plot No. {}", "Door No. {}/{}", "Old No. {}, New No. {}", "{}, {} Street"],
    },
    "MH": {
        "cities": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane", "Navi Mumbai", "Solapur", "Kolhapur", "Sangli", "Amravati"],
        "districts": ["Mumbai City", "Mumbai Suburban", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane", "Solapur", "Kolhapur", "Sangli", "Amravati", "Satara", "Ratnagiri", "Sindhudurg"],
        "villages": ["Lonavala", "Mahabaleshwar", "Alibaug", "Matheran", "Panchgani", "Shirdi", "Wai", "Phaltan", "Karad", "Pandharpur"],
        "landmarks": ["Near Mandir", "Opposite Station", "Near Highway", "Behind Hospital", "Near Chowk"],
        "building_formats": ["Flat No. {}, {} Society", "Room No. {}", "CTS No. {}", "Plot No. {}, Sector {}"],
    },
    "KA": {
        "cities": ["Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi", "Kalaburagi", "Davanagere", "Ballari", "Shivamogga", "Tumakuru"],
        "districts": ["Bengaluru Urban", "Bengaluru Rural", "Mysuru", "Dakshina Kannada", "Belagavi", "Kalaburagi", "Davanagere", "Ballari", "Shivamogga", "Tumakuru", "Raichur", "Hassan", "Udupi", "Chitradurga"],
        "villages": ["Srirangapatna", "Nanjangud", "Channapatna", "Ramanagara", "Mandya", "Hoskote", "Devanahalli", "Chintamani", "Kolar", "Mulbagal"],
        "landmarks": ["Near Circle", "Opposite Bus Stand", "Near Masjid", "Behind Park", "Near Lake"],
        "building_formats": ["No. {}", "#{}, {} Cross, {} Main", "Plot No. {}", "Door No. {}"],
    },
    "WB": {
        "cities": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Bardhaman", "Malda", "Haldia", "Kharagpur", "Baharampur"],
        "districts": ["Kolkata", "Howrah", "North 24 Parganas", "South 24 Parganas", "Hooghly", "Nadia", "Purba Bardhaman", "Paschim Bardhaman", "Murshidabad", "Birbhum", "Darjeeling", "Jalpaiguri", "Malda"],
        "villages": ["Shantiniketan", "Nabadwip", "Tarakeswar", "Bishnupur", "Mayapur", "Kalna", "Pandua", "Goghat", "Contai", "Jhargram"],
        "landmarks": ["Near Bazar", "Opposite School", "Near More", "Behind Thana", "Near Mandir"],
        "building_formats": ["{}/{} Lane", "House No. {}", "Flat {}, Block {}", "Plot {}"],
    },
    "TS": {
        "cities": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam", "Ramagundam", "Mahbubnagar", "Nalgonda", "Secunderabad"],
        "districts": ["Hyderabad", "Rangareddy", "Medchal-Malkajgiri", "Warangal Urban", "Karimnagar", "Nizamabad", "Khammam", "Nalgonda", "Mahbubnagar", "Sangareddy"],
        "villages": ["Shadnagar", "Vikarabad", "Zaheerabad", "Medak", "Siddipet", "Jangaon", "Bhongir", "Suryapet", "Kodad", "Miryalaguda"],
        "landmarks": ["Near Chowrasta", "Opposite Masjid", "Near Temple", "Behind Bus Depot", "Near Kaman"],
        "building_formats": ["H.No. {}-{}-{}", "Plot No. {}", "Door No. {}", "Flat No. {}, {} Colony"],
    },
    "GJ": {
        "cities": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar", "Anand", "Bharuch"],
        "districts": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar", "Anand", "Bharuch", "Mehsana", "Patan", "Kutch", "Banaskantha"],
        "villages": ["Lothal", "Dholavira", "Mandvi", "Dandi", "Palitana", "Saputara", "Modhera", "Patan", "Polo Vistar", "Ambaji"],
        "landmarks": ["Near Chowk", "Opposite Pol", "Near Darwaja", "Behind Mandir", "Near Bazaar"],
        "building_formats": ["{}, {} Society", "Plot No. {}", "Bungalow No. {}", "Block {}, Flat {}"],
    },
    "RJ": {
        "cities": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner", "Ajmer", "Alwar", "Bharatpur", "Sikar", "Bhilwara"],
        "districts": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner", "Ajmer", "Alwar", "Bharatpur", "Sikar", "Bhilwara", "Chittorgarh", "Pali", "Jaisalmer", "Tonk"],
        "villages": ["Pushkar", "Ranakpur", "Bundi", "Jhunjhunu", "Mandawa", "Neemrana", "Shekhawati", "Narlai", "Samode", "Dundlod"],
        "landmarks": ["Near Haveli", "Opposite Fort", "Near Pol", "Behind Mandir", "Near Bazaar"],
        "building_formats": ["House No. {}", "Plot No. {}", "Ward No. {}, Gali No. {}", "{}, {} Nagar"],
    },
}

# Street name patterns
STREET_NAMES = [
    "MG Road", "Station Road", "Gandhi Road", "Nehru Road", "Main Road",
    "Temple Street", "Church Street", "Market Road", "College Road", "Hospital Road",
    "Ring Road", "By-pass Road", "NH Road", "Cross Road", "Link Road",
    "Bazaar Road", "Trunk Road", "Old Road", "New Road", "Beach Road",
]

# Landmarks
GENERIC_LANDMARKS = [
    "Near Post Office", "Opposite Police Station", "Near School",
    "Behind City Hospital", "Near Railway Station", "Opposite Bus Stand",
    "Near Market", "Behind Town Hall", "Near Park", "Opposite Bank",
    "Near Temple", "Behind Masjid", "Near Church", "Opposite Stadium",
    "Near Petrol Pump", "Behind Govt. Office", "Near Water Tank",
]
