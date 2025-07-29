from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory task list
tasks = []

HTML_TEMPLATE = """
<!doctype html>
<title>Task Manager</title>
<h1>Task Manager</h1>
<form method="POST" action="/add">
  <input name="task" placeholder="Enter a task" required>
  <input type="submit" value="Add Task">
</form>
<h2>Tasks:</h2>
<ul>
{% for t in tasks %}
  <li>{{ t }}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

