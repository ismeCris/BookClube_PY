/* --- BUSCA DE LIVROS NA API --- */
async function buscarDadosLivro() {
    const query = document.getElementById('input_busca').value.trim();
    if (!query) return alert("Digite o título!");

    const url = `https://openlibrary.org/search.json?title=${encodeURIComponent(query)}`;
    const listaResultados = document.getElementById('lista_resultados');
    listaResultados.innerHTML = "<p style='color: var(--cor-primaria)'>Buscando na biblioteca...</p>"; 

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
                itemDiv.style = "display: flex; align-items: center; gap: 10px; margin-bottom: 10px; padding: 5px; border-bottom: 1px solid #eee;";
                itemDiv.innerHTML = `
                    <img src="${capaUrl}" alt="Capa" style="width: 40px; border-radius: 4px;">
                    <div style="flex-grow: 1;">
                        <strong style="font-size: 0.9rem;">${livro.title}</strong><br>
                        <small>${autor} (${ano})</small>
                    </div>
                    <button type="button" class="btn-selecionar" style="padding: 5px 10px; cursor: pointer;">Selecionar</button>
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

/* --- PREENCHIMENTO DO FORMULÁRIO --- */
function preencherFormulario(titulo, autor, ano, capaUrlFinal, capaId) {
    document.getElementById('titulo').value = titulo;
    document.getElementById('autor').value = autor;
    document.getElementById('descricao').value = `Publicado em: ${ano}. `;
    
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

function previewArquivoLocal(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('preview_capa');
            preview.src = e.target.result;
            preview.style.display = 'block';
            document.getElementById('capa_url').value = ""; // Limpa URL se enviou arquivo
        };
        reader.readAsDataURL(input.files[0]);
    }
}

/* --- GESTÃO DO MODAL (EDIÇÃO E CADASTRO) --- */
function abrirModal(id = null, titulo = '', autor = '', sinopse = '', capa = '', status = 'explorar', genero = '', avaliacao = 0) {
    const modal = document.getElementById('modalLivro');
    const form = document.getElementById('form_livro');
    const tituloModalTexto = document.getElementById('titulo_modal_texto');
    const secaoBusca = document.getElementById('secao_busca');
    const preview = document.getElementById('preview_capa');
// Dentro da sua função de salvar/enviar o formulário
const nota = document.querySelector('input[name="avaliacao"]:checked')?.value;
const statusSelect = document.getElementById('status');

if (nota == "5") {
    statusSelect.value = "favorito";
}
    // Reseta o scroll do formulário para o topo
    const scrollArea = document.querySelector('.modal-body-scroll');
    if(scrollArea) scrollArea.scrollTop = 0;

    if (id) {
        // MODO EDIÇÃO
        tituloModalTexto.innerText = "Editar Dados do Livro";
        form.action = `/livros/${id}/editar`; 
        secaoBusca.style.display = "none"; // Esconde a busca da API na edição
        
        document.getElementById('titulo').value = titulo;
        document.getElementById('autor').value = autor;
        document.getElementById('descricao').value = sinopse;
        document.getElementById('capa_url').value = capa;
        document.getElementById('status').value = status;
        document.getElementById('genero').value = genero;

        // Marcar a estrela correta
        if (avaliacao > 0) {
            const estrela = document.getElementById('star' + avaliacao);
            if (estrela) estrela.checked = true;
        } else {
            document.querySelectorAll('.star-rating input').forEach(i => i.checked = false);
        }

        preview.src = capa;
        preview.style.display = capa ? "inline-block" : "none";
    } else {
        // MODO CADASTRO
        tituloModalTexto.innerText = "Cadastrar Novo Livro";
        form.action = "/livros/salvar"; 
        secaoBusca.style.display = "block";
        form.reset();
        preview.style.display = "none";
        document.getElementById('lista_resultados').innerHTML = "";
        document.querySelectorAll('.star-rating input').forEach(i => i.checked = false);
    }

    modal.style.display = "block";
}

function fecharModal() {
    document.getElementById('modalLivro').style.display = "none";
}

// Fecha o modal ao clicar fora dele
window.onclick = function(event) {
    const modal = document.getElementById('modalLivro');
    if (event.target == modal) {
        fecharModal();
    }
}
function filtrarLivros(tipo) {
    const cards = document.querySelectorAll('.card-livro');

    cards.forEach(card => {
        const status = card.getAttribute('data-status')?.toLowerCase();

        if (tipo === 'todos') {
            card.style.display = 'block';
        } 
        else if (status === tipo) {
            card.style.display = 'block';
        } 
        else {
            card.style.display = 'none';
        }
    });
}