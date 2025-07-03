% rebase('layout.tpl', title='Registro')

<div class="row justify-content-center">
    <div class="col-md-6 col-lg-5">
        <h1 class="text-center mb-4">Criar Conta</h1>
        % if error:
            <div class="alert alert-danger">{{ error }}</div>
        % end
        <form action="/register" method="post">
            <div class="mb-3">
                <label for="name" class="form-label">Nome Completo:</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email:</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <div class="mb-3">
                <label for="birthdate" class="form-label">Data de Nascimento:</label>
                <input type="date" class="form-control" id="birthdate" name="birthdate">
            </div>
            <div class="d-grid">
                <button type="submit" class="btn btn-success">Registrar</button>
            </div>
        </form>
        <p class="text-center mt-3">
            Já tem uma conta? <a href="/login">Faça login aqui</a>.
        </p>
    </div>
</div>