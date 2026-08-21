from flask import Flask,request, jsonify

app = Flask(__name__)

task_list = []


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
    return jsonify(task_list),200


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_list[task_id]
    return jsonify({'id':task_id,
                    'task':task,
                    'message':'Tarefa encontrada com sucesso!'}),200


@app.route('/tasks/search', methods=['GET'])
def search_task():
    title = request.args.get('title')
    return jsonify({'title':title,
                    'message': 'Tarefa encontrada com sucesso!'}),200

            


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    task = {
         'id': len(task_list) + 1,
         'title': data.get('title')
    }

    task_list.append(task)
    return jsonify(task),201



@app.route('/tasks/<int:task_id>', methods=['PUT'])
def atualizar_task(task_id):
    data = request.json

    for task in task_list:
            if task['id'] == task_id:
                task['title'] = data.get('title', task['title'])

                return jsonify({
                    'id':task_id,
                    'task':task,
                    'message':'tarefa atualizada com sucesso!'
                })

    return jsonify({'message':'tarefa não encontrada!'}),404



@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def deletar_task(task_id):

    for task in task_list:
       if task['id'] == task_id:
            task_list.remove(task)
            return jsonify({
                'id':task_id,
                'message':'tarefa deletada com sucesso!'
            }),200

    return jsonify({'message':'tarefa não encontrada!'}),404 




if __name__ == '__main__':
    app.run(debug=True)