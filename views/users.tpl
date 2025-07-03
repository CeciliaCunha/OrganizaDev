% rebase('layout.tpl', title=title)
<h1>{{ title }}</h1>
<table class="table table-striped">
    <thead>
        <tr><th>ID</th><th>Nome</th><th>Email</th><th>Data de Nascimento</th></tr>
    </thead>
    <tbody>
        % for user in users:
        <tr>
            <td>{{ user.get_id() }}</td>
            <td>{{ user.get_name() }}</td>
            <td>{{ user.get_email() }}</td>
            <td>{{ user.get_birthdate() }}</td>
        </tr>
        % end
    </tbody>
</table>