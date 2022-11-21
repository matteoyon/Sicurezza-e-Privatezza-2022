.intel_syntax noprefix
.global _start

.section .text
_start:
  mov rax, 1
  mov rdi, 1
  lea rsi, [rip+win]
  mov rdx, 8
  syscall
  mov rax, 60
  syscall
  
win:
.string "You Win!"
