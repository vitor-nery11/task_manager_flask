from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

task_list = []


@tasks_bp.route('', methods=['GET'])
def tasks():
    return jsonify(task_list), 200


@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):

    for task in task_list:
        if task['id'] == task_id:
            return jsonify({
                'task': task,
                'message': 'Tarefa encontrada!'
            }), 200

    return jsonify({
        'message': 'Tarefa não encontrada!'
    }), 404


@tasks_bp.route('/search', methods=['GET'])
def search_task():

    title = request.args.get('title')

    return jsonify({
        'title': title,
        'message': 'Busca realizada!'
    }), 200


@tasks_bp.route('', methods=['POST'])
def create_task():

    data = request.json

    task = {
        'id': len(task_list) + 1,
        'title': data.get('title')
    }

    task_list.append(task)

    return jsonify(task), 201


@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def atualizar_task(task_id):

    data = request.json

    for task in task_list:
        if task['id'] == task_id:

            task['title'] = data.get(
                'title',
                task['title']
            )

            return jsonify({
                'task': task,
                'message': 'Tarefa atualizada com sucesso!'
            }), 200

    return jsonify({
        'message': 'Tarefa não encontrada!'
    }), 404


@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def deletar_task(task_id):

    for task in task_list:
        if task['id'] == task_id:

            task_list.remove(task)

            return jsonify({
                'message': 'Tarefa deletada com sucesso!'
            }), 200

    return jsonify({
        'message': 'Tarefa não encontrada!'
    }), 404