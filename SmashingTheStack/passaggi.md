# Lista di passaggi per eseguire un attacco del tipo Smashing the Stack

0. Disattiva la randomizzazione: `sudo sysctl -e kernel.randomize_va_space=0`
1. Installa [gef](https://hugsy.github.io/gef/)
2. Compili il .c con: `gcc -fno-stack-protector -zexecstack -g cookie3.c`
3. Compili l'assembly con: `gcc -nostdlib -static -o cookie3 cookie3.S`
4. Estrai il Raw con : `objcopy --dump-section .text=RawCookie cookie3` 
5. Esegui col gdb : `gdb -q a.out`
6. BreakPoint al main: `b main`
7. Esegui: `r < in.txt` (dove in.txt è il file generato dallo script python)
8. Disassembli: `disassemble`
9. BreakPoint alla prima istruzione dopo gets: `b *main+60` (può variare)
10. Esegui fino al breakpoint: `c`
11. Guardi dove si trova il return address (rbp +8): `x/xg $rbp +8`
12. Guardi il contenuto dei registri con: `x/140xg $rbp - 128`
13. In base a questo trovi dove viene salvato il tuo indirizzo scritto nel python e deve essere a rbp + 8, quindi modifichi gli offset per avere il tuo addr a rbp +8 (questo serve perchè magari invece di 80 byte ne alloca 96)
14. Esegui a.out per scoprire l'indirizzo del buffer e lo sostituisci a addr su python: `./a.out`
