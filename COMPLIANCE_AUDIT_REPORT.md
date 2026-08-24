# Compliance Audit Report
Generated: August 24, 2026
Scope: Read-only legal, regulatory, and compliance audit of the `Lawyer-Directory` codebase including frontend Astro pages, components, layout templates, utility scripts, configuration files, and legal policies (`src/pages/*`, `src/components/*`, `src/layouts/*`, `src/utils/*`, `scripts/*`, `README.md`).

## Summary
- **Total findings:** 16
- **Critical:** 0 | **High:** 6 | **Medium:** 7 | **Low/Ambiguous:** 3

---

## Findings by Category

### 1. ENTITY / CLINICAL BOUNDARY VIOLATIONS (CPOM)

#### CPOM — Unclarified Contingency Fee Disclosures & Expense Liability
- **File:** `src/pages/index.astro`
- **Line(s):** 65–69 (and FAQ Schema lines 65–69)
- **Excerpt:**
  > `"Most personal injury attorneys work on a contingency fee basis - no upfront cost. They are paid only if you win, typically 33–40% of the settlement or court award."`
- **Guideline violated:** Category 1 (Fee-splitting / outcome-contingent compensation disclosures) & Category 4 (UPL)
- **Why it's a violation:** Mentions percentage-of-recovery fee structures ("33–40% of the settlement or court award") without the required state bar disclaimers clarifying that clients may remain responsible for court costs and case expenses regardless of legal outcome (e.g., Florida Bar Rule 4-1.5(f)).
- **Severity:** Medium
- **Ambiguous?** Yes — While this describes standard industry practice, public legal directory copy mentioning specific contingency fee percentages must disclose cost allocation to avoid misleading consumers.

---

### 2. FDA / SOFTWARE-AS-MEDICAL-DEVICE (SaMD) BOUNDARY

*No issues found.* (The application operates strictly as an attorney directory and contains no clinical software, diagnostic tools, or SaMD features.)

---

### 3. HIPAA / PRIVACY / PHI HANDLING

#### Privacy — Unencrypted Contact Intake Form Handling Potential Health/Injury Details Without Confidentiality / PHI Disclaimers
- **File:** `src/pages/contact.astro`
- **Line(s):** 52–54, 102–134
- **Excerpt:**
  > `"Whether you're looking for an attorney, have a directory question, or want to list your practice - we'll get back to you within 1 business day."`
  > `<form id="contact-form" class="space-y-5">`
- **Guideline violated:** Category 3 (HIPAA / Privacy / PHI Handling)
- **Why it's a violation:** Solicits injury-related user inquiries ("Whether you're looking for an attorney...") via a standard unencrypted web form without displaying a confidentiality warning, zero-PHI notice, or disclaimer that submitting information does not create an attorney-client relationship or guarantee HIPAA protection.
- **Severity:** High
- **Ambiguous?** No.

---

### 4. UNAUTHORIZED PRACTICE OF LAW (UPL) / LEGAL CLAIMS

#### UPL — Direct Assessment of Entitlement Regarding Insurance Settlement Offers
- **File:** `src/pages/when-to-hire-a-personal-injury-attorney.astro`
- **Line(s):** 136–137
- **Excerpt:**
  > `"Initial offers are almost always lower than what you are entitled to - often significantly so."`
- **Guideline violated:** Category 4 (UPL / Legal Claims & Case Valuation) & Category 11 (General Red-Flag Language)
- **Why it's a violation:** States a definitive legal conclusion regarding legal entitlement ("lower than what you are entitled to") for unrepresented users without an attorney evaluation step. Non-lawyer entities cannot evaluate legal entitlement or deliver case valuation opinions.
- **Severity:** High
- **Ambiguous?** No.

#### UPL — False Active Verification Status for Unverified Attorneys in Texas Template
- **File:** `src/pages/personal-injury-attorneys/texas/[city]/[attorney].astro`
- **Line(s):** 101–106
- **Excerpt:**
  > ```astro
  > <span class="inline-flex items-center gap-1 bg-green-50 text-green-700 text-xs font-semibold px-2.5 py-1 rounded-full border border-green-200">
  >   <svg ...></svg>
  >   Licensed Attorney
  > </span>
  > ```
