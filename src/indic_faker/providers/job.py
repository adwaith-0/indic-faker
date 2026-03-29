"""Job & salary provider — Indian job market data."""

import random as _random


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

# Salary ranges in LPA (Lakhs Per Annum) by experience
SALARY_BANDS = {
    "fresher": (3.0, 8.0),
    "junior": (5.0, 15.0),
    "mid": (10.0, 30.0),
    "senior": (20.0, 50.0),
    "lead": (30.0, 75.0),
    "director": (50.0, 120.0),
    "vp": (75.0, 200.0),
    "cxo": (100.0, 500.0),
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

    def department(self):
        """Generate a department name."""
        return self.random.choice(DEPARTMENTS)

    def employer(self):
        """Generate an Indian employer name."""
        return self.random.choice(COMPANIES)

    def experience_level(self):
        """Generate an experience level."""
        return self.random.choice(EXPERIENCE_LEVELS)

    def salary_lpa(self, level=None):
        """
        Generate a salary in LPA (Lakhs Per Annum) format.
        
        Args:
            level: Experience level key (fresher/junior/mid/senior/lead/director/vp/cxo).
                   Random if not specified.
        
        Returns: String like "₹12.5 LPA"
        """
        if level is None:
            level = self.random.choice(list(SALARY_BANDS.keys()))
        
        min_sal, max_sal = SALARY_BANDS.get(level, (3.0, 50.0))
        salary = round(self.random.uniform(min_sal, max_sal), 1)
        return f"₹{salary} LPA"

    def salary_monthly(self, level=None):
        """
        Generate a monthly salary in INR.
        
        Returns: String like "₹1,04,167" (monthly equivalent of LPA)
        """
        if level is None:
            level = self.random.choice(list(SALARY_BANDS.keys()))
        
        min_sal, max_sal = SALARY_BANDS.get(level, (3.0, 50.0))
        annual = self.random.uniform(min_sal, max_sal) * 100000  # Convert to absolute
        monthly = annual / 12
        
        # Format in Indian number system
        from .finance import FinanceProvider
        return FinanceProvider._format_inr(round(monthly, 0))

    def job_record(self):
        """
        Generate a complete job record.
        
        Returns dict with title, employer, department, level, salary.
        """
        level_key = self.random.choice(list(SALARY_BANDS.keys()))
        return {
            "title": self.job_title(),
            "employer": self.employer(),
            "department": self.department(),
            "experience": self.experience_level(),
            "salary_lpa": self.salary_lpa(level=level_key),
            "years_experience": self.random.randint(0, 25),
        }
