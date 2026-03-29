"""Job & salary provider — Indian job market data."""

import random as _random


# All job titles (for standalone job_title() calls)
JOB_TITLES = [
    # IT / Software
    "Software Engineer", "Senior Software Engineer", "Staff Software Engineer",
    "Tech Lead", "Engineering Manager", "Principal Engineer",
    "Full Stack Developer", "Backend Developer", "Frontend Developer",
    "DevOps Engineer", "SRE", "Cloud Architect",
    "Data Scientist", "Data Engineer", "ML Engineer",
    "Data Analyst", "Business Analyst", "Product Analyst",
    "QA Engineer", "SDET", "Automation Engineer",
    "Product Manager", "Technical Program Manager", "Scrum Master",
    "UI/UX Designer", "Product Designer", "UX Researcher",
    "Mobile Developer (Android)", "Mobile Developer (iOS)", "Flutter Developer",
    "Solution Architect", "Enterprise Architect", "CTO",
    # Non-IT
    "Chartered Accountant", "Company Secretary", "Tax Consultant",
    "Civil Engineer", "Mechanical Engineer", "Electrical Engineer",
    "Doctor", "Surgeon", "Pharmacist",
    "Bank Manager", "Loan Officer", "Financial Advisor",
    "Teacher", "Professor", "Lecturer",
    "Government Officer (IAS)", "Government Officer (IPS)", "Sub-Inspector",
    "Advocate", "Legal Counsel", "Judicial Magistrate",
    "Marketing Manager", "Sales Executive", "HR Manager",
    "Content Writer", "Journalist", "Copy Editor",
]

# Direct degree → compatible job titles (no loose domain mapping)
DEGREE_JOB_MAP = {
    "MBBS": [
        "Doctor", "Surgeon", "Medical Officer",
    ],
    "BDS": [
        "Dentist", "Doctor",
    ],
    "MD": [
        "Doctor", "Surgeon", "Medical Officer",
        "Radiologist", "Pathologist",
    ],
    "MS": [
        "Surgeon", "Doctor", "Medical Officer",
    ],
    "D.M.": [
        "Surgeon", "Doctor", "Medical Officer",
    ],
    "B.Pharm": [
        "Pharmacist", "Medical Officer",
    ],
    "B.Tech": [
        "Software Engineer", "Senior Software Engineer", "Full Stack Developer",
        "Backend Developer", "Frontend Developer", "DevOps Engineer",
        "Data Engineer", "ML Engineer", "QA Engineer", "SDET",
        "Mobile Developer (Android)", "Mobile Developer (iOS)", "Flutter Developer",
        "Cloud Architect", "Civil Engineer", "Mechanical Engineer", "Electrical Engineer",
        "Data Analyst", "Product Analyst",
    ],
    "B.E.": [
        "Software Engineer", "Senior Software Engineer", "Full Stack Developer",
        "Backend Developer", "Frontend Developer", "DevOps Engineer",
        "Data Engineer", "QA Engineer", "SDET",
        "Civil Engineer", "Mechanical Engineer", "Electrical Engineer",
        "Data Analyst",
    ],
    "M.Tech": [
        "Senior Software Engineer", "Staff Software Engineer", "Tech Lead",
        "ML Engineer", "Data Scientist", "Data Engineer",
        "Cloud Architect", "Solution Architect", "Principal Engineer",
        "Research Scientist",
    ],
    "M.E.": [
        "Senior Software Engineer", "Staff Software Engineer", "Tech Lead",
        "ML Engineer", "Data Engineer", "Solution Architect",
    ],
    "B.Sc": [
        "Data Analyst", "Business Analyst", "QA Engineer",
        "Teacher", "Lecturer", "Research Associate",
        "Lab Technician",
    ],
    "M.Sc": [
        "Data Scientist", "Data Analyst", "Research Scientist",
        "Lecturer", "Professor", "Research Associate",
    ],
    "B.Com": [
        "Chartered Accountant", "Tax Consultant", "Financial Advisor",
        "Bank Manager", "Loan Officer", "Business Analyst",
        "Sales Executive",
    ],
    "M.Com": [
        "Chartered Accountant", "Tax Consultant", "Financial Advisor",
        "Bank Manager", "Company Secretary", "Business Analyst",
    ],
    "B.A.": [
        "Content Writer", "Journalist", "Copy Editor",
        "Teacher", "HR Manager", "Sales Executive",
        "Marketing Manager",
    ],
    "M.A.": [
        "Content Writer", "Journalist", "Professor", "Lecturer",
        "HR Manager", "UX Researcher",
    ],
    "BBA": [
        "Marketing Manager", "Sales Executive", "HR Manager",
        "Business Analyst", "Financial Advisor", "Bank Manager",
    ],
    "BCA": [
        "Software Engineer", "Full Stack Developer", "Frontend Developer",
        "QA Engineer", "Data Analyst", "Mobile Developer (Android)",
    ],
    "MCA": [
        "Software Engineer", "Senior Software Engineer", "Backend Developer",
        "Full Stack Developer", "Data Engineer", "DevOps Engineer",
    ],
    "MBA": [
        "Product Manager", "Marketing Manager", "HR Manager",
        "Business Analyst", "Financial Advisor", "Bank Manager",
        "Sales Executive", "Technical Program Manager", "Scrum Master",
        "Engineering Manager",
    ],
    "B.Arch": [
        "Architect", "Civil Engineer", "Urban Planner",
    ],
    "M.Arch": [
        "Architect", "Urban Planner", "Civil Engineer",
    ],
    "LL.B": [
        "Advocate", "Legal Counsel", "Judicial Magistrate",
        "Company Secretary",
    ],
    "B.Ed": [
        "Teacher", "Lecturer", "Professor",
    ],
    "M.Phil": [
        "Professor", "Lecturer", "Research Scientist",
        "Research Associate",
    ],
    "Ph.D": [
        "Professor", "Research Scientist", "Data Scientist",
        "Principal Engineer",
    ],
}