- **Guideline violated:** Category 4 (UPL / Credential Representation) & Category 5 (FTC Advertising Claims)
- **Why it's a violation:** In the Texas attorney profile page, if `attorney.status` is missing/null, the component automatically falls back to rendering a green "Licensed Attorney" active status badge. Sourcing public records and falsely presenting unverified attorney entries as confirmed "Licensed Attorney" status misleads consumers and misrepresents bar standing.
- **Severity:** High
- **Ambiguous?** No.

---

### 5. FTC / MARKETING / ADVERTISING CLAIMS

#### FTC — Absolute & Unsubstantiated Service Performance Claim ("Handle Everything")
- **File:** `src/pages/index.astro`
- **Line(s):** 144
- **Excerpt:**
  > `"They handle everything - evidence gathering, insurance negotiations, and court litigation - so you can focus entirely on recovery while they fight for your compensation."`
- **Guideline violated:** Category 5 (FTC / Marketing / Advertising Claims - Absolute Claims) & Category 11 (Red-Flag Language)
- **Why it's a violation:** Uses absolute language ("handle everything") describing attorney services. Promising total coverage of all legal/factual needs is an unsubstantiated absolute performance claim under FTC rules (16 C.F.R. § 255) and state lawyer advertising rules.
- **Severity:** High
- **Ambiguous?** No.

#### FTC — Unsubstantiated Comparative Performance Claim ("Research Consistently Shows...")
- **File:** `src/pages/personal-injury-attorneys/index.astro`
- **Line(s):** 107
- **Excerpt:**
  > `"Research consistently shows that accident victims with legal representation receive significantly higher settlements than those who negotiate alone"`
- **Guideline violated:** Category 5 (FTC / Marketing Claims - Unsubstantiated Empirical Claims)
- **Why it's a violation:** Asserts empirical research findings ("Research consistently shows...") regarding higher settlement outcomes without providing reference, study citation, or qualification required by FTC advertising guidelines.
- **Severity:** High
- **Ambiguous?** No.

#### FTC — Contradictory & Inaccurate Geographical State Coverage Copy
- **File:** `src/pages/index.astro`
- **Line(s):** 87, 109, 115, 253
- **Excerpt:**
  > Line 87: `"Browse licensed personal injury attorneys across the United States. Currently covering Florida - expanding nationwide."`  
  > Line 109: `"Nationwide PI Attorney Directory - Active in Florida, New Jersey & Texas"`  
  > Line 115: `"Currently covering 54 cities across Florida, New Jersey, and Texas - expanding to all 50 states."`  
  > Line 253: `"Currently covering Florida - with all 50 states coming."`
- **Guideline violated:** Category 5 (FTC / Misleading Service Scope)
- **Why it's a violation:** Contains conflicting statements on the homepage regarding active directory coverage (claiming FL-only in lines 87 & 253, but FL, NJ & TX in lines 109 & 115). Contradictory claims regarding service availability violate FTC truth-in-advertising principles.
- **Severity:** Medium
- **Ambiguous?** No.

#### FTC — Outdated State Coverage Scope in Privacy Policy
- **File:** `src/pages/privacy-policy.astro`
- **Line(s):** 49, 96
- **Excerpt:**
  > Line 49: `"FindPIAttorney.com ... is an independent online directory of personal injury attorneys licensed to practice in Florida and New Jersey."`  
  > Line 96: `"...maintained by state bar associations, including The Florida Bar and the New Jersey State Bar."`
- **Guideline violated:** Category 5 (FTC / Accurate Disclosure Obligations)
- **Why it's a violation:** The Privacy Policy explicitly limits its defined scope to Florida and New Jersey, omitting Texas. Texas attorney records and users are live on the site, making the legal privacy disclosures incomplete and inaccurate.
- **Severity:** Medium
- **Ambiguous?** No.

