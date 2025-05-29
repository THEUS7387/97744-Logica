//Limpar o terminal.
console.clear()

let idade = parseInt(prompt("Digite sua idade:"));

if (isNaN(idade)) {
  alert("Por favor, digite um número válido.");
} else if (idade < 16) {
  alert("Não pode votar");
} else if ((idade >= 16 && idade < 18) || idade > 65) {
  alert("Voto opcional");
} else {
  alert("Voto obrigatório");
}
