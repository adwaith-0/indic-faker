"""Education provider — Indian colleges, universities, degrees."""

import random as _random


# Premier institutions
IITS = [
    "IIT Bombay", "IIT Delhi", "IIT Madras", "IIT Kanpur", "IIT Kharagpur",
    "IIT Roorkee", "IIT Guwahati", "IIT Hyderabad", "IIT Indore", "IIT BHU",
    "IIT Gandhinagar", "IIT Patna", "IIT Ropar", "IIT Bhubaneswar",
    "IIT Mandi", "IIT Jodhpur", "IIT Tirupati", "IIT Palakkad",
    "IIT Dharwad", "IIT Bhilai", "IIT Goa", "IIT Jammu",
]

NITS = [
    "NIT Trichy", "NIT Surathkal", "NIT Warangal", "NIT Calicut",
    "NIT Rourkela", "NIT Allahabad", "NIT Nagpur", "NIT Jaipur",
    "NIT Kurukshetra", "NIT Durgapur", "NIT Silchar", "NIT Hamirpur",
    "NIT Srinagar", "NIT Jalandhar", "NIT Patna", "NIT Raipur",
    "NIT Agartala", "NIT Arunachal Pradesh", "NIT Goa", "NIT Meghalaya",
]

IIMS = [
    "IIM Ahmedabad", "IIM Bangalore", "IIM Calcutta", "IIM Lucknow",
    "IIM Kozhikode", "IIM Indore", "IIM Shillong", "IIM Rohtak",
    "IIM Kashipur", "IIM Trichy", "IIM Udaipur", "IIM Ranchi",
    "IIM Nagpur", "IIM Amritsar", "IIM Visakhapatnam", "IIM Bodh Gaya",
    "IIM Jammu", "IIM Sirmaur", "IIM Mumbai",
]

STATE_UNIVERSITIES = [
    "University of Mumbai", "University of Delhi", "Anna University",
    "University of Calcutta", "Savitribai Phule Pune University",
    "Osmania University", "University of Kerala", "Gujarat University",
    "University of Rajasthan", "Bangalore University",
    "Madras University", "Calicut University", "Andhra University",
    "Mysore University", "Gauhati University", "Patna University",
    "Lucknow University", "Allahabad University", "Banaras Hindu University",
    "Jawaharlal Nehru University", "Aligarh Muslim University",
    "Jamia Millia Islamia", "University of Hyderabad",
    "Pondicherry University", "Manipal Academy of Higher Education",
    "Amity University", "VIT University", "SRM University",
    "Christ University", "Symbiosis International University",
]

ENGINEERING_COLLEGES = [
    "RV College of Engineering", "BMS College of Engineering",
    "College of Engineering Trivandrum", "PSG College of Technology",
    "Jadavpur University", "BITS Pilani", "BITS Hyderabad", "BITS Goa",
    "IIIT Hyderabad", "IIIT Delhi", "IIIT Bangalore", "IIIT Allahabad",
    "DTU Delhi", "NSUT Delhi", "VJTI Mumbai", "ICT Mumbai",
    "Thiagarajar College of Engineering", "MIT Manipal",
    "Thapar University", "COEP Pune",
]

MEDICAL_COLLEGES = [
    "AIIMS Delhi", "AIIMS Bhopal", "AIIMS Jodhpur", "AIIMS Rishikesh",
    "CMC Vellore", "JIPMER Pondicherry", "Government Medical College Thiruvananthapuram",
    "Maulana Azad Medical College", "Grant Medical College Mumbai",
    "Madras Medical College", "King George's Medical University",
    "Armed Forces Medical College Pune", "St. John's Medical College Bangalore",
    "Kasturba Medical College Manipal", "KMC Mangalore",
]

DEGREES = [
    "B.Tech", "B.E.", "B.Sc", "B.Com", "B.A.",
    "BBA", "BCA", "MBBS", "BDS", "B.Arch",
    "B.Pharm", "LL.B", "B.Ed",
    "M.Tech", "M.E.", "M.Sc", "M.Com", "M.A.",
    "MBA", "MCA", "MD", "MS", "M.Arch",
    "M.Phil", "Ph.D", "D.M.",
]

ENGINEERING_BRANCHES = [
    "Computer Science", "Information Technology", "Electronics",
    "Electrical", "Mechanical", "Civil", "Chemical",
    "Aerospace", "Biotechnology", "Electronics & Communication",
    "Instrumentation", "Production", "Textile",
    "Computer Science & AI", "Data Science", "Cyber Security",
]


class EducationProvider:
    """Generates realistic Indian education data."""

    def __init__(self, random_instance=None):
        self.random = random_instance or _random.Random()

    def college(self):
        """Generate a random Indian college/university name."""
        pool = IITS + NITS + STATE_UNIVERSITIES + ENGINEERING_COLLEGES
        return self.random.choice(pool)

    def university(self):
        """Generate a university name."""
        return self.random.choice(STATE_UNIVERSITIES)

    def iit(self):
        """Generate an IIT name."""
        return self.random.choice(IITS)

    def nit(self):
        """Generate an NIT name."""
        return self.random.choice(NITS)

    def iim(self):
        """Generate an IIM name."""
        return self.random.choice(IIMS)

    def medical_college(self):
        """Generate a medical college name."""
        return self.random.choice(MEDICAL_COLLEGES)

    def degree(self):
        """Generate a degree name."""
        return self.random.choice(DEGREES)

    def engineering_branch(self):
        """Generate an engineering branch name."""
        return self.random.choice(ENGINEERING_BRANCHES)

    def education_record(self):
        """
        Generate a complete education record.
        
        Returns a dict with college, degree, branch, and year.
        """
        college = self.college()
        degree = self.random.choice(["B.Tech", "B.E.", "M.Tech", "M.E."])
        branch = self.engineering_branch()
        year = self.random.randint(2000, 2025)
        percentage = round(self.random.uniform(55.0, 98.0), 1)
        cgpa = round(self.random.uniform(5.5, 9.8), 2)

        return {
            "college": college,
            "degree": degree,
            "branch": branch,
            "graduation_year": year,
            "percentage": percentage,
            "cgpa": cgpa,
        }
