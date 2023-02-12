(function (win, doc) {
  'use strict';

  // Verifica se o usuário realmente quer deletar o veículo
  if (doc.querySelector(".btnDel")) {
    let btnDel = doc.querySelectorAll(".btnDel");
    for (let i = 0; i < btnDel.length; i++) {
      btnDel[i].addEventListener("click", (event) => {
        if (confirm("Deseja apagar este veículo?")) {
          return true;
        } else {
          event.preventDefault();
        };
      });
    };
  };
  // Verifica se o usuário realmente quer deletar o veículo

  // AJAX Form Script
  if (doc.querySelector("#form")) {
    let form = doc.querySelector("#form");
    function sendForm(event) {
      event.preventDefault();
      let data = new FormData(form);
      let ajax = new XMLHttpRequest();
      let token = doc.querySelectorAll("input")[0].value;
      ajax.open("POST", form.action);
      ajax.setRequestHeader("X-CSRF-TOKEN", token);
      ajax.onreadystatechange = (error) => {
        if (ajax.status === 200 && ajax.readyState === 4) {
          let result = doc.querySelector("#result");
          result.innerHTML = "Operação Realizada com Sucesso!";
          result.classList.add("alert");
          result.classList.add("alert-success");
        };
      };
      ajax.send(data);
      form.reset();
    };
    form.addEventListener("submit", sendForm, false);
  };
  // AJAX Form Script

})(window, document);