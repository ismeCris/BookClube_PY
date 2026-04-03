
const modal = document.getElementById("modalLogout");

function confirmarSaida() {
  modal.style.display = "flex";
  return false; // impede sair direto
}

document.getElementById("btnCancelar").onclick = function () {
  modal.style.display = "none";
};

document.getElementById("btnConfirmar").onclick = function () {
  window.location.href = "/auth/logout";
};
