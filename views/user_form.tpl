% rebase('layout.tpl', title=title)

<h1>{{ title }}</h1>

<form action="{{ action }}" method="post">
    <div class="mb-3">
        <label for="name" class="form-label">Nome Completo:</label>
        <input type="text" class="form-control" id="name" name="name" value="{{ user.get_name() if user else '' }}" required>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input type="email" class="form-control" id="email" name="email" value="{{ user.get_email() if user else '' }}" required>
    </div>
    <div class="mb-3">
        <label for="birthdate" class="form-label">Data de Nascimento:</label>
        <input type="date" class="form-control" id="birthdate" name="birthdate" value="{{ user.get_birthdate() if user else '' }}">
    </div>
    
    <div class="form-actions">
        <button type="submit" class="btn btn-success">Salvar</button>
        <a href="/users" class="btn btn-secondary">Cancelar</a>
    </div>
</form>