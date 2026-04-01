function filtrarClubes(filtro, botao) {
    // Remove classe ativa de todos
    document.querySelectorAll('.btn-filtro').forEach(b => b.classList.remove('ativo'));
    // Adiciona no clicado
    botao.classList.add('ativo');

    const meus = document.getElementById('secao-meus');
    const explorar = document.getElementById('secao-explorar');

    if (filtro === 'todos') {
        meus.style.display = 'block';
        explorar.style.display = 'block';
    } else if (filtro === 'meus') {
        meus.style.display = 'block';
        explorar.style.display = 'none';
    } else {
        meus.style.display = 'none';
        explorar.style.display = 'block';
    }
}