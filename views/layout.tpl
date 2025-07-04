<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF--8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'OrganizaDev' }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <header class="p-3 mb-3 border-bottom">
        <div class="container">
            <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none">
                    <strong>OrganizaDev</strong>
                </a>

                <div class="ms-auto">
                    % if logged_in_user_id:
                        <a href="/logout" type="button" class="btn btn-outline-primary">Logout</a>
                    % end
                </div>
            </div>
        </div>
    </header>
    <div class="container py-4">
        {{!base}}
    </div>

    <footer class="text-center mt-5 text-muted">
        <p>&copy; 2025, OrganizaDev. Todos os direitos reservados.</p>
    </footer>
</body>
</html>