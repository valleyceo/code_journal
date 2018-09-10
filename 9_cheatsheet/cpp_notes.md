# CPP Concepts

## Bits

<details>
<summary> ~ vs ! </summary>
~ is bitwise NOT and ! is boolean NOT  
ex:  
~011100 => 100011  
!011100 => 0  
</details>

<details>
<summary> bits </summary>
0x -> hexadecimal (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)  
0b -> binary (0, 1)  

0xFFFF is 0b1111111111111111  

</details>

## Class

<details>
<summary> Class Explicit </summary>

---
- Avoids implicit conversion (i.e. string input to int) on function call

---

</details>

## Function

<details>
<summary> Function Input using Pointer and Reference </summary>

---
- https://stackoverflow.com/questions/114180/pointer-vs-reference
- https://google.github.io/styleguide/cppguide.html#Reference_Arguments

---

```cpp
// method one
void func1(unsigned long& val) {
     val = 5;            
}
func1(x);

// method two - use when you need to use pointer increment (s.a. iterations), need to make sure pointer is not NULL
void func2(unsigned long* val) {
     *val = 5;
}
func2(&x);
```
</details>