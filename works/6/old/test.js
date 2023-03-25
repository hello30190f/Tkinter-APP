
var amount = 100000
for(var i = 0;i < 100; i++){
    window.scrollBy(0,amount)
}

const wait = async (ms) => new Promise(resolve => setTimeout(resolve, ms));
const main = async () => {
var amount = 100000
for(var i = 0;i < 100; i++){
    window.scrollBy(0,amount)
    await wait(1000)
}
};

await main();