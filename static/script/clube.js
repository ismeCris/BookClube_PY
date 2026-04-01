function filtrarClubes(filtro, botao) {
    document.querySelectorAll('.btn-filtro').forEach(b => b.classList.remove('ativo'));
    botao.classList.add('ativo');

    const secoes = {
        'meus': document.getElementById('secao-meus'),
        'participo': document.getElementById('secao-participo'),
        'explorar': document.getElementById('secao-explorar')
    };

    if (filtro === 'todos') {
        Object.values(secoes).forEach(s => s.style.display = 'block');
    } else {
        Object.keys(secoes).forEach(key => {
            secoes[key].style.display = (key === filtro) ? 'block' : 'none';
        });
    }
}