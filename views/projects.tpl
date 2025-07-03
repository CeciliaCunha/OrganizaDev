% rebase('layout.tpl', title=title)
<h1>{{ title }}</h1>
<p><a href="/projects/add" class="btn btn-primary">Adicionar Novo Projeto</a></p>
% if not projects:
<div class="alert alert-info">Nenhum projeto cadastrado ainda.</div>
% else:
<table class="table table-hover">
    <thead>
        <tr>
            <th>ID</th><th>Nome</th><th>Status</th><th>Data de Início</th><th>Prazo</th><th>Ações</th>
        </tr>
    </thead>
    <tbody>
        % for project in projects:
        <tr>
            <td>{{ project.get_id() }}</td>
            <td>{{ project.get_name() }}</td>
            <td>{{ project.get_status() }}</td>
            <td>{{ project.get_start_date() }}</td>
            <td>{{ project.get_due_date() }}</td>
            <td>
                <a href="/projects/{{ project.get_id() }}/tasks" class="btn btn-sm btn-success">Tarefas</a>
                
                <a href="/projects/edit/{{ project.get_id() }}" class="btn btn-sm btn-secondary">Editar</a>
                <form action="/projects/delete/{{ project.get_id() }}" method="post" class="d-inline">
                    <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Tem certeza? Isso deletará também todas as tarefas associadas.');">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    </tbody>
</table>
% end