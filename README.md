## cdn-university-api
Web API for [eINFO](http://www.electronicinfo.ca/programs/), Canadian university program data.

### Setup

- Clone repo, install requirements.
  
  ```sh
  $ git clone https://github.com/kshvmdn/cdn-university-api.git && cd cdn-university-api
  ```
  
  ```sh
  $ pip install -r ./requirements.txt
  ```

- Run app, should be listening at `localhost:8000`.

  ```sh
  $ python ./api.py
  ```

### Usage

#### Output format 

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

#### Endpoints

- Use the eINFO program ID (from the URL, see below) to retrive data for that program.

  ```
  http://www.electronicinfo.ca/programs/203/ -> http://localhost:8000/api/203
  ```
