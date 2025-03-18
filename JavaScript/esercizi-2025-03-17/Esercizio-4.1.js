let num = 5;
let i = 1;

console.log(`Tabbellina del ${num} (con for):`);

for (var cont = 1; cont<=10; cont++){
   console.log(`${num} x ${cont} = ${num*cont}`);
}

console.log(`Tabbellina del ${num} (con while):`);
while (i<=10){
   console.log(`${num} x ${i} = ${num*i}`);
   i++;
}