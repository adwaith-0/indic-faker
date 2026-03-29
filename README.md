<div align="center">
  <p>
    <img width="100%" src="https://raw.githubusercontent.com/adwaith-0/indic-faker/main/.github/banner.png" alt="indic-faker banner">
  </p>

  <p>
    <em>The Faker library India deserves. Generate production-quality Indian synthetic data in 8 languages.</em>
  </p>

[हिन्दी](#-8-indian-languages) | [മലയാളം](#-8-indian-languages) | [தமிழ்](#-8-indian-languages) | [తెలుగు](#-8-indian-languages) | [বাংলা](#-8-indian-languages) | [ಕನ್ನಡ](#-8-indian-languages) | [ગુજરાતી](#-8-indian-languages) | [मराठी](#-8-indian-languages)

  <div>
    <a href="https://github.com/adwaith-0/indic-faker/actions"><img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square&logo=github" alt="Build Status"></a>
    <a href="https://pypi.org/project/indic-faker/"><img src="https://img.shields.io/badge/pypi-v0.2.0-blue?style=flat-square&logo=pypi&logoColor=white" alt="PyPI Version"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.8+"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License: MIT"></a>
    <br>
    <a href="#-batch-generation-for-aiml"><img src="https://img.shields.io/badge/🤖_ML_Ready-DataFrame_Export-FF6F00?style=flat-square" alt="ML Ready"></a>
    <a href="#-8-indian-languages"><img src="https://img.shields.io/badge/🔤_Languages-8_Indic_Scripts-blueviolet?style=flat-square" alt="8 Languages"></a>
    <a href="#-id-numbers"><img src="https://img.shields.io/badge/✅_Aadhaar-Verhoeff_Valid-success?style=flat-square" alt="Verhoeff Checksum"></a>
    <a href="https://huggingface.co/datasets/adwaith06/indic-synthetic-profiles"><img src="https://img.shields.io/badge/🤗_HuggingFace-Dataset-FFD21E?style=flat-square" alt="HuggingFace Dataset"></a>
  </div>
</div>

<br>

**indic-faker** generates realistic Indian fake data — names in 8 native scripts, Aadhaar numbers with **valid Verhoeff checksums**, state-aware addresses with real pincodes, UPI IDs, salary data in LPA, company names (Pvt Ltd, LLP), IIT/NIT/IIM names, and batch export for AI/ML datasets. It's `faker`, but with **India as a first-class citizen**.

Every method that isn't India-specific (`.ipv4()`, `.text()`, `.uuid4()`) **automatically passes through** to vanilla Faker — so you only need one import.

<div align="center">

### ⚡ Why indic-faker?

</div>

| Feature | vanilla `Faker` | **`indic-faker`** |
|:--------|:---:|:---:|
| Names in 8 Indian scripts (native + Latin) | ❌ | ✅ |
| Aadhaar with Verhoeff checksum | ❌ | ✅ |
| GSTIN with valid state codes + checksum | ❌ | ✅ |
| INR formatting in lakhs/crores (₹12,34,567) | ❌ | ✅ |
| UPI IDs (@okicici, @ybl, @paytm) | ❌ | ✅ |
| Salary in LPA (₹18.5 LPA) | ❌ | ✅ |
| `profile()` — complete Indian identity | ❌ | ✅ |
| `to_dataframe(1000)` — batch for ML | ❌ | ✅ |
| `messy_address()` with "Nr.", "Opp.", old city names | ❌ | ✅ |
| IIT / NIT / IIM / medical college names | ❌ | ✅ |
| Indian company names (Pvt Ltd, LLP, HUF) | ❌ | ✅ |
| CIN, DL, Voter ID, Passport numbers | ❌ | ✅ |
| Faker pass-through (`.ipv4()` just works) | N/A | ✅ |

---

<details open>
<summary><h2>🚀 Install</h2></summary>

```bash
pip install indic-faker
```

For ML/AI dataset export (pandas DataFrame):

```bash
pip install indic-faker[ml]
```

That's it. No cloning, no setup — just install and use.

</details>

<details open>
<summary><h2>⚡ Quick Start</h2></summary>

```python
from indic_faker import IndicFaker

fake = IndicFaker(language="ml")  # Malayalam

# Names — Latin by default, native on demand
fake.name()                    # "Rajesh Krishnan"
fake.name(script="native")    # "രാജേഷ് കൃഷ്ണൻ"

# Indian ID numbers (algorithm-validated)
fake.aadhaar()                 # "3847 2918 4721"  ← Verhoeff checksum ✓
fake.pan()                     # "ABCPK1234F"
fake.gstin()                   # "32ABCPK1234F1Z5" ← Kerala state code ✓

# Contact
fake.phone()                   # "+91 94471 82931"
fake.upi_id()                  # "rajesh.krishnan@okicici"

# Money — Indian comma system (lakhs/crores, not millions)
fake.amount_inr()              # "₹4,29,150.00"
fake.salary_lpa()              # "₹12.5 LPA"

# Address — state-aware with valid pincodes
fake.address()                 # "TC 14/2341, Pettah, TVM - 695024"
fake.messy_address()           # "14/2341, Nr. Temple,Pettah, Trivandrum"

# Company & Career
fake.company_indian()          # "Sharma Technologies Pvt. Ltd."
fake.college()                 # "IIT Bombay"
fake.job_title()               # "Senior Software Engineer"

# Faker pass-through — these just work
fake.ipv4()                    # "192.168.1.1"
fake.text()                    # "Lorem ipsum..."
fake.uuid4()                   # "a1b2c3d4-..."
```

</details>

---

<details open>
<summary><h2>🔤 8 Indian Languages</h2></summary>

Every name is available in **both native script and Latin transliteration**. Default is Latin for database compatibility.

| Code | Language | Script | Example (Native) | Example (Latin) |
|:----:|:---------|:-------|:-----------------|:----------------|
| `hi` | Hindi | देवनागरी | दिनेश तिवारी | Dinesh Tiwari |
| `ml` | Malayalam | മലയാളം | രവി പണിക്കർ | Ravi Panikkar |
| `ta` | Tamil | தமிழ் | சதீஷ் சிவக்குமார் | Satheesh Sivakumar |
| `te` | Telugu | తెలుగు | నారాయణ కుమార్ | Narayana Kumar |
| `bn` | Bengali | বাংলা | রাহুল মিত্র | Rahul Mitra |
| `kn` | Kannada | ಕನ್ನಡ | ಸಂತೋಷ್ ಪಾಟೀಲ್ | Santosh Patil |
| `gu` | Gujarati | ગુજરાતી | તેજસ પંડ્યા | Tejas Pandya |
| `mr` | Marathi | मराठी | योगेश पवार | Yogesh Pawar |

```python
# Switch languages at any time
fake = IndicFaker(language="ta")
fake.name()                       # "Murugan Natarajan"
fake.name(script="native")        # "முருகன் நடராஜன்"

fake.set_language("bn")           # Switch to Bengali mid-session
fake.name(script="native")        # "সৌরভ গাঙ্গুলী"
```

</details>

<details open>
<summary><h2>👤 Profile — Complete Indian Identity</h2></summary>

Generate a **consistent, complete identity** in a single call. Every field belongs to the same person.

```python
profile = fake.profile()
```

```json
{
  "name": "Rajesh Krishnan",
  "name_native": "രാജേഷ് കൃഷ്ണൻ",
  "gender": "male",
  "dob": "15/08/1990",
  "age": 35,
  "language": "ml",
  "aadhaar": "3847 2918 4721",
  "pan": "ABCPK1234F",
  "phone": "+91 94471 82931",
  "email": "rajesh.krishnan@gmail.com",
  "address": "TC 14/2341, Pettah, TVM - 695024",
  "city": "Thiruvananthapuram",
  "state": "Kerala",
  "pincode": "695024",
  "bank_account": {"ifsc": "SBIN0001234", "account": "38291847291", "bank": "SBI"},
  "upi_id": "rajesh.krishnan@okicici",
  "employer": "Infosys",
  "job_title": "Software Engineer",
  "salary": "₹12.5 LPA",
  "college": "NIT Calicut",
  "degree": "B.Tech"
}
```

Pick specific fields only:
```python
fake.profile(fields=["name", "aadhaar", "phone", "email"])
```

</details>

<details open>
<summary><h2>📊 Batch Generation for AI/ML</h2></summary>

The **killer feature** for data scientists. Generate thousands of realistic Indian records instantly.

```python
# 🔥 Generate 1000 records as pandas DataFrame
df = fake.to_dataframe(1000)
df.to_csv("indian_test_data.csv", index=False)

# Custom fields only
df = fake.to_dataframe(500, fields=["name", "phone", "city", "salary"])

# JSON output
json_str = fake.to_json(100)

# CSV string
csv_str = fake.to_csv(100)

# Raw list of dicts
records = fake.generate_batch(100)
```

#### 👀 What `to_dataframe(5)` looks like:

<p align="center">
  <img src="https://raw.githubusercontent.com/adwaith-0/indic-faker/main/.github/dataframe_preview.svg" alt="to_dataframe() output preview" width="100%">
</p>

</details>

---

<details>
<summary><h2>🆔 ID Numbers</h2></summary>

All generated with **correct formats and validated checksums**. These pass real-world format validation.

```python
# Aadhaar — Verhoeff checksum validated (not just random 12 digits)
fake.aadhaar()                     # "3847 2918 4721"
fake.aadhaar(formatted=False)      # "384729184721"

# PAN — entity-type aware
fake.pan()                         # "ABCPK1234F" (Person)
fake.pan(entity_type="C")          # "XYZCK5678G" (Company)

# GSTIN — correct state code + modular checksum
fake.gstin()                       # "32ABCPK1234F1Z5"
fake.gstin(state="MH")             # "27..." (Maharashtra)

# Others
fake.dl_number()                   # "KL-09-2020-0012345"
fake.voter_id()                    # "ABC1234567"
fake.passport()                    # "A1234567"
```

</details>

<details>
<summary><h2>📍 Addresses</h2></summary>

State-aware with valid pincodes, building number formats, and landmarks.

```python
fake.address()             # "14/2341, MG Road, Pettah, TVM - 695024"
fake.full_address()        # "TC 14/2341, MG Road, Near Temple, Pettah, Kerala - 695024"
fake.city()                # "Thiruvananthapuram"
fake.district()            # "Ernakulam"
fake.village()             # "Punalur, Kollam District, Kerala"
fake.pincode()             # "695024" (valid for Kerala)
fake.landmark()            # "Near Government Hospital"

# 🔥 Messy address — simulates real-world Indian user input
fake.messy_address()
# "14/2341, Nr. Temple,Pettah, Trivandrum"
#  ↑ abbreviations  ↑ old city names  ↑ missing pincode
```

</details>

<details>
<summary><h2>💰 Finance</h2></summary>

```python
# INR with Indian comma system (lakhs/crores, NOT millions/billions)
fake.amount_inr()                      # "₹4,29,150.00"
fake.amount_inr(100000, 10000000)      # "₹45,82,391.20"

# Banking
fake.bank_account()  # {"ifsc": "SBIN0001234", "account": "38291847291", "bank": "SBI"}
fake.ifsc()                            # "HDFC0001234"
fake.upi_id()                          # "rajesh.k@okicici"
fake.bank_name()                       # "HDFC Bank"
fake.credit_card_indian()              # "4532 1234 5678 9012"
```

</details>

<details>
<summary><h2>🏢 Company Data</h2></summary>

```python
fake.company_indian()    # "Sharma Technologies Pvt. Ltd."
fake.company_type()      # "LLP"
fake.cin()               # "U12345MH2020PLC123456"
fake.gst_invoice()       # "INV/2024-25/001234"
```

</details>

<details>
<summary><h2>🎓 Education</h2></summary>

```python
fake.college()                  # "IIT Bombay"
fake.iit()                      # "IIT Madras"
fake.nit()                      # "NIT Trichy"
fake.iim()                      # "IIM Ahmedabad"
fake.medical_college()          # "AIIMS Delhi"
fake.university()               # "Anna University"
fake.degree()                   # "B.Tech"
fake.engineering_branch()       # "Computer Science"
fake.education_record()         # {"college": "BITS Pilani", "degree": "B.Tech", ...}
```

</details>

<details>
<summary><h2>💼 Jobs & Salary</h2></summary>

```python
fake.job_title()                   # "Senior Software Engineer"
fake.employer()                    # "Razorpay"
fake.salary_lpa()                  # "₹18.5 LPA"
fake.salary_lpa(level="fresher")   # "₹5.2 LPA"
fake.salary_lpa(level="cxo")       # "₹180.0 LPA"
fake.salary_monthly()              # "₹1,54,167"
fake.job_record()                  # {"title": ..., "employer": ..., "salary_lpa": ...}
```

Salary bands: `fresher` → `junior` → `mid` → `senior` → `lead` → `director` → `vp` → `cxo`

</details>

<details>
<summary><h2>📅 Indian Dates</h2></summary>

```python
fake.date_indian()         # "15/08/2024"  (DD/MM/YYYY, not MM/DD)
fake.date_of_birth()       # "23/11/1990"
fake.financial_year()      # "2024-25"     (Indian FY format)
```

</details>

<details>
<summary><h2>🌍 Cross-State Generation</h2></summary>

India has massive internal migration. Decouple language from geography:

```python
# Tamil name living in Delhi
fake = IndicFaker(language="ta", state="DL")
fake.name()       # "Murugan Natarajan"   ← Tamil name
fake.address()    # "H.No. 123, Dwarka, Delhi - 110075"  ← Delhi address
fake.gstin()      # "07..."               ← Delhi GST code
```

</details>

<details>
<summary><h2>🎲 Reproducibility</h2></summary>

```python
fake1 = IndicFaker(seed=42)
fake2 = IndicFaker(seed=42)

assert fake1.name() == fake2.name()       # Always True
assert fake1.aadhaar() == fake2.aadhaar() # Always True
```

</details>

---

## 📋 Complete API Reference

<details>
<summary><b>Person</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `name()` | Full name (Latin) | "Rajesh Krishnan" |
| `name(script="native")` | Full name (native) | "രാജേഷ് കൃഷ്ണൻ" |
| `name_male()` | Male name | "Arjun Sharma" |
| `name_female()` | Female name | "Priya Nair" |
| `first_name()` | Random first name | "Harish" |
| `last_name()` | Surname | "Patel" |
| `prefix()` | Honorific | "Mr." / "श्री" |

</details>

<details>
<summary><b>ID Numbers</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `aadhaar()` | Aadhaar (Verhoeff ✓) | "3847 2918 4721" |
| `pan()` | PAN number | "ABCPK1234F" |
| `gstin()` | GSTIN (checksum ✓) | "32ABCPK1234F1Z5" |
| `dl_number()` | Driving License | "KL-09-2020-0012345" |
| `voter_id()` | Voter ID | "ABC1234567" |
| `passport()` | Passport | "A1234567" |

</details>

<details>
<summary><b>Address</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `address()` | Full address | "14/2341, MG Road, TVM - 695024" |
| `messy_address()` | Messy address | "14/2341, Nr. Temple,TVM" |
| `city()` | City name | "Thiruvananthapuram" |
| `pincode()` | Valid pincode | "695024" |
| `village()` | Village + district | "Punalur, Kollam, Kerala" |
| `landmark()` | Landmark | "Near Govt Hospital" |

</details>

<details>
<summary><b>Finance</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `amount_inr()` | INR amount | "₹4,29,150.00" |
| `bank_account()` | Bank details dict | `{"ifsc": ..., "account": ..., "bank": ...}` |
| `upi_id()` | UPI ID | "rajesh.k@okicici" |
| `ifsc()` | IFSC code | "SBIN0001234" |

</details>

<details>
<summary><b>Company</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `company_indian()` | Company name | "Sharma Tech Pvt. Ltd." |
| `company_type()` | Type | "LLP" |
| `cin()` | CIN number | "U12345MH2020PLC123456" |
| `gst_invoice()` | Invoice number | "INV/2024-25/001234" |

</details>

<details>
<summary><b>Education</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `college()` | College name | "IIT Bombay" |
| `iit()` / `nit()` / `iim()` | Premier institute | "IIT Madras" |
| `degree()` | Degree | "B.Tech" |
| `education_record()` | Full record dict | `{"college": ..., "cgpa": 8.45}` |

</details>

<details>
<summary><b>Job & Salary</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `job_title()` | Job title | "Senior Software Engineer" |
| `employer()` | Employer | "Razorpay" |
| `salary_lpa()` | Salary in LPA | "₹18.5 LPA" |
| `salary_monthly()` | Monthly salary | "₹1,54,167" |
| `job_record()` | Full record dict | `{"title": ..., "salary_lpa": ...}` |

</details>

<details>
<summary><b>Batch Generation</b></summary>

| Method | Returns | Example |
|--------|---------|---------|
| `profile()` | Complete identity dict | `{"name": ..., "aadhaar": ...}` |
| `generate_batch(n)` | List of n profiles | `[{...}, {...}, ...]` |
| `to_csv(n)` | CSV string | `"name,aadhaar,...\n..."` |
| `to_json(n)` | JSON string | `'[{"name": ...}]'` |
| `to_dataframe(n)` | pandas DataFrame | `DataFrame(n rows)` |

</details>

---

## 🎯 Use Cases

Not sure what to do with `indic-faker`? Here are the things developers are building with it:

| Use Case | What You'd Generate | Why It Matters |
|:---------|:-------------------|:---------------|
| **🔍 Fraud Detection Training Data** | 100K profiles with Aadhaar, PAN, bank accounts | Train ML models to catch synthetic identity fraud, duplicate KYC submissions, and anomalous patterns — without touching real PII |
| **🤖 LLM Fine-Tuning** | Multilingual name/address pairs in 8 Indic scripts | Fine-tune models that actually understand Indian names, addresses, and ID formats instead of hallucinating Western data |
| **✅ KYC System Testing** | Aadhaar (Verhoeff ✓), PAN, GSTIN with valid checksums | Stress-test your e-KYC verification pipeline with structurally valid IDs — no compliance risk |
| **📊 Data Pipeline QA** | 10K–1M rows with messy addresses, mixed scripts | Validate ETL pipelines, UTF-8 handling, and data cleaning logic against realistic edge cases |
| **💰 Fintech Prototyping** | UPI IDs, IFSC codes, INR amounts in lakhs/crores | Populate fintech app demos with data that looks real to Indian users and investors |
| **🎓 Academic Research** | Balanced dataset across 8 languages + states | Study demographic distributions, NLP on Indic scripts, or benchmark multilingual models |
| **🧪 Load Testing** | Batch of 1M records via `to_dataframe()` | Generate arbitrarily large test datasets for database benchmarks and API load tests |

```python
# Example: Generate fraud detection training data
fake = IndicFaker(seed=42)
df = fake.to_dataframe(100_000, fields=[
    "name", "aadhaar", "pan", "phone", "address", 
    "bank_account", "upi_id", "dob", "age"
])
df.to_csv("fraud_training_data.csv", index=False)
# → 100K rows of realistic Indian KYC data, ready for ML
```

---

## 🤗 HuggingFace Dataset

Want to skip the generation step? We've published a **ready-to-use 10,000 row dataset** on HuggingFace with all 8 Indian languages equally represented:

👉 **[adwaith06/indic-synthetic-profiles on HuggingFace](https://huggingface.co/datasets/adwaith06/indic-synthetic-profiles)**

```python
# Load directly from HuggingFace
from datasets import load_dataset

dataset = load_dataset("adwaith06/indic-synthetic-profiles")
df = dataset["train"].to_pandas()

print(df.shape)  # (10000, 23)
print(df["language"].value_counts())
# hi    1250
# ml    1250
# ta    1250
# te    1250
# bn    1250
# kn    1250
# gu    1250
# mr    1250
```

The dataset includes 23 columns: name (Latin + native script), gender, DOB, age, language, Aadhaar, PAN, phone, email, full address, city, state, pincode, bank account details, UPI ID, employer, job title, salary, college, and degree.

**Need more data?** Generate your own with `pip install indic-faker[ml]` — the library can produce millions of rows in minutes.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help make indic-faker even better:

- 🔤 **Add a new language** — Create `src/indic_faker/data/names/<lang_code>.py`
- 🏘️ **Expand address data** — Add more cities/villages/districts
- 💡 **New provider ideas** — Create a provider in `src/indic_faker/providers/`
- 🐛 **Bug fixes** — Found wrong data? Open an issue or PR

```bash
# Development setup
git clone https://github.com/adwaith-0/indic-faker.git
cd indic-faker
pip install -e ".[dev]"
pytest tests/ -v
```

All 86 tests must pass before submitting a PR.

---

## 📜 License

[MIT License](LICENSE) — free for everyone, forever. Use it in personal projects, startups, enterprises, and everything in between.

---

<div align="center">
  <br>
  <p><b>Built with ❤️ for Indian developers</b></p>
  <p><em>Because AI deserves real Indian test data, not <code>"John Smith, 123 Main St"</code></em></p>
  <br>
  <a href="https://github.com/adwaith-0/indic-faker">
    <img src="https://img.shields.io/badge/⭐_Star_this_repo-If_it_helped_you!-yellow?style=for-the-badge" alt="Star this repo">
  </a>
</div>