#### FTC — Outdated State Coverage Scope in Terms of Service
- **File:** `src/pages/terms-of-service.astro`
- **Line(s):** 59
- **Excerpt:**
  > `"Our current coverage includes Florida and New Jersey, with expansion to additional states ongoing."`
- **Guideline violated:** Category 5 (FTC / Accurate Disclosure Obligations)
- **Why it's a violation:** The Terms of Service state that active coverage is restricted to FL and NJ. Because TX is active in the codebase and live data, the scope representation in the governing contract is inaccurate.
- **Severity:** Medium
- **Ambiguous?** No.

#### FTC — Outdated State Coverage Scope in Advertising Disclosure
- **File:** `src/pages/advertising-disclosure.astro`
- **Line(s):** 49, 61–62
- **Excerpt:**
  > Line 49: `"...listing personal injury attorneys licensed in Florida and New Jersey."`  
  > Lines 61–62: `"The Florida Bar ... The New Jersey State Bar Association..."`
- **Guideline violated:** Category 5 (FTC / Accurate Disclosure Obligations)
- **Why it's a violation:** The Advertising Disclosure omits Texas State Bar regulatory references and Texas listing coverage despite live Texas directory pages and listings.
- **Severity:** Medium
- **Ambiguous?** No.

#### FTC — Omission of Texas in Contact Page Information Card
- **File:** `src/pages/contact.astro`
- **Line(s):** 91
- **Excerpt:**
  > `"Coverage: Florida & New Jersey"`
- **Guideline violated:** Category 5 (FTC / Misleading Marketing Claims)
- **Why it's a violation:** Displays a coverage badge stating "Florida & New Jersey", omitting Texas which is live in the directory.
- **Severity:** Low
- **Ambiguous?** No.

---

### 6. DSHEA / SUPPLEMENT & DEVICE CLAIMS

*No issues found.* (The application contains no dietary supplement, health device, or OTC product content.)

---

### 7. TCPA / CAN-SPAM / DIRECT COMMUNICATIONS

#### TCPA — Absence of Explicit Opt-in Consent Capture & Privacy Terms Link on Contact Form
- **File:** `src/pages/contact.astro`
- **Line(s):** 102–134
- **Excerpt:**
  > ```html
  > <form id="contact-form" class="space-y-5">
  >   ...
  >   <button type="submit" ...> Send Message </button>
  > </form>
  > ```
- **Guideline violated:** Category 7 (TCPA / Direct Communications Consent Capture)
- **Why it's a violation:** The form collects user contact information (email, name) and triggers direct email communications without an explicit opt-in checkbox, legal consent language, or direct link to Privacy Policy/Terms near the submission button.
- **Severity:** High
- **Ambiguous?** No.

---

### 8. AI GOVERNANCE / LABELING / TRANSPARENCY

#### AI Governance — Unsubstantiated "Expert Advice" Claim on Educational Content Placeholder
- **File:** `src/pages/index.astro`
- **Line(s):** 265–266
- **Excerpt:**
  > `<h2 class="...">Legal Guides & Video Resources</h2>`  
  > `<p class="...">Expert advice, case studies, and what to expect when hiring a personal injury attorney.</p>`
- **Guideline violated:** Category 8 (AI Governance / Transparency) & Category 5 (FTC Marketing Claims)
- **Why it's a violation:** Promotes upcoming content as "Expert advice" without identifying qualified human authors/attorneys or establishing an expert/AI review disclosure framework.
- **Severity:** Low
- **Ambiguous?** Yes — The section is currently a placeholder ("Video Library Coming Soon"), but the surrounding published copy promises "Expert advice".

---

### 9. EVIDENCE INTEGRITY / PROVENANCE

#### Evidence Integrity — Silent Fallback City Assignment & Data Transformation in Data Ingestion Pipeline
- **File:** `scripts/import.py`
- **Line(s):** 256, 368–373, 447–453
- **Excerpt:**
  > ```python
  > fallback_city = "Newark" if default_state == "NJ" else ("Houston" if default_state == "TX" else "Miami")
  > description = f"Personal injury attorney at {firm}" if firm else f"Personal injury attorney in {city}, {state_display}"
  > ```
