// Laço de Repetição while.
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function perguntarNota() {
    rl.question('Digite uma nota entre 0 e 10: ', (input) => {
        const nota = parseFloat(input);

        if (isNaN(nota) || nota < 0 || nota > 10) {
            console.log('Nota inválida. Tente novamente.\n');
            perguntarNota(); // Repetir se a nota for inválida
        } else {
            console.log(`Nota válida: ${nota}`);
            rl.close(); // Finaliza a leitura
        }
    });
}

perguntarNota();
