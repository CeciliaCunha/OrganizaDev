% rebase('layout.tpl', title=title)

<div class="d-flex justify-content-between align-items-center mb-3">
    <h1>{{ title }}</h1>
    <a href="/projects" class="btn btn-outline-secondary">Voltar para Projetos</a>
</div>

<hr>

<h4>Adicionar Nova Tarefa</h4>
<form action="/projects/{{ project.get_id() }}/tasks" method="post" class="mb-5">
    <div class="mb-3">
        <label for="title" class="form-label">Título da Tarefa:</label>
        <input type="text" class="form-control" id="title" name="title" required>
    </div>
    <div class="mb-3">
        <label for="description" class="form-label">Descrição:</label>
        <textarea class="form-control" id="description" name="description" rows="2"></textarea>
    </div>
    <div class="row">
        <div class="col-md-6 mb-3">
            <label for="priority" class="form-label">Prioridade:</label>
            <select class="form-select" id="priority" name="priority" required>
                <option value="Baixa">Baixa</option>
                <option value="Média">Média</option>
                <option value="Alta">Alta</option>
            </select>
        </div>
        <div class="col-md-6 mb-3">
            <label for="due_date" class="form-label">Data de Prazo:</label>
            <input type="date" class="form-control" id="due_date" name="due_date">
        </div>
    </div>
    <button type="submit" class="btn btn-success">Adicionar Tarefa</button>
</form>

<h4>Tarefas Atuais</h4>
% if not tasks:
<div class="alert alert-info">Nenhuma tarefa cadastrada para este projeto ainda.</div>
% else:
<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Status</th>
            <th>Prioridade</th>
            <th>Prazo</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        % for task in tasks:
        <tr>
            <td>{{ task.get_id() }}</td>
            <td>{{ task.get_title() }}</td>
            <td>{{ task.get_status() }}</td>
            <td>{{ task.get_priority() }}</td>
            <td>{{ task.get_due_date() }}</td>
            <td>
                <a href="/tasks/edit/{{ task.get_id() }}" class="btn btn-sm btn-info">Editar</a>

                <form action="/tasks/delete/{{ task.get_id() }}" method="post" class="d-inline">
                    <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Tem certeza?');">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    </tbody>
</table>
% end