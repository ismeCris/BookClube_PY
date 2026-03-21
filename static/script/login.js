const card = document.getElementById('card-login');
const btnIrCadastro = document.getElementById('btn-ir-cadastro');
const conteudoForm = document.getElementById('conteudo-formulario');

btnIrCadastro.addEventListener('click', () => {
    // 1. Inverte os lados
    card.classList.add('modo-cadastro');

    // 2. Troca o conteúdo para Cadastro
    conteudoForm.innerHTML = `
        <h2>Cadastro</h2>
        <form action="/auth/cadastro" method="POST">
            <div class="input-group">
                <label>Nome Completo</label>
                <input type="text" name="nome" placeholder="Seu nome" required>
            </div>
            <div class="input-group">
                <label>Email</label>
                <input type="email" name="email" placeholder="Seu e-mail" required>
            </div>
            <div class="input-group">
                <label>Senha</label>
                <input type="password" name="senha" placeholder="Crie uma senha" required>
            </div>
            <button type="submit" class="btn-login">Cadastrar</button>
            <p class="link-voltar" onclick="window.location.reload()">Já tenho conta? Voltar ao Login</p>
        </form>
    `;
});