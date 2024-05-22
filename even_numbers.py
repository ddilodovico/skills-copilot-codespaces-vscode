# write a simple flask app that returns a list of even numbers from a list of numbers.
# create a function that takes a list of numbers and returns only the even numbers.
# create a sample list of numbers.
# create a list of even numbers from the sample list of numbers.
# return the list of even numbers as a json object.

from flask import Flask, jsonify

app = Flask(__name__)

def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_numbers(numbers)

@app.route('/')
def get_even_numbers():
    return jsonify(even_numbers)

if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Flask App
To run the flask app, execute the following command in the terminal.

```bash
$ python even_numbers.py
```

The flask app will start running on the default port 5000. Open a web browser and navigate to `http://
localhost:5000/` to view the list of even numbers.

### Output
The output of the flask app will be a JSON object containing the list of even numbers.

```json
[2, 4, 6, 8, 10]
```

## Conclusion
In this article, we have learned how to create a simple Flask app that returns a list of even numbers from a list of numbers. We have created a function that takes a list of numbers and returns only the even numbers. We have created a sample list of numbers and created a list of even numbers from the sample list of numbers. Finally, we have returned the list of even numbers as a JSON object.

## References
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Python JSON](https://docs.python.org/3/library/json.html)
- [Python List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python Flask Tutorial](https://www.tutorialspoint.com/flask/index.htm)
- [Python Flask Tutorial for Beginners](https://www.youtube.com/watch?v=Z1RJmh_OqeA)

## Summary
In this article, we have learned how to create a simple Flask app that returns a list of even numbers from a list of numbers. We have created a function that takes a list of numbers and returns only the even numbers. We have created a sample list of numbers and created a list of even numbers from the sample list of numbers. Finally, we have returned the list of even numbers as a JSON object.

## Next Steps
In the next article, we will learn how to create a simple Flask app that returns a list of odd numbers from a list of numbers. We will create a function that takes a list of numbers and returns only the odd numbers. We will create a sample list of numbers and create a list of odd numbers from the sample list of numbers. Finally, we will return the list of odd numbers as a JSON object.



