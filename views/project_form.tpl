% rebase('layout.tpl', title=title)
<h1>{{ title }}</h1>
<form action="{{ action }}" method="post">
    <div class="mb-3">
        <label for="name" class="form-label">Nome do Projeto:</label>
        <input type="text" class="form-control" id="name" name="name" value="{{ project.get_name() if project else '' }}" required>
    </div>
    <div class="mb-3">
        <label for="description" class="form-label">Descrição:</label>
        <textarea class="form-control" id="description" name="description" rows="3">{{ project.get_description() if project else '' }}</textarea>
    </div>
    <div class="row">
        <div class="col-md-6 mb-3">
            <label for="start_date" class="form-label">Data de Início:</label>
            <input type="date" class="form-control" id="start_date" name="start_date" value="{{ project.get_start_date() if project else '' }}" required>
        </div>
        <div class="col-md-6 mb-3">
            <label for="due_date" class="form-label">Data de Prazo:</label>
            <input type="date" class="form-control" id="due_date" name="due_date" value="{{ project.get_due_date() if project else '' }}">
        </div>
    </div>
    <div class="mb-3">
        <label for="status" class="form-label">Status:</label>
        <select class="form-select" id="status" name="status" required>
            <option value="Pendente" % if project and project.get_status() == 'Pendente': selected % end>Pendente</option>
            <option value="Em Progresso" % if project and project.get_status() == 'Em Progresso': selected % end>Em Progresso</option>
            <option value="Concluido" % if project and project.get_status() == 'Concluído': selected % end>Concluído</option>
        </select>
    </div>
    <button type="submit" class="btn btn-success">Salvar</button>
    <a href="/projects" class="btn btn-link">Cancelar</a>
</form>