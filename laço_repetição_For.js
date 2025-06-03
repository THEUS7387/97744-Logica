//Laço de Repetição.

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function perguntarNumero() {
    rl.question('Digite um número para ver a tabuada: ', (input) => {
        const numero = parseFloat(input);

        if (isNaN(numero)) {
            console.log('Valor inválido. Por favor, digite um número.\n');
            perguntarNumero(); // Repete a pergunta se não for número
        } else {
            console.log(`\nTabuada do ${numero}:`);
            for (let i = 1; i <= 10; i++) {
                console.log(`${numero} x ${i} = ${numero * i}`);
            }
            rl.close();
        }
    });
}

perguntarNumero();