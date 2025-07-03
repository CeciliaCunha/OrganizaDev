% rebase('layout.tpl', title=title)

<h1>{{ title }}</h1>

<form action="{{ action }}" method="post">
    <div class="mb-3">
        <label for="title" class="form-label">Título da Tarefa:</label>
        <input type="text" class="form-control" id="title" name="title" value="{{ task.get_title() }}" required>
    </div>
    <div class="mb-3">
        <label for="description" class="form-label">Descrição:</label>
        <textarea class="form-control" id="description" name="description" rows="3">{{ task.get_description() }}</textarea>
    </div>
    <div class="row">
        <div class="col-md-4 mb-3">
            <label for="priority" class="form-label">Prioridade:</label>
            <select class="form-select" id="priority" name="priority" required>
                <option value="Baixa" % if task.get_priority() == 'Baixa': selected % end>Baixa</option>
                <option value="Média" % if task.get_priority() == 'Média': selected % end>Média</option>
                <option value="Alta" % if task.get_priority() == 'Alta': selected % end>Alta</option>
            </select>
        </div>
        <div class="col-md-4 mb-3">
            <label for="status" class="form-label">Status:</label>
            <select class="form-select" id="status" name="status" required>
                <option value="Pendente" % if task.get_status() == 'Pendente': selected % end>Pendente</option>
                <option value="Em Progresso" % if task.get_status() == 'Em Progresso': selected % end>Em Progresso</option>
                <option value="Concluído" % if task.get_status() == 'Concluído': selected % end>Concluído</option>
            </select>
        </div>
        <div class="col-md-4 mb-3">
            <label for="due_date" class="form-label">Data de Prazo:</label>
            <input type="date" class="form-control" id="due_date" name="due_date" value="{{ task.get_due_date() }}">
        </div>
    </div>

    <button type="submit" class="btn btn-primary">Salvar Alterações</button>
    <a href="/projects/{{ task.get_project_id() }}/tasks" class="btn btn-secondary">Cancelar</a>
</form>