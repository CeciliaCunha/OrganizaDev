<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'OrganizaDev' }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <header class="p-3 mb-3 border-bottom bg-light">
        <div class="container">
            <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none me-lg-auto">
                    <strong>OrganizaDev</strong>
                </a>

                % if logged_in_user_id:
                <ul class="nav col-12 col-lg-auto me-lg-3 mb-2 justify-content-center mb-md-0">
                    <li><a href="/projects" class="nav-link px-2 text-dark">Meus Projetos</a></li>
                    <li><a href="/users" class="nav-link px-2 text-dark">Gestão de Utilizadores</a></li>
                </ul>
                % end

                <div class="ms-auto">
                    % if logged_in_user_id:
                        <a href="/logout" type="button" class="btn btn-outline-primary">Logout</a>
                    % else:
                        <a href="/login" type="button" class="btn btn-primary">Login</a>
                    % end
                </div>
            </div>
        </div>
    </header>

    <div class="container py-4">
        <main>
            {{!base}}
        </main>
    </div>

    <footer class="text-center mt-5 text-muted">
        <p>&copy; 2025, OrganizaDev. Todos os direitos reservados.</p>
    </footer>

    </body>
</html>