DEPARTMENTS = [
    "Engineering", "Product", "Design", "Data Science",
    "Finance", "Human Resources", "Marketing", "Sales",
    "Operations", "Legal", "Customer Support", "Quality Assurance",
    "Research & Development", "Supply Chain", "Administration",
]

COMPANIES = [
    # IT Services
    "TCS", "Infosys", "Wipro", "HCL Technologies", "Tech Mahindra",
    "Cognizant", "L&T Infotech", "Mindtree", "Mphasis", "Persistent Systems",
    # Product Companies
    "Google India", "Microsoft India", "Amazon India", "Flipkart",
    "Razorpay", "Zerodha", "PhonePe", "Paytm", "Zomato", "Swiggy",
    "CRED", "Meesho", "Ola", "Freshworks", "Postman",
    # Corporates
    "Tata Motors", "Reliance Industries", "HDFC Bank", "ICICI Bank",
    "SBI", "Bajaj Finance", "Mahindra & Mahindra", "Asian Paints",
    "Hindustan Unilever", "ITC Limited",
]

# Salary ranges in LPA — user-specified realistic Indian bands
SALARY_BANDS = {
    "fresher": (3.5, 8),
    "junior": (6, 15),
    "mid": (12, 25),
    "senior": (20, 45),
    "lead": (35, 70),
    "director": (60, 120),
    "vp": (100, 200),
    "cxo": (150, 400),
}

# Weight distribution — most people are mid/senior, very few are CXO
SALARY_LEVEL_WEIGHTS = {
    "fresher": 15,
    "junior": 20,
    "mid": 25,
    "senior": 20,
    "lead": 10,
    "director": 5,
    "vp": 3,
    "cxo": 2,
}

# Map job titles to salary bands (so a Flutter Developer gets fresher-senior, not CXO)
JOB_TITLE_BANDS = {
    # IC roles: fresher → senior
    "Software Engineer": ["fresher", "junior", "mid"],
    "Senior Software Engineer": ["mid", "senior"],
    "Staff Software Engineer": ["senior", "lead"],
    "Full Stack Developer": ["fresher", "junior", "mid"],
    "Backend Developer": ["fresher", "junior", "mid"],
    "Frontend Developer": ["fresher", "junior", "mid"],
    "Flutter Developer": ["fresher", "junior", "mid"],
    "Mobile Developer (Android)": ["fresher", "junior", "mid"],
    "Mobile Developer (iOS)": ["fresher", "junior", "mid"],
    "DevOps Engineer": ["junior", "mid", "senior"],
    "SRE": ["mid", "senior"],
    "QA Engineer": ["fresher", "junior", "mid"],
    "SDET": ["junior", "mid", "senior"],
    "Data Analyst": ["fresher", "junior", "mid"],
    "Business Analyst": ["junior", "mid", "senior"],
    "Product Analyst": ["junior", "mid"],
    "Data Scientist": ["mid", "senior", "lead"],
    "Data Engineer": ["junior", "mid", "senior"],
    "ML Engineer": ["mid", "senior", "lead"],
    "Research Scientist": ["mid", "senior", "lead"],
    # Leadership
    "Tech Lead": ["senior", "lead"],
    "Principal Engineer": ["lead", "director"],
    "Cloud Architect": ["senior", "lead"],
    "Solution Architect": ["senior", "lead", "director"],
    "Enterprise Architect": ["lead", "director"],
    "Engineering Manager": ["lead", "director"],
    "Product Manager": ["mid", "senior", "lead"],
    "Technical Program Manager": ["senior", "lead"],
    "Scrum Master": ["mid", "senior"],
    "CTO": ["director", "vp", "cxo"],
    "CEO": ["vp", "cxo"],
    "CFO": ["director", "vp", "cxo"],
    "VP Engineering": ["vp"],
    "VP Product": ["vp"],
    "Director of Engineering": ["director"],
    "General Manager": ["director", "vp"],
    # Design
    "UI/UX Designer": ["junior", "mid", "senior"],
    "Product Designer": ["mid", "senior"],
    "Graphic Designer": ["fresher", "junior", "mid"],
    "UX Researcher": ["mid", "senior"],
    # Non-IT
    "Chartered Accountant": ["junior", "mid", "senior"],
    "Company Secretary": ["mid", "senior"],
    "Tax Consultant": ["mid", "senior"],
    "Civil Engineer": ["fresher", "junior", "mid", "senior"],
    "Mechanical Engineer": ["fresher", "junior", "mid", "senior"],
    "Electrical Engineer": ["fresher", "junior", "mid", "senior"],
    "Doctor": ["mid", "senior", "lead"],
    "Surgeon": ["senior", "lead", "director"],
    "Medical Officer": ["junior", "mid", "senior"],
    "Radiologist": ["senior", "lead"],
    "Pathologist": ["senior", "lead"],
    "Dentist": ["mid", "senior"],
    "Pharmacist": ["fresher", "junior", "mid"],
    "Bank Manager": ["mid", "senior"],
    "Loan Officer": ["junior", "mid"],
    "Financial Advisor": ["mid", "senior"],
    "Teacher": ["fresher", "junior", "mid"],
    "Professor": ["mid", "senior", "lead"],
    "Lecturer": ["junior", "mid", "senior"],
    "Research Associate": ["fresher", "junior", "mid"],
    "Government Officer (IAS)": ["senior", "lead", "director"],
    "Government Officer (IPS)": ["senior", "lead", "director"],
    "Sub-Inspector": ["junior", "mid"],
    "Advocate": ["junior", "mid", "senior", "lead"],
    "Legal Counsel": ["mid", "senior", "lead"],
    "Judicial Magistrate": ["senior", "lead", "director"],
    "Marketing Manager": ["mid", "senior"],
    "Sales Executive": ["fresher", "junior", "mid"],
    "HR Manager": ["mid", "senior"],
    "Content Writer": ["fresher", "junior", "mid"],
    "Journalist": ["junior", "mid", "senior"],
    "Copy Editor": ["junior", "mid"],
    "Operations Manager": ["mid", "senior"],
    "Architect": ["mid", "senior", "lead"],
    "Urban Planner": ["mid", "senior"],
    "Lab Technician": ["fresher", "junior"],
}

