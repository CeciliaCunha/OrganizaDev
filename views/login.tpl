% rebase('layout.tpl', title='Login')

<div class="row justify-content-center">
    <div class="col-md-6 col-lg-4">
        <h1 class="text-center mb-4">Login</h1>
        % if error:
            <div class="alert alert-danger">{{ error }}</div>
        % end
        <form action="/login" method="post">
            <div class="mb-3">
                <label for="email" class="form-label">Email:</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <div class="d-grid">
                <button type="submit" class="btn btn-primary">Entrar</button>
            </div>
        </form>
        <p class="text-center mt-3">
            Não tem uma conta? <a href="/register">Registe-se aqui</a>.
        </p>
    </div>
</div>