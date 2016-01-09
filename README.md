# eINFO Scraper
RESTful API for Canadian post-secondary data from [eINFO](http://www.electronicinfo.ca/programs/).

### Prerequisites
Python 3

### Usage
Fork/clone and navigate to project. Install requirements with `pip3 install -r requirements.txt`. Run with `python 3 einfo.py`. 

Open `127.0.0.1:8000` in your browser. Access the API endpoint with the eINFO program code encoded as query parameter. Find the eINFO program code at the end of your URL. 

```
http://www.electronicinfo.ca/programs/203/ -> 127.0.0.1:8000/api?c=203
```

### Output format 
```js
{
  "data": {
    "admission": {
      "basic_requirements_for_admission": [String],
      "failed_and_repeated_courses_and_courses_other_than_day_school": [String],
      "timing_and_process_for_admission_decisions": [String]
    },
    "overview": {
      "degree": String,
      "enrollment": String,
      "experiential_learning": String,
      "grade_range": String,
      "instruction_language": String,
      "notes": String,
      "ouac_program_code": String,
      "title": String,
      "university": String
    },
    "requirements": {
      "prerequisites": [String]
    }
  },
  "meta": {
    "message": String,
    "status": Number
  }
}
```
