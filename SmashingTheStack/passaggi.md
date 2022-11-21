# Lista di passaggi per eseguire un attacco del tipo Smashing the Stack

1. Compili il .c con: `gcc -fno-stack-protector -zexecstack -g cookie3.c`
2. Compili il l'assembly con: `gcc -nostdlib -static -o cooki3 cookie3.S`
3. Estrai il Raw con : `objcopy --dump-section .text=RawCookie cookie3` 
4. Esegui col gdb : `gdb -q a.out`
5. BreakPoint al main: `b main`
6. Disassembli: `disassemble`
7. BreakPoint alla prima istruzione dopo gets: `b *main+60` (può variare)
8. Guardi il contenuto dei registri con: `x/140xg $rbp - 128`
9. In base a questo trovi dove viene salvato il tuo indirizzo scritto nel python e deve essere a rbp + 8
