# Screening-test
There are two folders in this repo, each corresponsing to the respective coding problems.
1. SpokenWrittenCoding_1
2. ObjectOrientedCoding_2

## 1. SpokenWrittenCoding_1
Here the file with name FlaskAPI.py is where the REST API is created. The SpokenToWritten.py consists of the conversion logic. Following rules are considered for conversion,
replace numbers in words,
replace currency,
replace tuples (double, triple, quadruple, etc.),
replace weight (kilogram, grams, etc.),
replace abbreviation (eg: H T M L, A M, P M, C M, etc.)
    
To run the program, 
i). You first have to run the server by running the FlaskAPI.py (it will be a local host).
ii). Then you can pass the input string using the following url, http://127.0.0.1:5000/spokentowritten/<input_str>
      where the <input_str> should have your own input string which is the spoken english text that you want to convert. This input can also contain spaces.
iii). The output is a json which has the input as well as the converted output.

## 2. ObjectOrientedCoding_2
You can run this using terminal with Main.py
Follow the onscreen menu choices and prompts.
