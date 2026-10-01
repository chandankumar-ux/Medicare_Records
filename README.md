# MediCare Patient Records Manager — Student Starter

**The business problem:** MediCare Clinic's reception exports a weekly
`patients_raw.csv`. It is messy — bad ages, missing fees, duplicate rows,
inconsistent names. The clinic needs the data validated, stored cleanly,
and summarised into revenue reports. Your program is the solution.

## Project structure

```
medicare-records-starter/
    .venv/                  <- you create this (see setup guide)
    main.py                 <- COMPLETE, read it first, do not edit
    requirements.txt        <- pip install -r requirements.txt
    data/patients_raw.csv   <- the messy input (do not fix by hand!)
    reports/                <- your program creates this folder
    clinic/                 <- the package YOU complete
        __init__.py
        validators.py       <- TODOs 1-4  (functions + exceptions)
        models.py           <- TODOs 5-9  (Patient class)
        storage.py          <- TODOs 10-12 (CSV in, JSON out)
```

## Setup (once)

1. Open this folder in VS Code (File > Open Folder).
2. Create and activate a virtual environment, then install requirements —
   full commands are in the setup guide.
3. Select the `.venv` interpreter in VS Code (bottom-right corner).

## Suggested order of work

1. **validators.py** (TODOs 1–4). Test each function in the terminal:
   `python -c "from clinic.validators import clean_name; print(clean_name('  priya sharma '))"`
2. **models.py** (TODOs 5–9). Self-test: `python -m clinic.models`
3. **storage.py** (TODOs 10–12).
4. Run the whole program: `python main.py`

## Definition of done

- [ ] `python main.py` runs without crashing
- [ ] The table shows exactly **7 valid patients**
- [ ] Exactly **3 rejected rows**, each with a clear reason
      (bad age, missing fee, duplicate id)
- [ ] Total revenue printed: **INR 7,130.75**
- [ ] `reports/patients_clean.json` and `reports/summary.json` exist
      and open as valid JSON
- [ ] Setting a negative fee (`p.consultation_fee = -5`) raises ValueError
- [ ] `python -m clinic.models` prints the self-test line;
      importing it from main.py does NOT

## Stretch goals (optional, great for your portfolio)

- Add `parse_visit_date` in validators using `datetime.strptime`,
  rejecting impossible dates.
- Add a `--department Cardiology` filter using `sys.argv`.
- Write rejected rows to `reports/rejected.csv` with a `reason` column.
- Swap `tabulate` for the `rich` library and add colour.
