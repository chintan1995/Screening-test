# Screening-test
There are two folders in this repo, each corresponsing to the respective coding problems.<br>
1. SpokenWrittenCoding_1<br>
2. ObjectOrientedCoding_2<br>

## 1. SpokenWrittenCoding_1
Here the file with name FlaskAPI.py is where the REST API is created. The SpokenToWritten.py consists of the conversion logic. Following rules are considered for conversion,<br>
replace numbers in words,<br>
replace currency,<br>
replace tuples (double, triple, quadruple, etc.),<br>
replace weight (kilogram, grams, etc.),<br>
replace abbreviation (eg: H T M L, A M, P M, C M, etc.)<br>
<br>
To run the program, <br>
i). You first have to run the server by running the FlaskAPI.py (it will be a local host).<br>
ii). Then you can pass the input string using the following url, http://127.0.0.1:5000/spokentowritten/<input_str><br>
      where the <input_str> should have your own input string which is the spoken english text that you want to convert. This input can also contain spaces.<br>
iii). The output is a json which has the input as well as the converted output.<br>
<br>
## 2. ObjectOrientedCoding_2
You can run this using terminal with Main.py<br>
Follow the onscreen menu choices and prompts.
