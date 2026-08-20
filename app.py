from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Task manager api'

@app.route('/about')
def about():
    return 'task manager'


@app.route('/contact')
def contact():
    return 'contact task manager'


@app.route('/tasks', methods=['GET'])
def tasks():
    return 'Lista de tarefas'

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return jsonify({'id':task_id,
                    'message':'Tarefa encontrada com sucesso!'}),200

@app.route('/tasks/search', methods=['GET'])
def search_task():
    title = request.args.get('title')
    return jsonify({'title':title,
                    'message': 'Tarefa encontrada com sucesso!'}),200

            


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    title = data.get('title')
    return jsonify({'message': f'tarefa {title} criada com sucesso!'}),201




if __name__ == '__main__':
    app.run(debug=True)