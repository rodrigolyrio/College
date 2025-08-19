const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout});

rl.question('', (nome) => {
    console.log(`Olá, ${nome}!`);
    rl.close();
});
