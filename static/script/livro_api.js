async function buscarDadosLivro() {
    const query = document.getElementById('input_busca').value.trim();
    if (!query) return alert("Digite o título!");

    const url = `https://openlibrary.org/search.json?title=${encodeURIComponent(query)}`;
    const listaResultados = document.getElementById('lista_resultados');
    listaResultados.innerHTML = "Buscando..."; 

    try {
        const response = await fetch(url);
        const data = await response.json();

        listaResultados.innerHTML = ""; 

        if (data.docs && data.docs.length > 0) {
            const livros = data.docs.slice(0, 10); 

            livros.forEach(livro => {
                const capaId = livro.cover_i;
            
                const IMAGEM_LOCAL = '/static/images/minha_capa_padrao.jpg'; 

                const capaUrl = capaId 
                    ? `https://covers.openlibrary.org/b/id/${capaId}-M.jpg` 
                    : IMAGEM_LOCAL; 

                const autor = livro.author_name ? livro.author_name.join(', ') : "Desconhecido";
                const ano = livro.first_publish_year || 'N/A';

                const itemDiv = document.createElement('div');
                itemDiv.className = 'item-busca';
                itemDiv.innerHTML = `
                    <img src="${capaUrl}" alt="Capa" style="width: 50px;">
                    <div>
                        <strong>${livro.title}</strong><br>
                        <small>${autor} (${ano})</small>
                    </div>
                    <button type="button" class="btn-selecionar">Selecionar</button>
                `;

                itemDiv.querySelector('.btn-selecionar').onclick = () => {
                    preencherFormulario(livro.title, autor, ano, capaUrl, capaId);
                    listaResultados.innerHTML = ""; 
                };

                listaResultados.appendChild(itemDiv);
            });

        } else {
            listaResultados.innerHTML = "Nenhum livro encontrado.";
        }
    } catch (error) {
        console.error("Erro:", error);
        listaResultados.innerHTML = "Erro de conexão.";
    }
}
function previewArquivoLocal(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const preview = document.getElementById('preview_capa');
            preview.src = e.target.result;
            preview.style.display = 'block';
            
            document.getElementById('capa_url').value = "";
        };
        
        reader.readAsDataURL(input.files[0]);
    }
}
function preencherFormulario(titulo, autor, ano, capaUrlFinal, capaId) {
    document.getElementById('titulo').value = titulo;
    document.getElementById('autor').value = autor;
    document.getElementById('descricao').value = `Publicado em: ${ano}`;
    
    document.getElementById('file_upload').value = "";

    if (capaId) {
        const capaUrlLg = `https://covers.openlibrary.org/b/id/${capaId}-L.jpg`;
        document.getElementById('capa_url').value = capaUrlLg;
        document.getElementById('preview_capa').src = capaUrlLg;
    } else {
        document.getElementById('capa_url').value = capaUrlFinal;
        document.getElementById('preview_capa').src = capaUrlFinal;
    }
    document.getElementById('preview_capa').style.display = 'block';
}

function abrirModal(id = null, titulo = '', autor = '', sinopse = '', capa = '') {
    const modal = document.getElementById('modalLivro');
    const form = document.getElementById('form_livro');
    const tituloModalTexto = document.getElementById('titulo_modal_texto');
    const secaoBusca = document.getElementById('secao_busca');
    const preview = document.getElementById('preview_capa');

    if (id) {
        //  MODO EDIÇÃO 
        tituloModalTexto.innerText = "Editar Dados do Livro";
    
        form.action = `/livros/${id}/editar`; 
        //escode a busca
        secaoBusca.style.display = "none";
        
        // Preenche os campos 
        document.getElementById('titulo').value = titulo;
        document.getElementById('autor').value = autor;
        document.getElementById('descricao').value = sinopse;
        document.getElementById('capa_url').value = capa;
        
        // Mostra a capa atual 
        preview.src = capa;
        preview.style.display = "inline-block";
    } else {
        //  MODO CADASTRO 
        tituloModalTexto.innerText = "Cadastrar Novo Livro";
        form.action = "/livros/salvar"; 
        
        secaoBusca.style.display = "block";
        form.reset();
        preview.style.display = "none";
        document.getElementById('lista_resultados').innerHTML = "";
    }

    modal.style.display = "block";
}

function fecharModal() {
    document.getElementById('modalLivro').style.display = "none";
}

// Fecha o modal
window.onclick = function(event) {
    const modal = document.getElementById('modalLivro');
    if (event.target == modal) {
        fecharModal();
    }
}