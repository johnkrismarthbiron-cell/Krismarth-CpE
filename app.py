from flask import Flask, render_template, request

app = Flask(__name__)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def values(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def total(self):
        return sum(self.values())


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/works/linked-list', methods=['GET', 'POST'])
def linked_list_calculator():
    values = None
    result = None
    error = None
    input_values = ''

    if request.method == 'POST':
        input_values = request.form.get('values', '').strip()
        try:
            numbers = [float(value.strip()) for value in input_values.split(',') if value.strip()]
            if not numbers:
                raise ValueError

            linked_list = LinkedList()
            for number in numbers:
                linked_list.append(number)
            values = list(linked_list.values())
            result = linked_list.total()
        except ValueError:
            error = 'Enter one or more numbers separated by commas.'

    return render_template(
        'linked_list.html',
        values=values,
        result=result,
        error=error,
        input_values=input_values,
    )


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = int(radius)*3.14*int(radius)
    return render_template('circle.html', result=result)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def triangle_area():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        if base and height:
            result = 0.5 * float(base) * float(height)
    return render_template('triangle.html', result=result)

# @app.route('/areaOfcirle', methods=['GET', 'POST'])
# def areaOfcirle():
#     result = None
#     name=request.get('name','')
#     print(name)
#     if request.method == 'POST':
#         input_string = request.form.get('inputradius', '')
#         result = int(input_string) * int(input_string) * 3.14
#     return render_template('areaCircle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