EXPERIENCE_LEVELS = [
    "Fresher", "Junior", "Mid-Level", "Senior",
    "Lead", "Principal", "Director", "VP",
]


class JobProvider:
    """Generates realistic Indian job and salary data."""

    def __init__(self, random_instance=None):
        self.random = random_instance or _random.Random()

    def job_title(self):
        """Generate an Indian job title."""
        return self.random.choice(JOB_TITLES)

    def job_title_for_degree(self, degree):
        """Generate a job title that's coherent with the given degree."""
        titles = DEGREE_JOB_MAP.get(degree)
        if titles:
            return self.random.choice(titles)
        # Fallback for unknown degrees
        return self.random.choice(JOB_TITLES)

    def salary_for_job(self, job_title):
        """Generate a salary appropriate for the given job title."""
        bands = JOB_TITLE_BANDS.get(job_title)
        if bands:
            level = self.random.choice(bands)
        else:
            level = self._pick_weighted_level()
        return self.salary_lpa(level=level)

    def department(self):
        """Generate a department name."""
        return self.random.choice(DEPARTMENTS)

    def employer(self):
        """Generate an Indian employer name."""
        return self.random.choice(COMPANIES)

    def experience_level(self):
        """Generate an experience level."""
        return self.random.choice(EXPERIENCE_LEVELS)

    def _pick_weighted_level(self):
        """Pick a salary level with realistic distribution."""
        levels = list(SALARY_LEVEL_WEIGHTS.keys())
        weights = list(SALARY_LEVEL_WEIGHTS.values())
        return self.random.choices(levels, weights=weights, k=1)[0]

    def salary_lpa(self, level=None):
        """
        Generate a salary in LPA (Lakhs Per Annum) format.

        Args:
            level: Experience level key (fresher/junior/mid/senior/lead/director/vp/cxo).
                   Weighted random if not specified.

        Returns: String like "₹12.5 LPA"
        """
        if level is None:
            level = self._pick_weighted_level()

        min_sal, max_sal = SALARY_BANDS.get(level, (3.5, 45))
        salary = round(self.random.uniform(min_sal, max_sal), 1)
        return f"₹{salary} LPA"

    def salary_monthly(self, level=None):
        """
        Generate a monthly salary in INR.

        Returns: String like "₹1,04,167" (monthly equivalent of LPA)
        """
        if level is None:
            level = self._pick_weighted_level()

        min_sal, max_sal = SALARY_BANDS.get(level, (3.5, 45))
        annual = self.random.uniform(min_sal, max_sal) * 100000
        monthly = annual / 12

        from .finance import FinanceProvider
        return FinanceProvider._format_inr(round(monthly, 0))

    def job_record(self):
        """
        Generate a complete job record.

        Returns dict with title, employer, department, level, salary.
        """
        title = self.job_title()
        return {
            "title": title,
            "employer": self.employer(),
            "department": self.department(),
            "experience": self.experience_level(),
            "salary_lpa": self.salary_for_job(title),
            "years_experience": self.random.randint(0, 25),
        }
