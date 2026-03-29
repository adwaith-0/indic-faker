"""Hindi (हिन्दी) name data — native + Latin transliterations."""

# Native script names (Devanagari)
MALE_FIRST_NAMES = [
    "अर्जुन", "राहुल", "विकास", "अमित", "सुनील",
    "राजेश", "मनोज", "संजय", "विजय", "अनिल",
    "प्रदीप", "सुरेश", "महेश", "रमेश", "दिनेश",
    "आशीष", "नरेन्द्र", "गौरव", "अभिषेक", "रोहित",
    "आकाश", "विवेक", "कृष्ण", "मोहन", "श्याम",
    "राम", "हरीश", "पवन", "अजय", "देवेन्द्र",
    "सचिन", "प्रशान्त", "योगेश", "निखिल", "आदित्य",
    "वरुण", "कार्तिक", "ऋषभ", "शिवम", "हिमांशु",
    "अंकित", "पंकज", "मयंक", "दीपक", "नवीन",
    "तरुण", "लोकेश", "जितेन्द्र", "उमेश", "कमलेश",
]

FEMALE_FIRST_NAMES = [
    "प्रिया", "अनिता", "सुनीता", "गीता", "रीना",
    "पूजा", "नेहा", "स्वाति", "ममता", "सरिता",
    "कविता", "रेखा", "मीना", "लता", "शोभा",
    "अंजली", "दीपिका", "श्रुति", "निधि", "रश्मि",
    "सपना", "ज्योति", "मधु", "रानी", "सीमा",
    "आरती", "रूपा", "विनीता", "शीला", "कमला",
    "पद्मा", "सरला", "उषा", "इंदु", "चंदा",
    "अनुराधा", "सुषमा", "शालिनी", "मंजू", "रजनी",
    "सोनाली", "तनुजा", "वंदना", "गरिमा", "दिव्या",
    "आयुषी", "तान्या", "इशिता", "अर्चना", "भावना",
]

LAST_NAMES = [
    "शर्मा", "वर्मा", "सिंह", "गुप्ता", "अग्रवाल",
    "जैन", "मिश्रा", "पांडे", "तिवारी", "दुबे",
    "चौधरी", "राजपूत", "यादव", "कुमार", "चौहान",
    "सक्सेना", "श्रीवास्तव", "त्रिपाठी", "दीक्षित", "बाजपेयी",
    "पाठक", "शुक्ला", "सोनी", "माहेश्वरी", "गोयल",
    "कश्यप", "भारद्वाज", "मेहता", "खन्ना", "कपूर",
    "मल्होत्रा", "अरोड़ा", "बत्रा", "सहगल", "चोपड़ा",
    "भट्ट", "नायक", "राय", "बोस", "दास",
    "ठाकुर", "नेगी", "रावत", "पंत", "जोशी",
    "उपाध्याय", "द्विवेदी", "चतुर्वेदी", "राठौर", "परमार",
]

# Latin transliterations (1:1 mapping with native lists above)
MALE_FIRST_NAMES_LATIN = [
    "Arjun", "Rahul", "Vikas", "Amit", "Sunil",
    "Rajesh", "Manoj", "Sanjay", "Vijay", "Anil",
    "Pradeep", "Suresh", "Mahesh", "Ramesh", "Dinesh",
    "Ashish", "Narendra", "Gaurav", "Abhishek", "Rohit",
    "Akash", "Vivek", "Krishna", "Mohan", "Shyam",
    "Ram", "Harish", "Pawan", "Ajay", "Devendra",
    "Sachin", "Prashant", "Yogesh", "Nikhil", "Aditya",
    "Varun", "Kartik", "Rishabh", "Shivam", "Himanshu",
    "Ankit", "Pankaj", "Mayank", "Deepak", "Naveen",
    "Tarun", "Lokesh", "Jitendra", "Umesh", "Kamlesh",
]

FEMALE_FIRST_NAMES_LATIN = [
    "Priya", "Anita", "Sunita", "Geeta", "Reena",
    "Pooja", "Neha", "Swati", "Mamta", "Sarita",
    "Kavita", "Rekha", "Meena", "Lata", "Shobha",
    "Anjali", "Deepika", "Shruti", "Nidhi", "Rashmi",
    "Sapna", "Jyoti", "Madhu", "Rani", "Seema",
    "Aarti", "Roopa", "Vineeta", "Sheela", "Kamala",
    "Padma", "Sarla", "Usha", "Indu", "Chanda",
    "Anuradha", "Sushma", "Shalini", "Manju", "Rajni",
    "Sonali", "Tanuja", "Vandana", "Garima", "Divya",
    "Ayushi", "Tanya", "Ishita", "Archana", "Bhavna",
]

LAST_NAMES_LATIN = [
    "Sharma", "Verma", "Singh", "Gupta", "Agrawal",
    "Jain", "Mishra", "Pandey", "Tiwari", "Dubey",
    "Chaudhary", "Rajput", "Yadav", "Kumar", "Chauhan",
    "Saxena", "Srivastava", "Tripathi", "Dixit", "Bajpai",
    "Pathak", "Shukla", "Soni", "Maheshwari", "Goyal",
    "Kashyap", "Bhardwaj", "Mehta", "Khanna", "Kapoor",
    "Malhotra", "Arora", "Batra", "Sahgal", "Chopra",
    "Bhatt", "Nayak", "Rai", "Bose", "Das",
    "Thakur", "Negi", "Rawat", "Pant", "Joshi",
    "Upadhyay", "Dwivedi", "Chaturvedi", "Rathore", "Parmar",
]

PREFIXES_MALE = ["श्री", "श्रीमान"]
PREFIXES_FEMALE = ["श्रीमती", "सुश्री"]
PREFIXES_MALE_LATIN = ["Shri", "Mr."]
PREFIXES_FEMALE_LATIN = ["Smt.", "Ms."]
