import PyPDF2
text = ""

with open(".venv/Sumanth S__U06PE23S0016.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:          # loops through ALL pages
        page_text = page.extract_text()
        if page_text:                  # safety check
            text += page_text.lower()

job_des=["opps in java","python","css","javascript","flutter"]
result=[]

for resume in job_des:
    if resume in text:
       result.append(resume)
print(result)

percentage= len(result)/len(job_des)*100
if percentage>=60:
   print(f"Candidate Pass his percentage is {percentage}%")
else:
    print(f"Candidate Fail his percentage is {percentage}%")
    