- **Guideline violated:** Category 9 (Evidence Integrity / Provenance)
- **Why it's a violation:** When raw attorney address records lack a recognizable city, the import script automatically assigns default fallback cities ("Newark", "Houston", "Miami") and synthesizes attorney descriptions without flagging the data as inferred or transformed. Publishing incorrect location data for licensed professionals compromises data provenance.
- **Severity:** Medium
- **Ambiguous?** Yes — Data ingestion fallbacks are standard in ETL pipelines, but assigning inaccurate physical office locations to attorneys on public legal directory profiles risks misrepresentation.

---

### 10. INSURANCE / CLAIMS-USE LANGUAGE

*No issues found.* (The application contains no insurance adjudication, automated claims evaluation, or coverage determination logic.)

---

### 11. GENERAL PROHIBITED / RED-FLAG LANGUAGE

#### Red-Flag Language — Outcome Guarantees & Unqualified Contingency Claims
- **File:** `src/pages/index.astro`
- **Line(s):** 292
- **Excerpt:**
  > `"They are paid only when you win, typically 33–40% of the settlement or verdict."`
- **Guideline violated:** Category 11 (General Prohibited / Red-Flag Language - Certainty Language) & Category 4 (UPL)
- **Why it's a violation:** Uses outcome-contingent phrasing ("only when you win") in a prominent FAQ block without an explicit disclaimer that past results do not guarantee future outcomes.
- **Severity:** Medium
- **Ambiguous?** Yes — While standard descriptive copy for contingency fee models, state bar advertising rules strictly regulate outcome-related phrasing in lawyer directory environments.

---

## Ambiguous / Borderline Cases

1. **`src/pages/index.astro` (Lines 65–69 & 292) — Contingency Fee Descriptions:**
   - *Issue:* Explains that attorneys are paid "33–40% of the settlement or verdict" and "only if you win".
   - *Uncertainty:* As an informational directory (rather than a law firm advertising its own services), explaining general industry fee structures is informative. However, state bar rules (such as Florida Bar Rule 4-1.5(f)) require specific statements regarding client liability for costs when contingency fees are discussed publicly.

2. **`scripts/import.py` (Lines 256) — Synthetic Location Fallbacks:**
   - *Issue:* Ingests Excel/CSV data and assigns fallback cities (e.g. "Miami" or "Houston") when addresses are unparseable.
   - *Uncertainty:* ETL script behavior is internal, but the resulting output directly populates public `attorneys.json` profiles with potentially inaccurate city associations. Legal review should determine if unverified location records should be omitted or flagged as "Location Unverified".

3. **`README.md` (Line 14) vs Profile Pages (`[attorney].astro`) — Profile Contact Field Documentation Discrepancy:**
   - *Issue:* `README.md` states profiles contain "contact details", whereas state profile templates explicitly suppress phone, email, and street address.
   - *Uncertainty:* Internal developer documentation inconsistency. Included for completeness under code comment/documentation audit guidelines.

---

## Coverage Notes

- **Fully Scanned:**
  - All Astro pages (`src/pages/*.astro` and all state/city/attorney routes).
  - All UI components (`Header.astro`, `Footer.astro`, `AttorneyCard.astro`, `USAMapSVG.astro`, etc.).
  - All legal documents (`privacy-policy.astro`, `terms-of-service.astro`, `advertising-disclosure.astro`).
  - All helper utilities and data schemas (`src/utils/attorneys.ts`, `src/types/attorney.ts`).
  - Data import and avatar generation scripts (`scripts/import.py`, `scripts/generate-avatars.js`).
  - Project documentation (`README.md`, `package.json`).

- **Gaps / Scope Limits:**
  - `src/data/attorneys.json` contains 1,000+ auto-generated records. Individual attorney names/firms in `attorneys.json` were audited via structural sampling and import script logic rather than reading all 1,000+ JSON entries manually.
